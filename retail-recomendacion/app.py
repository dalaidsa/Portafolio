import streamlit as st

# 1. Configuración visual de la página
st.set_page_config(page_title="Prototipo: Motor de Recomendación", page_icon="🛒")
st.title("🛒 Prototipo: Motor de Recomendación (Cross-Selling)")
st.write("Simulación de sugerencias en tiempo real dentro del carrito de compras.")

# 2. MOCK DATA: Matriz de productos comprados juntos
historial_compras = {
    "Laptop": ["Mouse Inalámbrico", "Funda protectora", "Monitor externo"],
    "Smartphone": ["Funda de silicón", "Audífonos Bluetooth", "Cargador rápido"],
    "Zapatos de correr": ["Calcetines deportivos", "Botella de agua"],
    "Cafetera": ["Filtros de papel", "Café en grano 1kg", "Taza térmica"]
}

# 3. Interacción del usuario (Selector de producto)
producto_seleccionado = st.selectbox(
    "Selecciona un producto para simular su ingreso al carrito:",
    options=list(historial_compras.keys())
)

# 4. Lógica de recomendación y despliegue en interfaz
if st.button("Simular Carrito de Compras"):
    st.subheader(f"Producto actual en carrito: {producto_seleccionado}")
    
    recomendaciones = historial_compras.get(producto_seleccionado, [])
    
    if recomendaciones:
        st.success("💡 Los clientes que compraron este artículo también llevaron:")
        # Mostrar las 2 recomendaciones principales en columnas visuales
        cols = st.columns(2)
        for idx, item in enumerate(recomendaciones[:2]):
            with cols[idx]:
                st.info(f"✅ **Sugerencia {idx + 1}:**\n\n{item}")
    else:
        st.warning("Sin recomendaciones específicas; mostrar promociones generales del día.")
