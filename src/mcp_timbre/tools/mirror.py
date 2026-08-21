import json
from ..core.config import load_state, load_profile, profile_exists
from ..core.analysis import compute_metrics, detect_register


def how_does_this_sound(text: str, context: str = "") -> str:
    if not profile_exists():
        return json.dumps({
            "status": "no_profile",
            "message": "No voice profile exists yet. Run 'calibrate' first so I have a baseline to compare against.",
        }, indent=2)

    profile = load_profile()
    metrics = compute_metrics(text)
    register = detect_register(text, context)
    state = load_state()
    register_data = state.get("calibrated_registers", {}).get(register, {})
    baseline_metrics = register_data.get("metrics", {})

    deviations = []
    if baseline_metrics:
        baseline_asl = baseline_metrics.get("avg_sentence_length", 0)
        if baseline_asl and abs(metrics.avg_sentence_length - baseline_asl) > 5:
            direction = "longer" if metrics.avg_sentence_length > baseline_asl else "shorter"
            deviations.append(f"Sentences are {direction} than your typical {register} writing ({metrics.avg_sentence_length} vs baseline {baseline_asl} words)")

        baseline_qd = baseline_metrics.get("qualifier_density", 0)
        if baseline_qd and abs(metrics.qualifier_density - baseline_qd) > 2:
            direction = "more hedging" if metrics.qualifier_density > baseline_qd else "more direct"
            deviations.append(f"This reads {direction} than your baseline ({metrics.qualifier_density} vs {baseline_qd} qualifiers per 100 words)")

    return json.dumps({
        "status": "ok",
        "detected_register": register,
        "metrics": {
            "word_count": metrics.word_count,
            "avg_sentence_length": metrics.avg_sentence_length,
            "short_sentence_pct": metrics.short_sentence_pct,
            "long_sentence_pct": metrics.long_sentence_pct,
            "qualifier_density": metrics.qualifier_density,
            "exclamation_count": metrics.exclamation_count,
            "question_count": metrics.question_count,
        },
        "deviations_from_baseline": deviations,
        "profile": profile,
        "instruction": "Using the voice profile and the metrics/deviations above, provide the user with a reflection on how this piece sounds relative to their established voice. Note what's consistent, what's different, and whether the differences seem intentional. Do not suggest corrections unless asked. Mirror only.",
    }, indent=2)


def what_is_my_pattern(register: str = "", context: str = "") -> str:
    if not profile_exists():
        return json.dumps({
            "status": "no_profile",
            "message": "No voice profile exists yet. Run 'calibrate' first.",
        }, indent=2)

    profile = load_profile()
    state = load_state()
    register_data = state.get("calibrated_registers", {}).get(register, {})

    return json.dumps({
        "status": "ok",
        "requested_register": register or "general",
        "context": context,
        "register_data": register_data,
        "profile": profile,
        "instruction": f"Using the voice profile, surface the user's patterns for the '{register or 'general'}' register. Include: how they typically open, their sentence rhythm, tone markers, structural preferences, and how they close. If context was provided, tailor the patterns to that specific situation. Be specific and concrete - use examples from the profile where possible.",
    }, indent=2)


def where_am_i_drifting(text: str, context: str = "") -> str:
    if not profile_exists():
        return json.dumps({
            "status": "no_profile",
            "message": "No voice profile exists yet. Run 'calibrate' first.",
        }, indent=2)

    profile = load_profile()
    metrics = compute_metrics(text)
    register = detect_register(text, context)
    state = load_state()
    register_data = state.get("calibrated_registers", {}).get(register, {})
    baseline_metrics = register_data.get("metrics", {})

    significant_drifts = []
    if baseline_metrics:
        baseline_asl = baseline_metrics.get("avg_sentence_length", 0)
        if baseline_asl and abs(metrics.avg_sentence_length - baseline_asl) > 8:
            significant_drifts.append({
                "dimension": "sentence_length",
                "current": metrics.avg_sentence_length,
                "baseline": baseline_asl,
                "severity": "high",
            })

        baseline_qd = baseline_metrics.get("qualifier_density", 0)
        if baseline_qd and abs(metrics.qualifier_density - baseline_qd) > 3:
            significant_drifts.append({
                "dimension": "qualifier_density",
                "current": metrics.qualifier_density,
                "baseline": baseline_qd,
                "severity": "high",
            })

        baseline_ssp = baseline_metrics.get("short_sentence_pct", 0)
        if baseline_ssp and abs(metrics.short_sentence_pct - baseline_ssp) > 0.2:
            significant_drifts.append({
                "dimension": "rhythm",
                "current": metrics.short_sentence_pct,
                "baseline": baseline_ssp,
                "severity": "moderate",
            })

    return json.dumps({
        "status": "ok",
        "detected_register": register,
        "significant_drifts": significant_drifts,
        "drift_count": len(significant_drifts),
        "profile": profile,
        "instruction": "Report the drifts to the user. Name what's different without correcting. If no significant drifts were detected quantitatively, use the LLM to compare the text against the voice profile qualitatively (tone, opener style, closer style, structural choices). The goal is noticing, not fixing.",
    }, indent=2)
