# -*- coding: utf-8 -*-
"""
Suvico International — static site generator.
Generates every HTML page from real product data and optimises all images.
Run:  python build/build.py        (from inside suvico-site/)
"""
import os, shutil, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # suvico-site/
SRC_ASSETS = os.path.abspath(os.path.join(ROOT, "..", "suvico-assets"))
SITE = "https://www.suvicointl.com"
WA = "919833561582"
PHONE = "+91-7045-788426"
PHONE_TEL = "+917045788426"
EMAIL = "apurva.suvarna@suvicointl.com"
EMAIL2 = "cust.eng@suvicointl.com"
ADDR = "13th Floor, Q2, Aurum Q Parc, Thane-Belapur Rd, Ghansoli, Navi Mumbai, Maharashtra, India"
OG_DEFAULT = "img/og/og-default.jpg"
CATALOGUE = "docs/Suvico-International-Catalogue.pdf"

# ---------------------------------------------------------------- icons
IC = {
"leaf":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M11 20A7 7 0 0 1 4 13C4 6 11 4 20 4c0 9-2 16-9 16Z"/><path d="M4 20c2-4 5-7 9-9"/></svg>',
"shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6Z"/><path d="m9 12 2 2 4-4"/></svg>',
"globe":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 3 2.5 15 0 18M12 3c-2.5 3-2.5 15 0 18"/></svg>',
"handshake":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="m11 17 2 2a1.4 1.4 0 0 0 2-2"/><path d="m13 17 3 3a1.4 1.4 0 0 0 2-2l-4-4"/><path d="M3 11l4-4 5 5"/><path d="M21 11l-4-4-3 3"/><path d="m7 14-2 2"/></svg>',
"flask":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M7.5 15h9"/></svg>',
"doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Z"/><path d="M14 3v6h6M8 13h8M8 17h6"/></svg>',
"truck":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M3 6h11v9H3Z"/><path d="M14 9h4l3 3v3h-7Z"/><circle cx="7" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/></svg>',
"sprout":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 21v-7"/><path d="M12 14c0-3-2-5-6-5 0 4 3 5 6 5Z"/><path d="M12 12c0-3 2-5 6-5 0 4-3 5-6 5Z"/></svg>',
"pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>',
"mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
"phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 4h4l2 5-3 2a12 12 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>',
"clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
"check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m5 12 5 5 9-11"/></svg>',
"wa":'<svg viewBox="0 0 32 32"><path d="M16 3C9 3 3.5 8.5 3.5 15.5c0 2.4.7 4.6 1.8 6.5L3 29l7.2-2.2c1.8 1 3.9 1.5 6 1.5 7 0 12.5-5.5 12.5-12.5S23 3 16 3Zm0 22.8c-1.9 0-3.7-.5-5.2-1.4l-.4-.2-4.3 1.3 1.3-4.1-.3-.4a10 10 0 0 1-1.6-5.4c0-5.6 4.6-10.2 10.2-10.2S26 9.9 26 15.5 21.6 25.8 16 25.8Zm5.7-7.6c-.3-.2-1.8-.9-2.1-1-.3-.1-.5-.2-.7.2s-.8 1-1 1.2-.4.2-.7.1a8.3 8.3 0 0 1-4-3.6c-.3-.5.3-.5.8-1.6.1-.2 0-.4 0-.5l-1-2.3c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.4-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.2 3.4 5.3 4.7 2 .8 2.7.9 3.7.8.6-.1 1.8-.8 2.1-1.5.3-.7.3-1.4.2-1.5-.1-.1-.3-.2-.6-.4Z"/></svg>',
"li":'<svg viewBox="0 0 24 24"><path d="M4.98 3.5A2.5 2.5 0 1 1 5 8.5a2.5 2.5 0 0 1 0-5ZM3 9h4v12H3Zm6 0h3.8v1.7h.1c.5-1 1.8-2 3.7-2 4 0 4.7 2.6 4.7 6V21h-4v-5.3c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9V21H9Z"/></svg>',
"ig":'<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4a3.8 3.8 0 0 1-1.4-.9 3.8 3.8 0 0 1-.9-1.4c-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2Zm0 1.8c-3.1 0-3.5 0-4.7.1-1.1.1-1.7.2-2.1.4-.5.2-.9.4-1.3.8-.4.4-.6.8-.8 1.3-.2.4-.3 1-.4 2.1-.1 1.2-.1 1.6-.1 4.7s0 3.5.1 4.7c.1 1.1.2 1.7.4 2.1.2.5.4.9.8 1.3.4.4.8.6 1.3.8.4.2 1 .3 2.1.4 1.2.1 1.6.1 4.7.1s3.5 0 4.7-.1c1.1-.1 1.7-.2 2.1-.4.5-.2.9-.4 1.3-.8.4-.4.6-.8.8-1.3.2-.4.3-1 .4-2.1.1-1.2.1-1.6.1-4.7s0-3.5-.1-4.7c-.1-1.1-.2-1.7-.4-2.1a3.5 3.5 0 0 0-.8-1.3 3.5 3.5 0 0 0-1.3-.8c-.4-.2-1-.3-2.1-.4-1.2-.1-1.6-.1-4.7-.1Zm0 3.1a4.9 4.9 0 1 1 0 9.8 4.9 4.9 0 0 1 0-9.8Zm0 8a3.2 3.2 0 1 0 0-6.4 3.2 3.2 0 0 0 0 6.4Zm6.2-8.2a1.1 1.1 0 1 1-2.3 0 1.1 1.1 0 0 1 2.3 0Z"/></svg>',
"x":'<svg viewBox="0 0 24 24"><path d="M18 3h3l-7 8 8.2 10H16l-5-6-5.8 6H2l7.5-9L1.6 3H8l4.6 5.7L18 3Zm-1 16h1.7L7.1 4.8H5.3Z"/></svg>',
}

# ---------------------------------------------------------------- data
GENERIC_OIL = [
    ("Purity", "100% pure & natural"),
    ("Grade", "Commercial / Therapeutic (on request)"),
    ("Packaging", "1 kg, 5 kg, 25 kg — aluminium / HDPE / food-grade"),
    ("MOQ", "On request (typical orders USD 2,500–10,000)"),
    ("Shelf life", "24–36 months, properly stored"),
    ("Documentation", "COA, SDS/MSDS, allergen & origin declarations"),
]
GENERIC_DEHY = [
    ("Purity", "100% natural, additive-free"),
    ("Moisture", "Typically < 5–8% (per spec)"),
    ("Packaging", "Food-grade bags / cartons, custom pack sizes"),
    ("MOQ", "On request (typical orders USD 2,500–10,000)"),
    ("Shelf life", "12–24 months, properly stored"),
    ("Documentation", "COA, FSSAI/HACCP compliance, origin declarations"),
]

