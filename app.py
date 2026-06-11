import streamlit as st
import random

st.title("🎨 ArtSpark")
st.subheader("Generador creativo de ideas para artistas")

# =====================

# LISTAS

# =====================

# PERSONA

edades = ["Niño", "Adolescente", "Joven", "Adulto", "Anciano"]

sexos = ["Hombre", "Mujer","Indefinido"]

pieles = [
"clara",
"trigueña",
"morena",
"oscura"
]

cabellos = [
"lacio corto",
"lacio largo",
"ondulado corto",
"ondulado largo",
"rizado corto",
"rizado largo"
]

ropa = [
"estilo urbano",
"ropa deportiva",
"ropa elegante",
"ropa casual",
"estilo gótico"
]

pasatiempos = [
"leer",
"dibujar",
"jugar videojuegos",
"hacer deporte",
"escuchar música",
"andar en bicicleta"
]

# PERSONAJE

tipos = [
"Mago",
"Dragón",
"Caballero",
"Pirata",
"Robot",
"Duende",
"Vampiro",
"Hada",
"Ninja",
"Cyborg"
"Zombi"
]

personalidades = [
"Valiente",
"Travieso",
"Sabio",
"Torpe",
"Misterioso",
"Alegre"
]

poderes = [
"Control del fuego",
"Magia de hielo",
"Invisibilidad",
"Telepatía",
"Superfuerza",
"Control de plantas"
]

accesorios = [
"Espada mágica",
"Libro encantado",
"Amuleto antiguo",
"Máscara dorada",
"Martillo rúnico"
]

objetivos = [
"Salvar un reino",
"Encontrar un tesoro",
"Derrotar a un villano",
"Proteger la naturaleza",
"Viajar en el tiempo"
]

# TREND CHALLENGE

colores = [
"Rojo",
"Azul pastel",
"Verde esmeralda",
"Amarillo neón",
"Púrpura"
]

frutas = [
"Mango",
"Sandía",
"Cereza",
"Limón",
"Manzana"
"Arandano"
"Fresa"
"Maracuya"
"Naranja"
"Frambuesa"
"Piña"
]

animales = [
"Panda",
"Zorro",
"Lobo",
"Gato",
"Águila"
]

acciones = [
"Bailando",
"Corriendo",
"Cantando",
"Saltando",
"Posando"
]

estilos = [
"Cyberpunk",
"Vintage",
"Elegante",
"Boho",
"Futurista"
]

objetos = [
"Cámara vintage",
"Paraguas roto",
"Reloj de arena",
"Globo aerostático",
"Máscara"
]

# PERSONAJE EXISTENTE

lugares = [
    "una cafetería",
    "el espacio",
    "una isla desierta",
    "un centro comercial",
    "un castillo abandonado",
    "un bosque mágico"
]

ropa_existente = [
    "ropa de invierno",
    "traje formal",
    "uniforme escolar",
    "ropa deportiva",
    "armadura medieval"
]

climas = [
    "tormenta",
    "lluvia intensa",
    "día soleado",
    "nieve",
    "niebla espesa"
]

animos = [
    "feliz",
    "triste",
    "enfadado",
    "pensativo",
    "confundido",
    "emocionado"
]

acciones_existente = [
    "leyendo",
    "corriendo",
    "cocinando",
    "bailando",
    "escondiéndose",
    "dibujando",
    "explorando"
]

# =====================

# BOTONES

# =====================

col1, col2, col3, col4 = st.columns(4)

# PERSONA

with col1:
    if st.button("🧑 Persona"):
        texto_resultado = (
            f"Edad: {random.choice(edades)}\n"
            f"Sexo: {random.choice(sexos)}\n"
            f"Piel: {random.choice(pieles)}\n"
            f"Cabello: {random.choice(cabellos)}\n"
            f"Ropa: {random.choice(ropa)}\n"
            f"Pasatiempo: {random.choice(pasatiempos)}"
        )
        st.success(texto_resultado)
        
# PERSONAJE

with col2:
    if st.button("🧙 Personaje"):
        texto_resultado = (
            f"Tipo: {random.choice(tipos)}\n"
            f"Personalidad: {random.choice(personalidades)}\n"
            f"Poder: {random.choice(poderes)}\n"
            f"Accesorio: {random.choice(accesorios)}\n"
            f"Objetivo: {random.choice(objetivos)}\n"
        )
        st.success(texto_resultado)

# TREND

with col3:
    if st.button("📈 Trend Challenge"):
        texto_resultado = (
            f"Color: {random.choice(colores)}\n"
            f"Fruta: {random.choice(frutas)}\n"
            f"Animal: {random.choice(animales)}\n"
            f"Acción: {random.choice(acciones)}\n"
            f"Estilo: {random.choice(estilos)}\n"
            f"Objeto: {random.choice(objetos)}"
        )
        st.success(texto_resultado)

# PERSONAJE EXISTENTE
with col4:
    if st.button("🎭 Personaje Existente"):
        texto_resultado = (
            "Dibuja a tu personaje favorito:\n\n"
            f"Acción:\n{random.choice(acciones_existente)}\n\n"
            f"Lugar:\n{random.choice(lugares)}\n\n"
            f"Ropa:\n{random.choice(ropa_existente)}\n\n"
            f"Clima:\n{random.choice(climas)}\n\n"
            f"Estado de ánimo:\n{random.choice(animos)}"
        )
        st.success(texto_resultado)
