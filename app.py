import streamlit as st
import datetime
from lorem_text import lorem

st.set_page_config(
    page_title = 'Mari belajar streamlit',
    layout='wide'
)

#Menulis teks di streamlit

st.write("hello world!")

"hello world!" #<- Magic

"_ini juga hello world!_"

"**ini juga**"

"# ini adalah header"

"## ini adalah subheader"

st.title("ini header")
st.header("ini juga header")

st.caption("Langit senja minum kopi")

st.code("import streamlit as st")

st.code('''
import pandas as pd
import streamlit as st #untuk memanggil package streamlit
''')

#latex
st.latex("ax^2+bx+c=0")

#widget <- Input element

ini_tombol = st.button("Tekan tombol ini")
ini_tombol

saya_setuju = st.checkbox("Centang jika setuju")
if saya_setuju:
    st.write("anda setuju untuk belajar lebih giat")
else:
    st.write("Ayo belajar")

#Radio button, memilih 1 dari sekian opsi
buah_favorit = st.radio(
    "Pilih buah favorit kamu",
    ['Apel','Anggur','Jeruk','Mangga']
)
buah_favorit

makanan = st.selectbox(
    "Pilih makanan yang akan diorder",
    ['Paket 1', 'Paket goceng','Kids meal']
)
makanan

belanjaan = st.multiselect(
    "Pilih item belanjaan kalian",
    ['Terigu','Minyak goreng','Biskuit','Minuman']
)
belanjaan #tipe nya list

parameter_alpha = st.slider(
    "Insert alpha value",
    min_value = 0.0,
    max_value = 1.0,
    step = 0.1,
    value = 0.5 #Menentukan nilai default
)
parameter_alpha

ukuran_baju = st.select_slider(
    "Ukuran baju",
    ['XS','S','M','L','XL','XXL']
)
ukuran_baju

kode_pos = st.number_input(
    "Masukan nomor hp kalian",
    min_value=0,
    max_value=99999,
    step=1
)
kode_pos

nama = st.text_input("Masukan nama kalian")
nama

komentar = st.text_area("Masukan komentar kamu")
komentar

tanggal_jadian = st.date_input("masukan tanggal jadian")

tanggal_lahir = st.date_input(
    "Tanggal lahir",
    min_value= datetime.date(1990,1,1)
)

jam_mulai = st.time_input("Masukan jam mulai")

warna = st.color_picker("masukan warna")
warna

#masukan image, video, dan suara

#container dan layouting

#kolom

col1, col2, col3 = st.columns(3)

with col1:
    lahir_saya= st.date_input("Tanggal lahir kamu")
with col2:
    lahir_kamu= st.date_input("Tanggal lahir dia")
with col3:
    jadian = st.date_input("Tanggal jadian")
st.button("Hitung")

kol1,kol2 = st.columns([2,6])
with kol1:
    lahir_aku= st.date_input("Tanggal lahir aku")
with kol2:
    lahir_dia= st.date_input("Tanggal lahir dirinya")

with st.sidebar:
    st.title("Titanic survival mode explorer")
    your_name= st.text_input("Enter your name")

    with st.expander("Lorem ipsum"):
        st.write(lorem.paragraphs(1))

tab1, tab2, tab3 = st.tabs(['Tab1','Tab2','Tab3'])
with tab1:
    st.write(lorem.paragraphs(1))
with tab2:
    st.write(lorem.paragraphs(2))
with tab3:
    st.write(lorem.paragraphs(3))

with st.container():#bagian metrics
    st.write("ini teks di dalam container")
    st.write("ini teks di dalam container")
    st.write("ini teks di dalam container")
    st.write("ini teks di dalam container")
st.write("ini teks di luar container")

st.markdown(''' div.stButton > button:first-child {
background-color: #00cc00;color:white;font-size:20px;height:3em;width:30em;border-radius:10px 10px 10px 10px;
}
''', unsafe_allow_html=True)