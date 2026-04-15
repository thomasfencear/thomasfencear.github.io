# tf-city-page.md — Thomas Fence City Page Template

**Load this file before building or editing any city page.**
The approved reference pages are `/springdale/` (HQ city, most detailed) and `/bentonville/`.
Every city page must match this structure exactly.

---

## The Six City Pages

| City | URL | Image filename on R2 | Notes |
|---|---|---|---|
| Springdale | `/springdale/` | `Springdale-Arkansas-Chamber-of-Commerce.png` | HQ city — mention 653 Kawneer Dr, founded here 1993 |
| Bentonville | `/bentonville/` | `Bentonville-Chamber-home-page-pic-city-overview.jpg` | Walmart HQ, HOA angle |
| Rogers | `/rogers/` | TBD — get from Nicole | |
| Fayetteville | `/fayetteville/` | TBD — get from Nicole | |
| Bella Vista | `/bella-vista/` | TBD — get from Nicole | |
| Siloam Springs | `/siloam-springs/` | TBD — get from Nicole | |

---

## Page Structure — Seven Zones, In Order

```
┌─────────────────────────────────────────────┐
│  ZONE 1 — Navy Hero                         │
│  H1 · subtitle mentioning 1993 · CTA        │
├─────────────────────────────────────────────┤
│  ZONE 2 — Red Trust Bar                     │
│  5 credentials across full width            │
├─────────────────────────────────────────────┤
│  CITY PHOTO — Full-width image              │
│  Chamber or local source · correct alt text │
├─────────────────────────────────────────────┤
│  ZONE 3 — Intro  (Cream background)        │
│  2–3 paragraphs of real local content       │
├─────────────────────────────────────────────┤
│  ZONE 4 — Services Grid  (White)           │
│  9 cards linking to service pages           │
├─────────────────────────────────────────────┤
│  ZONE 5 — Process  (Navy)                  │
│  4 steps — standard across all cities       │
├─────────────────────────────────────────────┤
│  ZONE 6 — Warranty  (Cream)               │
│  Shield box — standard across all cities    │
├─────────────────────────────────────────────┤
│  ZONE 7 — FAQs + Sidebar  (White)         │
│  6 FAQs LEFT · Full sidebar RIGHT          │
└─────────────────────────────────────────────┘
Then: Related Services (Cream) → CTA Band (handled by styles.css)
```

---

## Zone 1 — Navy Hero

```html
<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <ol>
        <li><a href="/">Home</a></li>
        <li aria-current="page">Fence Company in [City], AR</li>
      </ol>
    </nav>
    <h1>Fence Company in [City], Arkansas</h1>
    <p class="page-hero__sub">[One sentence specific to this city. Always mention 1993. For Springdale: mention it is headquarters.]</p>
    <a href="/contact/" class="btn-primary">Get a Free Estimate</a>
  </div>
</section>
```

**Rules:**
- H1 format is always: `Fence Company in [City], Arkansas`
- Subtitle must mention 1993 and something specific to this city
- Springdale subtitle must mention "headquartered here" — no other city gets that language

---

## Zone 2 — Trust Bar

```html
<section class="trust-bar" aria-label="Credentials">
  <div class="container">
    <ul class="trust-bar__list">
      <li>Serving NWA Since 1993</li>
      <li>AR License No. 015501</li>
      <li>AFA Certified Fence Contractor</li>
      <li>CGAT Certified Gate Automation</li>
      <li>1-Year Workmanship Warranty</li>
    </ul>
  </div>
</section>
```

Identical on every city page. Handled entirely by styles.css — no inline CSS needed.

---

## City Photo

```html
<div class="city-photo">
  <img
    src="https://pub-6a40f5c6ad754a17bcd29e0ef9adb06e.r2.dev/[filename]"
    alt="[City], Arkansas — photo courtesy of the [Source Name]"
    width="1600"
    height="460"
    loading="eager"
  >
</div>
```

**Alt text format:** `[City], Arkansas — photo courtesy of the [Source]`
- Springdale: `Springdale, Arkansas — photo courtesy of the Springdale Chamber of Commerce`
- Bentonville: `Bentonville, Arkansas city overview — photo courtesy of the Bentonville Area Chamber of Commerce`
- All others: match the same format using the actual image source

