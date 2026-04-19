# tf-nav-footer.md — Thomas Fence Nav & Footer Skill

Load this file before building any new page or editing nav/footer on any existing page.
This is the locked standard. Do not deviate from these structures.

---

## Two Nav Variants — Know Which One You're Building

| Page | Nav variant |
|---|---|
| Homepage (`/`) | Old Pattern A (dark, two-row). Do NOT convert. It uses a special floating pill style. |
| Every other page | Pattern B (white single-bar). Use the template below. |

---

## Pattern B Navigation — Every Non-Homepage Page

### What it looks like
```
[Logo] | Fencing▾  Gates▾  FAQs▾  Contact | (479) 636-4732 | [Get a Free Estimate]
```

### Nav items — sub-pages only (no Home, no Publications)

| Item | Destination | Dropdown |
|---|---|---|
| Fencing ▾ | `/fences/` | Yes |
| Gates ▾ | `/gates/` | Yes |
| FAQs ▾ | `/faqs/` | Yes |
| Contact | `/contact/` | No |

### Fencing dropdown
- Residential Fencing → `/fences/residential-fencing/`
- Commercial Fencing → `/fences/commercial-fencing/`
- Vinyl Fence → `/fences/vinyl-fence/`
- Wood Fence → `/fences/wood-fence/`
- Chain Link Fence → `/fences/chain-link-fence/`
- Ornamental Steel Fence → `/fences/ornamental-steel-fence/`
- Farm Fencing → `/fences/farm-fencing/`
- Temporary Fences → `/fences/temporary-fences/`

### Gates dropdown
- Gate Automation → `/gates/gate-automation/`
- Estate Gates → `/gates/estate-gates/`

### FAQs dropdown
- Get The Answers → `/faqs/`
- Warranty → `/warranty/`
- Financing → `/financing/`
- Fence Permits → `/permits/`
- Photo Gallery → `/photo-gallery/`
- Cities We Serve → `/arkansas-fence-company/`

### Right side of nav bar (in order)
1. `(479) 636-4732` → `tel:+14796364732` — class `site-nav__phone`
2. `Get a Free Estimate` → `/contact/` — class `btn-primary site-nav__cta`

---

## Pattern B Header HTML — Copy This Exactly for Any New Page

```html
  <header class="site-header">
    <div class="container">
      <nav class="site-nav" aria-label="Main navigation">

        <a href="/" class="site-nav__logo" aria-label="Thomas Fence — Home">
          <img
            src="https://pub-7b8614251f5b42d0856b82814f0460de.r2.dev/thomas-fence-logo.svg"
            alt="Thomas Fence logo"
            width="180"
            height="auto"
            loading="eager"
          >
        </a>

        <ul class="site-nav__links">
          <li class="site-nav__item site-nav__item--has-dropdown">
            <a href="/fences/">Fencing <span class="site-nav__chevron" aria-hidden="true">&#9662;</span></a>
            <ul class="site-nav__dropdown">
              <li><a href="/fences/residential-fencing/">Residential Fencing</a></li>
              <li><a href="/fences/commercial-fencing/">Commercial Fencing</a></li>
              <li><a href="/fences/vinyl-fence/">Vinyl Fence</a></li>
              <li><a href="/fences/wood-fence/">Wood Fence</a></li>
              <li><a href="/fences/chain-link-fence/">Chain Link Fence</a></li>
              <li><a href="/fences/ornamental-steel-fence/">Ornamental Steel Fence</a></li>
              <li><a href="/fences/farm-fencing/">Farm Fencing</a></li>
              <li><a href="/fences/temporary-fences/">Temporary Fences</a></li>
            </ul>
          </li>
          <li class="site-nav__item site-nav__item--has-dropdown">
            <a href="/gates/">Gates <span class="site-nav__chevron" aria-hidden="true">&#9662;</span></a>
            <ul class="site-nav__dropdown">
              <li><a href="/gates/gate-automation/">Gate Automation</a></li>
              <li><a href="/gates/estate-gates/">Estate Gates</a></li>
            </ul>
          </li>
          <li class="site-nav__item site-nav__item--has-dropdown">
            <a href="/faqs/">FAQs <span class="site-nav__chevron" aria-hidden="true">&#9662;</span></a>
            <ul class="site-nav__dropdown">
              <li><a href="/faqs/">Get The Answers</a></li>
              <li><a href="/warranty/">Warranty</a></li>
              <li><a href="/financing/">Financing</a></li>
              <li><a href="/permits/">Fence Permits</a></li>
              <li><a href="/photo-gallery/">Photo Gallery</a></li>
              <li><a href="/arkansas-fence-company/">Cities We Serve</a></li>
            </ul>
          </li>
          <li class="site-nav__item"><a href="/contact/">Contact</a></li>
        </ul>

        <a href="tel:+14796364732" class="site-nav__phone">(479) 636-4732</a>

        <a href="/contact/" class="btn-primary site-nav__cta">Get a Free Estimate</a>

        <input type="checkbox" id="nav-toggle" class="site-nav__toggle-input" aria-hidden="true">
        <label for="nav-toggle" class="site-nav__toggle-label" aria-label="Toggle navigation">
          <span></span><span></span><span></span>
        </label>

      </nav>
    </div>
  </header>
```

