import streamlit as st
import zipfile
import io
import json
import datetime

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v28.0 | Muskan Edition", 
    layout="wide", 
    page_icon="✨",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED UI SYSTEM (CSS) ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #3b82f6; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    .stTextInput input, .stTextArea textarea { border-radius: 8px !important; border: 1px solid #cbd5e1; }
    .stButton>button {
        background: linear-gradient(135deg, #0f172a 0%, #2563eb 100%);
        color: white; font-weight: 800; border: none; height: 3.5rem;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR CONTROLS ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v28.0 | Beauty Salon Core")
    st.divider()
    
    with st.expander("🎨 Visual DNA", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Luxury Gold", "Clean Corporate", "Midnight SaaS", "Ocean Breeze"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary (Brand)", "#C71585") # Default: Medium Violet Red
        s_color = c2.color_picker("Secondary (Action)", "#10B981") # Default: Emerald
        h_font = st.selectbox("Headings", ["Playfair Display", "Montserrat", "Oswald", "Great Vibes"])
        b_font = st.selectbox("Body Text", ["Open Sans", "Lato", "Roboto", "Inter"])
        
    with st.expander("🧩 Section Manager", expanded=False):
        show_hero = st.checkbox("Hero Carousel", value=True)
        show_stats = st.checkbox("Trust Stats", value=True)
        show_features = st.checkbox("Services Grid", value=True)
        show_gallery = st.checkbox("Visual Gallery", value=True)
        show_inventory = st.checkbox("Price List/Menu", value=True)
        show_testimonials = st.checkbox("Testimonials", value=True)
        show_faq = st.checkbox("F.A.Q.", value=True)

# --- 4. MAIN WORKSPACE ---
st.title("🏗️ Website Builder")
tabs = st.tabs(["1. Identity", "2. Content", "3. Services/Prices", "4. Legal & Footer"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "Muskan Beauty Salon")
        biz_tagline = st.text_input("Tagline", "Authentic Indian Beauty Care in Riyadh")
        biz_phone = st.text_input("Phone", "053 986 8999")
        biz_email = st.text_input("Email", "booking@muskansalon.sa")
    with c2:
        prod_url = st.text_input("Website URL", "https://muskansalon.sa")
        biz_addr = st.text_area("Address", "Prince Faisal Bin Turki Bin Abdulaziz St, Al Wizarat, Riyadh 12626", height=100)
        map_iframe = st.text_area("Google Map Embed (<iframe...>)", placeholder='<iframe src="..."></iframe>', height=100)
        logo_url = st.text_input("Logo URL (Leave empty for Text Logo)")

    st.subheader("Social Links")
    sc1, sc2, sc3 = st.columns(3)
    fb_link = sc1.text_input("Facebook URL")
    ig_link = sc2.text_input("Instagram URL")
    yt_link = sc3.text_input("YouTube URL")
    wa_num = st.text_input("WhatsApp Number (No +)", "966539868999")

with tabs[1]:
    st.subheader("Hero Carousel Images")
    st.caption("Enter 3 Image URLs for the slider.")
    hero_img_1 = st.text_input("Slide 1 (Main)", "https://images.unsplash.com/photo-1560750588-73207b1ef5b8?q=80&w=1600")
    hero_img_2 = st.text_input("Slide 2", "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?q=80&w=1600")
    hero_img_3 = st.text_input("Slide 3", "https://images.unsplash.com/photo-1522337660859-02fbefca4702?q=80&w=1600")
    
    st.subheader("Hero Text")
    hero_h = st.text_input("Headline", "Reveal Your Natural Radiance")
    hero_sub = st.text_input("Subtext", "The preferred destination in Al Wizarat for authentic Indian beauty treatments.")

    st.subheader("Trust Stats")
    s1, s2, s3 = st.columns(3)
    stat_1, lbl_1 = s1.text_input("Stat 1", "4.5★"), s1.text_input("Label 1", "Google Rating")
    stat_2, lbl_2 = s2.text_input("Stat 2", "280+"), s2.text_input("Label 2", "Happy Reviews")
    stat_3, lbl_3 = s3.text_input("Stat 3", "100%"), s3.text_input("Label 3", "Hygiene")

    st.subheader("Services (Icon | Title | Desc)")
    feat_data = st.text_area("Services List", 
        "star | Herbal Facials | Rejuvenating skin treatments using natural Indian herbal products.\n"
        "scissors | Hair Styling | Professional cuts, coloring, and traditional oil massages.\n"
        "heart | Bridal Packages | Complete makeover services for your special day, including Henna.", height=150)

    st.subheader("About Section")
    about_h = st.text_input("About Title", "Where Beauty Meets Tradition")
    about_txt = st.text_area("About Description", "Located in the vibrant Al Wizarat district, Muskan Beauty Salon brings the expertise of Indian beauty rituals to Riyadh...", height=150)
    about_img = st.text_input("About Image", "https://images.unsplash.com/photo-1633681926022-84c23e8cb2d6?q=80&w=1600")

with tabs[2]:
    st.info("⚡ Power your Price List with a Google Sheet")
    sheet_url = st.text_input("CSV Link", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Default Product Image", "https://images.unsplash.com/photo-1596462502278-27bfdd403cc2?q=80&w=800")

with tabs[3]:
    st.subheader("Legal & Footer")
    testi_data = st.text_area("Testimonials (Name | Quote)", "Priya M. | The best Indian salon in Hara! Facials are amazing.\nSara A. | Very clean place and polite staff.", height=100)
    faq_data = st.text_area("FAQ (Q? ? A)", "Do I need an appointment? ? Walk-ins welcome, but booking is better.\nDo you do Henna? ? Yes, Arabic and Indian designs.", height=100)
    priv_txt = st.text_area("Privacy Policy", "We respect your privacy...", height=100)
    term_txt = st.text_area("Terms of Service", "Cancellations must be made 2 hours in advance...", height=100)

# --- 5. COMPILER ENGINE ---

def get_theme_css():
    # Theme Variables
    bg, txt, card_bg, nav_bg = "#ffffff", "#0f172a", "#ffffff", "rgba(255, 255, 255, 0.95)"
    
    if "Luxury" in theme_mode:
        bg, txt, card_bg, nav_bg = "#fdfbf7", "#2c1810", "#ffffff", "rgba(253, 251, 247, 0.95)"
    elif "Midnight" in theme_mode:
        bg, txt, card_bg, nav_bg = "#0f172a", "#f8fafc", "#1e293b", "rgba(15, 23, 42, 0.95)"

    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg}; --txt: {txt}; --card: {card_bg}; --nav: {nav_bg}; --h-font: '{h_font}', serif; --b-font: '{b_font}', sans-serif; }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: var(--bg); color: var(--txt); font-family: var(--b-font); overflow-x: hidden; }}
    h1, h2, h3, h4 {{ font-family: var(--h-font); color: var(--p); }}
    
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    section {{ padding: 5rem 0; }}
    
    /* STICKY NAV */
    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; background: var(--nav); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.05); box-shadow: 0 5px 20px rgba(0,0,0,0.05); }}
    .nav-con {{ display: flex; justify-content: space-between; align-items: center; height: 80px; }}
    .logo {{ font-size: 1.5rem; font-weight: bold; color: var(--p); text-decoration: none; }}
    .nav-links {{ display: flex; gap: 2rem; align-items: center; }}
    .nav-links a {{ text-decoration: none; color: var(--txt); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; }}
    .nav-links a:hover {{ color: var(--s); }}
    .mobile-btn {{ display: none; font-size: 1.5rem; cursor: pointer; }}
    
    /* HERO CAROUSEL */
    .hero {{ position: relative; height: 90vh; overflow: hidden; display: flex; align-items: center; justify-content: center; text-align: center; color: white; margin-top: 0; }}
    .carousel-slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.5s ease-in-out; z-index: -1; }}
    .carousel-slide.active {{ opacity: 1; }}
    .hero-overlay {{ background: rgba(0,0,0,0.4); position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; }}
    .hero-content {{ z-index: 2; position: relative; animation: slideUp 1s ease-out; }}
    
    /* UI COMPONENTS */
    .btn {{ padding: 1rem 2.5rem; border-radius: 50px; text-decoration: none; font-weight: bold; display: inline-block; transition: 0.3s; border: none; cursor: pointer; }}
    .btn-p {{ background: var(--p); color: white; }}
    .btn-s {{ background: var(--s); color: white; }}
    .btn:hover {{ transform: translateY(-3px); filter: brightness(1.1); }}
    
    .card {{ background: var(--card); padding: 2rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: 0.3s; }}
    .card:hover {{ transform: translateY(-5px); border-color: var(--s); }}
    
    /* CONTACT FORM */
    input, textarea, select {{ width: 100%; padding: 1rem; margin-bottom: 1rem; border: 1px solid #ddd; border-radius: 8px; font-family: inherit; }}
    input:focus, textarea:focus {{ border-color: var(--s); outline: none; }}
    
    /* FOOTER */
    footer {{ background: var(--p); color: white; padding: 4rem 0; margin-top: auto; }}
    footer a {{ color: rgba(255,255,255,0.8); text-decoration: none; }}
    footer a:hover {{ color: white; text-decoration: underline; }}
    .social-icon {{ width: 24px; height: 24px; fill: white; margin-right: 1rem; }}

    /* KEYFRAMES */
    @keyframes slideUp {{ from {{ opacity:0; transform: translateY(30px); }} to {{ opacity:1; transform: translateY(0); }} }}

    /* MOBILE */
    @media (max-width: 768px) {{
        .nav-links {{ position: fixed; top: 80px; left: -100%; width: 100%; height: 100vh; background: var(--bg); flex-direction: column; padding: 2rem; transition: 0.3s; align-items: flex-start; border-top: 1px solid rgba(0,0,0,0.1); }}
        .nav-links.active {{ left: 0; }}
        .mobile-btn {{ display: block; }}
        .hero {{ height: 70vh; }}
        .grid-3 {{ grid-template-columns: 1fr; }}
    }}
    """

def get_simple_icon(name):
    name = name.lower()
    if "star" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>'
    if "sciss" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M6 6c0-2.21 1.79-4 4-4s4 1.79 4 4c0 1.25-.58 2.36-1.47 3.09l1.97 1.97C15.35 10.39 16.14 10 17 10c2.21 0 4 1.79 4 4s-1.79 4-4 4-4-1.79-4-4c0-.86.39-1.65 1.06-2.5l-1.97-1.97C11.36 10.42 10.25 11 9 11l-3 8v2H4v-2l3-8C6.35 10.42 6 9.25 6 8zm4-2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm7 8c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/></svg>'
    if "heart" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>'
    return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>'

def gen_schema():
    # Schema.org Structured Data (JSON-LD)
    schema = {
        "@context": "https://schema.org",
        "@type": "BeautySalon",
        "name": biz_name,
        "image": hero_img_1,
        "telephone": biz_phone,
        "email": biz_email,
        "address": {"@type": "PostalAddress", "streetAddress": biz_addr},
        "priceRange": "$$",
        "url": prod_url
    }
    return f'<script type="application/ld+json">{json.dumps(schema)}</script>'

# --- HTML GENERATORS ---

def build_page(title, content, extra_js=""):
    nav = f"""
    <nav><div class="container nav-con">
        <a href="index.html" class="logo">{biz_name}</a>
        <div class="mobile-btn" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</div>
        <div class="nav-links">
            <a href="index.html">Home</a>
            <a href="index.html#features">Services</a>
            <a href="index.html#gallery">Gallery</a>
            <a href="about.html">About</a>
            <a href="contact.html">Contact</a>
            <a href="https://wa.me/{wa_num}" class="btn-s" style="padding:0.5rem 1.5rem; border-radius:50px; color:white;">Book Now</a>
        </div>
    </div></nav>
    """
    
    # SVG ICONS FOR FOOTER
    yt_icon = '<svg class="social-icon" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>'
    fb_icon = '<svg class="social-icon" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>'
    ig_icon = '<svg class="social-icon" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>'

    footer = f"""
    <footer><div class="container">
        <div class="grid-3">
            <div>
                <h3>{biz_name}</h3>
                <p style="opacity:0.8">{biz_addr}</p>
                <div style="margin-top:1rem;">
                    {f'<a href="{fb_link}">{fb_icon}</a>' if fb_link else ''}
                    {f'<a href="{ig_link}">{ig_icon}</a>' if ig_link else ''}
                    {f'<a href="{yt_link}">{yt_icon}</a>' if yt_link else ''}
                </div>
            </div>
            <div>
                <h4>Explore</h4>
                <a href="index.html">Home</a><br>
                <a href="about.html">About Us</a><br>
                <a href="contact.html">Contact & Location</a>
            </div>
            <div>
                <h4>Legal</h4>
                <a href="privacy.html">Privacy Policy</a><br>
                <a href="terms.html">Terms of Service</a>
            </div>
        </div>
        <div style="text-align:center; margin-top:3rem; opacity:0.6; font-size:0.9rem;">
            &copy; {datetime.datetime.now().year} {biz_name}. All rights reserved.
        </div>
    </div></footer>
    """

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | {biz_name}</title>
        <link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ','+')}:wght@700&family={b_font.replace(' ','+')}:wght@400;600&display=swap" rel="stylesheet">
        <style>{get_theme_css()}</style>
        {gen_schema()}
    </head>
    <body>
        {nav}
        {content}
        {footer}
        {extra_js}
        <script>
            // Scroll Animation
            const observer = new IntersectionObserver(entries => {{
                entries.forEach(entry => {{ if(entry.isIntersecting) entry.target.classList.add('active'); }});
            }});
            document.querySelectorAll('.reveal').forEach(el => {{ el.style.opacity=0; el.style.transition='1s'; observer.observe(el); }});
            document.querySelectorAll('.reveal.active').forEach(el => {{ el.style.opacity=1; }});
        </script>
    </body>
    </html>
    """

def gen_hero():
    # CAROUSEL LOGIC
    return f"""
    <section class="hero">
        <div class="hero-overlay"></div>
        <div class="carousel-slide active" style="background-image: url('{hero_img_1}')"></div>
        <div class="carousel-slide" style="background-image: url('{hero_img_2}')"></div>
        <div class="carousel-slide" style="background-image: url('{hero_img_3}')"></div>
        
        <div class="container hero-content">
            <h1>{hero_h}</h1>
            <p style="font-size:1.2rem; opacity:0.9; margin-bottom:2rem;">{hero_sub}</p>
            <a href="contact.html" class="btn btn-p">Book Appointment</a>
        </div>
    </section>
    <script>
        let slides = document.querySelectorAll('.carousel-slide');
        let currentSlide = 0;
        setInterval(() => {{
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }}, 4000);
    </script>
    """

def gen_features():
    cards = ""
    lines = [x for x in feat_data.split('\n') if x.strip()]
    for line in lines:
        parts = line.split('|')
        if len(parts) >= 2:
            icon = get_simple_icon(parts[0]) if len(parts) > 2 else get_simple_icon("star")
            title = parts[1 if len(parts)>2 else 0].strip()
            desc = parts[2 if len(parts)>2 else 1].strip()
            cards += f"""
            <div class="card reveal" style="text-align:center;">
                <div style="color:var(--s); margin-bottom:1rem;">{icon}</div>
                <h3>{title}</h3>
                <p style="opacity:0.8; font-size:0.95rem;">{desc}</p>
            </div>"""
            
    return f'<section id="features"><div class="container"><h2 style="text-align:center; margin-bottom:3rem;">Our Services</h2><div class="grid-3">{cards}</div></div></section>'

def gen_gallery():
    # Static Gallery for Visual Proof
    return f"""
    <section id="gallery" style="background:#f9fafb;"><div class="container">
        <h2 style="text-align:center; margin-bottom:2rem;">Treatment Gallery</h2>
        <div class="grid-3">
            <img src="https://images.unsplash.com/photo-1596462502278-27bfdd403cc2?auto=format&fit=crop&q=80&w=600" style="width:100%; height:250px; object-fit:cover; border-radius:12px;">
            <img src="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&q=80&w=600" style="width:100%; height:250px; object-fit:cover; border-radius:12px;">
            <img src="https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?auto=format&fit=crop&q=80&w=600" style="width:100%; height:250px; object-fit:cover; border-radius:12px;">
        </div>
    </div></section>
    """

def gen_contact_page():
    return f"""
    <section class="hero" style="height:50vh;"><div class="container hero-content"><h1>Contact Us</h1></div></section>
    <section><div class="container">
        <div class="grid-3" style="grid-template-columns: 1fr 2fr;">
            <div>
                <h3>Visit Us</h3>
                <p>{biz_addr}</p><br>
                <h3>Call Us</h3>
                <p><a href="tel:{biz_phone}" style="color:var(--p); font-weight:bold;">{biz_phone}</a></p>
                <br>
                <a href="https://wa.me/{wa_num}" class="btn btn-s">Chat on WhatsApp</a>
            </div>
            <div class="card">
                <h3>Send a Message</h3>
                <form action="https://formsubmit.co/{biz_email}" method="POST">
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
                        <input type="text" name="name" placeholder="Your Name" required>
                        <input type="text" name="phone" placeholder="Phone Number" required>
                    </div>
                    <input type="email" name="email" placeholder="Email Address" required>
                    <textarea name="message" rows="5" placeholder="What service are you interested in?" required></textarea>
                    <button type="submit" class="btn btn-p" style="width:100%;">Send Request</button>
                    <input type="hidden" name="_captcha" value="false">
                    <input type="hidden" name="_next" value="{prod_url}/contact.html">
                </form>
            </div>
        </div>
        <div style="margin-top:3rem; border-radius:12px; overflow:hidden;">
            {map_iframe}
        </div>
    </div></section>
    """

# --- 6. PAGE ASSEMBLY ---
home_html = ""
if show_hero: home_html += gen_hero()
if show_stats: home_html += f'<div style="background:var(--p); color:white; padding:3rem 0; text-align:center;"><div class="container grid-3"><div><h2>{stat_1}</h2><p>{lbl_1}</p></div><div><h2>{stat_2}</h2><p>{lbl_2}</p></div><div><h2>{stat_3}</h2><p>{lbl_3}</p></div></div></div>'
if show_features: home_html += gen_features()
if show_gallery: home_html += gen_gallery()
if show_testimonials: home_html += f'<section style="background:#fdfbf7"><div class="container"><h2 style="text-align:center;">Client Stories</h2><div class="grid-3" style="margin-top:2rem;">' + "".join([f'<div class="card"><i>"{x.split("|")[1].strip()}"</i><br><br><b>- {x.split("|")[0].strip()}</b></div>' for x in testi_data.split('\n') if "|" in x]) + '</div></div></section>'

about_html = f'<section class="hero" style="height:50vh;"><div class="container hero-content"><h1>About Us</h1></div></section><section><div class="container"><div class="grid-3" style="grid-template-columns:1fr 1fr; align-items:center;"><div><h2>{about_h}</h2><p style="font-size:1.1rem; line-height:1.8;">{about_txt}</p></div><img src="{about_img}" style="width:100%; border-radius:12px;"></div></div></section>'

# --- 7. EXPORT & DOWNLOAD ---
c1, c2 = st.columns([3, 1])
with c1:
    st.success("Analysis Complete. Code optimized for Muskan Beauty Salon.")
    preview = st.radio("Preview", ["Home", "Contact"], horizontal=True)
    if preview == "Home": st.components.v1.html(build_page("Home", home_html), height=600, scrolling=True)
    elif preview == "Contact": st.components.v1.html(build_page("Contact", gen_contact_page()), height=600, scrolling=True)

with c2:
    if st.button("DOWNLOAD WEBSITE ZIP", type="primary"):
        b = io.BytesIO()
        with zipfile.ZipFile(b, "w") as z:
            z.writestr("index.html", build_page("Home", home_html))
            z.writestr("contact.html", build_page("Contact", gen_contact_page()))
            z.writestr("about.html", build_page("About", about_html))
            z.writestr("privacy.html", build_page("Privacy Policy", f"<section><div class='container'><h1>Privacy Policy</h1><p>{priv_txt}</p></div></section>"))
            z.writestr("terms.html", build_page("Terms of Service", f"<section><div class='container'><h1>Terms of Service</h1><p>{term_txt}</p></div></section>"))
        st.download_button("📥 Download ZIP", b.getvalue(), "muskan_salon.zip", "application/zip")