**CSS (inline `<style>` block on each page):**
```css
.city-photo { width: 100%; line-height: 0; }
.city-photo img { width: 100%; max-height: 460px; object-fit: cover; object-position: center; display: block; }
```

---

## Zone 3 — Intro (Cream)

```html
<section class="page-intro">
  <div class="container">
    <h2>[City-specific heading — not generic]</h2>
    <p>[Paragraph 1 — local identity, population, economy, or what makes this city distinct]</p>
    <p>[Paragraph 2 — neighborhoods, growth, HOA context if relevant, property types]</p>
    <p>[Paragraph 3 — what Thomas Fence does here specifically; tie local context to fencing demand]</p>
  </div>
</section>
```

**Content rules:**
- Minimum 2 paragraphs. Springdale gets 3 because it is HQ city.
- Pull real facts from the city's Chamber of Commerce site or official community profile
- Always mention Thomas Fence by name in the last paragraph of this section
- Springdale only: mention 653 Kawneer Dr and that this is headquarters
- Never use boilerplate phrases like "thriving community" or "great place to live" — use specific facts
- Include at least one local landmark, employer, neighborhood, or event per city

**CSS:**
```css
.page-intro { background: var(--color-cream); padding: 64px 0; }
.page-intro h2 { font-size: 1.9rem; margin-bottom: 20px; color: var(--color-navy); }
.page-intro p { font-size: 1.05rem; line-height: 1.8; margin-bottom: 16px; max-width: 820px; color: #1a1a1a; }
```

---

## Zone 4 — Services Grid (White)

```html
<section class="services-grid-section">
  <div class="container">
    <h2>Fencing Services We Provide in [City]</h2>
    <div class="services-grid">
      <a href="/fences/vinyl-fence/" class="services-grid__card">
        <h3>Vinyl Fence</h3>
        <p>[City-specific one-liner about vinyl in this market]</p>
      </a>
      <!-- 9 cards total — see list below -->
    </div>
  </div>
</section>
```

**9 cards, always in this order:**
1. Vinyl Fence → `/fences/vinyl-fence/`
2. Wood Fence → `/fences/wood-fence/`
3. Chain Link Fence → `/fences/chain-link-fence/`
4. Ornamental Steel Fence → `/fences/ornamental-steel-fence/`
5. Commercial Fencing → `/fences/commercial-fencing/`
6. Residential Fencing → `/fences/residential-fencing/`
7. Temporary Fencing → `/fences/temporary-fences/`
8. Gate Automation → `/gates/gate-automation/`
9. Estate Gates → `/gates/estate-gates/`

Each card description should be 1–2 sentences, city-specific where possible. Do not use identical descriptions on every city page.

**CSS:**
```css
.services-grid-section { background: var(--color-white); padding: 64px 0; }
.services-grid-section h2 { font-size: 1.9rem; margin-bottom: 36px; color: var(--color-navy); }
.services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.services-grid__card { border: 2px solid var(--color-cream); border-radius: 8px; padding: 28px 24px; text-decoration: none; color: var(--color-navy); transition: border-color 0.2s, box-shadow 0.2s; }
.services-grid__card:hover { border-color: var(--color-red-primary); box-shadow: 0 4px 16px rgba(0,0,0,0.10); }
.services-grid__card h3 { font-family: var(--font-heading); font-size: 1.1rem; margin: 0 0 8px; color: var(--color-navy); }
.services-grid__card p { font-size: 0.93rem; line-height: 1.6; margin: 0; color: #3a3a3a; }
@media (max-width: 860px) { .services-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 540px) { .services-grid { grid-template-columns: 1fr; } }
```

---

## Zone 5 — Process (Navy)

Identical on every city page. Only the Step 1 call-out changes to name the city.

