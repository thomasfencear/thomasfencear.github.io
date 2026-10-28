"""Build one video watch page per row in videos.json, from the live site's own gate page design.

Usage (from anywhere):  python3 build_video_pages.py
Writes docs/videos/<slug>/index.html and docs/videos/index.html is NOT touched (the hub is /video-gallery/).
Head, header, styles, tracking and footer are copied from docs/gates/automated-gates/index.html so every
page carries Tag Manager (GTM-PFPBCGNR), the consent default, and the Searchable script exactly as the site does.
Reviews: 3 per page from the saved Google reviews, only ones not already shown anywhere on the site, each used once.
"""
import glob
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DOCS = os.path.join(REPO, "docs")
SOURCE = os.path.join(DOCS, "gates", "automated-gates", "index.html")
REVIEWS = "/Users/besociallysmashinghome/repos/ThomasFence-Private/reviews-intake/Thomas_Fence_Google_Reviews_2026-10-25.json"
SITE = "https://thomasfencear.com"

# YouTube record for each video, read 2026-10-28 (publishedAt, duration).
YOUTUBE = {
    "q8yF3QqU40I": ("2026-05-22T05:00:00Z", "PT32S"),
    "g4M1JleJYPg": ("2026-05-24T14:15:20Z", "PT31S"),
    "y8mQl9OveXU": ("2026-05-23T22:00:31Z", "PT17S"),
    "Nd0gz9qvF-8": ("2026-05-23T10:15:19Z", "PT21S"),
    "2Q131QLRP-g": ("2026-05-23T12:00:15Z", "PT17S"),
    "_gsxnm0gKb0": ("2026-05-23T07:00:33Z", "PT23S"),
    "i_U3CMSPx9o": ("2026-05-23T18:00:22Z", "PT25S"),
}

FAQ_COMMON = [
    ("How much does a gate cost?",
     "Every gate is priced to the site: opening width, gate style, operator and access control. Thomas Fence gives a free estimate after a site evaluation, and you can get a quick online number from the <a href=\"https://thomasfence.mybudgetquote.com/budget\" target=\"_blank\" rel=\"noopener noreferrer\">Instant Price Estimator</a>.",
     "Every gate is priced to the site: opening width, gate style, operator and access control. Thomas Fence gives a free estimate after a site evaluation, and the Instant Price Estimator gives a quick online number."),
    ("Can I finance my gate?",
     "Yes. Financing is available through Hearth, up to $250K, with no home equity required, no prepayment penalties, and no credit score impact to check your rates. Funding takes 1 to 3 days. Thomas Fence is not a lender.",
     "Yes. Financing is available through Hearth, up to $250K, with no home equity required, no prepayment penalties, and no credit score impact to check your rates. Funding takes 1 to 3 days. Thomas Fence is not a lender."),
    ("Is Thomas Fence licensed and certified?",
     "Yes. Arkansas Contractor's License No. 0155010427, AFA Certified Fence Contractor, CGAT Certified Gate Automation Technician, and US Federal Contractor Registration. Thomas Fence has served Northwest Arkansas since 1993. See <a href=\"/licensing/\">licensing</a>.",
     "Yes. Arkansas Contractor's License No. 0155010427, AFA Certified Fence Contractor, CGAT Certified Gate Automation Technician, and US Federal Contractor Registration. Thomas Fence has served Northwest Arkansas since 1993."),
    ("What warranty comes with a gate?",
     "A written 1-year workmanship warranty on every installation. Gate operators and access control components carry their own manufacturer warranties for additional coverage. See the <a href=\"/warranty/\">warranty</a> page.",
     "A written 1-year workmanship warranty on every installation. Gate operators and access control components carry their own manufacturer warranties for additional coverage."),
    ("What safety devices come with an automated gate?",
     "UL 325 requires entrapment protection on all automated gates, typically safety edges, photo eyes or loop detectors depending on gate type. Thomas Fence installs all required safety devices as part of every gate automation project, not as add-ons.",
     "UL 325 requires entrapment protection on all automated gates, typically safety edges, photo eyes or loop detectors depending on gate type. Thomas Fence installs all required safety devices as part of every gate automation project, not as add-ons."),
    ("Do you repair gates you didn't install?",
     "Yes. Thomas Fence repairs automated gates of any brand or style, including failed operators, malfunctioning safety devices and retrofits.",
     "Yes. Thomas Fence repairs automated gates of any brand or style, including failed operators, malfunctioning safety devices and retrofits."),
    ("What areas do you serve?",
     "Springdale, Bentonville, Rogers, Fayetteville, Bella Vista, Siloam Springs and across Northwest Arkansas, from our yard at 653 Kawneer Dr in Springdale.",
     "Springdale, Bentonville, Rogers, Fayetteville, Bella Vista, Siloam Springs and across Northwest Arkansas, from our yard at 653 Kawneer Dr in Springdale."),
]

