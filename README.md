# timbre

A writing voice calibration plugin that helps you know your own voice better - not replace it.

---

## Philosophy

Most AI writing tools optimize for throughput. You describe what you want, the tool generates it, you edit. The implicit promise is speed: less time writing, more time doing other things.

This plugin takes a different position. Writing is not an obstacle between you and your ideas. Writing is how you discover, refine, and express your ideas. Your voice - the specific way you construct sentences, open emails, close arguments, signal warmth or authority or curiosity - is not a style sheet to be applied. It's a living relationship between you and language that develops through practice.

The problem this plugin solves is not "writing takes too long." The problem is: most people don't know their own voice well enough to wield it intentionally. They write differently in different contexts without noticing. They drift from their natural patterns under pressure. They have difficulty articulating what makes their writing theirs.

This plugin is a mirror first and a tool second. Its primary job is to show you who you are as a writer. Its secondary job - available when you consciously choose it - is to help you produce writing that sounds more like you across the different contexts within which you work.

The success metric is not "how much writing did we generate for the user." It's "does the user know their own voice better after six months of using this plugin than they did prior?"

---

## The Honest Tradeoffs

Building a tool that touches someone's writing voice carries real risks. This plugin was designed in direct conversation with the Ontological Footprint Framework by Dakota Fabro, which diagnoses how technology reshapes human capability at scale. Here's what we're watching for and how the design addresses it:

**Behavioral Substitution.** If the plugin generates writing for you by default, the generative struggle - the place where voice actually develops - gets bypassed. Over time, you lose familiarity with your own unmediated expression.

*Design response:* Generation is never the default mode. The primary mode is reflection. Generation requires you to provide substance first (outline, bullets, rough draft) and to consciously select throughput mode. The plugin never generates from nothing.

**Default Installation.** The risk that encountering a blank page triggers "let me get an output" instead of "let me think about what I want to say."

*Design response:* Craft mode disables generation entirely. The plugin only reflects. You choose your mode before writing, which means you're making a conscious decision about your relationship to the work.

**Exit Cost Escalation.** If you rely on the plugin long enough, your unassisted writing might feel unfamiliar - not because it's worse, but because you've lost contact with it.

*Design response:* The plugin tracks your generation ratio over time. If it's climbing, it tells you. It periodically asks: "Could you write effectively without this tomorrow?" Your voice profile is a readable document you own and can apply manually. Nothing is locked to the tool.

**Intermediation.** The plugin sits between you and your expression. Every piece of writing passes through an intermediary that shapes it according to prior calibration.

*Design response:* Mirror mode doesn't shape anything. It observes and reflects. In throughput mode, you've already done the thinking - the plugin handles surface expression while you retain the substance. The cognitive work stays with you.

---

## How It Works

### Calibration

You write. Not exercises - real writing you'd produce anyway. The plugin observes across registers (email, Slack, technical docs, narrative, persuasive) and extracts patterns:

- Sentence length and rhythm
- How you open and close communications
- Qualifier frequency (hedging vs. directness)
- Structural preferences (bullets vs. prose, paragraph length)
- Tone markers (warmth, formality, enthusiasm)
- How your voice shifts across contexts

The output is a `voice-profile.md` file. Human-readable. Editable. Yours. Not a black box embedding - a document that teaches you something about yourself.

### Three Modes

| Mode | When to use it | What the plugin does |
|---|---|---|
| **Craft** | Creative writing, personal correspondence, design docs, anything you want to own deeply | Mirror only. Reflects patterns, flags drift, never generates. |
| **Throughput** | Routine emails, status updates, Slack replies where voice consistency matters | Generates a draft in your voice from your substance (outline, bullets, rough draft). You edit. |
| **Learning** | When you're stretching into a new register or actively improving your craft | Scaffolding. Shows your patterns, suggests what the context calls for, lets you try it yourself. |

You choose the mode. The plugin never defaults to generation.

### The Mirror (Primary Function)

