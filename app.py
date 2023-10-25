import streamlit as st

# Título de la aplicación
st.title("Mi Aplicación Web con Streamlit")

# Texto en la aplicación
st.write("Esta es una aplicación web de ejemplo que utiliza Streamlit.")

# Componente de imagen
st.image("https://via.placeholder.com/300", caption="Imagen de ejemplo", use_column_width=True)

# Componente de selectbox
opciones = ["Opción 1", "Opción 2", "Opción 3"]
seleccion = st.selectbox("Selecciona una opción:", opciones)

# Mostrar el resultado de la selección
st.write("Has seleccionado:", seleccion)

# Botón para ejecutar una acción
if st.button("Haz clic aquí"):
    st.write("¡Has hecho clic en el botón!")

# Reproducción de audio
st.audio("https://file-examples.com/wp-content/uploads/2017/11/file_example_MP3_700KB.mp3", format="audio/mp3")

# Reproducción de video
st.video("https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_480_1_5MG.mp4")
