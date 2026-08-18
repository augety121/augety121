# Profile README design notes

This profile intentionally uses a **light, self-hosted visual system** instead of stacking many remote README widgets.

## Design goals

- One visual language across hero, featured work, focus map, system map, activity and footer.
- Light surfaces, quiet borders, low-contrast gradients, generous spacing and one restrained accent gradient.
- The profile should still make sense when animations are disabled.
- Core visuals live in this repository as editable SVG files.
- Markdown remains searchable, selectable and easy to maintain.

## Inspiration and components

### beautify-github-readme

Used as a design-method reference: establish content hierarchy first, derive a project-specific visual language, use SVG for visual modules, and keep body content in maintainable Markdown.

### capsule-render

Referenced for its use of clean section silhouettes and gradient rhythm. The public rendering service is **not** a runtime dependency of this profile; the equivalent visual treatment is generated locally into repository-owned SVG assets.

### Platane/snk

Used for the optional contribution animation. A scheduled GitHub Action generates `assets/contribution-snake.svg`, so profile visitors load a repository-owned asset instead of calling a remote image service on each page view.

### skill-icons

Used only for the compact technology icon row. The text immediately below it provides a readable fallback if the remote icon service is unavailable.

### lowlighter/metrics

Referenced for information-density and infographic ideas, but not enabled by default because the richer configurations introduce additional token/workflow maintenance. The profile already has a repository-local GitHub GraphQL stats generator.

## Palette

| Token | Value | Role |
|---|---|---|
| Canvas | `#F7FBFF` | page/card background |
| Surface | `#FFFFFF` | cards |
| Text | `#10233F` | primary text |
| Muted | `#61738D` | secondary text |
| Border | `#DCE8F6` | quiet outlines |
| Blue | `#4F7CFF` | primary accent |
| Cyan | `#4CB9E9` | secondary accent |
| Mint | `#48C9B0` | success/state accent |
| Violet | `#8D7CF7` | runtime/tooling accent |

## Regenerating visual assets

```bash
python scripts/generate_profile_visuals.py
```

The script intentionally uses system font fallbacks and SVG primitives only. There are no remote font or JavaScript dependencies inside the generated visual assets.
