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

## Asset URLs (Updated May 21, 2026)

### Active URLs — in all pages as of May 21, 2026
- Logo (nav, dark/navy background): `https://logo.thomasfencear.com/TF_Logo_White_fixed.svg`
- Logo (nav, white background): `https://logo.thomasfencear.com/TF_Logo_Red_fixed.svg`
- Logo (footer, all pages): `https://logo.thomasfencear.com/TF_Logo_White_fixed.svg`
- See `_skills/tf-nav-footer.md` for which logo goes on which page type. Never guess.
- Favicon: `https://logo.thomasfencear.com/thomas-fence-favicon.svg`
- Images base: `https://images.thomasfencear.com`
- Videos base: `https://videos.thomasfencear.com`
- YouTube channel: `https://www.youtube.com/@ThomasFenceArkansas`

**Logo fix note (May 21, 2026):** Original SVGs had a near-square viewBox (`0 0 6887.75 5241.6`) causing logos to render tiny. Fixed files (`TF_Logo_White_fixed.svg`, `TF_Logo_Red_fixed.svg`) have corrected viewBox `1776 2178 3452 534` (6.46:1 ratio). Old unfixed files (`TF_Logo_White.svg`, `TF_Logo_Red.svg`) still exist in R2 but are NOT used.

Cloudflare R2 custom subdomains connected May 5, 2026. Incident hswtxrx0fkd1 resolved.

### URL swap commands — COMPLETED May 5, 2026. Do not run again.
```bash
grep -rl "pub-7b8614251f5b42d0856b82814f0460de.r2.dev" . | xargs sed -i 's|pub-7b8614251f5b42d0856b82814f0460de.r2.dev|logo.thomasfencear.com|g'
grep -rl "pub-6a40f5c6ad754a17bcd29e0ef9adb06e.r2.dev" . | xargs sed -i 's|pub-6a40f5c6ad754a17bcd29e0ef9adb06e.r2.dev|images.thomasfencear.com|g'
grep -rl "pub-1f3d846fdda54894a47ecf31f412181f.r2.dev" . | xargs sed -i 's|pub-1f3d846fdda54894a47ecf31f412181f.r2.dev|videos.thomasfencear.com|g'
```

---

## Skill Files — Load These For The Tasks Listed

| Task | Load This Skill |
|---|---|
| Any schema work | `_skills/tf-schema.md` |
| Building any page | `_skills/tf-page-template.md` |
| Building a city page | `_skills/tf-city-page.md` |
| 301 redirect map | `_skills/tf-redirect-map.md` |
| Nav or footer | `_skills/tf-nav-footer.md` |
| Rich results / schema audit | `_skills/tf-rich-results.md` |

Always load the relevant skill before writing any code. Skills are the source of truth
for structure, schema, and content rules. Never guess on schema types or redirect destinations.

---

## Site Architecture

### Category 1 — Build with full schema

**Core pages**
- `/` — Homepage
- `/contact/`
- `/about-us/` — canonical. `/company/about-us/` 301s here (meta refresh + Cloudflare rule).
- `/reviews/` — canonical. `/company/testimonials/` 301s here (meta refresh + Cloudflare rule).

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
- `/gates/automated-gates/` — canonical. `/gates/gate-automation/` 301s here.
- `/gates/estate-gates/`
- `/gates/railings/`

**Resource pages**
- `/faqs/`
- `/financing/`
- `/permits/`
- `/warranty/`
- `/photo-gallery/`

**Publications**
- `/publications/`
- `/publications/not-all-cedar-fences-are-created-equal-what-you-need-to-know-before-you-buy/`
- `/publications/more-than-a-boundary-a-guide-to-temporary-fences-in-springdale-arkansas/`
- `/publications/what-is-the-7-year-fence-law-in-northwest-arkansas/`

**Authority hub — keep, do not redirect**
- `/arkansas-fence-company/`

**Legal pages (old — kept for redirect)**
- `/privacy/`
- `/terms/`
- `/accessibility/`

**Licensing page**
- `/licensing/` — Credentials & certifications page (modeled on About Us structure)

**Legal hub + compliance pages (noindex, follow)**
- `/legal/` — Accordion hub linking to all 7 legal pages (FTC-required footer listing)
- `/legal/terms-of-service/`
- `/legal/privacy-policy/`
- `/legal/scope-of-services/`
- `/legal/refund-cancellation-policy/`
- `/legal/service-results-disclaimer/`
- `/legal/testimonial-disclaimer/`
- `/legal/warranty/` — legal warranty page (separate from resource `/warranty/`)

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
- `/blog/category/commercial-fencing/` — noindex on live site (old URL, no redirect needed)
- `/blog/category/permits-regulations/` — noindex on live site (old URL, no redirect needed)
- `/blog/category/wood-fence/` — noindex on live site (old URL, no redirect needed)
- `/blog/category/residential-fencing/` — noindex on live site (old URL, no redirect needed)
- `/blog/category/general/` — noindex on live site (old URL, no redirect needed)
- `/network.cfm` — noindex on live site, legacy file
- `/terms.cfm` — replaced by `/terms/`

### Photo gallery query param redirects

