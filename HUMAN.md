# timbre - what changes for you

timbre helps you know your own writing voice. It's a mirror first. Generating writing is something you opt into, never the default. 

## What it does to the agent

You give it real writing across registers (email, Slack, docs, narrative). It builds a voice profile: sentence rhythm, how you open and close, hedging, structure, tone. Then you pick a mode:

- **Craft** - mirror only. It reflects and flags drift, and never generates.
- **Throughput** - you bring the substance (bullets, outline, rough draft) and it drafts in your voice. It never writes from nothing.
- **Learning** - it shows your patterns and suggests what the context calls for, and you try.

It tracks how much of your writing is generated versus your own, and tells you if that ratio climbs.

## When to use it

When you want to notice how you write, or keep your voice steady across contexts. Use craft mode for anything you want to own deeply.

## Reserved for human judgment

Your voice is yours. The profile is a readable file you can edit by hand. When timbre asks "could you write effectively without this tomorrow?", the answer and what to do about it are yours.

## What it reads, writes and sends

- Writes your profile to `~/.timbre/voice-profile.md` and tracking state to `~/.timbre/state.json`.
- Reads the samples you paste in.
- Network use by the server: not documented. The install command pulls it from GitHub.

## Cost

About 1,800 tokens of context (`token_cost` in bpm.json).

## Check it's working

Say "show me my voice profile" after calibrating, or "show me my trajectory" for the generation ratio.

## Turn it off

Remove the `timbre` extension from your goose config, then `bpm remove timbre`. Your `~/.timbre/` folder stays unless you delete it.
