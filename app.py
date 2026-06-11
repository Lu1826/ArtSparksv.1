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
"piel clara",
"piel trigueña",
"piel morena",
"piel oscura"
]

cabellos = [
"cabello lacio corto",
"cabello lacio largo",
"cabello ondulado corto",
"cabello ondulado largo",
"cabello rizado corto",
"cabello rizado largo"
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

# =====================

# BOTONES

# =====================

col1, col2, col3 = st.columns(3)

# PERSONA

with col1:
    if st.button("🧑 Persona"):
        # Asegúrate de que todo lo que sigue 
        # dentro del botón también tenga un nivel más de sangría
        st.success(f"""...""")

Edad: {random.choice(edades)}

Sexo: {random.choice(sexos)}

Piel: {random.choice(pieles)}

Cabello: {random.choice(cabellos)}

Ropa: {random.choice(ropa)}

Pasatiempo: {random.choice(pasatiempos)}
""")

# PERSONAJE

with col2:
if st.button("🧙 Personaje"):

```
    st.success(f"""
```

Tipo: {random.choice(tipos)}

Personalidad: {random.choice(personalidades)}

Poder: {random.choice(poderes)}

Accesorio: {random.choice(accesorios)}

Objetivo: {random.choice(objetivos)}
""")

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