All resolve to the clean gallery URL. No param pages survive.
- `/photo-gallery/index.cfm?type=*` → `/photo-gallery/`
- `/photo-gallery/?type=*` → `/photo-gallery/`

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
| Publications posts | BlogPosting, BreadcrumbList |
| `/faqs/` | FAQPage |
| `/reviews/` | Review, AggregateRating |
| `/licensing/` | LocalBusiness, BreadcrumbList |
| `/legal/` | BreadcrumbList (noindex) |
| `/legal/terms-of-service/` | BreadcrumbList (noindex) |
| `/legal/privacy-policy/` | BreadcrumbList (noindex) |
| `/legal/scope-of-services/` | BreadcrumbList (noindex) |
| `/legal/refund-cancellation-policy/` | BreadcrumbList (noindex) |
| `/legal/service-results-disclaimer/` | BreadcrumbList (noindex) |
| `/legal/testimonial-disclaimer/` | BreadcrumbList (noindex) |
| `/legal/warranty/` | BreadcrumbList (noindex) |
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

## Button Destination Map — Locked. Use Exactly This Everywhere.

Every CTA button on every page must link to exactly these destinations. No variations.

| Button / CTA Text | Destination |
|---|---|
| Get a Free Estimate | `/contact/` |
| Contact Us | `/contact/` |
| Instant Fence Estimator / Get a Quote | `https://thomasfence.mybudgetquote.com/budget` |
| Apply for Financing / Get Started (financing) | `https://app.gethearth.com/partners/thomas-fence/darrell/apply` |
| Join Our Team | `https://thomasfencear.hireclick.com/jobboard/` (opens in new tab) |
| Directions / map pin / Find Us | `https://goo.gl/maps/iofQNA6qrftW2DpL9` (opens in new tab) |
| Email | `mailto:sales@thomasfencear.com` |
| Phone | `tel:+14796364732` — always formatted as `(479) 636-4732` in display text |

Notes:
- Join Our Team and Directions always open in a new tab (`target="_blank" rel="noopener noreferrer"`)
- The estimator and financing links also open in a new tab — they are third-party tools
- `/contact/` stays internal — never opens in a new tab

---

## Business Hours — Locked

Monday–Friday: 8:00am – 4:00pm
Closed Saturday and Sunday.
Use exactly this format everywhere: **Mon–Fri, 8am–4pm**

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

## .ENV — ABSOLUTE RULE — NO EXCEPTIONS
- NEVER read, open, copy, reference, or touch any .env file in any project — ever
- NEVER copy an API key from anywhere — not from another .env, not from memory, not from any source
- If a .env file needs to be created, create it empty and wait for the user to provide the key
- NEVER read .gitignore to infer what is sensitive and then go look at it anyway
- This rule applies to every project in the VSC Project Files folder and everywhere else

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

1. ✓ DONE May 5, 2026 — Run logo URL swap command
2. ✓ DONE May 5, 2026 — Run images URL swap command
3. ✓ DONE May 5, 2026 — Run videos URL swap command
4. Visual check — 3 pages, images, logo, and videos confirmed loading
5. Switch DNS A record to GitHub Pages IP
6. Confirm Cloudflare SSL active
7. Submit sitemap.xml to Google Search Console
8. Submit sitemap.xml to Bing Webmaster Tools
9. Verify 301 redirects firing correctly
10. Monitor 48 hours

---

## Open Items (as of May 25, 2026)

**Pending — not yet done:**
- Client logos for `/reviews/` "Customers We've Worked With" section — pending 17 company names from Greg
- YouTube graphics for @ThomasFenceArkansas: profile picture (800×800px) + channel banner (2560×1440px) — Greg to source
- Greg email `greg-email-may21.txt` has `[INSERT VIDEO LINK HERE]` placeholder — insert YouTube video link before sending

**Completed May 25, 2026:**
- ✓ Cloudflare Bulk Redirect rules live: `/company/about-us/` → `/about-us/` and `/gates/gate-automation/` → `/gates/automated-gates/`
- ✓ Video Gallery page `/video-gallery/` — 21 gate videos, VideoObject schema, added to nav sitewide (45 pages)
- ✓ Logo SVG viewBox defect fixed — `TF_Logo_White_fixed.svg` + `TF_Logo_Red_fixed.svg` deployed sitewide (May 21)
- ✓ YouTube @ThomasFenceArkansas channel — footer icon added sitewide (45 pages), added to `sameAs` schema sitewide
- ✓ Gate Installation Videos — 6 YouTube embeds + VideoObject schema on `/gates/automated-gates/` (3×2 grid)
- ✓ Estate Gates page rebuilt — showcase-row pattern (5 geotagged images, hover zoom, AI-readable per row)
- ✓ Photo gallery Estate Gates section added (9 geotagged images, `id="estate-gates"` anchor)
- ✓ Photo gallery broken images fixed (Gates & Fences: 3 replaced; Farm Fencing: 1 replaced)

**Previously resolved:**
- ✓ BuildZoom entity conflict (Mark Thomas Fence Company LLC) — resolved April 24, 2026
- ✓ Birdeye entity conflict — resolved May 7, 2026
- ✓ Manta entity conflict — resolved May 11, 2026

---

*Nicole Jolie | Socially Smashing, LLC | Be the brand AI recommends first.*
