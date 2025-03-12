import streamlit as st
import random
import time

# Definir posibles configuraciones de electrones y sus números cuánticos
configuraciones = {
    "1s1": (1, 0, 0, 1/2),
    "2s2": (2, 0, 0, -1/2),
    "3p1": (3, 1, -1, 1/2),
    "4d10": (4, 2, 2, -1/2),
    "5f7": (5, 3, -3, 1/2),
    "6p5": (6, 1, 0, -1/2)
}

# Usar session_state para evitar que la pregunta cambie al interactuar con los inputs
if "configuracion_actual" not in st.session_state:
    st.session_state.configuracion_actual = random.choice(list(configuraciones.keys()))
    st.session_state.respuesta_correcta = configuraciones[st.session_state.configuracion_actual]

# UI en Streamlit
st.title("Juego de Números Cuánticos")
st.write("Ingresa los números cuánticos correctos para la configuración electrónica dada:")

st.subheader(f"Encuentra los números cuánticos de: {st.session_state.configuracion_actual}")

# Crear cuatro campos de entrada para los números cuánticos
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