def oil(name, latin, extr, origin, cas, img, app):
    return dict(kind="oil", name=name, latin=latin, extr=extr, origin=origin, cas=cas, img=img, app=app)
def dehy(name, latin, forms, origin, img, app):
    return dict(kind="dehy", name=name, latin=latin, forms=forms, origin=origin, img=img, app=app)

FAMILIES = {
 "floral": dict(title="Floral Essential Oils", cat="Essential Oils", hero="product/floral.webp",
   desc="Romantic, opulent florals — the heart of fine perfumery and luxury skincare.", parent=("essential-oils.html","Essential Oils"),
   items=[
     oil("Rose (Absolute)","Rosa damascena","Solvent Extraction","India","84604-12-6 / 8007-01-0 / 290-260-3","product/product-details/rose.webp","Prestige perfumery, skincare and aromatherapy blends."),
     oil("Lavender","Lavandula angustifolia","Steam Distillation","India","84776-65-8 / 8000-28-0 / 283-994-0","product/product-details/lavender.webp","Perfumery, personal care, soaps, candles and calming aromatherapy."),
     oil("Jasmine (Absolute)","Jasminum grandiflorum","Solvent Extraction","India","84776-64-7 / 8022-96-6 / 289-960-1","product/product-details/jasmine.webp","High-end perfumery, cosmetics and luxury fragrance compositions."),
   ]),
 "citrus": dict(title="Citrus Essential Oils", cat="Essential Oils", hero="product/citrus.webp",
   desc="Bright, zesty top notes prized in fragrance, flavour and home care.", parent=("essential-oils.html","Essential Oils"),
   items=[
     oil("Lemon","Citrus limonum","Steam Distillation","India","84929-31-7 / 8008-56-8 / 284-515-8","product/product-details/lemon.webp","Fragrance, flavour, household care and uplifting aromatherapy."),
     oil("Orange","Citrus sinensis","Steam Distillation","India","8028-48-6 / 8008-57-9 / 232-433-8","product/product-details/orange.webp","Beverages, confectionery flavour, cleaning products and perfumery."),
     oil("Bergamot","Citrus bergamia risso","Steam Distillation","Italy, China","89957-91-5 / 8007-75-8 / 289-612-9","product/product-details/bergamot.webp","Classic eau-de-cologne, fine fragrance and tea flavouring."),
   ]),
 "woody": dict(title="Woody Essential Oils", cat="Essential Oils", hero="product/woody.webp",
   desc="Grounding base notes that anchor and fix sophisticated accords.", parent=("essential-oils.html","Essential Oils"),
   items=[
     oil("Pine","Abies sibirica","Steam Distillation","India","91697-89-1 / 8021-29-2 / 294-351-9","product/product-details/pine.webp","Household and industrial fragrance, disinfectants and masculine perfumery."),
     oil("Vetiver","Vetiveria zizanioides","Steam Distillation","India","84238-29-9 / 8016-96-4 / 282-490-8","product/product-details/Vetiver.webp","Fixative in fine perfumery, oriental and woody bases."),
     oil("Cedarwood","Cedrus deodora","Steam Distillation","India","91771-47-0 / 68991-36-6 / 639-646-9","product/product-details/cedarwood.webp","Perfumery base notes, soaps, aromatherapy and insect-repellent formulas."),
   ]),
 "spicy": dict(title="Spicy Essential Oils", cat="Essential Oils", hero="product/spicy.webp",
   desc="Warm, characterful spice oils for flavour, fragrance and wellness.", parent=("essential-oils.html","Essential Oils"),
   items=[
     oil("Clove","Eugenia caryophyllata","Steam Distillation","India","84961-50-2 / 8000-34-8 / 284-638-7","product/product-details/clove.webp","Flavour, oral-care, fragrance and warming aromatherapy."),
     oil("Turmeric","Curcuma longa","Steam Distillation","India","84775-52-0 / 8024-37-1 / 283-882-1","product/product-details/turmeric.webp","Nutraceuticals, flavour, skincare and functional formulations."),
     oil("Cardamom","Elettaria cardamomum","Solvent Extraction","India","96507-91-4 / 8000-66-6 / 288-922-1","product/product-details/cardamom.webp","Gourmet flavour, beverages, fine fragrance and oriental accords."),
   ]),
 "herbal": dict(title="Herbal Essential Oils", cat="Essential Oils", hero="product/herbal.webp",
   desc="Fresh, therapeutic herbs spanning flavour, pharma and personal care.", parent=("essential-oils.html","Essential Oils"),
   items=[
     oil("Basil","Ocimum basilicum","Steam Distillation","India, Egypt","84775-71-3 / 8015-73-4 / 283-900-8","product/product-details/basil.webp","Flavour, perfumery, personal care and herbal aromatherapy."),
     oil("Eucalyptus","Eucalyptus globulus","Steam Distillation","India","84625-32-1 / 8000-48-4 / 283-406-2","product/product-details/eucalyptus.webp","Pharmaceutical, oral-care, balms, inhalants and cleaning products."),
     oil("Peppermint","Mentha piperita","Steam Distillation","India","84082-70-2 / 8006-90-4 / 282-015-4","product/product-details/peppermint.webp","Flavour, confectionery, oral-care, cosmetics and aromatherapy."),
   ]),
 "specialty-oils": dict(title="Specialty Essential Oils", cat="Essential Oils", hero="product/other-essential.webp",
   desc="Rare and indulgent oils for prestige fragrance and flavour houses.", parent=("essential-oils.html","Essential Oils"),
   items=[
     oil("Olibanum (Frankincense)","Boswellia carteri","Steam Distillation","India","8050-07-5 / 8016-36-2 / 289-620-2","product/product-details/olibanum.webp","Prestige perfumery, skincare, meditation and aromatherapy blends."),
     oil("Coffee","Coffea arabica","Solvent Extraction","India","84650-00-0 / 8001-67-0 / 283-481-1","product/product-details/coffee.webp","Gourmand fragrance, flavour and indulgent cosmetic formulations."),
     oil("Vanilla (Absolute)","Vanilla planifolia","Solvent Extraction","Madagascar","84650-63-5 / 8024-06-4 / 283-521-8","product/product-details/vanilla.webp","Fine fragrance, flavour, confectionery and luxury personal care."),
   ]),
 "fruits": dict(title="Dehydrated Fruits", cat="Dehydrates", hero="product/fruits.webp",
   desc="Freeze-dried and air-dried fruits with locked-in colour, flavour and nutrition.", parent=("dehydrates.html","Dehydrates"),
   items=[
     dehy("Banana","Musa acuminata","Powder, Sliced","India","product/product-details/banana.webp","Smoothies, desserts, baking and snack applications."),
     dehy("Mango","Mangifera indica","Powder, Diced, Sliced","India","product/product-details/mango.webp","Desserts, smoothies, confectionery and culinary applications."),
     dehy("Strawberry","Fragaria x ananassa","Powder, Sliced","India","product/product-details/strawberry.webp","Desserts, beverages, jams and bakery products."),
   ]),
 "vegetables": dict(title="Dehydrated Vegetables", cat="Dehydrates", hero="product/vegetables.webp",
   desc="Consistent, contaminant-tested dehydrated vegetables for food manufacturers.", parent=("dehydrates.html","Dehydrates"),
   items=[
     dehy("Onion","Allium cepa","Powder, Sliced, Chopped","India","product/product-details/onion.webp","Soups, sauces, seasoning mixes and snacks."),
     dehy("Potato","Solanum tuberosum","Powder, Sliced, Diced, Batonnet (French Fries)","India","product/product-details/potato.webp","Processed foods, frozen snacks and culinary applications."),
     dehy("Tomato","Solanum lycopersicum","Powder, Sliced, Chopped","India","product/product-details/tomato.webp","Sauces, soups, seasoning blends and culinary applications."),
   ]),
 "specialty-dehydrates": dict(title="Specialty Dehydrates", cat="Dehydrates", hero="product/other-products.webp",
   desc="Specialty dehydrated ingredients for seasonings, bakery and processed foods.", parent=("dehydrates.html","Dehydrates"),
   items=[
     dehy("Garlic","Allium sativum","Powder, Flakes, Granules","India","product/product-details/garlic.webp","Seasonings, processed foods and culinary use."),
     dehy("Mushroom","Selected genus / species","Powder, Sliced, Chopped","India","product/product-details/mushroom.webp","Soups, sauces, seasonings and culinary preparations."),
     dehy("Egg","—","Powder","India","product/product-details/egg.webp","Bakery, confectionery and processed foods."),
   ]),
}

