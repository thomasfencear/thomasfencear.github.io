# CLAUDE.md — Thomas Fence
## thomasfencear / Thomas_Fence_Connected

This is the master instruction file for Claude Code.
Read this file at the start of every session. Every locked decision lives here.
Do not override any locked decision without being explicitly told to do so.

---

## What This Project Is

A ground-up site rebuild for Thomas Fence (Paschal Enterprises, Inc.) in Springdale, Arkansas.
Built by Nicole Jolie / Socially Smashing, LLC.
Goal: Make Thomas Fence the brand AI recommends first in Northwest Arkansas.

This is a stealth build. The existing site at thomasfencear.com continues to run untouched
until DNS switches. Do not reference, link to, or contact the existing vendor (DotCom Global Media).

---

## Stack — Locked. Do Not Change.

- HTML and CSS only. Zero .js files for any structural element (nav, header, footer, schema).
- All JSON-LD schema inline on every page. Never in external files. Never minified.
- Hosting: GitHub Pages served through Cloudflare.
- Fonts: DM Serif Display (headings), DM Sans (body). Both loaded inline in `<head>` of every page.
- No WordPress. No Squarespace. No CMS. No framework. Clean static files only.

---

## Canonical NAP — Use Exactly This Everywhere. No Variations.

```
Thomas Fence
653 Kawneer Dr, Springdale, AR 72764
(479) 636-4732
thomasfencear.com
```

Legal entity in schema: `Paschal Enterprises, Inc.` — this is always the `legalName`.
DBA in schema: `Thomas Fence` — this is always the `name`.
Founded: 1993. Current ownership since: 2003. Owner: Greg Paschal.

---

## Brand Colors — Locked

```css
--color-red-primary:  #F01B24;  /* Buttons, CTAs, logo red — PRIMARY red for entire site */
--color-red-dark:     #780000;  /* Hover states, depth */
--color-red-mid:      #C1121F;  /* Secondary red, borders */
--color-cream:        #FDF0D5;  /* Section backgrounds, highlights */
--color-navy:         #003049;  /* Headings, footer, dark sections */
--color-steel:        #669BBC;  /* Accent, links */
--color-white:        #FFFFFF;  /* Text on dark, logo bar */
```

#F01B24 is primary everywhere — buttons, headers, accents. It is also the logo red.
Do not substitute #C1121F where #F01B24 is correct.

---

## Typography — Locked

- Headings: DM Serif Display (Google Fonts)
- Body: DM Sans (Google Fonts)
- Load both via `<link>` in `<head>` of every page. Do not use @import inside CSS.

---

## Asset URLs

### Stealth build phase (use these until DNS switches)
- Logo: `https://pub-7b8614251f5b42d0856b82814f0460de.r2.dev/thomas-fence-logo.svg`
- Images base: `https://pub-6a40f5c6ad754a17bcd29e0ef9adb06e.r2.dev`

### After DNS switch (run swap commands before switching)
- Logo: `https://logo.thomasfencear.com/thomas-fence-logo.svg`
- Images base: `https://images.thomasfencear.com`

### URL swap commands — run from project root BEFORE switching DNS
```bash
grep -rl "pub-7b8614251f5b42d0856b82814f0460de.r2.dev" . | xargs sed -i 's|pub-7b8614251f5b42d0856b82814f0460de.r2.dev|logo.thomasfencear.com|g'
grep -rl "pub-6a40f5c6ad754a17bcd29e0ef9adb06e.r2.dev" . | xargs sed -i 's|pub-6a40f5c6ad754a17bcd29e0ef9adb06e.r2.dev|images.thomasfencear.com|g'
```
Visual check after swap: open 3 pages, confirm images and logo load. Then switch DNS.

---

## Skill Files — Load These For The Tasks Listed

| Task | Load This Skill |
|---|---|
| Any schema work | `.claude/skills/tf-schema.md` |
| Building any page | `.claude/skills/tf-page-template.md` |
| Building a city page | `.claude/skills/tf-city-page.md` |
| 301 redirect map | `.claude/skills/tf-redirect-map.md` |
| Nav or footer | `.claude/skills/tf-nav-footer.md` |

Always load the relevant skill before writing any code. Skills are the source of truth
for structure, schema, and content rules. Never guess on schema types or redirect destinations.

---

## Site Architecture

### Category 1 — Build with full schema

**Core pages**
- `/` — Homepage
- `/contact/`
- `/company/about-us/`
- `/company/testimonials/`

