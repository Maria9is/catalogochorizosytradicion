import streamlit as st

# Esto configura el nombre que sale en la pestaña del navegador
st.set_page_config(page_title="Sabor & Tradición", page_icon="🥓")

# Títulos principales
st.title("🥓 Chorizos Sabor & Tradición 🍗")
st.write("¡Bienvenido a nuestro catálogo interactivo! Disfruta de la mejor calidad y sabor.")
st.divider() # Esto dibuja una línea horizontal elegante

# Tu base de datos de productos
catalogo = {
    "Panceta Natural": {"precio": 13000, "presentacion": "Libra", "linea": "🐷 Línea de Cerdo"},
    "Panceta Ahumada": {"precio": 15000, "presentacion": "Libra", "linea": "🐷 Línea de Cerdo"},
    "Alitas Finas Hierbas": {"precio": 12000, "presentacion": "Libra", "linea": "🐔 Línea de Pollo"},
    "Deditos de Pollo": {"precio": 20000, "presentacion": "Libra", "linea": "🥖 Línea de Apanados"}
}

st.subheader("Nuestro Menú")

# Aquí le decimos a Streamlit que dibuje cada producto
for producto, info in catalogo.items():
    st.markdown(f"### {producto}") # markdown(###) hace que el texto sea más grande
    st.write(f"**Categoría:** {info['linea']}")
    st.write(f"**Presentación:** {info['presentacion']}")
    st.write(f"**Precio:** ${info['precio']}")
    st.write("---") # Otra línea separadora
