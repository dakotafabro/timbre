import json
from datetime import datetime, timezone
from ..core.config import load_state, save_state, load_profile, profile_exists
from ..core.analysis import detect_register


def draft(mode: str, register: str = "", context: str = "") -> str:
    valid_modes = ["craft", "throughput", "learning"]
    if mode not in valid_modes:
        return json.dumps({
            "status": "error",
            "message": f"Invalid mode '{mode}'. Choose from: {', '.join(valid_modes)}",
        }, indent=2)

    if not profile_exists():
        return json.dumps({
            "status": "no_profile",
            "message": "No voice profile exists yet. Run 'calibrate' first.",
        }, indent=2)

    profile = load_profile()
    state = load_state()

    state.setdefault("mode_history", []).append({
        "mode": mode,
        "register": register,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })
    save_state(state)

    if mode == "craft":
        return json.dumps({
            "status": "craft_mode",
            "message": "Craft mode active. Generation is disabled. Mirror functions only.",
            "available_actions": ["how_does_this_sound", "what_is_my_pattern", "where_am_i_drifting"],
            "profile": profile,
            "instruction": "The user is in craft mode. Do NOT generate text for them. Only reflect, mirror, and observe. If they ask you to write something, remind them they're in craft mode and offer to switch to throughput if they want generation.",
        }, indent=2)

    if mode == "learning":
        return json.dumps({
            "status": "learning_mode",
            "message": "Learning mode active. Scaffolding only.",
            "register": register or "general",
            "context": context,
            "profile": profile,
            "instruction": "The user is in learning mode for writing. Show them their patterns for this register, suggest what the context calls for, and let them try it themselves. Offer challenges if appropriate. Do NOT generate text. Scaffold their attempt.",
        }, indent=2)

    if mode == "throughput":
        return json.dumps({
            "status": "throughput_mode",
            "message": "Throughput mode active. Provide your substance (outline, bullets, rough draft) and I'll generate a draft in your voice.",
            "register": register or "general",
            "context": context,
            "profile": profile,
            "instruction": "The user is in throughput mode. Wait for them to provide substance (outline, bullets, rough draft, key points). Do NOT generate from nothing. Once they provide substance, generate a draft that matches their voice profile for this register. After generating, increment generation_count via 'log_generation'.",
        }, indent=2)

    return json.dumps({"status": "error", "message": "Unexpected state"}, indent=2)


def generate(substance: str, register: str = "", context: str = "") -> str:
    if not profile_exists():
        return json.dumps({
            "status": "no_profile",
            "message": "No voice profile exists yet. Run 'calibrate' first.",
        }, indent=2)

    if not substance.strip():
        return json.dumps({
            "status": "error",
            "message": "Generation requires substance. Provide an outline, bullets, rough draft, or key points. The plugin never generates from nothing.",
        }, indent=2)

    profile = load_profile()
    detected_register = register or detect_register(substance, context)

    state = load_state()
    state["generation_count"] = state.get("generation_count", 0) + 1
    save_state(state)

    return json.dumps({
        "status": "ok",
        "register": detected_register,
        "substance_word_count": len(substance.split()),
        "profile": profile,
        "instruction": f"Generate a draft in the user's voice for the '{detected_register}' register. Use the voice profile to match their patterns: sentence length, opener style, closer style, tone, structural preferences. The substance provided is the user's thinking - transform it into polished writing that sounds like them. Present the draft and ask if they want to adjust anything.",
    }, indent=2)


def log_written() -> str:
    state = load_state()
    state["written_count"] = state.get("written_count", 0) + 1
    save_state(state)
    return json.dumps({
        "status": "ok",
        "written_count": state["written_count"],
        "generation_count": state.get("generation_count", 0),
    }, indent=2)