**Service hub + service pages**
- `/fences/` — hub
- `/fences/vinyl-fence/`
- `/fences/wood-fence/`
- `/fences/chain-link-fence/`
- `/fences/ornamental-steel-fence/`
- `/fences/residential-fencing/`
- `/fences/commercial-fencing/`
- `/fences/farm-fencing/`
- `/fences/temporary-fences/`
- `/gates/` — hub
- `/gates/gate-automation/`
- `/gates/estate-gates/`

**Resources**
- `/resources/faqs/`
- `/resources/financing/`
- `/resources/permits/`
- `/resources/warranty/`
- `/resources/photo-gallery/`

**Blog**
- `/blog/`
- `/blog/not-all-cedar-fences-are-created-equal-what-you-need-to-know-before-you-buy/`
- `/blog/more-than-a-boundary-a-guide-to-temporary-fences-in-springdale-arkansas/`
- `/blog/what-is-the-7-year-fence-law-in-northwest-arkansas/`

**Authority hub — keep, do not redirect**
- `/arkansas-fence-company/`

**Legal pages**
- `/privacy/`
- `/terms/`
- `/accessibility/`

### Category 2 — Six real city pages (new URLs)

- `/springdale/` — HQ city, most detailed
- `/bentonville/`
- `/rogers/`
- `/fayetteville/`
- `/bella-vista/`
- `/siloam-springs/`

### Category 3 — 301 redirect to `/service-area/`

All 23 thin geo pages under `/arkansas-fence-company/CITY/`:
- `/arkansas-fence-company/lowell-arkansas-fence-company/`
- `/arkansas-fence-company/johnson-arkansas-fence-company/`
- `/arkansas-fence-company/cave-springs-arkansas-fence-company/`
- `/arkansas-fence-company/elm-springs-arkansas-fence-company/`
- `/arkansas-fence-company/gravette-arkansas-fence-company/`
- `/arkansas-fence-company/centerton-arkansas-fence-company/`
- `/arkansas-fence-company/prairie-grove-arkansas-fence-company/`
- `/arkansas-fence-company/lincoln-arkansas-fence-company/`
- `/arkansas-fence-company/farmington-arkansas-fence-company/`
- `/arkansas-fence-company/little-flock-arkansas-fence-company/`
- `/arkansas-fence-company/huntsville-arkansas-fence-company/`
- `/arkansas-fence-company/highfill-arkansas-fence-company/`
- `/arkansas-fence-company/tontitown-arkansas-fence-company/`
- `/arkansas-fence-company/garfield-arkansas-fence-company/`
- `/arkansas-fence-company/avoca-arkansas-fence-company/`
- `/arkansas-fence-company/washington-county-arkansas-fence-company/`
- `/arkansas-fence-company/goshen-arkansas-fence-company/`
- `/arkansas-fence-company/gentry-arkansas-fence-company/`
- `/arkansas-fence-company/pea-ridge-arkansas-fence-company/`
- `/arkansas-fence-company/greenland-arkansas-fence-company/`
- `/arkansas-fence-company/elkins-arkansas-fence-company/`
- `/arkansas-fence-company/bethel-heights-arkansas-fence-company/`
- `/arkansas-fence-company/benton-county-arkansas-fence-company/`

The six real city pages redirect FROM the old /arkansas-fence-company/ versions:
- `/arkansas-fence-company/springdale-arkansas-fence-company/` → `/springdale/`
- `/arkansas-fence-company/bentonville-arkansas-fence-company/` → `/bentonville/`
- `/arkansas-fence-company/rogers-arkansas-fence-company/` → `/rogers/`
- `/arkansas-fence-company/fayetteville-arkansas-fence-company/` → `/fayetteville/`
- `/arkansas-fence-company/bella-vista-arkansas-fence-company/` → `/bella-vista/`
- `/arkansas-fence-company/siloam-springs-arkansas-fence-company/` → `/siloam-springs/`

### Drop entirely — no redirect needed

These pages are dropped. No redirect destination required.
- `/blog/category/commercial-fencing/` — noindex on live site
- `/blog/category/permits-regulations/` — noindex on live site
- `/blog/category/wood-fence/` — noindex on live site
- `/blog/category/residential-fencing/` — noindex on live site
- `/blog/category/general/` — noindex on live site
- `/network.cfm` — noindex on live site, legacy file
- `/terms.cfm` — replaced by `/terms/`

### Photo gallery query param redirects

