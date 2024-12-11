import streamlit as st

def home():
    col1, col2 = st.columns([3, 1])  # 3 partes de espacio para la izquierda, 1 para la derecha
    with col2:
        st.image("images/logo.png", width=150)
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

    st.image("images/redes.jpeg", use_container_width=True)

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