OIL_FAMS = ["floral","citrus","woody","spicy","herbal","specialty-oils"]
DEHY_FAMS = ["fruits","vegetables","specialty-dehydrates"]

CERTS = [
 ("img/clients/msme.png","MSME"),("img/clients/dgft-logo.jpg","DGFT"),("img/clients/APEDA.png","APEDA"),
 ("img/clients/FIEO11.png","FIEO"),("img/clients/CHEMEXCIL.webp","CHEMEXCIL"),("img/clients/fssai.jpg","FSSAI"),
 ("img/clients/fpi.jpg","Ministry of Food Processing"),("img/clients/EOAI.png","EOAI"),("img/certification/FAFAI1.png","FAFAI"),
]
COMPLIANCE = ["EU MRL","REACH","USDA / NOP","Halal","Kosher","GMP","HACCP","ISO","Spice Board","FSSAI"]

BLOG = [
 dict(slug="fresh-juicy-fruits", title="Fresh & Juicy Fruits for Every Day", date="January 15, 2026",
   cat="Fruits", img="product/fruits.webp",
   excerpt="Why dehydrated fruit is quietly becoming the smartest ingredient on the shelf — for flavour, shelf life and traceability.",
   body=["Dehydrated fruit has moved well beyond the trail-mix aisle. For food manufacturers, it solves three problems at once: it removes the moisture that drives spoilage, it concentrates flavour and colour, and it makes year-round sourcing of seasonal fruit realistic.",
     "At Suvico, every batch is traceable from the farm it grew on to the formulation it ends up in. That matters because a mango powder is only as good as the fruit — and the field — behind it.",
     "Whether you are formulating a smoothie blend, a cereal inclusion or a bakery filling, the right dehydrate gives you consistency that fresh fruit simply cannot promise across a production year."],
   quote="Good dehydrated fruit isn't a compromise on fresh — it's a different, more reliable tool."),
 dict(slug="farm-fresh-vegetables", title="Farm-Fresh Vegetables, Straight to Your Kitchen", date="January 15, 2026",
   cat="Vegetables", img="product/vegetables.webp",
   excerpt="From onion powder to batonnet potato, here's how dehydrated vegetables earn their place in industrial and retail kitchens alike.",
   body=["Dehydrated vegetables are the unsung workhorses of the food industry. They ship light, store long, and rehydrate predictably — which is exactly what a seasoning house, soup manufacturer or snack brand needs.",
     "The challenge is contamination and inconsistency. That's where sourcing discipline matters: tested raw material, controlled drying, and documentation that travels with the shipment.",
     "Our vegetable range — onion, potato, tomato and more — is processed to hold colour and aroma, and is backed by FSSAI and HACCP-aligned protocols so your QA team has the paperwork it expects."],
   quote="The difference between a commodity vegetable powder and a great one is everything you can't see: the testing, the traceability, the consistency."),
 dict(slug="woody-essential-oils", title="Ground Yourself with Woody Essential Oils", date="January 15, 2026",
   cat="Woody", img="product/woody.webp",
   excerpt="Cedarwood, vetiver and pine: the grounding base notes every perfumer and aromatherapist returns to.",
   body=["Woody essential oils are the foundation of countless fragrances. They are the base notes — the part of a scent that lingers — and they bring a grounding, earthy depth that brighter top notes simply cannot.",
     "Vetiver, with its smoky, rooty character, is one of perfumery's great fixatives. Cedarwood lends a soft, dry warmth. Pine brings a fresh, resinous lift that works as beautifully in a household cleaner as in a masculine accord.",
     "Each of our woody oils ships with full botanical and CAS/EINECS identification and compliance documentation — because a fragrance house needs certainty, not just a beautiful smell."],
   quote="Top notes get the attention; base notes do the work."),
]

# ---------------------------------------------------------------- shared HTML
def head(title, desc, path, og_image, jsonld=""):
    canonical = SITE + "/" + path
    og = SITE + "/" + og_image
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="author" content="Suvico International">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#10291d">
<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Suvico International">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{og}">
<link rel="icon" type="image/png" href="img/logos/favicon.png">
<link rel="apple-touch-icon" href="img/logos/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<!-- GA4: replace G-XXXXXXXXXX with your Measurement ID -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XXXXXXXXXX');</script>
{jsonld}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""

