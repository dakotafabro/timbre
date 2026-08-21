from fastmcp import FastMCP
from .tools.calibrate import (
    start_calibration,
    submit_sample,
    update_profile,
    get_profile,
)
from .tools.mirror import (
    how_does_this_sound,
    what_is_my_pattern,
    where_am_i_drifting,
)
from .tools.generate import (
    draft,
    generate,
    log_written,
)
from .tools.sovereignty import (
    trajectory,
    recalibration_check,
)

INSTRUCTIONS = """
Timbre is a writing voice calibration plugin. It helps users know their own
writing voice better - not replace it. Mirror first, generate second.

Use 'calibrate' to start voice calibration from real writing samples.
Use 'profile' to view the user's current voice profile.
Use 'how_does_this_sound' when a user wants reflection on a piece of writing.
Use 'what_is_my_pattern' when a user wants to know their patterns before writing.
Use 'where_am_i_drifting' to flag deviations from established voice.
Use 'draft' to start a writing session in a specific mode (craft/throughput/learning).
Use 'generate' ONLY in throughput mode, ONLY after the user provides substance.
Use 'trajectory' to show the user their generation ratio and evolution.
Use 'recalibration_check' to see if any registers need fresh samples.

Key principles:
- Never generate from nothing. Always require user substance first.
- Craft mode disables generation entirely. Mirror only.
- The voice profile is human-readable markdown the user owns.
- Track generation vs written ratio. Surface it when asked.
"""

mcp = FastMCP("timbre", instructions=INSTRUCTIONS)


@mcp.tool()
def timbre_calibrate() -> str:
    """Start or continue voice calibration. Guides the user through providing
    real writing samples across registers (email, slack, technical, narrative, persuasive)."""
    return start_calibration()


@mcp.tool()
def timbre_submit_sample(text: str, register: str) -> str:
    """Submit a writing sample for a specific register during calibration.
    The text should be real writing the user produced, not an exercise."""
    return submit_sample(text, register)


@mcp.tool()
def timbre_update_profile(profile_markdown: str) -> str:
    """Save or update the user's voice profile. The profile should be
    human-readable markdown documenting their patterns across registers."""
    return update_profile(profile_markdown)


@mcp.tool()
def timbre_profile() -> str:
    """View the user's current voice profile and calibration status."""
    return get_profile()


@mcp.tool()
def timbre_how_does_this_sound(text: str, context: str = "") -> str:
    """Reflect on a piece of writing relative to the user's established voice.
    Returns metrics and deviations. Does not correct - only mirrors."""
    return how_does_this_sound(text, context)


@mcp.tool()
def timbre_what_is_my_pattern(register: str = "", context: str = "") -> str:
    """Surface the user's patterns for a given register before they write.
    Helps them recall their own voice for the context they're about to write in."""
    return what_is_my_pattern(register, context)


@mcp.tool()
def timbre_where_am_i_drifting(text: str, context: str = "") -> str:
    """Flag significant deviations from the user's established voice.
    No correction. Just noticing."""
    return where_am_i_drifting(text, context)


@mcp.tool()
def timbre_draft(mode: str, register: str = "", context: str = "") -> str:
    """Start a writing session in a specific mode.
    Modes: 'craft' (mirror only), 'throughput' (generation enabled), 'learning' (scaffolding).
    The user must choose their mode consciously."""
    return draft(mode, register, context)


@mcp.tool()
def timbre_generate(substance: str, register: str = "", context: str = "") -> str:
    """Generate a draft in the user's voice from their provided substance.
    Only available in throughput mode. Requires outline, bullets, or rough draft as input.
    Never generates from nothing."""
    return generate(substance, register, context)


@mcp.tool()
def timbre_log_written() -> str:
    """Log that the user wrote something themselves (not generated).
    Call this when the user produces writing in craft or learning mode."""
    return log_written()


@mcp.tool()
def timbre_trajectory() -> str:
    """Show the user's writing trajectory: generation ratio, mode distribution,
    stale registers, and sovereignty alerts."""
    return trajectory()


@mcp.tool()
def timbre_recalibration_check() -> str:
    """Check if any registers need fresh calibration samples.
    Surfaces which registers are stale and prompts for real-work recalibration."""
    return recalibration_check()


def main() -> None:
    mcp.run()
