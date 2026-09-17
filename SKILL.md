---
name: bikini-bottom-econ-video-skill
description: "Create character-driven economics, business, workplace, or consumer short videos in a Bikini Bottom style; use for scripts, element-based storyboards, asset plans, and restrained Remotion editing."
---

# 比奇堡财经视频工作流

Turn an abstract economics, business, workplace, or consumer topic into a narration-led animated short video. The default world is Bikini Bottom, but the production method is character-system agnostic: the user may replace the cast and supplied assets with Rick and Morty, Tom and Jerry, Detective Conan, original characters, or another authorized universe.

## Start with scope

Read the user's existing script, subtitle file, storyboard, asset folder, and desired deliverable before creating anything. Confirm or infer:

- target duration, aspect ratio, and whether the result is a script, storyboard, asset plan, preview, or final video;
- the selected character universe and the assets the user is authorized to use;
- whether image generation, cutout processing, or video rendering has been authorized.

For public or commercial work, remind the user that a recognizable franchise, character art, audio, font, and reference video may need permission. Never include third-party character art, show footage, audio, or user material in this skill repository.

## Choose the stage

1. **Script** — Read [script method](references/script-method.md). Begin with a concrete, emotional hook in the first two seconds; explain the mechanism through a character problem before naming it.
2. **Storyboard** — Read [storyboard grammar](references/storyboard-grammar.md). Map each spoken phrase to an information group and an atomic visual asset plan.
3. **Assets** — Read [asset pipeline and QA](references/assets-and-qa.md). Generate or source one role action or one independent prop at a time; do not use a multi-character collage as a substitute for editable assets.
4. **Remotion edit** — Read [storyboard grammar](references/storyboard-grammar.md) and [asset pipeline and QA](references/assets-and-qa.md). Keep the background stable and make foreground entries follow narration timing, not a global transition preset.
5. **Preflight** — Use the checklist in [asset pipeline and QA](references/assets-and-qa.md) before a full render. Make a short preview before a long render when timing or assets changed materially.

## Non-negotiable visual rules

- Use a stable world background when the user requests it; it sits behind the story at reduced prominence. A door, shop, road, stair, sign, rail, or other spoken object is a foreground asset, not a permanent decoration.
- Count **information groups**, not PNG files. A character with a built-in hand-held item is one group. Independent people, objects, or mechanisms are separate groups.
- One group is centered. Two groups form a compact, centered pair. Three groups use left / center / right. All peer subjects share one visual baseline and must retain real alpha-boundary spacing.
- Plan all final slots before the first group enters. A left subject begins near the left slot; it never first appears in the centre and then moves aside for a later subject.
- Introduce foreground in the exact order the narration mentions it. Do not pre-load a later character, number, label, or result.
- Use short, readable, local entrances. Do not send left-slot items across from the right, cross over another subject, globally fade every scene, or add motion simply to make a static image move.
- Normal frames communicate through role actions and props. Text pages are rare, use the narration's exact key sentence, and retain the established background instead of cutting to an unrelated title card.
- Do not repeat a role pose as the main visual in different semantic units unless the user explicitly accepts the reuse.

## Deliverables

Use the templates in `templates/` when producing files. Preserve the user's established table fields when they already have a production template.

- `script.md` — titles, narration, factual notes.
- `storyboard.md` — timing, narration mapping, information groups, final slots, assets, and entrance order.
- `asset-manifest.json` — source / generated asset inventory, ownership, alpha QA, and allowed timeline usage.

Use `scripts/validate_asset_manifest.py` before a final render when an asset manifest is available. It catches reused role poses and basic asset/slot declaration mistakes; it does not replace visual alpha-boundary and timing review.
