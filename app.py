import streamlit as st
import random
from datetime import date

# DESAFIO DEL DIA

def generar_desafio_dia():

    hoy = str(date.today())
    random.seed(hoy)

    animal = random.choice(animales)
    color = random.choice(colores)
    accion = random.choice(acciones)
    estilo = random.choice(estilos)
    objeto = random.choice(objetos)

    random.seed()

    return (
        f"Dibuja una persona "
        f"{accion.lower()}"
        f" sosteniendo {objeto.lower()}"
        f" , con estilo {estilo} y como color principal el {color}."
    )
# GUARDAR FAVORITOS

if "favoritos" not in st.session_state:
    st.session_state.favoritos = []

if "ultima_idea" not in st.session_state:
    st.session_state.ultima_idea = ""
    
if "mostrar_favoritos" not in st.session_state:
    st.session_state.mostrar_favoritos = False

# ESTADISTICAS

if "total_generadas" not in st.session_state:
    st.session_state.total_generadas = 0

if "comun" not in st.session_state:
    st.session_state.comun = 0

if "rara" not in st.session_state:
    st.session_state.rara = 0

if "epica" not in st.session_state:
    st.session_state.epica = 0

if "legendaria" not in st.session_state:
    st.session_state.legendaria = 0

# TITLE

st.title("🎨 ArtSpark")
st.subheader("Generador creativo de ideas para artistas")

#COLUMNA DE PERFIL
with st.sidebar:

    st.title("👤 Mi Perfil ArtSpark")

    st.metric(
        "📊 Ideas Generadas",
        st.session_state.total_generadas
    )

    st.metric(
        "⭐ Favoritos",
        len(st.session_state.favoritos)
    )

    st.divider()

    st.subheader("Rarezas")

    st.write(
        f"🟢 Comunes: {st.session_state.comun}"
    )

    st.write(
        f"🔮 Raras: {st.session_state.rara}"
    )

    st.write(
        f"✨ Épicas: {st.session_state.epica}"
    )

    st.write(
        f"🏆 Legendarias: {st.session_state.legendaria}"
    )

    st.divider()

    if st.button("⭐ Ver Favoritos"):

        st.session_state.mostrar_favoritos = True

# CALCULADORA RAREZA
def calcular_rareza(elementos):

    palabras_raras = [
        "Dragón",
        "Cyborg",
        "Vampiro",
        "Hada",
        "Ninja",
        "Cyberpunk",
        "Amarillo neón",
        "Reloj de arena",
        "Viajar en el tiempo",
        "Telepatía"
    ]

    puntos = 0

    for elemento in elementos:
        if elemento in palabras_raras:
            puntos += 1

    if puntos >= 3:
        return "🏆 Legendaria"
    elif puntos == 2:
        return "✨ Épica"
    elif puntos == 1:
        return "🔮 Rara"
    else:
        return "🟢 Común"
        
# REGISTRAR RAREZAS/ESTADISTICAS

def registrar_rareza(rareza):

    st.session_state.total_generadas += 1

    if "Común" in rareza:
        st.session_state.comun += 1

    elif "Rara" in rareza:
        st.session_state.rara += 1

    elif "Épica" in rareza:
        st.session_state.epica += 1

    elif "Legendaria" in rareza:
        st.session_state.legendaria += 1
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
"Manzana",
"Arandano",
"Fresa",
"Maracuya",
"Naranja",
"Frambuesa",
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

# NIVELES DE RAREZA

palabras_raras = [
    "Dragón",
    "Cyborg",
    "Vampiro",
    "Hada",
    "Ninja",
    "Cyberpunk",
    "Amarillo neón",
    "Reloj de arena",
    "Viajar en el tiempo",
    "Telepatía"
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
        st.session_state.ultima_idea = texto_resultado
        st.success(texto_resultado)
        
# PERSONAJE

with col2:
    if st.button("🧙 Personaje"):

        tipo = random.choice(tipos)
        personalidad = random.choice(personalidades)
        poder = random.choice(poderes)
        accesorio = random.choice(accesorios)
        objetivo = random.choice(objetivos)

        rareza = calcular_rareza([
            tipo,
            poder,
            objetivo
        ])

        registrar_rareza(rareza)

        texto_resultado = (
            f"Tipo: {tipo}\n"
            f"Personalidad: {personalidad}\n"
            f"Poder: {poder}\n"
            f"Accesorio: {accesorio}\n"
            f"Objetivo: {objetivo}\n\n"
            f"Rareza: {rareza}"
        )

        st.session_state.ultima_idea = texto_resultado
        st.success(texto_resultado)

# TREND

with col3:
    if st.button("🌈 Trend Challenge"):

        color = random.choice(colores)
        fruta = random.choice(frutas)
        animal = random.choice(animales)
        accion = random.choice(acciones)
        estilo = random.choice(estilos)
        objeto = random.choice(objetos)

        rareza = calcular_rareza([
            color,
            estilo,
            objeto
        ])

        registrar_rareza(rareza)

        texto_resultado = (
            f"Color: {color}\n"
            f"Fruta: {fruta}\n"
            f"Animal: {animal}\n"
            f"Acción: {accion}\n"
            f"Estilo: {estilo}\n"
            f"Objeto: {objeto}\n\n"
            f"Rareza: {rareza}"
        )

        st.session_state.ultima_idea = texto_resultado
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
        st.session_state.ultima_idea = texto_resultado
        st.success(texto_resultado)
        
# GUARDAR FAVORITOS
st.divider()

colA, colB = st.columns(2)

with colA:
    if st.button("⭐ Guardar en Favoritos"):

        if st.session_state.ultima_idea != "":
            st.session_state.favoritos.append(
                st.session_state.ultima_idea
            )
            st.success("Idea guardada en favoritos")
        else:
            st.warning("Primero genera una idea")
with colB:
    if st.button("📚 Ver Favoritos"):

        if len(st.session_state.favoritos) == 0:
            st.info("No hay favoritos todavía")

        else:
            st.subheader("📚 Mis Favoritos")

            for i, favorito in enumerate(
                st.session_state.favoritos,
                start=1
            ):
                st.text(f"{i}. {favorito}")

# BOTON DEAFIO DEL DIA

st.divider()

if st.button("📅 Desafío del Día"):

    st.info(generar_desafio_dia())