def header(active=""):
    def cls(k): return ' class="active"' if k == active else ''
    sub_oils = "".join(f'<li><a href="{f}.html">{FAMILIES[f]["title"].replace(" Essential Oils","")}</a></li>' for f in OIL_FAMS)
    sub_dehy = "".join(f'<li><a href="{f}.html">{FAMILIES[f]["title"].replace("Dehydrated ","").replace(" Dehydrates","")}</a></li>' for f in DEHY_FAMS)
    return f"""<div class="topbar"><div class="container">
  <div class="pill">{IC['pin']}&nbsp;Navi Mumbai, India &nbsp;·&nbsp; Exporting worldwide</div>
  <div class="tb-right">
    <a class="pill hide-sm" href="{CATALOGUE}" target="_blank" rel="noopener">{IC['doc']}&nbsp;Download Catalogue</a>
    <a class="pill hide-sm" href="mailto:{EMAIL}">{IC['mail']}&nbsp;{EMAIL}</a>
    <a class="pill" href="tel:{PHONE_TEL}">{IC['phone']}&nbsp;{PHONE}</a>
  </div>
</div></div>
<header class="site-header"><div class="container"><nav class="nav" aria-label="Primary">
  <a class="brand" href="index.html" aria-label="Suvico International home">
    <img src="img/logos/logo.png" alt="Suvico International" height="50">
  </a>
  <div class="nav-menu">
    <ul class="menu">
      <li{cls('home')}><a href="index.html">Home</a></li>
      <li{cls('about')}><a href="our-story.html">Our Story</a></li>
      <li class="has-sub{' active' if active=='oils' else ''}"><a href="essential-oils.html">Essential Oils</a>
        <ul class="submenu">{sub_oils}</ul></li>
      <li class="has-sub{' active' if active=='dehy' else ''}"><a href="dehydrates.html">Dehydrates</a>
        <ul class="submenu">{sub_dehy}</ul></li>
      <li{cls('blog')}><a href="blog.html">Blog</a></li>
      <li{cls('contact')}><a href="contact.html">Contact</a></li>
    </ul>
  </div>
  <div class="nav-cta">
    <a class="btn btn--primary" href="contact.html">Get a Quote</a>
    <button class="hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="nav-menu"><span></span><span></span><span></span></button>
  </div>
</nav></div></header>
<div class="nav-backdrop" hidden></div>
<main id="main">
"""

def footer():
    cols = "".join(f'<li><a href="{f}.html">{FAMILIES[f]["title"]}</a></li>' for f in OIL_FAMS[:5])
    cold = "".join(f'<li><a href="{f}.html">{FAMILIES[f]["title"]}</a></li>' for f in DEHY_FAMS)
    return f"""</main>
<footer class="site-footer"><div class="container">
  <div class="footer-grid">
    <div class="footer-brand">
      <img src="img/logos/footer-light-logo.png" alt="Suvico International">
      <p>Premium Indian exporter of essential oils and fruit &amp; vegetable dehydrates — built on transparency, sustainability and fully traceable, ethical sourcing.</p>
      <div class="socials">
        <a href="#" aria-label="LinkedIn">{IC['li']}</a>
        <a href="#" aria-label="Instagram">{IC['ig']}</a>
        <a href="#" aria-label="X">{IC['x']}</a>
      </div>
    </div>
    <div><h4>Essential Oils</h4><ul>{cols}</ul></div>
    <div><h4>Dehydrates</h4><ul>{cold}<li><a href="our-story.html">Our Story</a></li><li><a href="blog.html">Blog</a></li></ul></div>
    <div><h4>Get in touch</h4><ul>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="mailto:{EMAIL2}">{EMAIL2}</a></li>
      <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
      <li>{ADDR}</li>
      <li><a href="{CATALOGUE}" target="_blank" rel="noopener">&#128196; Download Catalogue (PDF)</a></li>
      <li><a class="btn btn--gold" href="contact.html" style="margin-top:8px">Request a Quote</a></li>
    </ul></div>
  </div>
  <div class="footer-bottom">
    <span>&copy; <span id="year">2026</span> Suvico International. All rights reserved.</span>
    <span>Essential Oils &amp; Dehydrates · Made in India · Shipped worldwide</span>
  </div>
</div></footer>
<a class="wa-float" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{IC['wa']}</a>
<script src="js/main.js"></script>
</body></html>"""

def page_hero(eyebrow, title, desc, bg, crumbs=None):
    cr = ""
    if crumbs:
        parts = []
        for i,(href,label) in enumerate(crumbs):
            if href: parts.append(f'<a href="{href}">{label}</a>')
            else: parts.append(f'<span>{label}</span>' if i==len(crumbs)-1 else label)
        cr = '<div class="crumbs">' + ' <span>/</span> '.join(parts) + '</div>'
    return f"""<section class="page-hero"><div class="page-hero__bg"><img src="{bg}" alt="" loading="eager"></div>
<div class="container">{cr}<span class="eyebrow">{eyebrow}</span><h1>{title}</h1><p class="lead">{desc}</p></div></section>"""

def cta_band():
    return f"""<section class="section"><div class="container"><div class="cta-band reveal">
  <h2>Let's build a reliable supply line</h2>
  <p>Tell us your specification, volume and destination market. We'll respond with documentation, samples and a quote — usually within one business day.</p>
  <div class="btn-row">
    <a class="btn btn--gold" href="contact.html">Request a Quote</a>
    <a class="btn btn--ghost" href="https://wa.me/{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a>
  </div></div></div></section>"""

def write(path, content):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(content)

# ---------------------------------------------------------------- pages
def build_home():
    jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"Suvico International","url":"https://www.suvicointl.com/","logo":"https://www.suvicointl.com/img/logos/logo.png","description":"Premium Indian exporter of essential oils and fruit & vegetable dehydrates.","email":"apurva.suvarna@suvicointl.com","telephone":"+91-7045-788426","address":{"@type":"PostalAddress","streetAddress":"13th Floor, Q2, Aurum Q Parc, Thane-Belapur Rd, Ghansoli","addressLocality":"Navi Mumbai","addressRegion":"Maharashtra","addressCountry":"IN"},"sameAs":[]}
</script>"""
    oils_tiles = "".join(tile(f) for f in OIL_FAMS[:3])
    dehy_tiles = "".join(tile(f) for f in DEHY_FAMS)
    certs = "".join(f'<div class="cert"><img src="{src}" alt="{alt} certification" loading="lazy"></div>' for src,alt in CERTS)
    comp = "".join(f'<span class="tagpill">{c}</span>' for c in COMPLIANCE)
    feats = [
      ("leaf","Botanical purity","Single-origin raw material, ethically sourced and tested for residues, heavy metals and adulteration."),
      ("doc","Full traceability","Farm-to-formulation documentation: COA, SDS, allergen and origin declarations with every shipment."),
      ("globe","Global compliance","Aligned to EU MRL, REACH, USDA/NOP, Halal, Kosher, GMP and HACCP requirements."),
      ("handshake","True partnership","Responsive, single-point support and a relationship built to scale with your demand."),
    ]
    feat_html = "".join(f'<div class="feature reveal"><span class="ic">{IC[i]}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in feats)
    body = head("Suvico International | Premium Indian Exports — Essential Oils & Dehydrates",
        "Premium Indian exporter of essential oils and fruit & vegetable dehydrates. Traceable, sustainably sourced, certification-backed ingredients for global fragrance, food and nutraceutical markets.",
        "", OG_DEFAULT, jsonld) + header("home")
    body += f"""