PAGE_CSS = """
<style>
    .tf-watch { background: #111; padding: 40px 0 48px; }
    .tf-watch__frame { position: relative; margin: 0 auto; width: min(100%, calc(82vh * 9 / 16)); aspect-ratio: 9 / 16; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.45); background: #000; }
    .tf-watch__frame iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }
    .tf-watch__caption { color: #ddd; text-align: center; font-size: 0.95rem; margin: 18px auto 0; max-width: 640px; padding: 0 20px; }
    .tf-hook { background: var(--color-navy); color: #fff; text-align: center; padding: 40px 24px; }
    .tf-hook p { font-family: var(--font-heading); font-size: 1.7rem; line-height: 1.3; margin: 0 auto 22px; max-width: 760px; color: #fff; }
    .tf-hook__phone { display: block; margin-top: 14px; color: #fff; font-weight: 600; }
    .tf-hook__phone a { color: #fff; }
    .tf-what { padding: 56px 0 40px; }
    .tf-what .container { max-width: 820px; }
    .tf-what p { font-size: 1.08rem; line-height: 1.75; }
    .tf-contact { background: var(--color-red-primary, #c8102e); color: #fff; text-align: center; padding: 52px 24px; }
    .tf-contact h2 { color: #fff; margin: 0 0 12px; }
    .tf-contact p { margin: 0 auto 22px; max-width: 640px; font-size: 1.05rem; }
    .tf-contact .btn-white { font-size: 1.05rem; }
    .tf-contact__phone { display: block; margin-top: 14px; font-weight: 600; }
    .tf-contact__phone a { color: #fff; }
    .tf-finance { padding: 56px 0; background: var(--color-off-white, #f7f5f2); }
    .tf-finance__box { max-width: 820px; margin: 0 auto; background: #fff; border-radius: 12px; padding: 36px 32px; box-shadow: 0 2px 14px rgba(0,0,0,0.08); display: grid; grid-template-columns: 180px 1fr; gap: 28px; align-items: center; }
    .tf-finance__amount { font-family: var(--font-heading); font-size: 3rem; color: var(--color-navy); margin: 0; line-height: 1; }
    .tf-finance__label { margin: 6px 0 0; font-size: 0.9rem; color: #555; }
    .tf-finance ul { margin: 0 0 18px; padding-left: 20px; line-height: 1.8; }
    .tf-finance__disclaimer { font-size: 0.8rem; color: #777; margin: 12px 0 0; }
    @media (max-width: 640px) { .tf-finance__box { grid-template-columns: 1fr; text-align: center; } .tf-finance ul { text-align: left; } }
    .tf-license { padding: 56px 0 24px; }
    .tf-license .container { max-width: 900px; }
    .tf-license__list { list-style: none; padding: 0; margin: 20px 0 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
    .tf-license__list li { background: #fff; border: 1px solid #e5e1da; border-left: 4px solid var(--color-red-primary); border-radius: 8px; padding: 14px 16px; font-weight: 600; color: var(--color-navy); }
    .tf-faqs { padding: 40px 0 56px; }
    .tf-faqs .container { max-width: 900px; }
    .tf-more { text-align: center; padding: 8px 24px 56px; }
    .tf-more p { font-size: 1.05rem; margin: 0 0 16px; }
</style>
"""


