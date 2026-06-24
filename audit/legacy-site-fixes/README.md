# Suvico International — Drop-in Fixes

These files implement the critical/high-value fixes from the website audit.
Hand them to whoever maintains the site. Everything is plain HTML/text — no
build step. The site runs PHP on Hostinger, so all of this is paste-and-go.

> Tip: take a backup of the current files before editing, and test on one
> page first before rolling out site-wide.

---

## Install order (fastest impact first)

### 1. Analytics — `ga4-snippet.html`  ⏱ ~20 min
Create a GA4 property + Google Search Console, paste your `G-XXXXXXXXXX` ID,
then add the snippet as the **first thing inside `<head>`** on every page.
Without this you can't measure any of the other improvements.

### 2. Crawlability — `robots.txt` + `sitemap.xml`  ⏱ ~10 min
Upload both to the **site root** (`public_html/`), so they resolve at
`https://www.suvicointl.com/robots.txt` and `/sitemap.xml`.
Then in Search Console → Sitemaps → submit `sitemap.xml`.
> Currently these URLs return the homepage (a "soft 404"). Once the real
> files exist they'll serve correctly.

### 3. Error pages + headers + speed — `404.html` + `htaccess-additions.txt`  ⏱ ~30 min
- Upload `404.html` to the site root.
- Open `htaccess-additions.txt` and **append** the blocks to your existing
  `.htaccess` (read the warning at the top — do NOT replace the file).
- This fixes the `500 Internal Server Error` on mistyped URLs, adds security
  headers, enables gzip compression, and sets caching.

### 4. Link previews — `head-social-and-canonical.html`  ⏱ ~30 min
Paste the tags into each page's `<head>` (after the existing
`<meta name="description">`) and fill the 4 `{{...}}` values per page using
the ready-made list at the bottom of the file.
> Recommended: create a `1200×630` share image at `/img/og/og-default.jpg`.
> Until then the tags still work pointing at the logo.

### 5. Structured data — `schema-organization.html` + `schema-product-example-floral.html`  ⏱ ~45 min
- `schema-organization.html`: paste once into `<head>` on every page. Fill in
  your real LinkedIn/Instagram/Facebook URLs (or delete those lines).
- `schema-product-example-floral.html`: example for one product page. Copy the
  pattern to the other detail pages, swapping name/image/CAS values.

---

## After you ship — verify

| What | Tool |
|------|------|
| Link previews | https://www.opengraph.xyz (paste a page URL) |
| Structured data | https://search.google.com/test/rich-results |
| 404 now returns 404 (not 500) | visit `suvicointl.com/does-not-exist` |
| Security headers | https://securityheaders.com |
| Speed / image weight | https://pagespeed.web.dev |
| Indexing | Google Search Console → URL Inspection |

---

## Still worth doing (not code — content/assets)

- **Compress images.** Several are 250–500 KB (`dehydrates.png` 496 KB,
  `turmeric.webp` 384 KB). Re-export under 100 KB; convert PNG/JPEG → WebP.
  Add `loading="lazy"` to `<img>` tags below the fold.
- **Add a downloadable catalog / company-profile PDF** and per-product spec
  sheets (COA/SDS). B2B buyers expect these before enquiring.
- **Add social proof** — client/region count, testimonials, factory photos.
- **Add real social media links** (LinkedIn for B2B) — there are none today.
- **Fix the typo** in the asset filename `strawverry.webp` → `strawberry.webp`.
- **Revisit the blog** — 3 thin posts look abandoned; either commit to regular
  buyer-focused articles or hide the section.
