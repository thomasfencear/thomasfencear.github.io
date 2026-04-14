# tf-financing-estimator.md — Sidebar CTA Blocks Skill

Load this file before building or editing any fence or gate page sidebar.
These two blocks appear together on every fence sub-page and gate sub-page.

---

## Where These Blocks Go

Both blocks live in `<aside>` in the right-sidebar column.
Order: CTA card → Credentials card → **Estimator card** → **Financing card**

Pages that use this pattern (10 total):
- `/fences/residential-fencing/`
- `/fences/commercial-fencing/`
- `/fences/vinyl-fence/`
- `/fences/wood-fence/`
- `/fences/chain-link-fence/`
- `/fences/ornamental-steel-fence/`
- `/fences/farm-fencing/`
- `/fences/temporary-fences/`
- `/gates/gate-automation/`
- `/gates/estate-gates/`

---

## System 1 Pages — Fence Sub-pages (inline CSS, `sidebar-*` classes)

### Required CSS (add to inline `<style>` block)

```css
.sidebar-estimator { background: var(--color-red-primary); border-radius: 8px; padding: 24px; text-align: center; margin-bottom: 24px; }
.sidebar-estimator h3 { color: var(--color-white); font-size: 1.1rem; margin-bottom: 10px; }
.sidebar-estimator p { color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-bottom: 16px; }
.sidebar-financing { background: var(--color-navy); border-radius: 8px; padding: 28px 24px; margin-top: 24px; text-align: center; }
.sidebar-financing__amount { font-family: var(--font-heading); font-size: 3rem; color: var(--color-cream); margin: 0 0 4px; line-height: 1; }
.sidebar-financing__label { font-size: 0.68rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--color-steel); margin: 0 0 20px; }
.sidebar-financing__list { list-style: none; padding: 0; margin: 0 0 20px; text-align: left; }
.sidebar-financing__list li { padding: 7px 0; border-bottom: 1px solid rgba(255,255,255,0.08); font-size: 0.88rem; color: rgba(255,255,255,0.85); }
.sidebar-financing__list li:last-child { border-bottom: none; }
.sidebar-financing__list li::before { content: "✓ "; color: var(--color-cream); font-weight: 700; }
.sidebar-financing__btn { display: block; text-align: center; margin-bottom: 16px; }
.sidebar-financing__disclaimer { font-size: 0.72rem; color: rgba(255,255,255,0.45); line-height: 1.5; margin: 0; }
```

### Estimator Block HTML

```html
          <div class="sidebar-estimator">
            <h3>Instant Price Estimator</h3>
            <p>Get a quick quote on your fence project online.</p>
            <a href="https://thomasfence.mybudgetquote.com/budget" target="_blank" rel="noopener noreferrer" class="btn-white">Get a Quote</a>
          </div>
```

### Financing Block HTML (place directly after estimator block)

```html
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
            <p class="sidebar-financing__disclaimer">Financing provided by Hearth. Thomas Fence is not a lender. Approval and terms are determined by Hearth based on individual creditworthiness.</p>
          </div>
```

---

## System 2 Pages — Gate Sub-pages (`sidebar-card` pattern)

### Financing Block HTML (place after `sidebar-card--red` estimator card)

```html
        <div class="sidebar-card sidebar-card--navy">
          <div class="sidebar-card__heading">Financing Available</div>
          <ul class="sidebar-card__creds">
            <li>Up to $250K loan amount</li>
            <li>No home equity required</li>
            <li>No prepayment penalties</li>
            <li>Funding in 1–3 days</li>
            <li>No credit score impact to check</li>
          </ul>
          <a class="btn btn--red btn--full" href="https://app.gethearth.com/partners/thomas-fence/darrell/apply" target="_blank" rel="noopener noreferrer">Apply for Financing</a>
          <p style="font-size:0.72rem;color:rgba(255,255,255,0.4);margin-top:12px;line-height:1.5;">Financing provided by Hearth. Thomas Fence is not a lender.</p>
        </div>
```

---

## Button Destination Map

| Button | Destination | Opens |
|---|---|---|
| Get a Quote (estimator) | `https://thomasfence.mybudgetquote.com/budget` | New tab |
| Apply for Financing | `https://app.gethearth.com/partners/thomas-fence/darrell/apply` | New tab |

Both are third-party tools — always `target="_blank" rel="noopener noreferrer"`.

---

## Disclaimer — Required on Every Financing Block

> Financing provided by Hearth. Thomas Fence is not a lender. Approval and terms are determined by Hearth based on individual creditworthiness.

Never omit this. It's a legal disclosure.
