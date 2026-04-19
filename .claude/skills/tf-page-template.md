# tf-page-template.md — Thomas Fence Service Page Template

**Load this file before building or editing any fence or gate service page.**
This is the locked standard. The commercial fencing page (`/fences/commercial-fencing/`) is the approved reference. Every fence and gate service page must match this structure exactly.

---

## The One Rule That Cannot Break

Greg's photos are never decorative. They are the primary content of the page.
They live in the work showcase section — full-width, front and center, never in the sidebar.
If a real Thomas Fence job photo does not exist for a slot, leave it out. Do not fill it with stock, AI-generated, or vendor images. Ever.

---

## Page Structure — Five Zones, In Order

```
┌─────────────────────────────────────────────┐
│  ZONE 1 — Navy Hero                         │
│  Plain --color-navy background              │
│  H1 · subtitle · CTA button                │
├─────────────────────────────────────────────┤
│  ZONE 2 — Red Trust Bar                     │
│  Credentials across full width              │
├─────────────────────────────────────────────┤
│  ZONE 3 — Work Showcase  ← FOCAL POINT     │
│  White background                           │
│  Greg's job photos · full-width rows        │
│  Photo LEFT · Text + button RIGHT           │
│  Outside the sidebar grid                   │
├─────────────────────────────────────────────┤
│  ZONE 4A — Intro         Cream background  │
│  ZONE 4B — Process       Navy background   │
│  ZONE 4C — Warranty      Cream background  │
├─────────────────────────────────────────────┤
│  ZONE 5 — FAQs + Sidebar  White background │
│  FAQs LEFT · Sidebar RIGHT                 │
└─────────────────────────────────────────────┘
```

---

## Zone 1 — Navy Hero

```html
<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <ol>
        <li><a href="/">Home</a></li>
        <li><a href="/fences/">Fencing Services</a></li>
        <li aria-current="page">[Page Name]</li>
      </ol>
    </nav>
    <h1>[Page H1]</h1>
    <p class="page-hero__sub">[Subtitle — one sentence, specific to NWA]</p>
    <a href="/contact/" class="btn-primary">Get a Free Estimate</a>
  </div>
</section>
```

**CSS (inline `<style>` block on each page):**
```css
.page-hero { background: var(--color-navy); padding: 72px 0 64px; }
```

**Rules:**
- Plain navy only — no background images, no overlays, no photos
- H1 and subtitle text are white (handled by styles.css)
- CTA always links to `/contact/`

---

## Zone 2 — Trust Bar

```html
<section class="trust-bar" aria-label="Credentials">
  <div class="container">
    <ul class="trust-bar__list">
      <li>AR License No. 015501</li>
      <li>AFA Certified Fence Contractor</li>
      <li>US Federal Contractor</li>
      <li>Serving NWA Since 1993</li>
      <li>1-Year Workmanship Warranty</li>
    </ul>
  </div>
</section>
```

Handled entirely by styles.css. No inline CSS needed.

---

## Zone 3 — Work Showcase

This section lives **outside** the sidebar grid. It is never inside `.page-content`.

```html
<section class="work-showcase">
  <div class="container">
    <h2>[Section heading — e.g. "Commercial Fencing Solutions for Every Business"]</h2>
    <div class="showcase-rows">

      <div class="showcase-row">
        <div class="showcase-row__img">
          <img
            src="[R2 URL — real Thomas Fence job photo only]"
            alt="[Specific alt text — see alt text rules below]"
            width="800"
            loading="eager"
          >
        </div>
        <div class="showcase-row__text">
          <h3>[Fence/Gate Type Name]</h3>
          <p>[Description — 2–3 sentences, specific to NWA customers]</p>
          <a href="[internal link]" class="btn-primary">[CTA — e.g. "See Chain Link Options"]</a>
        </div>
      </div>

      <!-- Repeat for each type on this page -->

    </div>
  </div>
</section>
```

