import streamlit as st

def home():
    st.title("Social Pulse: Análisis de Interacciones y Tendencias para Marcas en Redes Sociales")

    st.write(
        """
        En un mundo donde las redes sociales son esenciales para conectar marcas y consumidores, interpretar datos generados en plataformas 
        como Instagram se ha convertido en un desafío clave. Este proyecto propone un análisis descriptivo y predictivo del comportamiento 
        de las audiencias, transformando datos complejos en insights claros mediante un dashboard interactivo en Streamlit. Así, las marcas 
        podrán optimizar sus estrategias de marketing digital para lograr un mayor impacto y engagement con su audiencia.
        """
    )
    
    st.markdown("---")

    st.image("streamlit_app/redes.jpeg", use_container_width=True)

    st.markdown("---")
    
        st.markdown(
    "[Carpeta de archivos Google Drive Grupo 5](https://drive.google.com/drive/u/0/folders/1_UbfHd6ebG1pEbCCWzNR5vGxIldwqxHA)", 
    unsafe_allow_html=True
    )
    st.markdown(
    "[Github Grupo 5](https://github.com/Angiea18/ProyectoFinalGrupo5)", 
    unsafe_allow_html=True
    )

     st.markdown("---")

    st.markdown("**Integrantes Grupo 5**")
    integrantes = [
        "Andrea Ximena Castaño | Angie Arango Zapata | Esneider Álvarez | Sebastián Loaiza | Álvaro Lozano"
    ]
    for integrante in integrantes:
        st.markdown(f"- {integrante}")
    
    st.markdown("---")

# Llama la función de la página principal dentro de tu estructura
if __name__ == "__main__":
    home()

