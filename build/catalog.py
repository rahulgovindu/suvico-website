# -*- coding: utf-8 -*-
"""
Generates the Suvico International company profile + product catalogue PDF
from the same data used to build the website (build.py).
Run:  python build/catalog.py
Output: docs/Suvico-International-Catalogue.pdf
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B
from fpdf import FPDF

ROOT = B.ROOT
OUT = os.path.join(ROOT, "docs", "Suvico-International-Catalogue.pdf")
GREEN=(16,41,29); GREEN2=(27,67,50); GOLD=(176,132,66); INK=(29,39,33); MUTE=(93,107,98); LINE=(228,222,210); CREAM=(243,238,228)

def A(p): return os.path.join(ROOT, p)

TRANS = str.maketrans({'—':'-','–':'-','‘':"'",'’':"'",
    '“':'"','”':'"','•':chr(149),' ':' ','…':'...','×':'x'})
class PDF(FPDF):
    def normalize_text(self, txt):
        return super().normalize_text(txt.translate(TRANS) if isinstance(txt,str) else txt)
    def header(self):
        if self.page_no()==1: return
        self.set_y(10); self.set_font("Helvetica","",8); self.set_text_color(*MUTE)
        self.cell(0,5,"SUVICO INTERNATIONAL  ·  Company Profile & Product Catalogue",align="L")
        self.set_draw_color(*LINE); self.line(15,18,195,18)
        self.set_xy(15,24)   # reset cursor to left so first content cell isn't offset
    def footer(self):
        if self.page_no()==1: return
        self.set_y(-15); self.set_font("Helvetica","",8); self.set_text_color(*MUTE)
        self.cell(0,5,"www.suvicointl.com   ·   apurva.suvarna@suvicointl.com   ·   +91-7045-788426",align="C")
        self.set_y(-15); self.cell(0,5,str(self.page_no()),align="R")

def H(pdf,txt,size=22):
    pdf.set_x(15); pdf.set_font("Times","B",size); pdf.set_text_color(*GREEN)
    pdf.multi_cell(0,size*0.42,txt); pdf.ln(2)
def eyebrow(pdf,txt):
    pdf.set_x(15); pdf.set_font("Helvetica","B",9); pdf.set_text_color(*GOLD)
    pdf.cell(0,5,txt.upper()); pdf.ln(7)
def body(pdf,txt,size=10.5):
    pdf.set_x(15); pdf.set_font("Helvetica","",size); pdf.set_text_color(*INK)
    pdf.multi_cell(0,5.4,txt); pdf.ln(2)

pdf=PDF(format="A4"); pdf.set_auto_page_break(True,margin=20); pdf.set_margins(15,20,15)

# ---------- COVER ----------
pdf.add_page()
pdf.set_fill_color(*GREEN); pdf.rect(0,0,210,297,"F")
pdf.set_fill_color(*GREEN2); pdf.rect(0,170,210,127,"F")
try: pdf.image(A("product/essential-oils.webp"),x=0,y=170,w=210,h=127)
except Exception as e: print("cover img:",e)
pdf.set_fill_color(*GREEN);
# fade strip
for i in range(40):
    pass
try: pdf.image(A("img/logos/footer-light-logo.png"),x=15,y=22,w=70)
except Exception as e: print("logo:",e)
pdf.set_xy(15,80); pdf.set_text_color(*GOLD); pdf.set_font("Helvetica","B",11)
pdf.cell(0,6,"PREMIUM INDIAN EXPORTS  ·  ETHICALLY SOURCED")
pdf.set_xy(15,92); pdf.set_text_color(255,255,255); pdf.set_font("Times","B",40)
pdf.multi_cell(150,16,"Company Profile &\nProduct Catalogue")
pdf.set_xy(15,138); pdf.set_font("Helvetica","",13); pdf.set_text_color(214,228,219)
pdf.multi_cell(150,7,"Essential Oils  ·  Dehydrated Fruits & Vegetables\nTraceable from farm to formulation")
pdf.set_xy(15,156); pdf.set_text_color(255,255,255); pdf.set_font("Helvetica","",10)
pdf.cell(0,5,"Navi Mumbai, India   ·   www.suvicointl.com   ·   "+B.PHONE)

# ---------- ABOUT ----------
pdf.add_page()
eyebrow(pdf,"Who we are")
H(pdf,"Founded on transparency, built on trust")
body(pdf,"Suvico International is a premium Indian exporter of essential oils and dehydrated fruits & "
        "vegetables. Founded during the COVID-19 lockdown after our founder saw how opaque and "
        "contamination-prone global ingredient supply chains had become, Suvico exists to supply "
        "premium, sustainably sourced ingredients with genuine farm-to-formulation traceability — "
        "so quality is something we can prove, not just promise.")
pdf.ln(2)
eyebrow(pdf,"Our philosophy")
pdf.set_font("Times","BI",13); pdf.set_text_color(*GOLD); pdf.cell(0,7,"Vasudhaiva Kutumbakam  —  The world is one family"); pdf.ln(7)
body(pdf,"We treat interconnectedness as a business principle: collective welfare, ethical sourcing, "
        "environmental stewardship and benefit that reaches every stakeholder, from farmer to formulator.")
pdf.set_font("Times","BI",13); pdf.set_text_color(*GOLD); pdf.cell(0,7,"Parasparam Bhavayantah  —  Mutual cooperation"); pdf.ln(7)
body(pdf,"Progress is collaborative. We grow by celebrating the success of our partners, vendors and "
        "employees, built on transparency and trust.")
pdf.ln(2)
eyebrow(pdf,"Vision & mission")
body(pdf,"Vision: to become a globally trusted name in sustainable ingredient sourcing, where Indian "
        "agriculture meets world-class standards of quality and transparency.")
body(pdf,"Mission: to deliver traceable, compliant, consistently excellent essential oils and dehydrates, "
        "while raising the bar for ethical conduct across the supply chains we touch.")

# ---------- CERTIFICATIONS ----------
pdf.add_page()
eyebrow(pdf,"Credentials"); H(pdf,"Registered, certified & compliant")
body(pdf,"Suvico International is registered with / a member of India's principal export, food and "
        "fragrance authorities, and aligns to the standards demanded by international markets.")
pdf.ln(1)
pdf.set_font("Helvetica","B",10.5); pdf.set_text_color(*GREEN); pdf.cell(0,7,"Registrations & memberships"); pdf.ln(8)
pdf.set_font("Helvetica","",10.5); pdf.set_text_color(*INK)
regs=["MSME","DGFT","APEDA","FIEO","CHEMEXCIL","FSSAI","Ministry of Food Processing","EOAI","FAFAI"]
for i in range(0,len(regs),3):
    row=regs[i:i+3]
    for r in row:
        pdf.set_text_color(*GOLD); pdf.cell(5,6,chr(149))
        pdf.set_text_color(*INK); pdf.cell(55,6,r)
    pdf.ln(7)
pdf.ln(3)
pdf.set_font("Helvetica","B",10.5); pdf.set_text_color(*GREEN); pdf.cell(0,7,"Compliance & standards"); pdf.ln(8)
pdf.set_font("Helvetica","",10.5)
comp=["EU MRL","REACH","USDA / NOP","Halal","Kosher","GMP","HACCP","ISO","Spice Board","FSSAI"]
for i in range(0,len(comp),3):
    for c in comp[i:i+3]:
        pdf.set_text_color(*GOLD); pdf.cell(5,6,chr(149))
        pdf.set_text_color(*INK); pdf.cell(55,6,c)
    pdf.ln(7)
pdf.ln(4)
pdf.set_fill_color(*CREAM); pdf.set_draw_color(*GOLD)
y=pdf.get_y(); pdf.rect(15,y,180,22,"DF")
pdf.set_xy(20,y+4); pdf.set_font("Helvetica","B",10); pdf.set_text_color(*GREEN)
pdf.cell(0,6,"Documentation with every shipment"); pdf.ln(6); pdf.set_x(20)
pdf.set_font("Helvetica","",9.5); pdf.set_text_color(*INK)
pdf.multi_cell(170,5,"Certificate of Analysis (COA), SDS / MSDS, allergen & origin declarations and applicable compliance certificates.")

# ---------- PRODUCT TABLES ----------
def section_title(title,intro):
    pdf.add_page(); eyebrow(pdf,"Product range"); H(pdf,title)
    body(pdf,intro); pdf.ln(1)

def oil_table(fam):
    d=B.FAMILIES[fam]
    pdf.set_font("Times","B",13); pdf.set_text_color(*GREEN2); pdf.cell(0,8,d["title"]); pdf.ln(9)
    headings=["Product","Botanical name","Extraction","Origin","CAS / EINECS"]
    widths=[30,38,29,22,61]
    pdf.set_x(15); pdf.set_font("Helvetica","B",8.5); pdf.set_fill_color(*GREEN); pdf.set_text_color(255,255,255)
    for h,w in zip(headings,widths): pdf.cell(w,7,h,border=0,fill=True)
    pdf.ln(7)
    pdf.set_font("Helvetica","",8.5); pdf.set_text_color(*INK)
    fill=False
    for it in d["items"]:
        cells=[it["name"],it["latin"],it["extr"],it["origin"],it["cas"]]
        h=7; x0=15; y0=pdf.get_y()
        pdf.set_fill_color(*(CREAM if fill else (255,255,255)))
        pdf.rect(x0,y0,sum(widths),h,"F")
        for i,(txt,w) in enumerate(zip(cells,widths)):
            pdf.set_xy(x0,y0)
            pdf.set_font("Helvetica","I" if i==1 else "",8.2 if i==4 else 8.5)
            pdf.cell(w,h,txt if txt else "",border=0)
            x0+=w
        pdf.set_xy(15,y0+h); fill=not fill
    pdf.ln(4)

def dehy_table(fam):
    d=B.FAMILIES[fam]
    pdf.set_font("Times","B",13); pdf.set_text_color(*GREEN2); pdf.cell(0,8,d["title"]); pdf.ln(9)
    headings=["Product","Botanical name","Available forms","Applications"]
    widths=[28,38,46,68]
    pdf.set_font("Helvetica","B",8.5); pdf.set_fill_color(*GREEN); pdf.set_text_color(255,255,255)
    for h,w in zip(headings,widths): pdf.cell(w,7,h,fill=True)
    pdf.ln(7)
    pdf.set_text_color(*INK); fill=False
    for it in d["items"]:
        cells=[it["name"],it["latin"],it["forms"],it["app"]]
        x0=15; y0=pdf.get_y()
        # compute row height from longest wrapping (forms/app)
        pdf.set_font("Helvetica","",8.5)
        nlines=max(1, pdf.get_string_width(it["app"])//( widths[3]-3)+1, pdf.get_string_width(it["forms"])//(widths[2]-3)+1)
        h=5*nlines+2
        pdf.set_fill_color(*(CREAM if fill else (255,255,255)))
        pdf.rect(x0,y0,sum(widths),h,"F")
        cx=x0
        for txt,w,idx in zip(cells,widths,range(4)):
            pdf.set_xy(cx,y0+1)
            pdf.set_font("Helvetica","I" if idx==1 else "",8.5)
            pdf.multi_cell(w,5,txt if txt else "-",border=0)
            cx+=w
        pdf.set_xy(15,y0+h); fill=not fill
    pdf.ln(4)

section_title("Essential Oils",
   "Steam-distilled and solvent-extracted oils with full botanical and CAS/EINECS identification. "
   "Packaging: 1 / 5 / 25 kg (aluminium, HDPE or food-grade). Shelf life 24-36 months. MOQ on request.")
for fam in B.OIL_FAMS:
    if pdf.get_y()>235: pdf.add_page()
    oil_table(fam)

section_title("Dehydrated Fruits & Vegetables",
   "Freeze-dried and air-dried products with locked-in colour, flavour and nutrition. FSSAI / HACCP-aligned. "
   "Packaging in food-grade bags or cartons, custom pack sizes. Shelf life 12-24 months. MOQ on request.")
for fam in B.DEHY_FAMS:
    if pdf.get_y()>225: pdf.add_page()
    dehy_table(fam)

# ---------- HOW TO ORDER / CONTACT ----------
pdf.add_page()
eyebrow(pdf,"Working with us"); H(pdf,"How to order")
steps=[("1. Enquire","Share your product, specification, required volume and destination market."),
       ("2. Samples & quote","We respond with documentation, sample options and a quote — usually within one business day."),
       ("3. Confirm","Approve specs and commercial terms. Minimum order value typically USD 2,500–10,000."),
       ("4. Produce & ship","GMP/HACCP-aligned processing, full documentation, and shipment worldwide.")]
for t,dsc in steps:
    pdf.set_font("Helvetica","B",11); pdf.set_text_color(*GREEN); pdf.cell(0,6,t); pdf.ln(6)
    pdf.set_font("Helvetica","",10); pdf.set_text_color(*INK); pdf.multi_cell(0,5.4,dsc); pdf.ln(2)
pdf.ln(4)
y=pdf.get_y(); pdf.set_fill_color(*GREEN); pdf.rect(15,y,180,52,"F")
pdf.set_xy(22,y+7); pdf.set_text_color(255,255,255); pdf.set_font("Times","B",16); pdf.cell(0,8,"Let's build a reliable supply line");
pdf.set_xy(22,y+20); pdf.set_font("Helvetica","",10.5); pdf.set_text_color(214,228,219)
pdf.multi_cell(166,6,
 "Apurva Suvarna\n"
 "Email:  apurva.suvarna@suvicointl.com   /   cust.eng@suvicointl.com\n"
 "Phone / WhatsApp:  +91-7045-788426\n"
 "Office:  13th Floor, Q2, Aurum Q Parc, Ghansoli, Navi Mumbai, India\n"
 "Web:  www.suvicointl.com")

os.makedirs(os.path.dirname(OUT),exist_ok=True)
pdf.output(OUT)
print("Catalogue written:", OUT, os.path.getsize(OUT),"bytes,", pdf.page_no(),"pages")
