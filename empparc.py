import streamlit as st

st.title("Empresas Parceiras")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3.3, 3.3, 3.3])

with col1:
  st.image("spacex.jpg")
  st.title("SpaceX")
  st.write("Fabricante estadunidense de sistemas aeroespaciais, transporte espacial e comunicaçõe.")
  st.link_button("Acessar Site", "https://www.spacex.com/")
  
with col2:
  st.image("apple.jpg")
  st.title("Apple")
  st.write("Multinacional americana. Famosa por revolucionar a tecnologia pessoal com o iPhone, Mac e iPad.")
  st.link_button("Acessar Site", "https://www.apple.com/br/")
  
with col3:
  st.image("netflix.jpg")
  st.title("Netflix")
  st.write("Principal serviço de streaming por assinatura do mundo. Permite assistir a um vasto catálogo de séries, filmes e documentários em TVs, celulares e computadores.")
  st.link_button("Acessar Site", "https://www.netflix.com/br/")

st.write("")