**CSS (add to inline `<style>` block on each page):**
```css
.work-showcase { padding: 64px 0; background: var(--color-white); }
.work-showcase > .container > h2 { font-size: 2rem; text-align: center; margin-bottom: 48px; color: var(--color-navy); }
.showcase-rows { display: flex; flex-direction: column; gap: 28px; }
.showcase-row { display: grid; grid-template-columns: 1fr 1fr; min-height: 380px; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.10); }
.showcase-row__img { overflow: hidden; }
.showcase-row__img img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.4s ease; }
.showcase-row:hover .showcase-row__img img { transform: scale(1.03); }
.showcase-row__text { padding: 52px 56px; display: flex; flex-direction: column; justify-content: center; background: var(--color-white); border-left: 6px solid var(--color-red-primary); }
.showcase-row__text h3 { font-family: var(--font-heading); font-size: 1.8rem; margin: 0 0 18px; line-height: 1.2; color: var(--color-navy); }
.showcase-row__text p { font-size: 1.02rem; line-height: 1.75; margin-bottom: 28px; color: #2a2a2a; }
.showcase-row__text .btn-primary { align-self: flex-start; }
@media (max-width: 820px) {
  .showcase-row { grid-template-columns: 1fr; min-height: auto; }
  .showcase-row__img img { height: 280px; }
  .showcase-row__text { padding: 36px 32px; border-left: none; border-top: 6px solid var(--color-red-primary); }
}
```

**Rules:**
- Only real Thomas Fence job photos — no stock, no AI, no vendor images
- First image in the HTML source should be the strongest / most recognizable photo for that page
- Each row gets its own real photo — do not repeat photos across rows
- If a real photo doesn't exist yet, omit that row entirely until the photo is ready

---

## Zone 4A — Intro (Cream)

```html
<section class="page-intro">
  <div class="container">
    <h2>[Page-specific heading]</h2>
    <p>[Paragraph 1 — what Thomas Fence does for this service in NWA]</p>
    <p>[Paragraph 2 — credentials, longevity, trust signal]</p>
  </div>
</section>
```

**CSS:**
```css
.page-intro { background: var(--color-cream); padding: 64px 0; }
.page-intro h2 { font-size: 1.9rem; margin-bottom: 20px; color: var(--color-navy); }
.page-intro p { font-size: 1.05rem; line-height: 1.8; margin-bottom: 16px; max-width: 820px; color: #1a1a1a; }
```

---

## Zone 4B — Our Easy Process (Navy)

```html
<section class="page-process">
  <div class="container">
    <h2>Our Easy Process</h2>
    <p>[One sentence intro]</p>
    <div class="process-grid">
      <div class="process-card">
        <p class="process-card__num">Step 1</p>
        <h3>Schedule Your Free Estimate</h3>
        <p>Call <a href="tel:+14796364732">(479) 636-4732</a>. [Page-specific detail about estimate timeline.]</p>
      </div>
      <div class="process-card">
        <p class="process-card__num">Step 2</p>
        <h3>Approve &amp; Sign</h3>
        <p>Accept by phone, email, or through your sales representative. We will send over a contract for your signature.</p>
      </div>
      <div class="process-card">
        <p class="process-card__num">Step 3</p>
        <h3>Get on the Schedule</h3>
        <p>Once the contract is signed, your project is officially in line to be completed — typically within 1 to 3 weeks.</p>
      </div>
      <div class="process-card">
        <p class="process-card__num">Step 4</p>
        <h3>Final Prep &amp; Install</h3>
        <p>We call 811 to mark underground utilities before any digging, and check in with you before crews arrive.</p>
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

## Zone 4C — Warranty (Cream)

```html
<section class="page-warranty">
  <div class="container">
    <div class="warranty-box">
      <div class="warranty-box__icon">🛡</div>
      <div class="warranty-box__text">
        <h2>1-Year Workmanship Warranty</h2>
        <p>Thomas Fence provides a written 1-year workmanship warranty on every [fence type] installation. We use [material]-grade materials from reputable manufacturers — many of which carry their own product warranties for additional protection.</p>
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

## Zone 5 — FAQs + Sidebar (White)