```html
<section class="page-process">
  <div class="container">
    <h2>How It Works</h2>
    <p>Four straightforward steps from your first call to a finished fence.</p>
    <div class="process-grid">
      <div class="process-card">
        <p class="process-card__num">Step 1</p>
        <h3>Schedule Your Free Estimate</h3>
        <p>Call <a href="tel:+14796364732">(479) 636-4732</a> or fill out our contact form. We'll schedule a visit at your [City] property to measure and review your options.</p>
      </div>
      <div class="process-card">
        <p class="process-card__num">Step 2</p>
        <h3>Approve &amp; Sign</h3>
        <p>Accept your estimate by phone, email, or with your sales rep. We send a written contract for your signature. No deposit required for standard installations.</p>
      </div>
      <div class="process-card">
        <p class="process-card__num">Step 3</p>
        <h3>Get on the Schedule</h3>
        <p>Once signed, your project is in line. Standard residential jobs are typically scheduled within 1 to 3 weeks. We handle the 811 utility locate call.</p>
      </div>
      <div class="process-card">
        <p class="process-card__num">Step 4</p>
        <h3>Installation Day</h3>
        <p>Our crew arrives on time, handles all ground prep and concrete setting, and walks you through the finished job before we leave. Most residential fences install in 2–3 business days.</p>
      </div>
    </div>
  </div>
</section>
```

**CSS:**
```css
.page-process { background: var(--color-navy); padding: 72px 0; }
.page-process h2 { color: var(--color-white); font-size: 1.9rem; margin-bottom: 12px; }
.page-process > .container > p { color: rgba(255,255,255,0.82); margin-bottom: 40px; font-size: 1.02rem; max-width: 700px; }
.process-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
@media (max-width: 900px) { .process-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 560px) { .process-grid { grid-template-columns: 1fr; } }
.process-card { background: rgba(255,255,255,0.07); border-radius: 8px; padding: 28px 24px; border-top: 4px solid var(--color-red-primary); }
.process-card__num { font-size: 0.72rem; font-weight: 700; color: var(--color-red-primary); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 10px; }
.process-card h3 { color: var(--color-white); font-family: var(--font-heading); font-size: 1.05rem; margin: 0 0 10px; }
.process-card p { color: rgba(255,255,255,0.78); font-size: 0.92rem; margin: 0; line-height: 1.6; }
.process-card a { color: var(--color-cream); }
```

---

## Zone 6 — Warranty (Cream)

Nearly identical on every city page — only the city name changes in the body copy.

```html
<section class="page-warranty">
  <div class="container">
    <div class="warranty-box">
      <div class="warranty-box__icon">&#128737;</div>
      <div class="warranty-box__text">
        <h2>1-Year Workmanship Warranty</h2>
        <p>Thomas Fence provides a written 1-year workmanship warranty on every installation in [City]. We use materials from reputable manufacturers — many of which carry their own product warranties for additional long-term protection. If something is not right with the work, we come back and make it right. In writing, every time.</p>
      </div>
    </div>
  </div>
</section>
```

**CSS:**
```css
.page-warranty { background: var(--color-cream); padding: 56px 0; }
.warranty-box { background: var(--color-white); border-radius: 10px; padding: 44px 52px; border-left: 6px solid var(--color-red-primary); box-shadow: 0 2px 14px rgba(0,0,0,0.08); display: flex; gap: 32px; align-items: center; }
.warranty-box__icon { font-size: 3rem; flex-shrink: 0; line-height: 1; }
.warranty-box__text h2 { font-size: 1.6rem; margin-bottom: 12px; color: var(--color-navy); }
.warranty-box__text p { font-size: 1.02rem; line-height: 1.75; margin: 0; color: #2a2a2a; }
@media (max-width: 600px) { .warranty-box { flex-direction: column; gap: 16px; padding: 32px 28px; } }
```

---

## Zone 7 — FAQs + Sidebar (White)

