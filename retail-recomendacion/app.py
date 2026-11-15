# MOCK DATA: Matriz simple de productos comprados juntos
historial_compras = {
    "Laptop": ["Mouse Inalámbrico", "Funda protectora", "Monitor externo"],
    "Smartphone": ["Funda de silicón", "Audífonos Bluetooth", "Cargador rápido"],
    "Zapatos de correr": ["Calcetines deportivos", "Botella de agua"]
}

# Lógica del motor de recomendación
def generar_recomendacion(producto_en_carrito):
    print(f"--- Carrito Actual: {producto_en_carrito} ---")
    if producto_en_carrito in historial_compras:
        recomendaciones = historial_compras[producto_en_carrito]
        print("💡 Sugerencia del sistema: Los clientes también compraron:")
        for item in recomendaciones[:2]: # Mostrar solo las top 2
            print(f"  ✅ Agregar: {item}")
    else:
        print("💡 Sugerencia: Promociones generales del día.")

# Prototipado ejecutable en consola
generar_recomendacion("Laptop")
print("\n")
generar_recomendacion("Smartphone")
