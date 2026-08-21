from pathlib import Path
import json
import yaml

TIMBRE_DIR = Path.home() / ".timbre"
PROFILE_PATH = TIMBRE_DIR / "voice-profile.md"
STATE_PATH = TIMBRE_DIR / "state.json"
SAMPLES_DIR = TIMBRE_DIR / "samples"
HISTORY_DIR = TIMBRE_DIR / "history"


def ensure_dirs():
    TIMBRE_DIR.mkdir(exist_ok=True)
    SAMPLES_DIR.mkdir(exist_ok=True)
    HISTORY_DIR.mkdir(exist_ok=True)


def load_state() -> dict:
    ensure_dirs()
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {
        "calibrated_registers": {},
        "generation_count": 0,
        "written_count": 0,
        "mode_history": [],
        "version": "0.1.0",
    }


def save_state(state: dict):
    ensure_dirs()
    STATE_PATH.write_text(json.dumps(state, indent=2))


def load_profile() -> str | None:
    if PROFILE_PATH.exists():
        return PROFILE_PATH.read_text()
    return None


def save_profile(content: str):
    ensure_dirs()
    PROFILE_PATH.write_text(content)


def profile_exists() -> bool:
    return PROFILE_PATH.exists()
