
import streamlit as st



st.set_page_config(
    page_title="Portfolio | ulil izzah",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("My Profile")
   st.image("ulil.jpg", width= 300)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : Ulil Izaah karim")
   st.caption("NIM : 0402201091")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 16 mei 1981
            - Alamat               : sengon-tanjung-brebes
            - Hobi                 : Menulis
            - Cita-cita            : Pengusaha
            - Hal yang disukai     : Mayoran
            - Status               : menikah 
            """
        )
st.header("*Call Me If You Want*")