<section class="hero"><div class="hero__bg"><img src="product/essential-oils.webp" alt="" fetchpriority="high"></div>
  <div class="container"><div class="hero__inner">
    <span class="eyebrow">Premium Indian Exports · Ethically Sourced</span>
    <h1>From flower to formula, with nothing to hide.</h1>
    <p>Suvico International supplies the world's fragrance, food and nutraceutical houses with traceable essential oils and dehydrated fruits &amp; vegetables — sourced sustainably, documented fully, and delivered consistently.</p>
    <div class="btn-row">
      <a class="btn btn--gold" href="essential-oils.html">Explore Essential Oils</a>
      <a class="btn btn--ghost" href="dehydrates.html">View Dehydrates</a>
    </div>
    <div class="hero__badges">
      <div><b>27+</b>Products &amp; variants</div>
      <div><b>9</b>Trade &amp; quality bodies</div>
      <div><b>100%</b>Traceable sourcing</div>
    </div>
  </div></div>
</section>

<section class="section"><div class="container">
  <div class="center" style="max-width:720px;margin-inline:auto;margin-bottom:46px">
    <span class="eyebrow">Why Suvico</span>
    <h2>Ingredients you can stand behind</h2>
    <p class="lead">We started Suvico to fix what we saw broken in global ingredient supply chains: opacity. Everything we do is built around proof — of origin, of quality, and of conduct.</p>
  </div>
  <div class="grid grid-4">{feat_html}</div>
</div></section>

<section class="section section--tint"><div class="container">
  <span class="eyebrow center" style="display:block;text-align:center">Our Range</span>
  <h2 class="center">Essential Oils</h2>
  <p class="lead center" style="margin-bottom:36px">Floral, citrus, woody, spicy, herbal and specialty oils — each with full botanical and CAS/EINECS identification.</p>
  <div class="grid grid-3">{oils_tiles}</div>
  <div class="center" style="margin-top:30px"><a class="btn btn--outline" href="essential-oils.html">See all essential oils</a></div>
</div></section>

<section class="section"><div class="container">
  <h2 class="center">Dehydrated Fruits &amp; Vegetables</h2>
  <p class="lead center" style="margin-bottom:36px">Colour, flavour and nutrition preserved by engineered dehydration — for food manufacturers and brands.</p>
  <div class="grid grid-3">{dehy_tiles}</div>
  <div class="center" style="margin-top:30px"><a class="btn btn--outline" href="dehydrates.html">See all dehydrates</a></div>
</div></section>

<section class="section section--dark"><div class="container">
  <div class="stats">
    <div class="stat"><b data-count="27" data-suffix="+">0</b><span>Products &amp; variants</span></div>
    <div class="stat"><b data-count="9">0</b><span>Trade &amp; quality memberships</span></div>
    <div class="stat"><b data-count="100" data-suffix="%">0</b><span>Documented &amp; traceable</span></div>
    <div class="stat"><b data-count="24" data-suffix="/7">0</b><span>Partner support</span></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="center" style="max-width:680px;margin-inline:auto;margin-bottom:40px">
    <span class="eyebrow">Credentials</span>
    <h2>Registered, certified &amp; compliant</h2>
    <p class="muted">Member of and registered with India's principal export, food and fragrance authorities — and aligned to the standards your market demands.</p>
  </div>
  <div class="cert-grid reveal">{certs}</div>
  <div class="compliance">{comp}</div>
</div></section>
{cta_band()}
"""
    body += footer()
    write("index.html", body)

def tile(fam):
    d = FAMILIES[fam]
    chips = "".join(f'<span class="chip">{it["name"].split(" (")[0]}</span>' for it in d["items"])
    short = d["title"].replace(" Essential Oils","").replace("Dehydrated ","")
    return f"""<a class="tile reveal" href="{fam}.html"><img src="{d['hero']}" alt="{d['title']}" loading="lazy">
  <div class="tile__c"><h3>{short}</h3><p>{d['desc']}</p><div class="chips">{chips}</div></div></a>"""

def build_category(slug, title, eyebrow, desc, hero, fams, active, intro):
    crumbs=[("index.html","Home"),(None,title)]
    body = head(f"{title} | Suvico International", desc, slug+".html", OG_DEFAULT) + header(active)
    body += page_hero(eyebrow, title, desc, hero, crumbs)
    tiles = "".join(tile(f) for f in fams)
    body += f"""<section class="section"><div class="container">
  <div style="max-width:760px;margin-bottom:40px"><p class="lead">{intro}</p></div>
  <div class="grid grid-3">{tiles}</div>
</div></section>
<section class="section section--tint"><div class="container">
  <div class="center" style="max-width:680px;margin-inline:auto">
    <span class="eyebrow">Documentation</span><h2>Every order, fully papered</h2>
    <p class="muted">Certificate of Analysis, SDS/MSDS, allergen &amp; origin declarations and compliance certificates accompany every shipment — so your QA and regulatory teams have what they need before the goods land.</p>
    <div class="btn-row" style="justify-content:center;margin-top:22px"><a class="btn btn--primary" href="contact.html">Request specs &amp; samples</a></div>
  </div>
