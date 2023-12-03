
import streamlit as st



st.set_page_config(
    page_title="Riwayat Sekolah | ulil izzah",
    page_icon="👨‍🎓",
    layout="wide"
)
st.title("BEBERAPA JENJANG PENDIDIKAN YANG SAYA LALUI SELAMA MASA HIDUP")


st.container()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("Sdn sengon 2")
   
with col2:
    st.subheader("SMPN 01 tanjung")
    
with col3:
    st.subheader("MA matholiul falah pati")
   
with col4:
    st.subheader("UNU Rombel AL Bukhori")
   
st.container()
st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
   
    st.image("sd.png", width= 190)
with col2:
   
    st.image("smp.jpeg", width= 190)
with col3:
    
    st.image("ma.jpeg", width= 190)
with col4:
    
    st.image("unuu.png", width= 190)