- **"How does this sound?"** - You write something, the plugin reflects: "This reads more formal than your typical professional register. Shorter sentences than usual. Missing your typical warm close."
- **"What's my pattern here?"** - Before writing, the plugin surfaces relevant patterns: "In emails to external collaborators, you tend to open with genuine enthusiasm, keep the body conversational, and close with gratitude toward the person."
- **"Where am I drifting?"** - The plugin flags significant deviations from your established voice. No correction. Just noticing.

### Recalibration on Real Work

Voice evolves. The plugin tracks when a register was last calibrated and prompts you when a fresh sample is needed:

"A fresh writing sample for professional email is needed. The next professional email you write will be used to calibrate this register."

You opt in. You write your real email with intentionality - aware that this one is being observed, aware that this is a moment to show how you're writing now. The email gets sent. It serves its actual purpose. The plugin updates your profile from real work, not throwaway exercises.

This creates a micro-moment of craft every time it fires. The awareness itself - "this one counts" - is the plugin doing its job.

### Sovereignty Safeguards

The plugin monitors its own impact on you:

- **Generation ratio tracking:** What percentage of your writing is generated vs. written by you? Is that ratio moving in the direction you want?
- **Atrophy detection:** If you're generating in registers that used to be craft mode, the plugin surfaces it. "You used to write your own team updates. You've generated the last 8. Want to keep delegating or write the next one yourself?"
- **Drift alerts:** If you're defaulting to throughput for everything, the plugin flags it.
- **Evolution tracking:** How has your voice changed since you started? Are your sentences getting tighter? Is your confidence growing? The plugin shows you your own trajectory.

---

## Pairing with Learning Mode