</div></section>"""
    body += footer()
    write(slug+".html", body)

def spec_rows(it):
    if it["kind"]=="oil":
        rows=[("Botanical name",f'<em>{it["latin"]}</em>'),("Extraction method",it["extr"]),
              ("Country of origin",it["origin"]),("EU / US CAS · EINECS",it["cas"])]
        rows += GENERIC_OIL
    else:
        rows=[("Botanical name",f'<em>{it["latin"]}</em>' if it["latin"]!="—" else "—"),
              ("Available forms",it["forms"]),("Country of origin",it["origin"])]
        rows += GENERIC_DEHY
    return "".join(f'<tr><th>{k}</th><td>{v}</td></tr>' for k,v in rows)

def build_family(fam):
    d = FAMILIES[fam]
    parent_href, parent_label = d["parent"]
    crumbs=[("index.html","Home"),(parent_href,parent_label),(None,d["title"])]
    # product JSON-LD
    blocks=[]
    for it in d["items"]:
        desc = f'{it["name"]} ({it["latin"]}), origin {it["origin"]}.' if it["latin"]!="—" else it["name"]
        extra = f' Extraction: {it["extr"]}.' if it["kind"]=="oil" else f' Forms: {it["forms"]}.'
        j = ('{"@context":"https://schema.org","@type":"Product","name":"%s","image":"%s","category":"%s","brand":{"@type":"Brand","name":"Suvico International"},"description":"%s"}'
             % (it["name"].replace('"','')+" — Suvico International", SITE+"/"+it["img"], d["cat"], (desc+extra).replace('"','')))
        blocks.append('<script type="application/ld+json">\n'+j+'\n</script>')
    jsonld="\n".join(blocks)
    title=f'{d["title"]} Exporter India | Suvico International'
    metadesc=f'{d["title"]} from Suvico International — {", ".join(it["name"].split(" (")[0] for it in d["items"])}. Full botanical, CAS/EINECS and compliance documentation. Request a quote or sample.'
    body = head(title, metadesc, fam+".html", d["hero"], jsonld) + header("oils" if d["cat"]=="Essential Oils" else "dehy")
    body += page_hero(d["cat"], d["title"], d["desc"], d["hero"], crumbs)
    prods=""
    for it in d["items"]:
        latin = f'<span class="product__latin">{it["latin"]}</span>' if it["latin"]!="—" else ""
        subj = "I would like a sample"
        prods += f"""<article class="product reveal" id="{it['name'].split(' (')[0].lower()}">
  <div class="product__media"><img src="{it['img']}" alt="{it['name']} — {d['title']}" loading="lazy" width="600" height="600"></div>
  <div class="product__info">
    <div class="product__name"><h3>{it['name']}</h3>{latin}</div>
    <div class="applications"><b>Applications:</b> {it['app']}</div>
    <table class="spec"><tbody>{spec_rows(it)}</tbody></table>
    <div class="btn-row">
      <a class="btn btn--primary" href="contact.html">Request a Quote</a>
      <a class="btn btn--outline" href="contact.html">Request a Sample</a>
    </div>
    <div class="docnote">{IC['check']} COA, SDS/MSDS &amp; origin documentation available on request.</div>
  </div>
</article>"""
    body += f'<section class="section"><div class="container">{prods}</div></section>'
    body += cta_band()
    body += footer()
    write(fam+".html", body)

def build_our_story():
    crumbs=[("index.html","Home"),(None,"Our Story")]
    body = head("Our Story | Suvico International",
      "How Suvico was founded on transparency and traceability, and the philosophy — Vasudhaiva Kutumbakam and Parasparam Bhavayantah — that guides our sourcing.",
      "our-story.html","img/Philosophy.jpeg") + header("about")
    body += page_hero("Our Story","Founded on transparency, built on trust",
      "Suvico International began with a simple conviction: the world deserves ingredients it can trust — and proof to back it up.", "img/Philosophy.jpeg", crumbs)
    body += f"""
<section class="section"><div class="container"><div class="split">
  <div class="reveal"><span class="eyebrow">The beginning</span><h2>From a lockdown realisation to a sourcing company</h2>
    <p>Suvico was founded during the COVID-19 lockdown. Watching documentaries that exposed how contaminated and opaque global food supply chains had become — films like <em>Poisoned</em>, <em>Rotten</em> and <em>Food, Inc.</em> — our founder saw the same gap again and again: buyers had no real visibility into where their ingredients came from, or how they were handled.</p>
    <p>That gap became our reason to exist. Suvico International was built to supply premium, sustainably sourced essential oils and dehydrates with genuine farm-to-formulation traceability — so quality is something we can <em>prove</em>, not just promise.</p>
  </div>
  <div class="reveal"><img src="img/exper.png" alt="Sourcing and quality at Suvico International" style="border-radius:var(--radius);box-shadow:var(--shadow)" loading="lazy"></div>
</div></div></section>

<section class="section section--tint"><div class="container">
  <div class="center" style="max-width:680px;margin-inline:auto;margin-bottom:40px">
    <span class="eyebrow">Our Philosophy</span><h2>Two ancient Indian principles, one modern company</h2></div>
  <div class="grid grid-2">
    <div class="principle reveal"><div class="sk">Vasudhaiva Kutumbakam</div>
      <h3>The world is one family</h3>
      <p>We treat interconnectedness as a business principle, not a slogan. That means prioritising collective welfare — ethical sourcing, environmental stewardship and benefit that reaches every stakeholder in the chain, from the farmer to the formulator.</p></div>
    <div class="principle reveal"><div class="sk">Parasparam Bhavayantah</div>
      <h3>Mutual cooperation</h3>
      <p>Progress is collaborative. We grow by celebrating the success of our partners, vendors and employees — built on transparency, trust and a genuine commitment to each other's outcomes.</p></div>
  </div>
</div></section>

<section class="section"><div class="container"><div class="split">
  <div class="reveal"><span class="eyebrow">What drives us</span><h2>Vision &amp; mission</h2>
    <p><b>Our vision</b> is to become a globally trusted name in sustainable ingredient sourcing — where Indian agriculture meets world-class standards of quality and transparency.</p>
    <p><b>Our mission</b> is to deliver traceable, compliant, consistently excellent essential oils and dehydrates, while raising the bar for ethical conduct across the supply chains we touch.</p>
  </div>
  <div class="reveal"><ul class="timeline">
    <li><b>The problem we saw</b><p class="muted">Opaque, contamination-prone ingredient supply chains with no real traceability.</p></li>
    <li><b>Our answer</b><p class="muted">Single-origin sourcing, residue and adulteration testing, and full documentation.</p></li>
    <li><b>How we operate</b><p class="muted">GMP and HACCP-aligned processing, with COA, SDS and origin declarations as standard.</p></li>
    <li><b>Where we're going</b><p class="muted">A dependable China-plus-one partner for fragrance, food and nutraceutical buyers worldwide.</p></li>
  </ul></div>
