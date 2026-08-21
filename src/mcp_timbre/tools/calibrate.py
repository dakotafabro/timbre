import json
from datetime import datetime, timezone
from ..core.config import (
    load_state, save_state, save_profile, load_profile,
    profile_exists, SAMPLES_DIR, ensure_dirs,
)
from ..core.analysis import compute_metrics, detect_register


CALIBRATION_PROMPTS = {
    "email": "Provide a professional email you've written recently (or write one now for a real recipient). This will calibrate your email voice.",
    "slack": "Provide a Slack message or casual team communication you've written. This will calibrate your informal/conversational voice.",
    "technical": "Provide a piece of technical writing - documentation, a PR description, a design doc section. This will calibrate your technical voice.",
    "narrative": "Provide a piece of narrative or creative writing - a blog post intro, a personal essay paragraph, a story opening. This will calibrate your narrative voice.",
    "persuasive": "Provide a piece of persuasive writing - a proposal, a pitch, an argument for a decision. This will calibrate your persuasive voice.",
}


def start_calibration() -> str:
    state = load_state()
    calibrated = state.get("calibrated_registers", {})
    uncalibrated = [r for r in CALIBRATION_PROMPTS if r not in calibrated]

    if not uncalibrated:
        return json.dumps({
            "status": "complete",
            "message": "All registers are calibrated. Use 'recalibrate' to refresh a specific register, or provide new writing to update your profile.",
            "calibrated_registers": list(calibrated.keys()),
        }, indent=2)

    next_register = uncalibrated[0]
    return json.dumps({
        "status": "in_progress",
        "next_register": next_register,
        "prompt": CALIBRATION_PROMPTS[next_register],
        "calibrated": list(calibrated.keys()),
        "remaining": uncalibrated,
        "instruction": "Ask the user to provide the writing sample. When they do, call 'submit_sample' with the text and register.",
    }, indent=2)


def submit_sample(text: str, register: str) -> str:
    ensure_dirs()
    state = load_state()
    metrics = compute_metrics(text)

    sample_file = SAMPLES_DIR / f"{register}_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.txt"
    sample_file.write_text(text)

    if "calibrated_registers" not in state:
        state["calibrated_registers"] = {}

    state["calibrated_registers"][register] = {
        "last_calibrated": datetime.now(timezone.utc).isoformat(),
        "sample_count": state["calibrated_registers"].get(register, {}).get("sample_count", 0) + 1,
        "metrics": {
            "avg_sentence_length": metrics.avg_sentence_length,
            "short_sentence_pct": metrics.short_sentence_pct,
            "long_sentence_pct": metrics.long_sentence_pct,
            "qualifier_density": metrics.qualifier_density,
            "exclamation_count": metrics.exclamation_count,
            "question_count": metrics.question_count,
            "avg_paragraph_length": metrics.avg_paragraph_length,
            "word_count": metrics.word_count,
        },
    }

    save_state(state)

    uncalibrated = [r for r in CALIBRATION_PROMPTS if r not in state["calibrated_registers"]]

    result = {
        "status": "sample_recorded",
        "register": register,
        "metrics": {
            "sentence_count": metrics.sentence_count,
            "avg_sentence_length": metrics.avg_sentence_length,
            "short_sentence_pct": metrics.short_sentence_pct,
            "long_sentence_pct": metrics.long_sentence_pct,
            "qualifier_density": metrics.qualifier_density,
            "word_count": metrics.word_count,
        },
        "instruction": "Analyze this sample using the LLM to extract voice patterns: opener style, closer style, tone markers, structural preferences, distinctive habits. Then call 'update_profile' with the analysis for this register.",
    }

    if uncalibrated:
        result["next_register"] = uncalibrated[0]
        result["next_prompt"] = CALIBRATION_PROMPTS[uncalibrated[0]]
    else:
        result["calibration_complete"] = True
        result["instruction"] += " All registers are now calibrated. Generate the full voice-profile.md."

    return json.dumps(result, indent=2)


def update_profile(profile_markdown: str) -> str:
    save_profile(profile_markdown)
    return json.dumps({
        "status": "profile_updated",
        "message": "Voice profile saved to ~/.timbre/voice-profile.md",
        "instruction": "Present the profile to the user. They can edit it at any time with 'edit-profile'.",
    }, indent=2)


def get_profile() -> str:
    profile = load_profile()
    if profile is None:
        return json.dumps({
            "status": "no_profile",
            "message": "No voice profile exists yet. Run 'calibrate' to create one.",
        }, indent=2)

    state = load_state()
    return json.dumps({
        "status": "ok",
        "profile": profile,
        "calibrated_registers": list(state.get("calibrated_registers", {}).keys()),
        "generation_count": state.get("generation_count", 0),
        "written_count": state.get("written_count", 0),
    }, indent=2)
