import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(page_title="Temario del Curso de Química", page_icon="🧪", layout="wide")
##############
st.sidebar.image("img/combustion-metano.svg", caption="Curso Química General")

#############################Pagina 1############################## 
def Home():
    # Título principal
    st.title("📘 QUÍMICA GENERAL")
    #st.info("Dr. Jesus Alvarado Huayhuaz")
    st.markdown("---")
  
    # Sección de presentación
    titulo_curso = "Bachillerato en Ciencias Militares | Ciencias y Humanidades"
    st.subheader(titulo_curso)
    st.write("Bienvenidos al curso de Química General donde aprenderemos desde los principios básicos de la química hasta aplicaciones en la vida cotidiana y en la investigación científica.")
    st.markdown("---")

    #st.info("NOVEDADES: Números cuánticos")
    #enlace = "https://numeroscuanticos.streamlit.app/"
    #st.write("Practica los números cuánticos con ejercicios [aquí](%s)" % enlace)
    #st.image("img/nuclido1.png", caption="https://numeroscuanticos.streamlit.app/")
    #st.markdown("---")
    
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
    
    # URL del archivo PDF en tu repositorio °de GitHub
    repasoPC1_url = "https://github.com/jesusalvarado2023/emch2025/raw/refs/heads/main/Practicas_QUIMICA_EMCH/REPASO_PC1_QUIMICA_EMCH.pdf"
    st.markdown(f"[⬇️ Repaso para PC1]( {repasoPC1_url} )", unsafe_allow_html=True)
    
    clase1_url = "https://github.com/jesusalvarado2023/emch2025/raw/refs/heads/main/Clases/Clase1.pdf"
    st.markdown(f"[⬇️ Semana 1: Materia y estructura atómica]( {clase1_url} )", unsafe_allow_html=True)

    clase2_url = "https://github.com/jesusalvarado2023/emch2025/raw/refs/heads/main/Clases/Clase2.pdf"
    st.markdown(f"[⬇️ Semana 2: Configuración electrónica y Tabla Periódica]( {clase2_url} )", unsafe_allow_html=True)
    
    silabo_url1 = "https://github.com/jesusalvarado2023/emch2025/raw/refs/heads/main/Clases/SILABO.pdf"
    st.markdown(f"[⬇️ Sílabo]( {silabo_url1} )", unsafe_allow_html=True)

    # Pie de página
    st.markdown("---")
    st.write("Jesus Alvarado-Huayhuaz © 2025")

#############################Pagina 2############################## 

def page2():
    st.header('Semana 1: Estructura atómica y Números cuánticos', divider='rainbow')
    diapositivas1 = "https://docs.google.com/presentation/d/1mrNHsc_6a0d4AQsiWsYsQvvRqqctcFey/preview"
    st.markdown(f'<iframe src="{diapositivas1}" width="800" height="500"></iframe>', unsafe_allow_html=True)

    st.info("Números cuánticos")
    enlace = "https://numeroscuanticos.streamlit.app/"
    st.write("Practica los números cuánticos con ejercicios [aquí](%s)" % enlace)
    st.image("img/nuclido1.png", caption="https://numeroscuanticos.streamlit.app/")

    st.info("Isótopos")
    phet3 = "https://phet.colorado.edu/sims/html/isotopes-and-atomic-mass/latest/isotopes-and-atomic-mass_all.html"
    st.components.v1.iframe(phet3, width=800, height=600, scrolling=False)

#############################Pagina 3############################## 
def page3():
    st.header('Semana 2: Configuración electrónica y Tabla Periódica', divider='rainbow')
    diapositivas2 = "https://docs.google.com/presentation/d/1-DfJRnfVsC4PgaiBUFDLZ1eoEV1Ix0MP/preview"  #"https://docs.google.com/presentation/d/1uB9ZxmqtUurYLzW52iniCsM94g14drSy/preview"
    st.markdown(f'<iframe src="{diapositivas2}" width="800" height="500"></iframe>', unsafe_allow_html=True)

    st.info("Construye átomos")
    phet1 = "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_all.html"
    st.components.v1.iframe(phet1, width=800, height=600, scrolling=False)
    
    st.info("Estados de la materia")
    phet2 = "https://phet.colorado.edu/sims/html/states-of-matter-basics/latest/states-of-matter-basics_en.html"
    st.components.v1.iframe(phet2, width=800, height=600, scrolling=False)
    
    st.info("Formas de las moléculas")
    phet3 = "https://phet.colorado.edu/sims/html/molecule-shapes/latest/molecule-shapes_all.html"
    st.components.v1.iframe(phet3, width=800, height=600, scrolling=False)

    #Polaridad
    #https://phet.colorado.edu/sims/html/molecule-polarity/latest/molecule-polarity_all.html

