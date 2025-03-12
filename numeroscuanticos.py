import streamlit as st
import random
import time

st.sidebar.image("img/cuantica.png", caption="Autor: Dr. Jesús Alvarado-Huayhuaz")
st.sidebar.image("img/nuclido1.png")

configuraciones = {
    "1s1": (1, 0, 0, 1/2), "1s2": (1, 0, 0, -1/2),  
    "2s1": (2, 0, 0, 1/2), "2s2": (2, 0, 0, -1/2),
    "2p1": (2, 1, -1, 1/2), "2p2": (2, 1, 0, -1/2),
    "2p3": (2, 1, 1, 1/2), "2p4": (2, 1, -1, -1/2),
    "2p5": (2, 1, 0, -1/2), "2p6": (2, 1, 1, -1/2),
    "3s1": (3, 0, 0, 1/2), "3s2": (3, 0, 0, -1/2),
    "3p1": (3, 1, -1, 1/2), "3p2": (3, 1, 0, 1/2),
    "3p3": (3, 1, 1, 1/2), "3p4": (3, 1, -1, -1/2),
    "3p5": (3, 1, 0, -1/2), "3p6": (3, 1, 1, -1/2),
    "4s1": (4, 0, 0, 1/2), "4s2": (4, 0, 0, -1/2),
    "3d1": (3, 2, -2, 1/2), "3d2": (3, 2, -1, 1/2),
    "3d3": (3, 2, 0, 1/2), "3d4": (3, 2, 1, 1/2),
    "3d5": (3, 2, 2, 1/2), "3d6": (3, 2, -2, -1/2),
    "3d7": (3, 2, -1, -1/2), "3d8": (3, 2, 0, -1/2),
    "3d9": (3, 2, 1, -1/2), "3d10": (3, 2, 2, -1/2),
    "4p1": (4, 1, -1, 1/2), "4p2": (4, 1, 0, 1/2),
    "4p3": (4, 1, 1, 1/2), "4p4": (4, 1, -1, -1/2),
    "4p5": (4, 1, 0, -1/2), "4p6": (4, 1, 1, -1/2),    
    "5s1": (5, 0, 0, 1/2), "5s2": (5, 0, 0, -1/2),
    "4d1": (4, 2, -2, 1/2), "4d2": (4, 2, -1, 1/2),
    "4d3": (4, 2, 0, 1/2), "4d4": (4, 2, 1, 1/2),
    "4d5": (4, 2, 2, 1/2), "4d6": (4, 2, -2, -1/2),
    "4d7": (4, 2, -1, -1/2), "4d8": (4, 2, 0, -1/2),
    "4d9": (4, 2, 1, -1/2), "4d10": (4, 2, 2, -1/2),
    "5p1": (5, 1, -1, 1/2), "5p2": (5, 1, 0, 1/2),
    "5p3": (5, 1, 1, 1/2), "5p4": (5, 1, -1, -1/2),
    "5p5": (5, 1, 0, -1/2), "5p6": (5, 1, 1, -1/2),
    "6s1": (6, 0, 0, 1/2), "6s2": (6, 0, 0, -1/2),
    "4f1": (4, 3, -3, 1/2), "4f2": (4, 3, -2, 1/2),
    "4f3": (4, 3, -1, 1/2), "4f4": (4, 3, 0, 1/2),
    "4f5": (4, 3, 1, 1/2), "4f6": (4, 3, 2, 1/2),
    "4f7": (4, 3, 3, 1/2), 
    "4f8": (4, 3, -3, -1/2), "4f9": (4, 3, -2, -1/2),
    "4f10": (4, 3, -1, -1/2), "4f11": (4, 3, 0, -1/2),
    "4f12": (4, 3, 1, -1/2), "4f13": (4, 3, 2, -1/2),
    "4f14": (4, 3, 3, -1/2), 
    "5d1": (5, 2, -2, 1/2), "5d2": (5, 2, -1, 1/2),
    "5d3": (5, 2, 0, 1/2), "5d4": (5, 2, 1, 1/2),
    "5d5": (5, 2, 2, 1/2), "5d6": (5, 2, -2, -1/2),
    "5d7": (5, 2, -1, -1/2), "5d8": (5, 2, 0, -1/2),
    "5d9": (5, 2, 1, -1/2), "5d10": (5, 2, 2, -1/2),
    "6p1": (6, 1, -1, 1/2), "6p2": (6, 1, 0, 1/2),
    "6p3": (6, 1, 1, 1/2), "6p4": (6, 1, -1, -1/2),
    "6p5": (6, 1, 0, -1/2), "6p6": (6, 1, 1, -1/2),
    "7s1": (7, 0, 0, 1/2), "7s2": (7, 0, 0, -1/2),
    "5f1": (5, 3, -3, 1/2), "5f2": (5, 3, -2, 1/2),
    "5f3": (5, 3, -1, 1/2), "5f4": (5, 3, 0, 1/2),
    "5f5": (5, 3, 1, 1/2), "5f6": (5, 3, 2, 1/2),
    "5f7": (5, 3, 3, 1/2), 
    "5f8": (5, 3, -3, -1/2), "5f9": (5, 3, -2, -1/2),
    "5f10": (5, 3, -1, -1/2), "5f11": (5, 3, 0, -1/2),
    "5f12": (5, 3, 1, -1/2), "5f13": (5, 3, 2, -1/2),
    "5f14": (5, 3, 3, -1/2), 
    "6d1": (6, 2, -2, 1/2), "6d2": (6, 2, -1, 1/2),
    "6d3": (6, 2, 0, 1/2), "6d4": (6, 2, 1, 1/2),
    "6d5": (6, 2, 2, 1/2), "6d6": (6, 2, -2, -1/2),
    "6d7": (6, 2, -1, -1/2), "6d8": (6, 2, 0, -1/2),
    "6d9": (6, 2, 1, -1/2), "6d10": (6, 2, 2, -1/2),
    "7p1": (7, 1, -1, 1/2), "7p2": (7, 1, 0, 1/2),
    "7p3": (7, 1, 1, 1/2), "7p4": (7, 1, -1, -1/2),
    "7p5": (7, 1, 0, -1/2), "7p6": (7, 1, 1, -1/2),
}