Timbre on its own helps you know your voice and maintain consistency. For writers who want to actively develop their craft - not just preserve it but push it forward - timbre pairs with [learning-mode](https://github.com/block/goose) to create a deeper practice.

When both are installed, learning-mode shifts the agent from "do it for you" to "do it with you." Applied to writing, this means:

- **Craft challenges:** "Rewrite this paragraph in half the words." "Write this email without any qualifiers." "Match the directness of your Slack voice in this formal doc."
- **Register expansion:** You're comfortable in professional email but uncertain in narrative. Learning-mode scaffolds the stretch - showing what the new register calls for, letting you attempt it, reflecting on what worked.
- **Pattern-breaking:** Timbre shows you your habits. Learning-mode helps you decide which habits serve you and which have become ruts. "You always open with acknowledgment. What happens if you lead with the ask?"
- **Growth tracking:** Measurable improvement in specific dimensions over time. Timbre provides the baseline and the mirror. Learning-mode provides the challenges and the progression.

This pairing is for writers who treat writing as a practice - something that develops through intentional effort, not just repetition. Timbre alone is the mirror. Timbre plus learning-mode is the mirror and the coach.

---

## Who This Is For

Writers who want to:
- Know their own voice well enough to wield it intentionally
- Maintain consistency across high-volume communication without sacrificing craft
- Develop their writing practice with a tool that builds capability rather than replacing it
- Reduce rework on routine writing so they can share ideas more quickly - while keeping the creative work for themselves

Writers have their own style and craft. This plugin respects that. It's here if you want it. The goal is to make you a better, more self-aware writer - not to write for you.

---

## What Success Looks Like

After using this plugin for three to six months:

- You can articulate your own voice patterns without consulting the profile
- Your unassisted writing is more confident and consistent than before
- Your generation ratio is trending down (you need the plugin less, not more)
- You notice your own drift in real time, without the plugin flagging it
- You've expanded into registers you weren't comfortable in before

If all of that is true, the plugin did its job. It scaffolded and stepped back.

---

## Installation

```bash
goose extension add timbre --from git+https://github.com/dakotafabro/timbre
```

Or add manually to `~/.config/goose/config.yaml`:

```yaml
extensions:
  timbre:
    enabled: true
    type: stdio
    name: timbre
    description: Writing voice calibration - mirror, generate, and grow your craft
    cmd: uvx
    args:
    - --from
    - git+https://github.com/dakotafabro/timbre
    - mcp_timbre
    timeout: 300
```

---

## Usage

Timbre runs inside a Goose (or any MCP-compatible) session. You interact with it through natural language in your chat. The agent calls the tools on your behalf based on what you say.

### Getting Started

Say any of these to your agent:

- **"Let's calibrate my writing voice"** - Starts the calibration flow. The agent will ask you to provide real writing samples across different registers.
- **"Show me my voice profile"** - Displays your current profile with patterns across registers.
- **"I want to edit my profile"** - Opens your voice-profile.md for manual adjustment.

### Mirror Mode (Reflection)

- **"How does this sound?"** + paste your writing - The agent reflects on how it compares to your established voice. No corrections, just observations.
- **"What's my pattern for emails?"** - Before you write, the agent surfaces your typical patterns for that register.
- **"What's my pattern for Slack messages?"** - Same, for casual communication.
- **"Am I drifting?"** + paste your writing - The agent flags where you've deviated from your baseline. Just noticing.

### Writing Sessions

- **"I'm writing an email, craft mode"** - Starts a session with generation disabled. Mirror only.
- **"I need to write a status update, throughput mode"** - Starts a session where you can provide substance and get a draft in your voice.
- **"I'm working on my blog voice, learning mode"** - Starts a session with scaffolding. The agent shows patterns, suggests what the context calls for, and lets you try.

### Generation (Throughput Mode Only)

- **"Here are my bullet points, draft this as an email"** - You provide the substance, the agent generates in your voice.
- **"Turn these notes into a Slack message"** - Same pattern: your thinking in, polished writing out.
- **"I wrote this rough draft, clean it up in my voice"** - Agent refines while matching your profile.

### Sovereignty & Trajectory

- **"Show me my trajectory"** - Generation ratio, mode distribution, stale registers, alerts.
- **"Am I generating too much?"** - Same as trajectory, focused on the ratio.
- **"Do any registers need recalibration?"** - Checks staleness and prompts for fresh samples on real work.

### Learning Mode

- **"Challenge me"** - Get a craft challenge for your current growth edge.
- **"Help me write more concisely"** - Scaffolding for a specific dimension.
- **"I want to expand into narrative writing"** - Register expansion with scaffolding.

---

## Tool Reference

Under the hood, these are the MCP tools the agent calls:

| Tool | Mode | Description |
|---|---|---|
| `timbre_calibrate` | - | Start or continue voice calibration |
| `timbre_submit_sample` | - | Submit a writing sample for a register |
| `timbre_update_profile` | - | Save/update the voice profile |
| `timbre_profile` | - | View current voice profile |
| `timbre_how_does_this_sound` | Mirror | Reflect on a piece of writing |
| `timbre_what_is_my_pattern` | Mirror | Surface patterns for a given context |
| `timbre_where_am_i_drifting` | Mirror | Flag deviations from established voice |
| `timbre_draft` | All | Start a writing session in a specific mode |
| `timbre_generate` | Throughput | Generate a draft from provided substance |
| `timbre_log_written` | - | Log that the user wrote something themselves |
| `timbre_trajectory` | - | Show generation ratio and evolution |
| `timbre_recalibration_check` | - | Check if registers need fresh samples |

---

## Technical Details

- **Runtime:** FastMCP (Python)
- **Storage:** Local JSON + human-readable markdown profile
- **LLM:** Uses your session's model for analysis and generation
- **Data:** Everything stays on your machine. Exportable. Portable. Yours.

---

## Related Work

This plugin was designed in conversation with:

- **The Ontological Footprint Framework** - A diagnostic for understanding how technology reshapes human capability at scale. The plugin's sovereignty safeguards are a direct application of Restorative Scale design principles.
- **The Three Dimensions of AI Collaboration Maturity** - The plugin's mode system maps to the DOK and ADT dimensions: craft mode keeps you at high cognitive engagement, throughput mode is conscious delegation, learning mode builds capability.
- **The Orchestra Model** - Mirror mode is the maestro listening. Throughput mode is the ensemble executing the maestro's vision. The user never cedes the creative seat.

---

## License

Apache 2.0

---

## Author

[Dakota Fabro](https://github.com/dakotafabro)
