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
    ####################################
    #st.info("NOVEDADES: PRACTICANDO PARA EL EXAMEN PARCIAL")
    
    #st.markdown("Cada pregunta vale **4 puntos**. Total: **20 puntos**.") 
    #score = 0
    
    # Pregunta 1
    #st.subheader("Pregunta 1")
    #st.markdown("""
    #La capsaicina (C₁₈H₂₇NO₃) es una sustancia que se encuentra en los pimientos picantes. Se utiliza en la elaboración del gas pimienta.  
    #(C = 12g/mol; H = 1g/mol; O = 16g/mol; N = 14g/mol)  
    #Respecto a este compuesto:
    #""")
    #q1 = st.radio("Seleccione la respuesta correcta:",
    #              options=[
    #                  "a) Masa molecular: 305 g/mol; %C ≈ 70.8%; Moles en 100g: 0.33",
    #                  "b) Masa molecular: 295 g/mol; %C ≈ 72%; Moles en 100g: 0.40",
    #                  "c) Masa molecular: 323 g/mol; %C ≈ 67%; Moles en 100g: 0.30"
    #              ],
    #              key="q1")
    
    # Pregunta 2
    #st.subheader("Pregunta 2")
    #st.markdown("""
    #El gas cloro (Cl₂) es un gas tóxico. La reacción química es:  
    #**KMnO₄ + HCl → KCl + MnCl₂ + H₂O + Cl₂**  
    #Seleccione la respuesta correcta:
    #""")
    #q2 = st.radio("Seleccione la respuesta correcta:",
    #              options=[
    #                  "a) Ecuación balanceada: 2 KMnO₄ + 16 HCl → 2 KCl + 2 MnCl₂ + 8 H₂O + 5 Cl₂ / Reacción irreversible",
    #                  "b) Ecuación balanceada: KMnO₄ + 8 HCl → KCl + MnCl₂ + 4 H₂O + 2 Cl₂ / Reacción reversible",
    #                  "c) Ecuación balanceada: KMnO₄ + HCl → KCl + MnCl₂ + H₂O + Cl₂ / Reacción reversible"
    #              ],
    #              key="q2")
    
    # Pregunta 3
    #st.subheader("Pregunta 3")
    #st.markdown("""
    #C₇H₈ + HNO₃ → C₆H₂(NO₂)₃CH₃ + H₂O  
    #Balancear por tanteo e indicar la suma de coeficientes estequiométricos de los reactantes.
    #""")
    #q3 = st.radio("Seleccione la respuesta correcta:",
    #              options=[
    #                  "a) 1 C₇H₈ + 3 HNO₃ → ... / Suma: 4",
    #                  "b) 2 C₇H₈ + 3 HNO₃ → ... / Suma: 5",
    #                  "c) 1 C₇H₈ + 2 HNO₃ → ... / Suma: 3"
    #              ],
    #              key="q3")
    
    # Pregunta 4
    #st.subheader("Pregunta 4")
    #st.markdown("""
    #Complete la reacción indicando cuáles son los productos, cuánto es la suma de coeficientes estequiométricos y clasifique la reacción:  
    #**Al + H₂SO₄ → _______ + ______**
    #""")
    #q4 = st.radio("Seleccione la respuesta correcta:",
    #              options=[
    #                  "a) Al₂(SO₄)₃ + H₂ / 9 / Desplazamiento simple",
    #                  "b) Al(SO₄)₃ + H / 8 / Desplazamiento doble",
    #                  "c) Al₃(SO₄)₂ + H / 10 / Desplazamiento simple",
    #                  "d) Al₂SO₄ + H₂ / 9 / Desplazamiento doble"
    #              ],
    #              key="q4")
    
    # Pregunta 5
    #st.subheader("Pregunta 5")
    #st.markdown("""
    #Indique la correspondencia correcta entre reacción y clasificación:  
    #a) CaCO₃ (s) → CaO (s) + CO₂ (g)  
    #b) Zn (s) + CuSO₄ (ac) → ZnSO₄ (ac) + Cu (s)  
    #c) AgNO₃ (ac) + HCl (ac) → HNO₃ (ac) + AgCl (s)
    #""")
    #q5 = st.radio("Seleccione la respuesta correcta:",
    #              options=[
    #                  "a) (b) Desplazamiento simple / (a) Descomposición / (c) Doble desplazamiento",
    #                  "b) (a) Descomposición / (b) Desplazamiento simple / (c) Doble desplazamiento",
    #                  "c) (c) Descomposición / (a) Doble desplazamiento / (b) Desplazamiento simple"
    #              ],
    #              key="q5")
    
    # Evaluación
    #if st.button("Enviar respuestas"):
    #    if q1.startswith("a)"):
    #        score += 4
    #    if q2.startswith("a)"):
    #        score += 4
    #    if q3.startswith("a)"):
    #        score += 4
    #    if q4.startswith("a)"):
    #        score += 4
    #    if q5.startswith("b)"):
    #        score += 4
    
    #    st.success(f"Tu puntaje es: {score} / 20")
        
    
    #enlace = "https://numeroscuanticos.streamlit.app/"
    #st.write("Practica los números cuánticos con ejercicios [aquí](%s)" % enlace)
    #st.image("img/nuclido1.png", caption="https://numeroscuanticos.streamlit.app/")
    st.markdown("---")
    ####################################    
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
    st.header('Semana 5: Estequiometría', divider='rainbow')

    diapositivas6 = "https://docs.google.com/presentation/d/1Ji7QVOSaUglLYNA6ipRadnnO3aRqwn5i/preview"
    st.markdown(f'<iframe src="{diapositivas6}" width="800" height="500" allow="autoplay"></iframe>', unsafe_allow_html=True)

