import streamlit as st
import random
from datetime import date
import json
import os
import base64

#BARRA LATERAL DE FONDO

def get_base64(imagen):
    with open(imagen, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("profile.png")

st.markdown(f"""
<style>

section[data-testid="stSidebar"] {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-repeat: no-repeat;
}}

</style>
""", unsafe_allow_html=True)

#IMAGEN DE FONDO
def get_base64(imagen):
    with open(imagen, "rb") as f:
        return base64.b64encode(f.read()).decode()

fondo = get_base64("assets/fondo.png")

st.markdown(
    f"""
    <style>

    .stApp {{
        background-image: url("data:image/png;base64,{fondo}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    </style>
    """,
    unsafe_allow_html=True
)
# ALMACENAR DATOS

ARCHIVO_DATOS = "datos.json"

if not os.path.exists(ARCHIVO_DATOS):

    datos_iniciales = {
    "favoritos": [],

    "estadisticas": {
        "total": 0,
        "comun": 0,
        "rara": 0,
        "epica": 0,
        "legendaria": 0
    },

    "racha": {
        "actual": 0,
        "mejor": 0,
        "ultima_fecha": ""
    }
}
    with open(ARCHIVO_DATOS, "w") as f:
        json.dump(datos_iniciales, f, indent=4)

def cargar_datos():

    with open(ARCHIVO_DATOS, "r") as f:
        return json.load(f)

def guardar_datos(datos):

    with open(ARCHIVO_DATOS, "w") as f:
        json.dump(datos, f, indent=4)

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


# COLUMNA DE PERFIL
datos = cargar_datos()
with st.sidebar:
    
    st.title("👤 Mi Perfil ArtSpark")

    st.metric(
        "📊 Ideas Generadas",
        st.session_state.total_generadas
    )

    st.metric(
        "⭐ Favoritos",
        len(datos["favoritos"])
    )

    st.divider()

    st.subheader("Rarezas")

    st.write(f"🟢 Comunes: {datos['estadisticas']['comun']}")
    st.write(f"🔮 Raras: {datos['estadisticas']['rara']}")
    st.write(f"✨ Épicas: {datos['estadisticas']['epica']}")
    st.write(f"🏆 Legendarias: {datos['estadisticas']['legendaria']}")

    st.divider()

    # Mostrar/Ocultar favoritos
    if st.button("⭐ VIEW FAVORITES"):
        st.session_state.mostrar_favoritos = not st.session_state.mostrar_favoritos

    st.divider()

    # Aquí luego pondremos la racha
    st.write("🔥 Racha: Próximamente")

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

    datos = cargar_datos()

    datos["estadisticas"]["total"] += 1

    if "Común" in rareza:
        datos["estadisticas"]["comun"] += 1

    elif "Rara" in rareza:
        datos["estadisticas"]["rara"] += 1

    elif "Épica" in rareza:
        datos["estadisticas"]["epica"] += 1

    elif "Legendaria" in rareza:
        datos["estadisticas"]["legendaria"] += 1

    guardar_datos(datos)
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
"Cyborg",
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

#ESPACIO HACIA ABAJO PARA BOTONES
st.markdown("<br>" * 9, unsafe_allow_html=True)

#TAMAÑO LETRA Y BOTONES

st.markdown(""" 
<style> 
.stButton > button {
    width: 170px !important; 
    height: 70px !important; 
} 
/* TEXTO DEL BOTÓN */ 
.stButton > button p { 
    font-size: 22px !important; 
    font-weight: 900 !important; 
} 
</style> 
""", unsafe_allow_html=True)

#RESULTADO
if "resultado" not in st.session_state:
    st.session_state.resultado = ""

col1, col2, col3, col4 = st.columns(4, gap="large")

# PERSONA

with col1:
    if st.button("🧑 PEOPLE"):
        texto_resultado = (
            f"Edad: {random.choice(edades)}\n"
            f"Sexo: {random.choice(sexos)}\n"
            f"Piel: {random.choice(pieles)}\n"
            f"Cabello: {random.choice(cabellos)}\n"
            f"Ropa: {random.choice(ropa)}\n"
            f"Pasatiempo: {random.choice(pasatiempos)}"
        )
        st.session_state.ultima_idea = texto_resultado
        st.session_state.resultado = texto_resultado

        
# PERSONAJE

with col2:
    if st.button("CHARACTER"):

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
        st.session_state.resultado = texto_resultado

    
# TREND

with col3:
    if st.button("🌈FULL CHALLENGE"):

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
        st.session_state.resultado = texto_resultado


# PERSONAJE EXISTENTE
with col4:
    if st.button("CHARACTER EXIST"):
        texto_resultado = (
            "Dibuja a tu personaje favorito:\n\n"
            f"Acción:\n{random.choice(acciones_existente)}\n\n"
            f"Lugar:\n{random.choice(lugares)}\n\n"
            f"Ropa:\n{random.choice(ropa_existente)}\n\n"
            f"Clima:\n{random.choice(climas)}\n\n"
            f"Estado de ánimo:\n{random.choice(animos)}"
        )
        st.session_state.ultima_idea = texto_resultado
        st.session_state.resultado = texto_resultado



# MOSTRAR RESULTADO
    
st.markdown("---")

if st.session_state.resultado != "":

    st.subheader("🎨 Resultado")

    st.markdown(f"""
    <div style="
        background-color:#151827;
        padding:25px;
        border-radius:12px;
        border:2px solid #c86fff;
        color:white;
        font-size:18px;
        white-space:pre-line;
    ">
    {st.session_state.resultado}
    </div>
    """, unsafe_allow_html=True)

        
# GUARDAR FAVORITOS
st.divider()

colA, colB = st.columns(2)

with colA:
    if st.button("⭐SAVE FAVORITES"):

        if st.session_state.ultima_idea != "":

            datos = cargar_datos()

            datos["favoritos"].append(
                st.session_state.ultima_idea
            )

            guardar_datos(datos)

            st.success("Idea guardada en favoritos")

        else:
            st.warning("Primero genera una idea")

# BOTON DEAFIO DEL DIA

st.divider()

if st.button("CHALLENGE OF THE DAY"):

    st.info(generar_desafio_dia())

# FAVORITOS
if st.session_state.mostrar_favoritos:

    st.subheader("⭐ MY FAVORITES")

    datos = cargar_datos()

    if len(datos["favoritos"]) == 0:

        st.info("No tienes favoritos todavía")

    else:

        for i, favorito in enumerate(
            datos["favoritos"],
            start=1
        ):
            st.code(f"{i}. {favorito}")
