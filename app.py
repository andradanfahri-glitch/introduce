import streamlit as st
from PIL import Image
# =============================
# HERO
# =============================

st.markdown("""
<div style="
background:white;
padding:35px;
border-radius:20px;
box-shadow:0px 10px 25px rgba(0,0,0,.15);
margin-bottom:35px;
">

<h1 style="margin-bottom:0;color:#222;">
Hi! I'm
</h1>

<h1 style="
font-size:50px;
color:#0f172a;
margin-top:0;
">
Adicandra Irsyad Firdaus Herianto
</h1>

<h3 style="color:gray;">
UI / UX Designer
</h3>

<p style="font-size:18px;color:#555;">
Selamat datang di website portfolio saya.
Saya merupakan mahasiswa yang memiliki minat
di bidang User Interface (UI) dan User Experience (UX).
Saya senang membuat tampilan website maupun aplikasi
yang modern, minimalis, dan nyaman digunakan.
</p>

</div>
""", unsafe_allow_html=True)


# =============================
# ABOUT
# =============================

col1, col2 = st.columns([1,2])

with col1:

    image = Image.open("andra.jpeg")
    st.image(image, use_container_width=True)

with col2:

    st.markdown("""
<div class="card">

<h1 style="margin-top:0;">
ABOUT ME
</h1>

<h2>
Adicandra Irsyad Firdaus Herianto
</h2>

<p style="font-size:18px; line-height:32px;">
Saya adalah mahasiswa berusia <b>20 tahun</b>
yang memiliki minat di bidang
<b>User Interface (UI)</b> dan
<b>User Experience (UX)</b>.

Saya senang mendesain tampilan website maupun
aplikasi agar terlihat modern,
menarik, dan nyaman digunakan.

Saya terus belajar mengenai desain digital,
wireframe, prototype, serta
pengembangan antarmuka menggunakan berbagai tools desain.
</p>

<hr>

<h2>Biodata</h2>

<p>👤 <b>Nama :</b> Adicandra Irsyad Firdaus Herianto</p>

<p>🎂 <b>Umur :</b> 20 Tahun</p>

<p>💼 <b>Keahlian :</b> UI & UX Designer</p>

</div>
""", unsafe_allow_html=True)