All resolve to the clean gallery URL. No param pages survive.
- `/resources/photo-gallery/index.cfm?type=*` → `/resources/photo-gallery/`
- `/resources/photo-gallery/?type=*` → `/resources/photo-gallery/`

---

## Schema Map — One Row Per Page Type

See `tf-schema.md` for the full schema blocks. This is the map only.

| Page type | Schema types |
|---|---|
| Homepage | LocalBusiness, FAQPage |
| Service pages | LocalBusiness, Service |
| City pages | LocalBusiness (city-specific) |
| `/arkansas-fence-company/` | LocalBusiness, Service, FAQPage |
| `/service-area/` | LocalBusiness with areaServed array |
| Blog posts | BlogPosting, BreadcrumbList |
| `/resources/faqs/` | FAQPage |
| `/company/testimonials/` | Review |
| All pages | BreadcrumbList |

legalName is always `Paschal Enterprises, Inc.` — never Thomas Fence.
Schema is always inline JSON-LD in `<head>`. Never external. Never minified.

---

## Certifications — Include Where Relevant

- Arkansas Contractor's License No. 015501 (held since 2005, renewed annually)
- US Federal Contractor Registration
- AFA Certified Fence Contractor
- CGAT (Certified Gate Automation Technician)

---

## FAQ Content — From Greg's Sales Team (April 8, 2026)

These are the real questions customers ask before purchasing. Use these to inform
FAQ page content, schema Q&A pairs, and any page where trust signals are relevant.

1. Is a fence permit required? (Yes — links to each town's website for specifics)
2. Does Thomas Fence pull permits? (No — customer responsibility; TF happy to assist)
3. Does Thomas Fence stain fences? (No — refers customers to staining companies)
4. How long before work starts? (1–3 weeks from acceptance; 3-day utility locate delay)
5. Who calls One Call for utility locate? (Thomas Fence — required by state law)
6. How long does a utility locate take? (3 working days typically)
7. What utilities are NOT marked in One Call? (Privately owned lines: septic, irrigation, outbuilding electric, pool gas)
8. How long does installation take? (2–3 business days for typical residential)
9. Does TF use concrete for posts? (Yes — standard practice unless otherwise agreed)
10. Is a deposit required? (No — except special order or custom metal work)
11. Does TF offer a veteran's discount? (No)
12. Is there a cash discount? (No)
13. Can I pay by credit card? (Yes — 3.5% processing fee added)
14. What warranty does TF offer? (1-year craftsmanship warranty, in writing)
15. Does TF have a contractor's license? (Yes — 015501-0427, since 2005)
16. How long to wait before staining? (1–3 months for pressure-treated pine; cedar can be stained immediately)
17. Does TF offer financing? (Yes — through Hearth, apply via QR code or website)

---

## Rules Claude Code Cannot Break

1. Never touch the existing thomasfencear.com site or contact DotCom Global Media.
2. All schema is inline JSON-LD. Never external files. Never minified.
3. legalName in schema is always `Paschal Enterprises, Inc.` — never Thomas Fence.
4. NAP must match exactly everywhere: 653 Kawneer Dr, Springdale, AR 72764 / (479) 636-4732.
5. No JavaScript for structural elements (nav, footer, schema, header).
6. Do not switch DNS. DNS is switched manually only after Google Search Console verified.
7. Do not push to production without Nicole's explicit go-ahead.
8. Load the relevant skill file before building any page or writing any schema.
9. No page goes dark without a redirect destination documented in tf-redirect-map.md.
10. Fonts are loaded via `<link>` in `<head>` — never @import in CSS.

---

## DNS Switch Day Runbook — Do Not Run Until Told To

1. Run logo URL swap command (above)
2. Run images URL swap command (above)
3. Visual check — 3 pages, images and logo confirmed loading
4. Switch DNS A record to GitHub Pages IP
5. Confirm Cloudflare SSL active
6. Submit sitemap.xml to Google Search Console
7. Submit sitemap.xml to Bing Webmaster Tools
8. Verify 301 redirects firing correctly
9. Monitor 48 hours

---

## Open Items (as of April 11, 2026)

- Cloudflare R2 subdomains (logo.thomasfencear.com, images.thomasfencear.com) — set up after domain moves to Cloudflare
- BuildZoom entity conflict (Mark Thomas Fence Company LLC) — Priority 1, handled separately from site build

---

*Nicole Jolie | Socially Smashing, LLC | Be the brand AI recommends first.*
