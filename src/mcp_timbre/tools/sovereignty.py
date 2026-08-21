import json
from datetime import datetime, timezone, timedelta
from ..core.config import load_state, save_state, HISTORY_DIR, ensure_dirs


def trajectory() -> str:
    state = load_state()
    gen_count = state.get("generation_count", 0)
    written_count = state.get("written_count", 0)
    total = gen_count + written_count

    if total == 0:
        return json.dumps({
            "status": "no_data",
            "message": "No writing activity tracked yet. Use timbre during writing sessions to build trajectory data.",
        }, indent=2)

    generation_ratio = gen_count / total if total > 0 else 0

    mode_history = state.get("mode_history", [])
    recent_modes = mode_history[-20:] if mode_history else []
    mode_counts = {}
    for entry in recent_modes:
        m = entry.get("mode", "unknown")
        mode_counts[m] = mode_counts.get(m, 0) + 1

    calibrated = state.get("calibrated_registers", {})
    stale_registers = []
    for reg, data in calibrated.items():
        last_cal = data.get("last_calibrated", "")
        if last_cal:
            try:
                cal_date = datetime.fromisoformat(last_cal)
                if datetime.now(timezone.utc) - cal_date > timedelta(days=30):
                    stale_registers.append(reg)
            except (ValueError, TypeError):
                stale_registers.append(reg)

    alerts = []
    if generation_ratio > 0.7:
        alerts.append({
            "type": "high_generation_ratio",
            "severity": "warning",
            "message": f"Your generation ratio is {generation_ratio:.0%}. Most of your writing is being generated rather than written by you. Consider using craft mode more often.",
        })

    if mode_counts.get("throughput", 0) > 0 and mode_counts.get("craft", 0) == 0:
        alerts.append({
            "type": "no_craft_mode",
            "severity": "notice",
            "message": "You haven't used craft mode in your recent sessions. Are there contexts where you'd benefit from writing without generation?",
        })

    if stale_registers:
        alerts.append({
            "type": "stale_registers",
            "severity": "notice",
            "message": f"These registers haven't been recalibrated in 30+ days: {', '.join(stale_registers)}. Your voice may have evolved. Consider a recalibration on your next real piece in these registers.",
        })

    return json.dumps({
        "status": "ok",
        "generation_ratio": round(generation_ratio, 2),
        "generation_count": gen_count,
        "written_count": written_count,
        "total_tracked": total,
        "recent_mode_distribution": mode_counts,
        "stale_registers": stale_registers,
        "alerts": alerts,
        "instruction": "Present the trajectory data to the user. If there are alerts, surface them conversationally - not as warnings but as observations. The goal is awareness, not judgment. Ask if the ratios reflect what they want.",
    }, indent=2)


def recalibration_check() -> str:
    state = load_state()
    calibrated = state.get("calibrated_registers", {})

    needs_recalibration = []
    for reg, data in calibrated.items():
        last_cal = data.get("last_calibrated", "")
        if last_cal:
            try:
                cal_date = datetime.fromisoformat(last_cal)
                days_since = (datetime.now(timezone.utc) - cal_date).days
                if days_since > 21:
                    needs_recalibration.append({
                        "register": reg,
                        "days_since_calibration": days_since,
                    })
            except (ValueError, TypeError):
                needs_recalibration.append({
                    "register": reg,
                    "days_since_calibration": -1,
                })

    if not needs_recalibration:
        return json.dumps({
            "status": "all_fresh",
            "message": "All registers have been calibrated within the last 21 days.",
        }, indent=2)

    next_reg = needs_recalibration[0]
    return json.dumps({
        "status": "recalibration_needed",
        "registers_needing_refresh": needs_recalibration,
        "suggested_next": next_reg["register"],
        "message": f"A fresh writing sample for {next_reg['register']} is needed. The next {next_reg['register']} you write will be used to calibrate this register.",
        "instruction": "Surface this to the user conversationally. They opt in. The next real piece of writing they produce in this register becomes the recalibration sample. Remind them: this is a moment to be intentional about how they're writing now.",
    }, indent=2)