---

## CSS Requirements for New Pages

Every new non-homepage page **must** load styles.css. Place this link just before `</head>`,
after any inline `<style>` blocks so styles.css wins on cascade conflicts:

```html
  <link rel="stylesheet" href="/css/styles.css">
</head>
```

styles.css contains all nav styles (`.site-header`, `.site-nav`, `.site-nav__phone`,
`.site-nav__cta`, dropdowns, hamburger, mobile responsive). No extra nav CSS needed in
inline `<style>` blocks for new pages.

---

## Site Footer — Locked Structure

Four columns. One consistent footer on all pages. No JS. All inline in HTML.

### Column 1 — NAP + Hours + Social
- Logo: `https://pub-7b8614251f5b42d0856b82814f0460de.r2.dev/thomas-fence-logo.svg`
  - After DNS switch: `https://logo.thomasfencear.com/thomas-fence-logo.svg`
- Name: Thomas Fence
- Address: 653 Kawneer Dr, Springdale, AR 72764
- Phone: `(479) 636-4732` → `tel:+14796364732`
- Email: `Sales@ThomasFenceAR.com` → `mailto:Sales@ThomasFenceAR.com`
- Hours: Mon–Fri, 8am–4pm
- CTA button: "Get a Free Estimate" → `/contact/`
- Social icons: Facebook, Pinterest, Instagram (all live), LinkedIn (pending — `<span>`, not `<a>`)

### Column 2 — Site
- Fences → `/fences/`
- Gates → `/gates/`
- FAQs → `/faqs/`
- Warranty → `/warranty/`
- Financing → `/financing/`
- Who We Are → `/company/about-us/`
- Contact → `/contact/`
- Licensing → `/licensing/`

### Column 3 — Legal Pages
- Heading: "Legal Pages" → `/legal/` (heading is a hyperlink)
- Terms of Service → `/legal/terms-of-service/`
- Privacy Policy → `/legal/privacy-policy/`
- Scope of Services → `/legal/scope-of-services/`
- Refund & Cancellation Policy → `/legal/refund-cancellation-policy/`
- Service & Results Disclaimer → `/legal/service-results-disclaimer/`
- Testimonials Disclaimer → `/legal/testimonial-disclaimer/`
- Warranty Information → `/legal/warranty/`

### Column 4 — Cities We Serve
- Heading: "Cities We Serve" → `/arkansas-fence-company/` (heading is a hyperlink)
- Springdale → `/springdale/`
- Bentonville → `/bentonville/`
- Rogers → `/rogers/`
- Fayetteville → `/fayetteville/`
- Bella Vista → `/bella-vista/`
- Siloam Springs → `/siloam-springs/`

### Bottom bar
- Left: `© 2026 Paschal Enterprises, Inc. dba Thomas Fence. All rights reserved.`
- Right: Privacy Policy | Terms | Legal

---

## Footer HTML Block — Copy This Exactly

