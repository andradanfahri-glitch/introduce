import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="Perkenalan Diri",
    page_icon="👨‍💻",
    layout="centered"
)

# CSS
st.markdown("""
<style>
body{
    background-color:#f5f5f5;
}
.title{
    text-align:center;
    color:#0F172A;
    font-size:40px;
    font-weight:bold;
}
.sub{
    text-align:center;
    color:gray;
    font-size:18px;
}
.box{
    background-color:#ffffff;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 10px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# Judul
st.markdown('<p class="title">👋 Perkenalan Diri</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Selamat Datang di Website Profil Saya</p>', unsafe_allow_html=True)

st.divider()

# Foto
image = Image.open("andra.jpeg")
st.image(image, width=280)

st.divider()

# Biodata
st.markdown('<div class="box">', unsafe_allow_html=True)

st.header("📌 Biodata")

st.write("**Nama :** Adicandra Irsyad Firdaus Herianto")
st.write("**Umur :** 20 Tahun")
st.write("**Keahlian :** UI Design & UX Design")

st.markdown("""
### Tentang Saya

Halo!

Saya adalah mahasiswa yang memiliki minat pada bidang
**User Interface (UI)** dan **User Experience (UX)**.

Saya senang membuat desain aplikasi maupun website yang
modern, sederhana, dan nyaman digunakan oleh pengguna.

Saya terus belajar mengenai desain digital, prototyping,
serta pengembangan antarmuka agar dapat menghasilkan
produk yang menarik dan bermanfaat.
""")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# Skill
st.header("💡 Skill")

st.progress(90)
st.write("UI Design - 90%")

st.progress(85)
st.write("UX Design - 85%")

st.progress(70)
st.write("Figma - 70%")

st.progress(60)
st.write("HTML & CSS - 60%")

st.divider()

st.success("Terima kasih telah mengunjungi website perkenalan saya 😊")
