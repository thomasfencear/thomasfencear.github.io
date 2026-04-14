# tf-nav-footer.md — Thomas Fence Nav & Footer Skill

Load this file before building any new page or touching nav/footer on any existing page.
This is the locked standard for both the site navigation and the site footer.

---

## Site Navigation — Locked Structure

Every page uses the same nav HTML block. Copy exactly. Do not add or remove items without updating this file and every existing page.

### Nav items and destinations

| Label | Destination | Has Dropdown |
|---|---|---|
| Home | `/` | No |
| Fences | `/fences/` | Yes |
| Gates | `/gates/` | Yes |
| Who We Are | `/company/about-us/` | Yes |
| FAQs | `/faqs/` | No |
| Publications | `/publications/` | No |
| Contact | `/contact/` | No — CTA button (red) |

### Fences dropdown
- All Fencing Services → `/fences/`
- Vinyl Fence → `/fences/vinyl-fence/`
- Wood Fence → `/fences/wood-fence/`
- Chain Link Fence → `/fences/chain-link-fence/`
- Ornamental Steel → `/fences/ornamental-steel-fence/`
- Residential Fencing → `/fences/residential-fencing/`
- Commercial Fencing → `/fences/commercial-fencing/`
- Farm Fencing → `/fences/farm-fencing/`
- Temporary Fencing → `/fences/temporary-fences/`

### Gates dropdown
- All Gate Services → `/gates/`
- Gate Automation → `/gates/gate-automation/`
- Estate Gates → `/gates/estate-gates/`

### Who We Are dropdown
- About Us → `/company/about-us/`
- Testimonials → `/company/testimonials/`
- Join Our Team → `https://thomasfencear.hireclick.com/jobboard/` (new tab)
- Contact Us → `/contact/`

---

## Site Footer — Locked Structure

Three columns. One consistent footer on all 44 pages. No JS. All inline in HTML.

### Column 1 — NAP + Hours + Social
- Logo (white, filtered): `https://pub-7b8614251f5b42d0856b82814f0460de.r2.dev/thomas-fence-logo.svg`
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

### Column 3 — Legal
- Privacy Policy → `/legal/privacy-policy/`
- Terms of Service → `/legal/terms-of-service/`
- Warranty → `/warranty/`
- Legal (All Pages) → `/legal/`

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
          </ul>
        </div>

        <!-- Column 3: Legal -->
        <div class="site-footer__col site-footer__col--legal">
          <h3 class="site-footer__heading">Legal</h3>
          <ul class="site-footer__list site-footer__list--legal">
            <li><a href="/legal/privacy-policy/">Privacy Policy</a></li>
            <li><a href="/legal/terms-of-service/">Terms of Service</a></li>
            <li><a href="/warranty/">Warranty</a></li>
            <li><a href="/legal/">Legal (All Pages)</a></li>
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

## CSS Notes

- Pages that load `/css/styles.css` get footer styles automatically — no extra CSS needed.
- Pages with inline CSS get `<style id="tf-footer-css">` injected before `</head>` — this block contains all footer styles with hardcoded values (no CSS vars).
- The `.site-footer__inner` wrapper is used on ALL pages (replaces `.container` inside footer). This is defined in both styles.css and the inline CSS block.

---

## LinkedIn — When URL Is Ready

When the LinkedIn page is live, change the `<span>` to an `<a>` tag:

```html
<!-- Before (pending) -->
<span class="site-footer__social-link site-footer__social-link--pending" ...>

<!-- After (live) -->
<a href="https://www.linkedin.com/company/thomas-fence" target="_blank" rel="noopener noreferrer" class="site-footer__social-link" aria-label="Thomas Fence on LinkedIn">
```

Run a sitewide find-and-replace across all 44 pages when ready.
