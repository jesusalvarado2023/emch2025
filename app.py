import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Temario del Curso de Química", page_icon="🧪", layout="wide")

##############
st.sidebar.image("img/combustion-metano.svg",
                 caption="Curso Química General")

#############################Pagina 1############################## 

def Home():
    # Título principal
    st.title("📘 QUÍMICA GENERAL")
    st.info("Dr. Jesus Alvarado Huayhuaz")
    st.markdown("---")
    
    # Sección de presentación
    titulo_curso = "Bachillerato en Ciencias Militares | Ciencias y Humanidades"
    st.subheader(titulo_curso)
    st.write("Bienvenidos al curso de Química General donde aprenderemos desde los principios básicos de la química hasta aplicaciones en la vida cotidiana y en la investigación científica.")
    st.markdown("---")
    #st.write("Dr. Jesus Alvarado Huayhuaz")
    
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
    st.markdown(f"[⬇️ Semana 1: Materia y estructura atómica]( {clase1_url} )", unsafe_allow_html=True)
    
    silabo_url1 = "https://github.com/jesusalvarado2023/emch2025/raw/refs/heads/main/Clases/SILABO.pdf"
    st.markdown(f"[⬇️ Sílabo]( {silabo_url1} )", unsafe_allow_html=True)

    # Pie de página
    st.markdown("---")
    st.write("Jesus Alvarado-Huayhuaz © 2025")

#############################Pagina 2############################## 

def page2():
    st.header('Semana 1: Estructura atómica y Tabla periódica', divider='rainbow')
    diapositivas1 = "https://drive.google.com/file/d/1if24LYZp-r2vLb9IeMDZcfsRzN6jLJwb/preview"
    st.markdown(f'<iframe src="{diapositivas1}" width="800" height="500"></iframe>', unsafe_allow_html=True)
    #https://drive.google.com/file/d/1if24LYZp-r2vLb9IeMDZcfsRzN6jLJwb/view?usp=sharing
#############################Pagina 3############################## 

def page3():
    st.header('Semana 2:', divider='rainbow')

#############################Pagina 4############################## 

def page4():
    st.header('Semana 3:', divider='rainbow')

#############################Pagina 5############################## 

def page5():
    st.header('Semana 4:', divider='rainbow')

#############################Pagina 6############################## 

def page6():
    st.header('Semana 5: Reacciones Químicas', divider='rainbow')

    diapositivas5 = "https://docs.google.com/presentation/d/1yjiifuX45QFjLBRFF8xks4ltaSuhz7lr/preview"
    st.markdown(f'<iframe src="{diapositivas5}" width="800" height="500" allow="autoplay"></iframe>', unsafe_allow_html=True)

#############################Pagina 7############################## 

def page7():
   st.header('Semana 6:', divider='rainbow')

#############################Pagina 8############################## 

def page8():
    st.header('Semana 7:', divider='rainbow')

#############################Pagina 9############################## 

def page9():
    st.header('Semana 8:', divider='rainbow')

#############################Pagina 10############################## 

def page10():
    st.header('Semana 9:', divider='rainbow')

#############################Pagina 11############################## 

def page11():
   st.header('Semana 10:', divider='rainbow')
   
################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Generalidades": Home,
  "Semana 1: Estructura atómica": page2,
  "Semana 2": page3,
  "Semana 3": page4,
  "Semana 4": page5,
  "Semana 5: Reacciones Químicas": page6,
  "Semana 6": page7,
  "Semana 7": page8,
  "Semana 8": page9,
  "Semana 9": page10,
  "Semana 10": page11,
}

selected_page = st.sidebar.selectbox("Temario", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

#https://docs.google.com/presentation/d/1yjiifuX45QFjLBRFF8xks4ltaSuhz7lr/edit?usp=sharing&ouid=116234516776721649949&rtpof=true&sd=true
