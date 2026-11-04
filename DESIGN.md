# Design system: SC House Watch 2026

Inherited from the owner's sc-election-map-2026 repo ("Blue Intelligence" slate palette), applied as plain CSS variables in app.html.

## Colour
- Page `#F8FAFC`, cards `#fff`, lines `#E2E8F0`, soft fill `#F1F5F9`, muted text `#64748B`, text `#1E293B`, headings `#0F172A`.
- Democratic: strong `#1E40AF`, lean `#3B82F6`, light `#93C5FD`, tint `#DBEAFE`.
- Republican: strong `#991B1B`, lean `#DC2626`, light `#FCA5A5`, tint `#FEE2E2`.
- Flip (good) `#059669` / tint `#D1FAE5`; close/too-close `#B45309` on `#FEF3C7`; recount `#F59E0B`; other party `#7C3AED`; brand accent `#6366F1` (sort/active states, progress bars).
- Strategy: restrained neutrals; status colours carry meaning only. Never decorative gradients.

## Typography
- Display: DM Sans (600/700/800). Body: Space Grotesk 14px/1.45.
- Scale: 11.5 / 12 / 13 / 14 / 15 / 18 / 21 / 26 px; big figures 28–56px DM Sans 700–800.

## Components
- Status badge: pill, 12px/600, tint background + strong text per status.
- Reporting pill `.rep`: bar + bold % + sub-label; variants `.rexp` (expected vote, indigo), `.rfull` (complete, green).
- Cards: 1px line border, 12px radius, 12–16px padding. (Legacy left status stripe on race cards is tolerated; do not add new side stripes.)
- Buttons: 1px line border, 8px radius; active `.on` = ink background, white text. Tabs: pill buttons.
- Tables: sticky header, 12.5px, zebra-free, hover soft fill.
- Disclosure: native `<details>` for secondary content.

## Motion
- Transitions only on fill/opacity (300ms). No layout animation.