```html
<section class="page-faqs">
  <div class="container">
    <div class="page-faqs__grid">

      <div>
        <h2>[City] Fencing FAQs</h2>

        <!-- 6 FAQ items — see FAQ rules below -->

      </div>

      <aside>
        <div class="sidebar-cta">
          <h3>Get a Free Estimate</h3>
          <p>Thomas Fence serves [City] and all of Northwest Arkansas. No deposit required for standard residential installations.</p>
          <a href="/contact/" class="btn-primary">Contact Us</a>
          <p class="sidebar-cta__phone"><a href="tel:+14796364732">(479) 636-4732</a></p>
        </div>

        <div class="sidebar-financing">
          <p class="sidebar-financing__amount">$250K</p>
          <p class="sidebar-financing__label">Maximum Loan Amount</p>
          <ul class="sidebar-financing__list">
            <li>No home equity required</li>
            <li>No prepayment penalties</li>
            <li>Funding in 1–3 days</li>
            <li>Check rates in minutes</li>
            <li>No credit score impact to check</li>
          </ul>
          <a href="https://app.gethearth.com/partners/thomas-fence/darrell/apply" target="_blank" rel="noopener noreferrer" class="btn-primary sidebar-financing__btn">Apply for Financing</a>
          <p class="sidebar-financing__disclaimer">Financing provided by Hearth. Thomas Fence is not a lender.</p>
        </div>

        <div class="sidebar-estimator">
          <h3>Instant Price Estimator</h3>
          <p>Get a quick quote on your project online.</p>
          <a href="https://thomasfence.mybudgetquote.com/budget" target="_blank" rel="noopener noreferrer" class="btn-white">Get a Quote</a>
        </div>

        <div class="sidebar-credentials">
          <h3>Licensed &amp; Certified</h3>
          <ul>
            <li>AR License No. 015501</li>
            <li>AFA Certified Fence Contractor</li>
            <li>CGAT Certified Gate Automation</li>
            <li>US Federal Contractor</li>
            <li>In Business Since 1993</li>
          </ul>
        </div>
      </aside>

    </div>
  </div>
</section>
```

**Sidebar order — locked:**
1. `sidebar-cta` (Get a Free Estimate)
2. `sidebar-financing` (Hearth — $250K)
3. `sidebar-estimator` (Instant Price Estimator)
4. `sidebar-credentials` (Licensed & Certified)

**CSS:**
```css
.page-faqs { background: var(--color-white); padding: 72px 0; }
.page-faqs__grid { display: grid; grid-template-columns: 1fr 340px; gap: 56px; align-items: start; }
@media (max-width: 900px) { .page-faqs__grid { grid-template-columns: 1fr; } }
.page-faqs h2 { font-size: 1.9rem; margin-bottom: 32px; color: var(--color-navy); }
```

---

## FAQ Rules — 6 Per City Page

Always include these 4 (with city name swapped in):
1. Is a fence permit required in [City]? → Yes, links to `/resources/permits/`
2. How soon can installation start after I sign? → 1–3 weeks, we call 811
3. Does Thomas Fence offer financing? → Yes, Hearth, link to `/resources/financing/`
4. Is a deposit required? → No for standard installs

Add 2 city-specific FAQs based on what is unique about that market:
- HOA-heavy cities (Bentonville, Bella Vista, Rogers): add HOA FAQ
- Farm/rural cities (Siloam Springs): add agricultural fencing FAQ
- Springdale (HQ): add "Does Thomas Fence pull permits?" since it's the HQ city and gets the most calls

---

## Related Services — Bottom of Every City Page

```html
<section class="related-services">
  <div class="container">
    <h2>Related Services</h2>
    <div class="related-grid">
      <a href="/fences/residential-fencing/" class="related-card">
        <h3>Residential Fencing</h3>
        <p>Privacy, picket, and decorative fencing for homes throughout [City] and NWA.</p>
      </a>
      <a href="/fences/commercial-fencing/" class="related-card">
        <h3>Commercial Fencing</h3>
        <p>Perimeter fencing, access control, and job site enclosures for [City] businesses and contractors.</p>
      </a>
      <a href="/gates/gate-automation/" class="related-card">
        <h3>Gate Automation</h3>
        <p>Automated entry systems for residential and commercial properties — CGAT certified.</p>
      </a>
    </div>
  </div>
</section>
```

