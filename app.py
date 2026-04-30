import streamlit as st

# Configuración de la pestaña
st.set_page_config(page_title="Sabor & Tradición", page_icon="🥓", layout="wide")

# Títulos principales
st.title("🥓 Chorizos Sabor & Tradición 🍗")
st.markdown("### ¡Bienvenido! Disfruta de la mejor calidad y sabor artesanal.")
st.divider()

# --- TU BASE DE DATOS DE PRODUCTOS (CON FOTOS DE PRUEBA) ---
# Nota: Usamos enlaces de internet por ahora. Luego las cambiaremos por tus fotos reales.
catalogo = {
    "Panceta Natural": {
        "precio": 13000, 
        "presentacion": "Libra", 
        "linea": "🐷 Cerdo",
        "imagen": "https://raw.githubusercontent.com/t-dedios/images/main/panceta_prueba.jpg"
    },
    "Panceta Ahumada": {
        "precio": 15000, 
        "presentacion": "Libra", 
        "linea": "🐷 Cerdo",
        "imagen": "https://raw.githubusercontent.com/t-dedios/images/main/panceta_ahumada_prueba.jpg"
    },
    "Alitas Finas Hierbas": {
        "precio": 12000, 
        "presentacion": "Libra", 
        "linea": "🐔 Pollo",
        "imagen": "https://raw.githubusercontent.com/t-dedios/images/main/alitas_prueba.jpg"
    },
    "Deditos de Pollo": {
        "precio": 20000, 
        "presentacion": "Libra", 
        "linea": "🥖 Apanados",
        "imagen": "https://raw.githubusercontent.com/t-dedios/images/main/deditos_prueba.jpg"
    }
}

st.subheader("Nuestro Menú")
st.write("Toca la foto para ampliarla")

# --- DISEÑO VISUAL DEL CATÁLOGO ---
# Creamos filas y columnas para que se vea ordenado
# 'st.columns(2)' crea dos columnas principales

for producto, info in catalogo.items():
    # Creamos un contenedor blanco para cada producto
    with st.container(border=True):
        # Dividimos el espacio: 1 parte para la foto, 2 partes para el texto
        col_foto, col_texto = st.columns([1, 2])
        
        with col_foto:
            # Mostramos la imagen. 'use_column_width=True' la ajusta al ancho de la columna
            st.image(info['imagen'], use_column_width=True)
            
        with col_texto:
            st.markdown(f"## {producto}")
            st.markdown(f"**Categoría:** {info['linea']}")
            st.markdown(f"**Presentación:** {info['presentacion']}")
            # Formateamos el precio para que se vea más profesional (con puntos)
            precio_formateado = f"${info['precio']:,}".replace(",", ".")
            st.success(f"**Precio: {precio_formateado}**")

# Pie de página simple
st.divider()
st.caption("Chorizos Sabor & Tradición - Todos los derechos reservados.")
