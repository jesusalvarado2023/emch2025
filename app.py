import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Temario del Curso de Química", page_icon="🧪", layout="wide")

# Título principal
st.title("📘 QUÍMICA GENERAL")
st.markdown("---")

# Sección de presentación
titulo_curso = "Bachillerato en Ciencias Militares | Ciencias y Humanidades"
st.subheader(titulo_curso)
st.write("Bienvenidos a este curso donde aprenderemos desde los principios básicos de la química hasta sus aplicaciones en la vida cotidiana y en la investigación científica.")
st.markdown("---")
st.write("Dr. Jesus Alvarado Huayhuaz")

# Temario
st.markdown("## 📌 Temario del Curso")
temario = {
    "1️⃣ Unidad I": "Estructura atómica y Tabla periódica",
    "2️⃣ Unidad II": "Reacciones químicas y estequiometría",
    "3️⃣ Unidad III": "Estado gaseoso y soluciones",
    "4️⃣ Unidad IV": "Unidades de concentración y medio ambiente",
    #"5️⃣ Química Orgánica": "Hidrocarburos, grupos funcionales, reacciones orgánicas básicas.",
    #"6️⃣ Química Bioinorgánica": "Metales en sistemas biológicos, mecanismos de transporte y almacenamiento.",
}

for tema, descripcion in temario.items():
    st.markdown(f"### {tema}")
    st.write(f"{descripcion}")

##########################################
st.markdown("---")
st.markdown("## 📥 Descargas")
st.write("Archivos en formatos PDF.")

# URL del archivo PDF en tu repositorio de GitHub
clase1_url = "https://github.com/jesusalvarado2023/emch2025/raw/refs/heads/main/Clases/Clase1.pdf"
st.markdown(f"[⬇️ Clase 1]( {clase1_url} )", unsafe_allow_html=True)

silabo_url1 = "https://github.com/jesusalvarado2023/emch2025/raw/refs/heads/main/Clases/SILABO.pdf"
st.markdown(f"[⬇️ Sílabo]( {silabo_url1} )", unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.write("© 2025")
