import streamlit as st
from PIL import Image

# =============================
# KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="Portfolio Adicandra",
    page_icon="👨‍💻",
    layout="wide"
)

# =============================
# CSS
# =============================
st.markdown("""
<style>

.stApp{
    background-color:#f4f4f4;
}

.card{
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0px 10px 20px rgba(0,0,0,.15);
}

.section-title{
    text-align:center;
    font-size:35px;
    font-weight:bold;
    color:#333;
    margin-top:40px;
    margin-bottom:20px;
}

.skill-box{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,.1);
    text-align:center;
}

.stat-box{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,.1);
    text-align:center;
}

img{
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# =============================
# HERO
# =============================

st.title("👋 Hi! I'm Adicandra")
st.subheader("UI / UX Designer")

st.markdown("---")

# =============================
# ABOUT
# =============================

col1, col2 = st.columns([1,2])

with col1:
    image = Image.open("andra.jpeg")
    st.image(image, use_container_width=True)

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("ABOUT ME")

    st.write("### Adicandra Irsyad Firdaus Herianto")

    st.write("""
Saya adalah mahasiswa berusia **20 tahun** yang memiliki minat
di bidang **User Interface (UI)** dan **User Experience (UX)**.

Saya senang mendesain tampilan website maupun aplikasi
agar terlihat modern, menarik, dan nyaman digunakan.

Saya terus belajar mengenai desain digital, wireframe,
prototype, serta pengembangan antarmuka menggunakan
berbagai tools desain.
""")

    st.write("### Biodata")

    st.write("👤 **Nama :** Adicandra Irsyad Firdaus Herianto")
    st.write("🎂 **Umur :** 20 Tahun")
    st.write("💼 **Keahlian :** UI & UX Designer")

    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# WHAT I DO
# =============================

st.markdown("<h1 class='section-title'>WHAT I DO</h1>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
<div class="skill-box">
<h3>🎨 UI Design</h3>
<p>Membuat desain antarmuka website dan aplikasi yang modern.</p>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="skill-box">
<h3>📱 UX Design</h3>
<p>Merancang pengalaman pengguna agar nyaman dan mudah digunakan.</p>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="skill-box">
<h3>💻 Web Design</h3>
<p>Mendesain website yang responsive dan profesional.</p>
</div>
""", unsafe_allow_html=True)

# =============================
# MY SKILLS
# =============================

st.markdown("<h1 class='section-title'>MY SKILLS</h1>", unsafe_allow_html=True)

st.write("UI Design")
st.progress(90)

st.write("UX Design")
st.progress(85)

st.write("Figma")
st.progress(80)

st.write("HTML & CSS")
st.progress(70)

# =============================
# MY STATS
# =============================

st.markdown("<h1 class='section-title'>MY STATS</h1>", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
<div class="stat-box">
<h2>20</h2>
<p>Age</p>
</div>
""", unsafe_allow_html=True)

with s2:
    st.markdown("""
<div class="stat-box">
<h2>5+</h2>
<p>Projects</p>
</div>
""", unsafe_allow_html=True)

with s3:
    st.markdown("""
<div class="stat-box">
<h2>90%</h2>
<p>UI Skill</p>
</div>
""", unsafe_allow_html=True)

with s4:
    st.markdown("""
<div class="stat-box">
<h2>85%</h2>
<p>UX Skill</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown(
"""
<center>
<h4>© 2026 Adicandra Irsyad Firdaus Herianto</h4>
</center>
""",
unsafe_allow_html=True
)
