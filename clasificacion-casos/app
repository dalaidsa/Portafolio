# Importar la librería para crear interfaces web rápidas
import streamlit as st

# 1. Interfaz de Usuario (UI): Título y contexto para el directivo
st.title("Prototipo: Agente Clasificador de Casos")
st.write("Esta maqueta demuestra cómo el sistema leerá los reportes y los asignará automáticamente.")

# 2. Entrada de datos: El usuario puede escribir casos reales aquí
texto_reporte = st.text_area("Ingresa la descripción del problema (Ej. 'El cajero no me dio mi dinero'):")

# 3. Lógica de Negocio Simulada (Mock de IA / Reglas)
# En el prototipo usamos reglas básicas. En producción, esto se conecta a GPT/Gemini.
def clasificar_texto(texto):
    texto = texto.lower()
    if "cajero" in texto or "dinero" in texto or "tarjeta" in texto:
        return "Operaciones ATM", "Alta 🔴"
    elif "app" in texto or "contraseña" in texto or "bloqueo" in texto:
        return "Soporte Digital", "Media 🟡"
    else:
        return "Atención General", "Baja 🟢"

# 4. Interacción y Procesamiento
if st.button("Analizar Reporte"):
    if texto_reporte:
        # Ejecutar la función simulada
        area_asignada, nivel_prioridad = clasificar_texto(texto_reporte)
        
        # 5. Mostrar el resultado operativo en pantalla
        st.success("Análisis automatizado completado.")
        
        # Mostrar métricas visuales
        col1, col2 = st.columns(2)
        col1.metric(label="Área Asignada", value=area_asignada)
        col2.metric(label="Prioridad del Caso", value=nivel_prioridad)
    else:
        st.warning("Por favor, ingresa un reporte para hacer la prueba.")
