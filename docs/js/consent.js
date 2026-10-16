/* Thomas Fence cookie banner. Added 2026-10-16.
 *
 * The visitor's choice is saved in their own browser only, as the cookie tf_consent
 * ("granted" or "denied", one year). Nothing is sent to a server or kept anywhere else.
 * The inline snippet in each page head reads the same cookie and sets Google consent mode
 * before Tag Manager loads. This file shows the banner when there is no choice yet, and
 * updates consent mode when the visitor clicks.
 *
 * GA4 and Google Ads follow consent mode on their own. The OpenAI Pixel does not, so for a
 * visitor who declined, the head snippet sets window.oaiq to an empty function first; the
 * Pixel's own loader sees it and never loads OpenAI's script.
 */
(function () {
  var NAME = 'tf_consent';

  function saved() {
    var m = document.cookie.match(/(?:^|; )tf_consent=(granted|denied)/);
    return m ? m[1] : null;
  }

  function save(value) {
    document.cookie = NAME + '=' + value + '; Max-Age=31536000; Path=/; SameSite=Lax; Secure';
  }

  function update(value) {
    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    gtag('consent', 'update', {
      ad_storage: value,
      ad_user_data: value,
      ad_personalization: value,
      analytics_storage: value
    });
    window.dataLayer.push({ event: 'tf_consent_' + value });
  }

  function style() {
    var css =
      '#tf-consent{position:fixed;left:16px;right:16px;bottom:16px;z-index:9999;max-width:720px;margin:0 auto;' +
      'background:var(--color-navy,#003049);color:var(--color-white,#fff);border-radius:8px;' +
      'box-shadow:var(--shadow-lg,0 8px 40px rgba(0,0,0,.18));padding:18px 20px;' +
      'font-family:var(--font-body,"DM Sans",Arial,sans-serif);font-size:15px;line-height:1.5;' +
      'display:flex;flex-wrap:wrap;align-items:center;gap:12px 20px}' +
      '#tf-consent p{margin:0;flex:1 1 320px}' +
      '#tf-consent a{color:var(--color-white,#fff);text-decoration:underline}' +
      '#tf-consent .tf-consent-buttons{display:flex;gap:10px}' +
      '#tf-consent button{font:inherit;font-weight:700;border-radius:6px;padding:10px 18px;cursor:pointer;' +
      'border:2px solid var(--color-white,#fff)}' +
      '#tf-consent .tf-accept{background:var(--color-red-primary,#F01B24);border-color:var(--color-red-primary,#F01B24);color:#fff}' +
      '#tf-consent .tf-decline{background:transparent;color:#fff}' +
      '#tf-consent button:focus-visible{outline:3px solid var(--color-steel,#669BBC);outline-offset:2px}';
    var el = document.createElement('style');
    el.textContent = css;
    document.head.appendChild(el);
  }

  function show() {
    style();
    var box = document.createElement('div');
    box.id = 'tf-consent';
    box.setAttribute('role', 'region');
    box.setAttribute('aria-label', 'Cookie choice');
    box.innerHTML =
      '<p>We use cookies to see how visitors find us and to measure our ads. ' +
      'You can accept or decline. <a href="/legal/privacy-policy/">Privacy Policy</a></p>' +
      '<div class="tf-consent-buttons">' +
      '<button type="button" class="tf-decline">Decline</button>' +
      '<button type="button" class="tf-accept">Accept</button>' +
      '</div>';
    document.body.appendChild(box);

    function choose(value) {
      save(value);
      update(value);
      box.parentNode.removeChild(box);
    }
    box.querySelector('.tf-accept').addEventListener('click', function () { choose('granted'); });
    box.querySelector('.tf-decline').addEventListener('click', function () { choose('denied'); });
  }

  if (saved()) return;
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', show);
  } else {
    show();
  }
})();
