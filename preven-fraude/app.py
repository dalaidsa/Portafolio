import streamlit as st

st.title("Prototipo: Motor Anti-Fraude Transaccional")

# Entrada del directivo/usuario
monto = st.number_input("Monto de la transferencia (MXN):", min_value=0)
pais_destino = st.selectbox("País destino:", ["México", "EEUU", "Islas Caimán", "Panamá"])
intentos_previos = st.slider("Intentos fallidos de NIP en las últimas 24h:", 0, 5)

# Lógica simulada del modelo
def evaluar_riesgo(monto, pais, intentos):
    if pais in ["Islas Caimán", "Panamá"] and monto > 50000:
        return "ALTO RIESGO - Bloqueo Preventivo 🔴"
    elif intentos >= 3:
        return "RIESGO MEDIO - Requerir Token Adicional 🟡"
    return "APROBADA - Operación Normal 🟢"

if st.button("Simular Transacción"):
    resultado = evaluar_riesgo(monto, pais_destino, intentos_previos)
    st.subheader(f"Resolución del Motor: {resultado}")
