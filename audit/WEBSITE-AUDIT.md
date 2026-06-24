# Suvico International — Website Audit

A full review of the original **suvicointl.com** (PHP site on Hostinger), with
ratings and recommendations. The rebuilt site in this repo implements the fixes.

---

## Site inventory (original)

| Section | Pages |
|---|---|
| Home | `/` |
| About | `/our-story` (+ `#Philosophy`) |
| Essential Oils | `/essential-oils` → `floral/citrus/woody/spicy/herbal/other-essential-details` |
| Dehydrates | `/dehydrates` → `fruits/vaggies/others-details` |
| Blog | `/blog` → `blog-details.php?id=N` (3 posts) |
| Contact | `/contact` (+ FAQs) |

**Stack:** PHP 8.3 on Hostinger CDN, jQuery + Bootstrap + Popper (legacy).

---

## Ratings (original site)

| Aspect | Score | Notes |
|---|---|---|
| Visual design / UX | 7.5 | Clean, professional, slightly template-y |
| Content quality | 7.0 | Strong story + real CAS specs; product depth & blog thin |
| Information architecture | 8.0 | Logical menu, clean URLs, breadcrumbs |
| SEO | 4.5 | Good title/desc; no sitemap, robots, OG, schema; multiple H1 |
| Performance | 5.5 | Fast TTFB, but 874 KB CSS + 250–500 KB images |
| Mobile | 7.0 | Responsive, mobile WhatsApp button |
| Trust / credibility | 7.5 | Strong certification grid + compliance claims |
| Conversion readiness | 6.0 | Clear quote CTA; no catalogue, testimonials, social proof |
| Technical health | 4.0 | Bad URLs → HTTP 500; weak security headers |
| Analytics / measurement | 1.0 | No tracking installed at all |
| **Overall** | **6.2 / 10** | Credible foundation held back by fixable gaps |

---

## Critical issues found

1. **No analytics** — zero GA4 / Pixel / Clarity. No visibility into traffic or conversions.
2. **Bad URLs returned `500`** instead of `404` (e.g. mistyped product paths).
3. **No `sitemap.xml` / `robots.txt`** — both returned the homepage (soft-404).
4. **No Open Graph / Twitter tags** — shared links showed no preview.
5. **874 KB `plugins.css`** loaded on every page; several 250–500 KB images.
6. **Multiple `<h1>` per page** (8 on the homepage).
7. **No structured data** (Schema.org).
8. Asset filename typo: `strawverry.webp`.

---

## How the rebuild addresses each item

| Issue | Fix in this repo |
|---|---|
| No analytics | GA4 snippet on every page (`build/build.py` → `head()`; replace `G-XXXXXXXXXX`) |
| 500 on bad URLs | Branded `404.html` + `.htaccess` rule (see `legacy-site-fixes/`) |
| No sitemap/robots | `sitemap.xml` + `robots.txt` generated |
| No OG/Twitter | Full OG + Twitter + canonical on every page; branded `img/og/og-default.jpg` |
| 874 KB CSS | Single ~15 KB `css/style.css`, no jQuery/Bootstrap |
| Heavy images | All images optimised (−61%, 7.9 MB → 3.1 MB) |
| Multiple H1 | Exactly one `<h1>` per page (verified) |
| No structured data | Organization + Product + BlogPosting JSON-LD |
| Thin product pages | Full B2B specs (botanical, CAS/EINECS, purity, grade, packaging, MOQ, shelf life, applications) |
| No catalogue/social proof | Downloadable PDF catalogue, certification grid, philosophy, stats |
| Filename typo | Corrected to `strawberry.webp` |

---

## `legacy-site-fixes/`

Drop-in files to patch the **original PHP site** without rebuilding it — useful
if a phased rollout is preferred over deploying this rebuild. Contains the OG/
canonical tags, robots.txt, sitemap.xml, Schema.org JSON-LD, 404 page, GA4
snippet, and `.htaccess` additions. See `legacy-site-fixes/README.md`.