def esc(s):
    return html.escape(s, quote=True)


def norm(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def load_source():
    lines = open(SOURCE, encoding="utf-8").read().split("\n")
    text = "\n".join(lines)
    head_open = text[: text.index('  <script type="application/ld+json">')]
    styles_and_tail = text[text.index("  <style>"): text.index("</head>")]
    body_top = text[text.index("<body>"): text.index("<main>")]
    footer = text[text.index('<footer class="site-footer">'):]
    first_ld = re.search(r'<script type="application/ld\+json">(.*?)</script>', text, re.S).group(1)
    business = next(n for n in json.loads(first_ld)["@graph"] if n.get("@id") == SITE + "/#business")
    for k in ("aggregateRating", "review"):
        business.pop(k, None)
    rating_line = re.search(r'<p class="tf-reviews__rating">.*?</p>', text, re.S).group(0)
    google_link = re.search(r'<a href="(https://www\.google\.com/search\?q=thomas\+fence[^"]+)"', text).group(1)
    return head_open, styles_and_tail, body_top, footer, business, rating_line, google_link


def pick_reviews(n_pages, exclude_pages):
    pages = {p: norm(open(p, encoding="utf-8", errors="replace").read())
             for p in glob.glob(DOCS + "/**/*.html", recursive=True)
             if not any(p.startswith(x) for x in exclude_pages)}
    pool = []
    for r in json.load(open(REVIEWS))["reviews"]:
        t = (r.get("text") or "").strip()
        if len(t) < 60 or not str(r.get("stars", "")).startswith("5"):
            continue
        key = norm(t)[:70]
        if any(key in body for body in pages.values()):
            continue
        pool.append(r)
    gate = [r for r in pool if "gate" in r["text"].lower()]
    other = sorted([r for r in pool if r not in gate], key=lambda r: abs(len(r["text"]) - 320))
    picks = [[] for _ in range(n_pages)]
    for i, r in enumerate(gate):
        picks[i % n_pages].append(r)
    it = iter(other)
    for p in picks:
        while len(p) < 3:
            p.append(next(it))
    return [p[:3] for p in picks]


def review_html(r):
    return f"""        <div class="tf-review">
          <div class="tf-review__stars" aria-label="5 out of 5 stars">★★★★★</div>
          <div class="tf-review__name">{esc(r['name'])}</div>
          <div class="tf-review__meta">Google review</div>
          <p class="tf-review__text">{esc(r['text'])}</p>
        </div>"""


def build(v, business, parts, reviews):
    head_open, styles_and_tail, body_top, footer, _, rating_line, google_link = parts
    url = f"{SITE}/videos/{v['slug']}/"
    vid = v["youtube_id"]
    upload, duration = YOUTUBE[vid]
    thumb = f"https://i.ytimg.com/vi/{vid}/maxresdefault.jpg"

    head = head_open
    head = re.sub(r"<title>.*?</title>", f"<title>{esc(v['title'])}</title>", head)
    head = re.sub(r'(<meta name="description" content=")[^"]*', r"\g<1>" + esc(v["meta"]).replace("\\", "\\\\"), head)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*', r"\g<1>" + url, head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\g<1>" + esc(v["title"]), head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\g<1>" + esc(v["meta"]).replace("\\", "\\\\"), head)
    head = re.sub(r'(<meta property="og:url" content=")[^"]*', r"\g<1>" + url, head)
    head = re.sub(r'(<meta property="og:type" content=")[^"]*', r"\g<1>video.other", head)
    head = re.sub(r'(<meta property="og:image" content=")[^"]*', r"\g<1>" + thumb, head)

    tail = styles_and_tail
    tail = re.sub(r'(<meta name="twitter:title" content=")[^"]*', r"\g<1>" + esc(v["title"]), tail)
    tail = re.sub(r'(<meta name="twitter:description" content=")[^"]*', r"\g<1>" + esc(v["meta"]).replace("\\", "\\\\"), tail)
    tail = re.sub(r'(<meta name="twitter:image" content=")[^"]*', r"\g<1>" + thumb, tail)

    faqs = [(q, a, a) for q, a in v["faq_specific"]] + FAQ_COMMON
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            business,
            {
                "@type": "WebPage",
                "@id": url + "#webpage",
                "url": url,
                "name": v["title"],
                "description": v["meta"],
                "isPartOf": {"@id": SITE + "/#website"},
                "about": {"@id": SITE + "/#business"},
                "mainEntity": {"@id": url + "#video"},
                "primaryImageOfPage": thumb,
                "breadcrumb": {"@id": url + "#breadcrumb"},
            },
            {
                "@type": "VideoObject",
                "@id": url + "#video",
                "name": v["h1"],
                "description": v["video_description"],
                "thumbnailUrl": [thumb, f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"],
                "uploadDate": upload,
                "duration": duration,
                "embedUrl": f"https://www.youtube.com/embed/{vid}",
                "url": url,
                "publisher": {"@id": SITE + "/#business"},
                "creator": {"@id": SITE + "/#business"},
                "inLanguage": "en-US",
                **({"contentLocation": {"@type": "Place", "name": f"{v['town']}, Arkansas"}} if v["town"] else {}),
            },
            {
                "@type": "BreadcrumbList",
                "@id": url + "#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Gates", "item": SITE + "/gates/"},
                    {"@type": "ListItem", "position": 3, "name": "Video Gallery", "item": SITE + "/video-gallery/"},
                    {"@type": "ListItem", "position": 4, "name": v["gate_type"] + (" in " + v["town"] if v["town"] else ""), "item": url},
                ],
            },
            {
                "@type": "FAQPage",
                "@id": url + "#faq",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain}}
                    for q, _, plain in faqs
                ],
            },
        ],
    }
    schema = '  <script type="application/ld+json">\n' + json.dumps(graph, indent=2, ensure_ascii=False) + "\n  </script>\n"

    crumb = esc(v["gate_type"] + (" in " + v["town"] if v["town"] else ""))
    what = "\n".join(f"      <p>{esc(p)}</p>" for p in v["what"])
    faq_html = "\n".join(
        f"""      <details class="faq-item">
        <summary>{esc(q)}</summary>
        <div class="faq-item__answer">
          <p>{a}</p>
        </div>
      </details>""" for q, a, _ in faqs)

    main = f"""<main>

  <section class="page-hero">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <ol>
          <li><a href="/">Home</a></li>
          <li><a href="/gates/">Gates</a></li>
          <li><a href="/video-gallery/">Video Gallery</a></li>
          <li aria-current="page">{crumb}</li>
        </ol>
      </nav>
      <h1>{esc(v['h1'])}</h1>
    </div>
  </section>

  <section class="tf-watch" aria-label="Video">
    <div class="tf-watch__frame">
      <iframe src="https://www.youtube.com/embed/{vid}?rel=0" title="{esc(v['h1'])}" loading="eager" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <p class="tf-watch__caption">{esc(v['video_description'])}</p>
  </section>

  <section class="tf-hook">
    <p>{esc(v['hook'])}</p>
    <a href="/contact/" class="btn-primary">Get Your Free Quote</a>
    <span class="tf-hook__phone">or call <a href="tel:+14796364732">(479) 636-4732</a></span>
  </section>

  <section class="tf-what">
    <div class="container">
      <h2>What Is a {esc(v['gate_type'])}?</h2>
{what}
    </div>
  </section>

  <section class="tf-reviews" id="reviews">
    <div class="tf-reviews__banner">
      <h2>What Our Customers Say</h2>
      {rating_line}
    </div>
    <div class="tf-reviews__inner">
      <div class="tf-reviews__grid">
{chr(10).join(review_html(r) for r in reviews)}
      </div>
      <div class="tf-reviews__cta">
        <p>Selected reviews from our Google Business Profile, shown as written.</p>
        <a href="{google_link}" target="_blank" rel="noopener noreferrer" class="btn-primary">Read All Our Reviews on Google &#8599;</a>
      </div>
    </div>
  </section>

  <section class="tf-contact">
    <h2>Contact Us for a Free Quote</h2>
    <p>Tell us about your gate and we will visit your property, check the opening, grade and power, and give you a written estimate.</p>
    <a href="/contact/" class="btn-white">Contact Us</a>
    <span class="tf-contact__phone"><a href="tel:+14796364732">(479) 636-4732</a> &middot; Mon&ndash;Fri, 8am&ndash;4pm</span>
  </section>

  <section class="tf-finance">
    <div class="container">
      <div class="tf-finance__box">
        <div>
          <p class="tf-finance__amount">$250K</p>
          <p class="tf-finance__label">Maximum Loan Amount</p>
        </div>
        <div>
          <h2>Financing Available</h2>
          <ul>
            <li>No home equity required</li>
            <li>No prepayment penalties</li>
            <li>Funding in 1&ndash;3 days</li>
            <li>Check rates in minutes, with no credit score impact</li>
          </ul>
          <a href="https://app.gethearth.com/partners/thomas-fence/darrell/apply" target="_blank" rel="noopener noreferrer" class="btn-primary">Apply for Financing</a>
          <p class="tf-finance__disclaimer">Financing provided by Hearth. Thomas Fence is not a lender. <a href="/financing/">More on financing</a>.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="tf-license">
    <div class="container">
      <h2>Licensed, Certified and Warrantied</h2>
      <ul class="tf-license__list">
        <li>Arkansas Contractor's License No. 0155010427</li>
        <li>CGAT Certified Gate Automation Technician</li>
        <li>AFA Certified Fence Contractor</li>
        <li>US Federal Contractor Registration</li>
        <li>Serving Northwest Arkansas Since 1993</li>
        <li>1-Year Workmanship Warranty</li>
      </ul>
    </div>
  </section>

  <section class="tf-faqs">
    <div class="container">
      <h2>{esc(v['gate_type'])} FAQs</h2>
{faq_html}
    </div>
  </section>

  <section class="tf-more">
    <p>See more of our gates: cantilever, swing, ornamental, pivot, farm and chain link.</p>
    <a href="/video-gallery/" class="btn-primary">Watch More Gate Videos</a>
  </section>

  <section class="cta-band">
    <div class="container">
      <h2>Let's Build Your Gate</h2>
      <p>CGAT-certified installation, financing available, and a 1-year workmanship warranty.</p>
      <a href="/contact/" class="btn-primary">Get a Free Estimate</a>
    </div>
  </section>

</main>

"""
    return head + schema + "\n" + tail + PAGE_CSS + "</head>\n" + body_top + main + footer


def main():
    data = json.load(open(os.path.join(HERE, "videos.json")))["videos"]
    parts = load_source()
    business = parts[4]
    out_dirs = [os.path.join(DOCS, "videos", v["slug"]) for v in data]
    picks = pick_reviews(len(data), out_dirs)
    for v, revs, d in zip(data, picks, out_dirs):
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(build(v, business, parts, revs))
        print(f"built /videos/{v['slug']}/  reviews: {', '.join(r['name'] for r in revs)}")


if __name__ == "__main__":
    main()
