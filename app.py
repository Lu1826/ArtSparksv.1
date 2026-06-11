import streamlit as st
import random

st.title("🎨 ArtSpark")
st.subheader("Generador creativo de ideas para artistas")

personajes = [
    "astronauta",
    "pirata",
    "chef",
    "detective",
    "mago"
]

emociones = [
    "feliz",
    "triste",
    "enojado",
    "curioso",
    "sorprendido"
]

lugares = [
    "una ciudad futurista",
    "un castillo abandonado",
    "el espacio",
    "una isla misteriosa",
    "un bosque mágico"
]

rarezas = [
    "🟢 Común",
    "🔮 Rara",
    "✨ Épica",
    "🏆 Legendaria"
]

if st.button("Generar Idea"):
    
    personaje = random.choice(personajes)
    emoción = random.choice(emociones)
    lugar = random.choice(lugares)
    rareza = random.choice(rarezas)

    st.success(f'Dibuja un {personaje} {emocion} en {lugar}')
    st.markdown(f'### {rareza}')
