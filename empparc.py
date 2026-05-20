import streamlit as st

st.title("Empresas Parceiras")

col1, col2, col3 = st.columns([1, 2, 3])

with col1:
  st.image("spacex.jpg")
  st.write("SpaceX é uma fabricante estadunidense de sistemas aeroespaciais, transporte espacial e comunicações com sede em Boca Chica, perto de Brownsville, no Texas.")
  st.link_button("Acessar Site", "https://www.spacex.com/")
  
with col2:
  st.image("apple.jpg")
  st.write("A Apple é uma multinacional americana. Famosa por revolucionar a tecnologia pessoal com o iPhone, Mac e iPad, ela destaca-se pelo design premium e a forte integração entre seus produtos.")
  st.link_button("Acessar Site", "https://www.apple.com/br/")

with col3:
  st.image("netflix.jpg")
  st.write("A Netflix é o principal serviço de streaming por assinatura do mundo. A plataforma permite assistir a um vasto catálogo de séries, filmes e documentários em TVs, celulares e computadores.")
  st.link_button("Acessar Site", "https://www.netflix.com/br/")

st.write("")

st.markdown("<br>", unsafe_allow_html=True)