**CSS:**
```css
.related-services { background: var(--color-cream); padding: 64px 0; }
.related-services h2 { font-size: 1.9rem; margin-bottom: 36px; color: var(--color-navy); }
.related-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
@media (max-width: 760px) { .related-grid { grid-template-columns: 1fr; } }
.related-card { background: var(--color-white); border-radius: 8px; padding: 32px 28px; text-decoration: none; border-top: 4px solid var(--color-red-primary); box-shadow: 0 2px 10px rgba(0,0,0,0.07); transition: box-shadow 0.2s; }
.related-card:hover { box-shadow: 0 6px 24px rgba(0,0,0,0.13); }
.related-card h3 { font-family: var(--font-heading); font-size: 1.2rem; margin: 0 0 10px; color: var(--color-navy); }
.related-card p { font-size: 0.95rem; line-height: 1.65; margin: 0; color: #3a3a3a; }
```

---

## CTA Band — Identical on Every City Page

```html
<section class="cta-band">
  <div class="container">
    <h2>Ready to Start Your Fencing Project in [City]?</h2>
    <p>Call Thomas Fence or request a free estimate online. No deposit required for standard residential installations.</p>
    <a href="/contact/" class="btn-primary">Get a Free Estimate</a>
  </div>
</section>
```

Handled entirely by styles.css. No inline CSS needed.

---

## Schema — Required on Every City Page

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "FenceContractor",
      "@id": "https://thomasfencear.com/#business",
      "name": "Thomas Fence",
      "legalName": "Paschal Enterprises, Inc.",
      "url": "https://thomasfencear.com",
      "telephone": "(479) 636-4732",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "653 Kawneer Dr",
        "addressLocality": "Springdale",
        "addressRegion": "AR",
        "postalCode": "72764",
        "addressCountry": "US"
      },
      "areaServed": {
        "@type": "City",
        "name": "[City]",
        "containedInPlace": {
          "@type": "State",
          "name": "Arkansas"
        }
      },
      "description": "Thomas Fence is a locally owned fence company headquartered in Springdale, AR, installing residential and commercial fencing throughout [City] and Northwest Arkansas since 1993.",
      "foundingDate": "1993",
      "hasCredential": [
        "Arkansas Contractor's License No. 015501",
        "AFA Certified Fence Contractor",
        "US Federal Contractor Registration",
        "CGAT Certified Gate Automation Technician"
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://thomasfencear.com"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "[City] Fence Company",
          "item": "https://thomasfencear.com/[city-slug]/"
        }
      ]
    }
  ]
}
```

**Schema rules:**
- `legalName` is always `Paschal Enterprises, Inc.` — never Thomas Fence
- `address` always points to Springdale HQ — never the city being served
- `areaServed` changes per city
- Schema is always inline JSON-LD in `<head>` — never external, never minified

---

## CSS Load Order — Required

```html
  <link rel="stylesheet" href="/css/styles.css">
</head>
```

`styles.css` loads LAST, after the inline `<style>` block. This is mandatory.

---

## Footer — Do Not Modify Until All 6 City Pages Are Complete

The footer gets a 4th column ("Cities Served") after all city pages are approved. That column links to:
- `/springdale/`
- `/bentonville/`
- `/rogers/`
- `/fayetteville/`
- `/bella-vista/`
- `/siloam-springs/`
- `/arkansas-fence-company/` (authority hub)

Until then, use the current 3-column footer exactly as it appears in Springdale and Bentonville.

---

## Checklist Before Committing Any City Page

- [ ] H1 matches format: `Fence Company in [City], Arkansas`
- [ ] Trust bar present (5 items)
- [ ] City photo present with correct alt text citing image source
- [ ] Intro has minimum 2 paragraphs with real local facts (not boilerplate)
- [ ] Services grid has all 9 cards in correct order
- [ ] Process section present (navy, 4 steps)
- [ ] Warranty section present (cream, shield icon)
- [ ] FAQs: 6 questions including 4 standard + 2 city-specific
- [ ] Sidebar order: CTA → Financing → Estimator → Credentials
- [ ] Related services: 3 cards
- [ ] CTA band present
- [ ] Schema: legalName = Paschal Enterprises, Inc. / areaServed = this city
- [ ] Canonical URL matches this city's URL
- [ ] OG image points to this city's R2 photo
- [ ] styles.css loads last in `<head>`
- [ ] Committed and pushed to origin/main