# Usar session_state para evitar que la pregunta cambie al interactuar con los inputs
if "configuracion_actual" not in st.session_state:
    st.session_state.configuracion_actual = random.choice(list(configuraciones.keys()))
    st.session_state.respuesta_correcta = configuraciones[st.session_state.configuracion_actual]

# Encabezado
st.header(":blue[Números Cuánticos]") #:sunglasses:", divider='rainbow')

st.info("Encuentra los números cuánticos de:")
st.subheader(st.session_state.configuracion_actual)

# Campos de entrada para los números cuánticos
n = st.number_input("Número cuántico principal (n):", min_value=1, max_value=7, step=1)
l = st.number_input("Número cuántico azimutal (l):", min_value=0, max_value=3, step=1)
m = st.number_input("Número cuántico magnético (m):", min_value=-3, max_value=3, step=1)
s = st.selectbox("Número cuántico de espín (s):", options=[-1/2, 1/2])

# Botón para verificar la respuesta
if st.button("Verificar respuesta"):
    if (n, l, m, s) == st.session_state.respuesta_correcta:
        st.success("¡Correcto! 🎉")
        st.balloons()  # Animación de globos si la respuesta es correcta
    else:
        st.error("Incorrecto. Intenta de nuevo.")

# Botón para generar una nueva pregunta
if st.button("Nueva pregunta"):
    st.session_state.configuracion_actual = random.choice(list(configuraciones.keys()))
    st.session_state.respuesta_correcta = configuraciones[st.session_state.configuracion_actual]
    st.rerun()

st.image("img/nuclido.png")
