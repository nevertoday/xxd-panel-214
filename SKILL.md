---
name: xxd-panel-214
description: "Create Panel 214 raster artwork: Rough Cut-out Spot with Local Colours. Use when the user invokes xxd-panel-214 or requests this specific visual language."
---

# XXD Panel 214

Create finished PNG artwork from the current user-supplied photograph or image directory. Read `references/original-prompt/zh-CN.md` completely immediately before every generation. That Chinese source brief is the sole creative and aesthetic authority; never summarise, translate, blend, or replace it with this file, a README, a sample, or another Panel.

## Delivery contract

- One source photograph produces its own isolated outputs. Never combine source photographs or reuse another source's subject, wording, or result.
- The canonical presentation is a 3:4 portrait canvas with reality above and the source-brief transformation below, exactly 50:50.
- Support `top-bottom`, `left-right`, `design-only`, and `wallpaper-pack`. Comparison modes always have exactly two equal regions: reality above or left, design below or right. Do not add extra outer canvas regions. Source-required internal grids, frames, image containers and sidebars belong entirely inside the designed region and must be preserved.
- A directory is explicit batch intent. Inventory supported raster files recursively in stable order, report the count, resolve shared settings once, generate each source independently, and account for every success and failure.
- Resolve mode(s), size(s), text mode, locale, wallpaper relationship, device sizes, and output root before generation. Do not infer a silent ratio or locale.

Before asking for unresolved delivery settings, read `references/runtime-preferences.md` completely and follow its reuse / edit / fresh gate. Current explicit requirements win; never reuse source images, exact copy or style decisions.

## Prompt authority

For each output, concatenate the complete verbatim Chinese source brief, then a short delivery preamble, exactly one selected mode contract, exactly one text contract, and only the user's explicit non-style requirements. Runtime additions may change delivery variables only. In `left-right`, explicitly override the source brief's upper/lower positional terms with left/right, preserving its aesthetic instructions and strict equal halves. In `design-only` and `wallpaper-pack`, the design occupies the entire canvas and the source is not displayed. Never add an outer palette, title, slogan, or aesthetic theory.

Text modes are `prompt`, `exact`, and `none`. Resolve the target locale explicitly. Exact text is passed verbatim; text-free output contains no letters, numbers, logos, labels, or pseudo-text. In prompt text mode, follow the source brief’s exact typography, hierarchy, scale, material and placement in the resolved locale. A source-required oversized title must not be reduced to a tiny caption. Exact and text-free requests override wording or presence only; preserve the remaining aesthetic instructions.

Prefer the built-in image tool and make one complete-canvas generation per distinct output. Never feed an intermediate stylisation, another Panel's result, or a sample back through a second transformation pass. If no compatible image route is available, ask the user to enable one or voluntarily provide an API key; never expose secrets. Use `scripts/compose_panel.py` only for exact raster sizing, pixel-preserving composition, or read-only audits, never to invent the design.

## Resource discipline

Generate only the outputs the current user requests. Repository samples are optional documentation, never a runtime prerequisite. See `references/sample-workflow.md` only when maintaining or creating requested sample artwork. Do not generate previews, alternative styles or automatic retries merely because this package has no sample artwork. Report a failed or uncertain acceptance check honestly and ask before extra generation beyond the agreed output count. Reuse the deterministic helpers instead of rewriting them.

## Output and acceptance

Check this Panel against the complete canonical source, including its specific composition, subject scale, medium, palette and image–text relationship. Do not import another Panel's acceptance criteria.

Write final PNGs directly inside one fresh task directory under `~/Desktop/xxd/xxd-panel-214/` or the explicit output root. Use collision-safe filenames; do not create source, mode, or size subdirectories and do not generate an automatic contact sheet.

Inspect every result at full and thumbnail size. Accept only when the source, ratio, and source visibility are correct; for comparison modes, the split direction and exact 50:50 midpoint are correct; the transformed region follows the complete current source brief directly, including its distinctive medium, exact source-brief palette (fixed or source-derived), subject scale, abundant intentional whitespace and specified image–text relationship; text follows the chosen mode and locale; and there is no watermark, SVG substitute, UI, third band, or second-pass artefact.

For linked wallpapers, create one anchor from the original source, then independently recompose each remaining device using the original source plus that anchor. Independent wallpapers receive only the original source.

## References

Before delivery or publication, clean the final images using the available `xxd-strip-ai-meta` workflow and verify the supported provenance metadata is removed. Preserve pixels and colour profiles during cleanup. This is metadata hygiene, not a claim that the artwork was not AI-generated.

- `references/original-prompt/zh-CN.md` — canonical runtime brief
- `references/original-prompt/README.md` — source index and authority note
- `references/runtime-preferences.md` — safe delivery-preference reuse
- `references/xxd-panel-214-prompt.zh-CN.md` and `.en.md` — delivery adapter notes