```html
<section class="page-faqs">
  <div class="container">
    <div class="page-faqs__grid">

      <div>
        <h2>[Page] FAQs</h2>

        <details class="faq-item">
          <summary>[Question]</summary>
          <div class="faq-item__answer"><p>[Answer]</p></div>
        </details>
        <!-- Repeat for each FAQ -->
      </div>

      <aside>
        <div class="sidebar-cta">
          <h3>Get a Free Estimate</h3>
          <p>[One sentence specific to this page's service]</p>
          <a href="/contact/" class="btn-primary">Contact Us</a>
          <p class="sidebar-cta__phone"><a href="tel:+14796364732">(479) 636-4732</a></p>
        </div>
        <div class="sidebar-credentials">
          <h3>Licensed &amp; Certified</h3>
          <ul>
            <li>AR License No. 015501</li>
            <li>AFA Certified Fence Contractor</li>
            <li>US Federal Contractor</li>
            <li>In Business Since 1993</li>
          </ul>
        </div>
        <div class="sidebar-estimator">
          <h3>Instant Price Estimator</h3>
          <p>Get a quick quote on your project online.</p>
          <a href="https://thomasfence.mybudgetquote.com/budget" target="_blank" rel="noopener noreferrer" class="btn-white">Get a Quote</a>
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
      </aside>

    </div>
  </div>
</section>
```

**CSS:**
```css
.page-faqs { background: var(--color-white); padding: 72px 0; }
.page-faqs__grid { display: grid; grid-template-columns: 1fr 340px; gap: 56px; align-items: start; }
@media (max-width: 900px) { .page-faqs__grid { grid-template-columns: 1fr; } }
.page-faqs h2 { font-size: 1.9rem; margin-bottom: 32px; color: var(--color-navy); }
```

**Sidebar rules — locked:**
- "Get a Free Estimate" heading: `--color-navy` (NOT white)
- Credentials list: handled by `styles.css` — red dot, flexbox, gap. Do NOT add inline CSS for `.sidebar-credentials li` on any page. `styles.css` owns this.
- Sidebar never contains photos, gallery images, or any of Greg's work

---

## Sidebar — What styles.css Owns (Do Not Override Inline)

These are fixed in `styles.css` and must not be re-declared in any page's inline `<style>` block:

- `.sidebar-credentials li` — flexbox, red dot bullet, gap, border-bottom
- `.sidebar-credentials li::before` — 8px red circle, flex-shrink, margin-top
- `.sidebar-cta` — navy background, white body text
- `.sidebar-cta h3` — navy heading color

---

## Alt Text Rules — Every Image

Format: `[What it is] — Thomas Fence, [City], Arkansas`

**Examples:**
```
✓  Commercial chain link fence installed by Thomas Fence in Springdale, Arkansas
✓  Board-on-board wood privacy fence — Thomas Fence, Rogers, Arkansas
✓  Vinyl estate gate with swing operator — Thomas Fence, Bentonville, Arkansas

✗  Chain link fence (too generic — no location, no company)
✗  Image of a fence (never use "image of" or "photo of")
✗  LiftMaster gate (vendor name — not Thomas Fence)
```

Always include Thomas Fence and a location. Always.

---

## Image Loading Order

The order images appear in the HTML source is the order Google and AI crawlers index them.

1. First showcase row image — strongest job photo for this page
2. Subsequent showcase rows — in order of customer search popularity
3. Never reorder for visual reasons at the expense of this sequence

---

## Bottom of Every Page — Related Services + CTA Band

After Zone 5, every page ends with:

```html
<section class="related-services">
  <div class="container">
    <h2>Related Services</h2>
    <div class="related-grid">
      <!-- 3 related-card items linking to other service pages -->
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>[Page-specific CTA headline]</h2>
    <p>[One sentence]</p>
    <a href="/contact/" class="btn-primary">Get a Free Estimate</a>
  </div>
</section>
```

Both handled by `styles.css`. No inline CSS needed.

---

## CSS Load Order — Required

Every service page must load `styles.css` as the LAST stylesheet before `</head>`:

```html
  <link rel="stylesheet" href="/css/styles.css">
</head>
```

This ensures `styles.css` wins over any conflicting inline rules at equal specificity.

---

## Reference Page

`/fences/commercial-fencing/` — approved April 14, 2026.
When in doubt, look at that page. That is what every fence and gate service page should look like.