</div></div></section>
{cta_band()}
"""
    body += footer()
    write("our-story.html", body)

def build_blog_index():
    body = head("Blog | Suvico International",
      "Insights on essential oils, dehydrated ingredients, sourcing and global ingredient supply from Suvico International.",
      "blog.html",OG_DEFAULT) + header("blog")
    body += page_hero("Journal","Notes on ingredients, sourcing & trade",
      "Practical perspective on essential oils, dehydrates and what it takes to source them responsibly.", "product/woody.webp",
      [("index.html","Home"),(None,"Blog")])
    cards=""
    for p in BLOG:
        cards += f"""<a class="card post-card reveal" href="blog-{p['slug']}.html">
  <div class="card__media"><img src="{p['img']}" alt="{p['title']}" loading="lazy"></div>
  <div class="card__body"><span class="card__tag">{p['cat']}</span><h3>{p['title']}</h3>
    <div class="post-meta"><span>{p['date']}</span></div>
    <p class="muted">{p['excerpt']}</p><span class="card__link">Read article</span></div></a>"""
    body += f'<section class="section"><div class="container"><div class="grid grid-3">{cards}</div></div></section>'
    body += footer()
    write("blog.html", body)

def build_blog_posts():
    for idx,p in enumerate(BLOG):
        others=[q for q in BLOG if q["slug"]!=p["slug"]][:2]
        rel="".join(f"""<a class="card post-card reveal" href="blog-{q['slug']}.html"><div class="card__media"><img src="{q['img']}" alt="{q['title']}" loading="lazy"></div>
        <div class="card__body"><span class="card__tag">{q['cat']}</span><h3>{q['title']}</h3><span class="card__link">Read article</span></div></a>""" for q in others)
        jsonld=('<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"BlogPosting","headline":"%s","datePublished":"2026-01-15","image":"%s","author":{"@type":"Organization","name":"Suvico International"},"publisher":{"@type":"Organization","name":"Suvico International","logo":{"@type":"ImageObject","url":"%s/img/logos/logo.png"}}}\n</script>'
                % (p["title"].replace('"',''), SITE+"/"+p["img"], SITE))
        body = head(f"{p['title']} | Suvico International", p["excerpt"], f"blog-{p['slug']}.html", p["img"], jsonld)
        body += header("blog")
        body += f"""<article class="section"><div class="container">
  <div class="article">
    <div class="crumbs" style="color:var(--muted)"><a href="index.html">Home</a> <span>/</span> <a href="blog.html">Blog</a> <span>/</span> <span>{p['cat']}</span></div>
    <span class="eyebrow">{p['cat']}</span>
    <h1>{p['title']}</h1>
    <div class="post-meta" style="margin-bottom:8px"><span>{p['date']}</span><span>·</span><span>Suvico International</span></div>
    <img src="{p['img']}" alt="{p['title']}">
    <p style="font-size:1.18rem">{p['body'][0]}</p>
    <blockquote>{p['quote']}</blockquote>
    <p>{p['body'][1]}</p>
    <p>{p['body'][2]}</p>
    <div class="btn-row" style="margin-top:26px"><a class="btn btn--primary" href="contact.html">Talk to our team</a></div>
  </div>
</div></article>
<section class="section section--tint"><div class="container"><h2 class="center" style="margin-bottom:34px">Keep reading</h2>
  <div class="grid grid-2" style="max-width:760px;margin-inline:auto">{rel}</div></div></section>"""
        body += footer()
        write(f"blog-{p['slug']}.html", body)

def build_contact():
    fams_opts="".join(f'<option>{FAMILIES[f]["title"]}</option>' for f in OIL_FAMS+DEHY_FAMS)
    faqs=[
     ("What products does Suvico export?","We export a full range of essential oils — floral, citrus, woody, spicy, herbal and specialty — alongside dehydrated fruits, vegetables and specialty products such as garlic, mushroom and egg."),
     ("How do you assure quality?","Raw material is sourced single-origin and tested for residues, heavy metals and adulteration. Processing follows GMP and HACCP-aligned protocols, and every shipment carries a Certificate of Analysis, SDS/MSDS and origin documentation."),
     ("Which certifications and standards do you hold?","We are registered with / members of MSME, DGFT, APEDA, FIEO, CHEMEXCIL, FSSAI, the Ministry of Food Processing, EOAI and FAFAI, and align to EU MRL, REACH, USDA/NOP, Halal, Kosher, GMP and HACCP requirements."),
     ("What processing technologies do you use?","Essential oils are produced by steam distillation and solvent extraction; dehydrates use controlled freeze-drying and air-drying to preserve colour, flavour and nutrition."),
     ("What is your minimum order?","Minimum order value typically ranges from USD 2,500 to USD 10,000 depending on the product and demand. Samples can be arranged ahead of bulk orders."),
     ("How do I order samples or place a bulk order?","Send us your specification, required volume and destination market via the form, email or WhatsApp. We'll respond with documentation, sample options and a quote — usually within one business day."),
    ]
    faq_html="".join(f'<details class="faq reveal"><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)
    body = head("Contact / Request a Quote | Suvico International",
      "Request a quote or sample of Suvico essential oils and dehydrates. Based in Navi Mumbai, India. MOQ from USD 2,500. We reply within one business day.",
      "contact.html",OG_DEFAULT) + header("contact")
    body += page_hero("Contact","Let's start a conversation",
      "Request a quote, order a sample or just ask a question — our team replies within one business day.", "img/about.jpg",
      [("index.html","Home"),(None,"Contact")])
    body += f"""<section class="section"><div class="container"><div class="split" style="align-items:start">
  <div class="reveal">
    <h2>Send an enquiry</h2>
    <p class="muted">Tell us what you need. The more detail (product, volume, destination, target spec), the faster we can come back with something useful.</p>
    <form id="contactForm" class="form" novalidate>
      <div class="field"><label for="name">Your name *</label><input id="name" name="name" required></div>
      <div class="field"><label for="company">Company</label><input id="company" name="company"></div>
      <div class="field"><label for="designation">Designation</label><input id="designation" name="designation"></div>
      <div class="field"><label for="email">Email *</label><input id="email" name="email" type="email" required></div>
      <div class="field"><label for="contact">Contact no.</label><input id="contact" name="contact"></div>
      <div class="field"><label for="country">Country</label><input id="country" name="country"></div>
      <div class="field full"><label for="product">Product of interest</label><select id="product" name="product"><option value="">— Select —</option>{fams_opts}</select></div>
      <div class="field full"><label for="subject">I would like to *</label><select id="subject" name="subject" required>
        <option value="">— Select —</option><option>Make an enquiry</option><option>Request a quote</option><option>Request a sample</option></select></div>
      <div class="field full"><label for="message">Message</label><textarea id="message" name="message" placeholder="Specification, volume, destination market..."></textarea></div>
      <div class="full"><button class="btn btn--primary" type="submit">Send enquiry</button>
        <p id="formNote" role="status" hidden style="margin-top:14px;color:var(--green-600);font-weight:600"></p></div>
    </form>
  </div>
  <div class="reveal">
    <div class="info-card">
      <h3>Reach us directly</h3>
      <div class="info-row">{IC['pin']}<div><b>Office</b><br>{ADDR}</div></div>
      <div class="info-row">{IC['mail']}<div><b>Email</b><br><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="mailto:{EMAIL2}">{EMAIL2}</a></div></div>
      <div class="info-row">{IC['phone']}<div><b>Phone</b><br><a href="tel:{PHONE_TEL}">{PHONE}</a></div></div>
      <div class="info-row">{IC['clock']}<div><b>Response time</b><br>Within one business day</div></div>
      <a class="btn btn--gold" href="https://wa.me/{WA}" target="_blank" rel="noopener" style="margin-top:6px">Chat on WhatsApp</a>
    </div>
    <iframe class="map-embed" title="Suvico International location" loading="lazy" style="margin-top:22px"
      src="https://www.google.com/maps?q=Aurum%20Q%20Parc%20Ghansoli%20Navi%20Mumbai&output=embed"></iframe>
  </div>
