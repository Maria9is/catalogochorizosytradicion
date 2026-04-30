import streamlit as st

# Configuración de la pestaña
st.set_page_config(page_title="Sabor & Tradición", page_icon="🥓", layout="wide")

# Títulos principales
st.title("🥓 Chorizos Sabor & Tradición 🍗")
st.markdown("### ¡Bienvenido! Disfruta de la mejor calidad y sabor artesanal.")
st.divider()

# --- CATÁLOGO CON IMÁGENES REALES DE INTERNET ---
catalogo = {
    "Panceta Natural": {
        "precio": 13000, 
        "presentacion": "Libra", 
        "linea": "🐷 Cerdo",
        "imagen": "https://images.unsplash.com/photo-1602410204242-af1575a6b1d0?w=500" # Foto de tocino/panceta
    },
    "Panceta Ahumada": {
        "precio": 15000, 
        "presentacion": "Libra", 
        "linea": "🐷 Cerdo",
        "imagen": "https://images.unsplash.com/photo-1529854140021-a548ef59b3bc?w=500" # Foto de carne ahumada
    },
    "Alitas Finas Hierbas": {
        "precio": 12000, 
        "presentacion": "Libra", 
        "linea": "🐔 Pollo",
        "imagen": "https://images.unsplash.com/photo-1527477396000-e27163b481c2?w=500" # Foto de alitas
    },
    "Deditos de Pollo": {
        "precio": 20000, 
        "presentacion": "Libra", 
        "linea": "🥖 Apanados",
        "imagen": "https://images.unsplash.com/photo-1562967914-608f82629710?w=500" # Foto de pollo apanado
    }
}

st.subheader("Nuestro Menú")

for producto, info in catalogo.items():
    with st.container(border=True):
        col_foto, col_texto = st.columns([1, 2])
        with col_foto:
            st.image(info['imagen'], use_container_width=True) # Actualizado para nuevas versiones de Streamlit
        with col_texto:
            st.markdown(f"## {producto}")
            st.markdown(f"**Categoría:** {info['linea']}")
            st.markdown(f"**Presentación:** {info['presentacion']}")
            precio_formateado = f"${info['precio']:,}".replace(",", ".")
            st.success(f"**Precio: {precio_formateado}**")

st.divider()
st.caption("Chorizos Sabor & Tradición - Todos los derechos reservados.")
