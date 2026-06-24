# Suvico International — Website

A complete, production-ready rebuild of **[suvicointl.com](https://www.suvicointl.com/)** —
a premium Indian exporter of essential oils and dehydrated fruits & vegetables.

This rebuild fixes every issue from the [website audit](audit/WEBSITE-AUDIT.md):
modern responsive design, full SEO + structured data, optimised images, rich
product pages, a downloadable PDF catalogue, and analytics-ready markup.

## Quick start

```bash
# preview locally
python -m http.server 8123
# open http://localhost:8123
```

The site is **static HTML/CSS/JS** — deploy by uploading the repo root to any
web host (it's drop-in compatible with the existing Hostinger setup).

## Structure

```
.
├── *.html                 19 pages (home, our-story, 9 product pages, blog + 3 posts, contact, 404)
├── css/style.css          Single design-system stylesheet (~15 KB)
├── js/main.js             Vanilla JS — menu, scroll reveal, counters, form
├── img/  product/         Optimised images (-61% vs. original)
├── docs/                  Suvico-International-Catalogue.pdf (generated)
├── sitemap.xml robots.txt SEO
├── build/
│   ├── build.py           Site generator — edit data & copy here, then rebuild
│   └── catalog.py         PDF catalogue generator
└── audit/
    ├── WEBSITE-AUDIT.md    Full audit of the original site + ratings
    └── legacy-site-fixes/  Drop-in patches for the original PHP site
```

## Regenerating

All HTML, the sitemap, the PDF catalogue, and image optimisation are produced
from the `build/` scripts. Edit product data or copy in `build/build.py`, then:

```bash
python build/build.py      # pages + sitemap + image optimisation
python build/catalog.py    # PDF catalogue
```

> Generated `.html` files should not be hand-edited — they're overwritten on build.
> Image optimisation reads originals from a sibling `suvico-assets/` folder; if it's
> absent the existing optimised `img/` and `product/` files are used as-is.

## Before going live

1. **GA4** — replace `G-XXXXXXXXXX` in `build/build.py` (`head()`) with your real
   Measurement ID and rebuild; verify in Search Console and submit `sitemap.xml`.
2. **Contact form** — wire `#contactForm` to your live `send.php` (it currently
   shows a client-side success message in this static build).
3. Replace placeholder footer social links (`#`) with real profiles.

## Highlights vs. the original

- One `<h1>` per page · full Open Graph / Twitter / canonical · Organization,
  Product & BlogPosting JSON-LD · `sitemap.xml` + `robots.txt` · branded 404.
- 874 KB of jQuery/Bootstrap CSS replaced with a single ~15 KB stylesheet.
- Rich product pages with botanical name, CAS/EINECS, purity, grade, packaging,
  MOQ, shelf life and applications for all 27 products.
- Downloadable PDF catalogue, certification grid, philosophy and stats sections.
- Fully responsive, keyboard-accessible, reduced-motion aware.

---

*See [audit/WEBSITE-AUDIT.md](audit/WEBSITE-AUDIT.md) for the full review and ratings.*