</div></div></section>
<section class="section section--tint"><div class="container">
  <div class="center" style="max-width:680px;margin-inline:auto;margin-bottom:34px"><span class="eyebrow">FAQ</span><h2>Frequently asked questions</h2></div>
  <div style="max-width:820px;margin-inline:auto">{faq_html}</div>
</div></section>"""
    body += footer()
    write("contact.html", body)

def build_404():
    body = head("Page Not Found (404) | Suvico International","The page you were looking for could not be found.","404.html","product/essential-oils.webp")
    body += header()
    body += f"""<section class="section center"><div class="container" style="padding-block:60px">
  <div class="eyebrow">Error 404</div>
  <h1 style="font-size:clamp(3rem,9vw,6rem);color:var(--gold-600)">404</h1>
  <h2>This page couldn't be found</h2>
  <p class="lead center">The page may have moved or no longer exists. Let's get you back on track.</p>
  <div class="btn-row" style="justify-content:center;margin-top:24px">
    <a class="btn btn--primary" href="index.html">Back to Home</a>
    <a class="btn btn--outline" href="contact.html">Request a Quote</a>
  </div></div></section>"""
    body += footer()
    write("404.html", body)

def build_seo_files():
    pages = ["","our-story.html","essential-oils.html","dehydrates.html","blog.html","contact.html"] \
        + [f+".html" for f in OIL_FAMS+DEHY_FAMS] + [f"blog-{p['slug']}.html" for p in BLOG]
    urls=""
    for p in pages:
        loc = SITE+"/"+p
        pr = "1.0" if p=="" else ("0.9" if p in ("essential-oils.html","dehydrates.html","contact.html") else "0.7")
        urls += f"  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n"
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'</urlset>\n')
    write("robots.txt", "User-agent: *\nAllow: /\nDisallow: /build/\n\nSitemap: "+SITE+"/sitemap.xml\n")

# ---------------------------------------------------------------- images
def optimize_images():
    try:
        from PIL import Image
    except Exception as e:
        print("Pillow missing, copying images as-is:", e)
        for dirpath,_,files in os.walk(SRC_ASSETS):
            for fn in files:
                s=os.path.join(dirpath,fn); rel=os.path.relpath(s,SRC_ASSETS)
                d=os.path.join(ROOT,rel); os.makedirs(os.path.dirname(d),exist_ok=True); shutil.copy2(s,d)
        return
    LIMITS={"hero":1700,"product":900,"tile":1100,"cert":320,"logo":400}
    def limit_for(rel):
        r=rel.replace("\\","/")
        if "logos" in r: return LIMITS["logo"]
        if "clients" in r or "certification" in r: return LIMITS["cert"]
        if "product-details" in r: return LIMITS["product"]
        if r.startswith("product/"): return LIMITS["tile"]
        return LIMITS["hero"]
    saved_before=saved_after=0
    for dirpath,_,files in os.walk(SRC_ASSETS):
        for fn in files:
            s=os.path.join(dirpath,fn); rel=os.path.relpath(s,SRC_ASSETS).replace("\\","/")
            # fix the strawberry typo on the way out
            out_rel = rel.replace("strawverry","strawberry")
            d=os.path.join(ROOT,out_rel); os.makedirs(os.path.dirname(d),exist_ok=True)
            ext=fn.lower().rsplit(".",1)[-1]
            saved_before+=os.path.getsize(s)
            if ext not in ("jpg","jpeg","png","webp"):
                shutil.copy2(s,d); saved_after+=os.path.getsize(d); continue
            try:
                im=Image.open(s); im.load()
                mx=limit_for(rel)
                if max(im.size)>mx:
                    r=mx/max(im.size); im=im.resize((round(im.size[0]*r),round(im.size[1]*r)), Image.LANCZOS)
                params={}
                if ext in ("jpg","jpeg"):
                    if im.mode in ("RGBA","P"): im=im.convert("RGB")
                    params=dict(quality=82,optimize=True,progressive=True)
                elif ext=="png":
                    params=dict(optimize=True)
                    if im.mode=="P": im=im.convert("RGBA")
                elif ext=="webp":
                    params=dict(quality=80,method=6)
                im.save(d,**params)
                if os.path.getsize(d)>os.path.getsize(s):  # keep smaller original
                    shutil.copy2(s,d)
                saved_after+=os.path.getsize(d)
            except Exception as e:
                print("  ! could not optimize",rel,e); shutil.copy2(s,d); saved_after+=os.path.getsize(d)
    print(f"Images: {saved_before/1e6:.2f} MB -> {saved_after/1e6:.2f} MB ({100*(1-saved_after/saved_before):.0f}% smaller)")

# ---------------------------------------------------------------- run
def main():
    optimize_images()
    build_home()
    build_category("essential-oils","Essential Oils","Our Range",
        "Steam-distilled and solvent-extracted essential oils from India — every oil with full botanical, CAS and EINECS identification, and EU MRL / REACH / USDA-NOP-ready documentation.",
        "product/essential-oils.webp", OIL_FAMS, "oils",
        "From opulent florals to grounding woods, our essential oils serve fragrance, flavour, cosmetic and nutraceutical houses worldwide. Browse by family below — each product page carries complete identification and compliance data.")
    build_category("dehydrates","Dehydrates","Our Range",
        "Freeze-dried and air-dried fruits, vegetables and specialty products — FSSAI / APEDA / HACCP-aligned and built for food and nutraceutical manufacturers.",
        "product/dehydrates.png", DEHY_FAMS, "dehy",
        "Engineered dehydration locks in colour, flavour and nutrition while removing the moisture that drives spoilage. Our range is contaminant-tested and documented for demanding food manufacturers.")
    for fam in FAMILIES: build_family(fam)
    build_our_story()
    build_blog_index()
    build_blog_posts()
    build_contact()
    build_404()
    build_seo_files()
    print("Build complete.")

if __name__=="__main__":
    main()