#############################Pagina 7############################## 
def page7():
    st.header('Semana 6: Estado Gaseoso', divider='rainbow')

    diapositivas7 = "https://docs.google.com/presentation/d/15u81D0lWS8UYIfNir7sr3hxtsr7gO0yR/preview"
    st.markdown(f'<iframe src="{diapositivas7}" width="800" height="500" allow="autoplay"></iframe>', unsafe_allow_html=True)

    st.info("Introducción a los Gases")
    phet7 = "https://phet.colorado.edu/sims/html/gases-intro/latest/gases-intro_all.html"
    st.components.v1.iframe(phet7, width=800, height=600, scrolling=False)

    st.info("Propiedades de los Gases")
    phet7a = "https://phet.colorado.edu/sims/html/gas-properties/latest/gas-properties_all.html"
    st.components.v1.iframe(phet7a, width=800, height=600, scrolling=False)
#############################Pagina 8############################## 

def page8():
    st.header('Semana 7: Soluciones', divider='rainbow')
    diapositivas8 = "https://docs.google.com/presentation/d/1zeQYdC_fhoyhl4fMWv5gNwrpOIS9jgOV/preview"
    st.markdown(f'<iframe src="{diapositivas8}" width="800" height="500" allow="autoplay"></iframe>', unsafe_allow_html=True)

    st.info("Soluciones")
    phet8 = "https://phet.colorado.edu/sims/html/concentration/latest/concentration_all.html"
    st.components.v1.iframe(phet8, width=800, height=600, scrolling=False)

    st.info("Soluciones Ácido-Base")
    phet8a = "https://phet.colorado.edu/sims/html/acid-base-solutions/1.2.24/acid-base-solutions_es_PE.html"
    st.components.v1.iframe(phet8a, width=800, height=600, scrolling=False)

#############################Pagina 9############################## 

def page9():
    st.header('Semana 8: ', divider='rainbow')

#############################Pagina 10############################## 

def page10():
    st.header('Semana 9: ', divider='rainbow')

#############################Pagina 11############################## 

def page11():
   st.header('Semana 10: ', divider='rainbow')
   
################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Generalidades": Home,
  "Semana 1: Estructura atómica": page2,
  "Semana 2: Configuración y Tabla Periódica": page3,
  "Semana 3: Unidades Químicas de Masa": page4,
  "Semana 4: Reacciones Químicas": page5,
  "Semana 5: Estequiometría": page6,
  "Semana 6: ": page7,
  "Semana 7: ": page8,
  "Semana 8: ": page9,
  "Semana 9: ": page10,
  "Semana 10: ": page11,
}

selected_page = st.sidebar.selectbox("Temario", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

st.sidebar.info("Autor: Dr. Jesus Alvarado Huayhuaz")
st.sidebar.write("Laboratorio de Ingeniería Biomédica, Universidad Peruana Cayetano Heredia")
st.sidebar.write("Contacto: jesus.alvarado@upch.pe")