```html
  <footer class="site-footer">
    <div class="site-footer__inner">
      <div class="site-footer__grid">

        <!-- Column 1: NAP + Hours + Social -->
        <div class="site-footer__col site-footer__col--contact">
          <a href="/" aria-label="Thomas Fence — Home">
            <img
              src="https://pub-7b8614251f5b42d0856b82814f0460de.r2.dev/thomas-fence-logo.svg"
              alt="Thomas Fence logo"
              width="160"
              height="auto"
              loading="lazy"
              class="site-footer__logo"
            >
          </a>
          <address class="site-footer__nap">
            <strong>Thomas Fence</strong><br>
            653 Kawneer Dr<br>
            Springdale, AR 72764<br>
            <a href="tel:+14796364732">(479) 636-4732</a><br>
            <a href="mailto:Sales@ThomasFenceAR.com">Sales@ThomasFenceAR.com</a>
          </address>
          <p class="site-footer__hours"><strong>Hours:</strong> Mon–Fri, 8am–4pm</p>
          <a href="/contact/" class="btn-primary site-footer__contact-btn">Get a Free Estimate</a>
          <div class="site-footer__socials">
            <a href="https://www.facebook.com/ThomasFenceAR" target="_blank" rel="noopener noreferrer" class="site-footer__social-link" aria-label="Thomas Fence on Facebook">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
            </a>
            <a href="https://www.pinterest.com/thomasfencear/_saved/" target="_blank" rel="noopener noreferrer" class="site-footer__social-link" aria-label="Thomas Fence on Pinterest">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 0C5.373 0 0 5.373 0 12c0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738a.36.36 0 0 1 .083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.163 0 7.398 2.967 7.398 6.931 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.632-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0z"/></svg>
            </a>
            <a href="https://www.instagram.com/thomasfencear/" target="_blank" rel="noopener noreferrer" class="site-footer__social-link" aria-label="Thomas Fence on Instagram">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
            </a>
            <span class="site-footer__social-link site-footer__social-link--pending" aria-label="Thomas Fence on LinkedIn (coming soon)" title="LinkedIn — coming soon">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
            </span>
          </div>
        </div>

        <!-- Column 2: Site Navigation -->
        <div class="site-footer__col site-footer__col--site">
          <h3 class="site-footer__heading">Site</h3>
          <ul class="site-footer__list">
            <li><a href="/fences/">Fences</a></li>
            <li><a href="/gates/">Gates</a></li>
            <li><a href="/faqs/">FAQs</a></li>
            <li><a href="/warranty/">Warranty</a></li>
            <li><a href="/financing/">Financing</a></li>
            <li><a href="/company/about-us/">Who We Are</a></li>
            <li><a href="/contact/">Contact</a></li>
            <li><a href="/licensing/">Licensing</a></li>
          </ul>
        </div>

        <!-- Column 3: Legal Pages -->
        <div class="site-footer__col site-footer__col--legal">
          <h3 class="site-footer__heading"><a href="/legal/" style="color:inherit;text-decoration:none;">Legal Pages</a></h3>
          <ul class="site-footer__list site-footer__list--legal">
            <li><a href="/legal/terms-of-service/">Terms of Service</a></li>
            <li><a href="/legal/privacy-policy/">Privacy Policy</a></li>
            <li><a href="/legal/scope-of-services/">Scope of Services</a></li>
            <li><a href="/legal/refund-cancellation-policy/">Refund &amp; Cancellation Policy</a></li>
            <li><a href="/legal/service-results-disclaimer/">Service &amp; Results Disclaimer</a></li>
            <li><a href="/legal/testimonial-disclaimer/">Testimonials Disclaimer</a></li>
            <li><a href="/legal/warranty/">Warranty Information</a></li>
          </ul>
        </div>

        <!-- Column 4: Cities We Serve -->
        <div class="site-footer__col site-footer__col--cities">
          <h3 class="site-footer__heading"><a href="/arkansas-fence-company/" style="color:inherit;text-decoration:none;">Cities We Serve</a></h3>
          <ul class="site-footer__list">
            <li><a href="/springdale/">Springdale</a></li>
            <li><a href="/bentonville/">Bentonville</a></li>
            <li><a href="/rogers/">Rogers</a></li>
            <li><a href="/fayetteville/">Fayetteville</a></li>
            <li><a href="/bella-vista/">Bella Vista</a></li>
            <li><a href="/siloam-springs/">Siloam Springs</a></li>
          </ul>
        </div>

      </div>

      <div class="site-footer__bottom">
        <span>&copy; 2026 Paschal Enterprises, Inc. dba Thomas Fence. All rights reserved.</span>
        <nav class="site-footer__bottom-legal" aria-label="Legal">
          <a href="/legal/privacy-policy/">Privacy Policy</a>
          <a href="/legal/terms-of-service/">Terms</a>
          <a href="/legal/">Legal</a>
        </nav>
      </div>
    </div>
  </footer>
```

---

## Footer Grid CSS — Required

`styles.css` defines the footer grid. The 4-column layout requires these values:

```css
.site-footer__grid {
  grid-template-columns: 1.5fr 1fr 1fr 1fr;
}
/* 1024px breakpoint */
@media (max-width: 1024px) {
  .site-footer__grid { grid-template-columns: 1.2fr 1fr 1fr 1fr; }
}
/* 768px breakpoint — stack to single column */
@media (max-width: 768px) {
  .site-footer__grid { grid-template-columns: 1fr; }
}
```

If a page has **inline** footer CSS that overrides styles.css (older pages do this),
update the `grid-template-columns` in that page's inline `<style>` block to match the
4-column values above. Do not leave 3-column overrides in place.

---

## LinkedIn — When URL Is Ready

When the LinkedIn page is live, swap the `<span>` to an `<a>` sitewide:

```html
<!-- Before (pending) -->
<span class="site-footer__social-link site-footer__social-link--pending" ...>

<!-- After (live) -->
<a href="https://www.linkedin.com/company/thomas-fence" target="_blank" rel="noopener noreferrer" class="site-footer__social-link" aria-label="Thomas Fence on LinkedIn">
```

Run a sitewide find-and-replace across all pages when ready.