#############################Pagina 4############################## 
def page4():
    st.header('Semana 3: Unidades Químicas de Masa', divider='rainbow')
    diapositivas3 = "https://docs.google.com/presentation/d/1dPRATUw6erKgP5Nj8hkSR8gTqMOinjap/preview"
    st.markdown(f'<iframe src="{diapositivas3}" width="800" height="500"></iframe>', unsafe_allow_html=True)

    st.info("Concentraciones")
    phet4 = "https://phet.colorado.edu/sims/html/concentration/latest/concentration_all.html"
    st.components.v1.iframe(phet4, width=800, height=600, scrolling=False)

#############################Pagina 5############################## 

def page5():
    st.header('Semana 4: Reacciones Químicas', divider='rainbow')

    diapositivas5 = "https://docs.google.com/presentation/d/1MCUcEQO-ALoaTvGrPy_6ac1anN5k-JV0/preview"
    st.markdown(f'<iframe src="{diapositivas5}" width="800" height="500" allow="autoplay"></iframe>', unsafe_allow_html=True)

    st.info("Reacciones químicas")
    reaccion5 = "https://phet.colorado.edu/sims/html/reactants-products-and-leftovers/latest/reactants-products-and-leftovers_all.html"
    st.components.v1.iframe(reaccion5, width=800, height=600, scrolling=False)

    st.info("Balance de ecuaciones químicas")
    reaccion6 = "https://phet.colorado.edu/sims/html/balancing-chemical-equations/latest/balancing-chemical-equations_en.html"
    st.components.v1.iframe(reaccion6, width=800, height=600, scrolling=False)

#############################Pagina 6############################## 

def page6():
    st.header('Semana 5:', divider='rainbow')


#############################Pagina 7############################## 
def page7():
   st.header('Semana 6:', divider='rainbow')

   #diapositivas6 = "https://docs.google.com/presentation/d/1fYiv0TwEqXue4sgTAmpw7kUX6L4q-gJp/preview"
   #st.markdown(f'<iframe src="{diapositivas6}" width="800" height="500" allow="autoplay"></iframe>', unsafe_allow_html=True)



#############################Pagina 8############################## 

def page8():
    st.header('Semana 7: Estequiometría', divider='rainbow')

#############################Pagina 9############################## 

def page9():
    st.header('Semana 8: Estado Gaseoso', divider='rainbow')

#############################Pagina 10############################## 

def page10():
    st.header('Semana 9: Unidades de Concentración', divider='rainbow')

#############################Pagina 11############################## 

def page11():
   st.header('Semana 10: Medio Ambiente', divider='rainbow')
   
################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Generalidades": Home,
  "Semana 1: Estructura atómica": page2,
  "Semana 2: Configuración y Tabla Periódica": page3,
  "Semana 3: Unidades Químicas de Masa": page4,
  "Semana 4: Reacciones Químicas": page5,
  "Semana 5: ": page6,
  "Semana 6: ": page7,
  "Semana 7: Estequiometría": page8,
  "Semana 8: Estado Gaseoso": page9,
  "Semana 9: Unidades de Concentración": page10,
  "Semana 10: Medio Ambiente": page11,
}

selected_page = st.sidebar.selectbox("Temario", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

st.sidebar.info("Autor: Dr. Jesus Alvarado Huayhuaz")
st.sidebar.write("Laboratorio de Ingeniería Biomédica, Universidad Peruana Cayetano Heredia")
st.sidebar.write("Contacto: jesus.alvarado@upch.pe")
