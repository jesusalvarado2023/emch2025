import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Temario del Curso de Química", page_icon="🧪", layout="wide")

# Título principal
st.title("📘 Temario del Curso de Química")
st.markdown("---")

# Sección de presentación
titulo_curso = "Explorando los Fundamentos y Aplicaciones de la Química"
st.subheader(titulo_curso)
st.write("Bienvenidos a este curso donde aprenderemos desde los principios básicos de la química hasta sus aplicaciones en la vida cotidiana y en la investigación científica.")

# Temario
st.markdown("## 📌 Temario del Curso")
temario = {
    "1️⃣ Introducción a la Química": "Conceptos básicos, historia y ramas de la química.",
    "2️⃣ Estructura Atómica y Enlace Químico": "Átomos, modelos atómicos, tipos de enlaces químicos.",
    "3️⃣ Termodinámica Química": "Leyes de la termodinámica, energía libre, equilibrio químico.",
    "4️⃣ Cinética Química": "Velocidad de reacción, factores que afectan la velocidad de reacción.",
    "5️⃣ Química Orgánica": "Hidrocarburos, grupos funcionales, reacciones orgánicas básicas.",
    "6️⃣ Química Bioinorgánica": "Metales en sistemas biológicos, mecanismos de transporte y almacenamiento.",
}

for tema, descripcion in temario.items():
    st.markdown(f"### {tema}")
    st.write(f"{descripcion}")

# Botón de descarga de la Clase 1

with open('Clase1.pdf', 'r') as f:
      st.download_button('Descargar', f, file_name='Clase1.pdf', mime='Clases/pdf')

# Pie de página
st.markdown("---")
st.write("© 2025 - Curso de Química | Creado con ❤️ y Streamlit")
