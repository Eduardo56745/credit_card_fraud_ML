import streamlit as st
import joblib
import numpy as np

# Carga del modelo
model = joblib.load('modelo_fraude.pkl')  # tu modelo ya entrenado y exportado

st.title("🕵️‍♀️ Detector de Fraude con Tarjeta de Crédito")

st.markdown("Ingresa los datos de la transacción para evaluar si es fraudulenta.")

# Explicación sobre PCA
st.info("Nota: Los datos se procesaron usando una técnica llamada Análisis de Componentes Principales (PCA) para mantener el anonimato de la información original.")

# Botón para valores aleatorios
if st.button("Generar valores aleatorios"):
    v11 = np.round(np.random.uniform(-15, 15), 2)
    v4 = np.round(np.random.uniform(-15, 15), 2)
    v2 = np.round(np.random.uniform(-15, 15), 2)
    v17 = np.round(np.random.uniform(-15, 15), 2)
    amount = np.round(np.random.uniform(0.01, 5000.0), 2)
else:
    # Inputs manuales
    amount = st.number_input(
        "Monto de la transacción ($)", min_value=0.01, max_value=5000.0, value=100.0)

    v11 = st.slider("V11 (componente PCA)", min_value=-
                    15.0, max_value=15.0, value=0.0)
    v4 = st.slider("V4", min_value=-15.0, max_value=15.0, value=0.0)
    v2 = st.slider("V2", min_value=-15.0, max_value=15.0, value=0.0)
    v17 = st.slider("V17", min_value=-15.0, max_value=5.0, value=0.0)

# Preparar input para el modelo
input_array = np.zeros((1, 30))
input_array[0, 1] = v11
input_array[0, 2] = v2
input_array[0, 4] = v4
input_array[0, 17] = v17
input_array[0, 29] = amount

# Predicción
if st.button("Detectar"):
    resultado = model.predict(input_array)
    if resultado[0] == 1:
        st.error("🚨 Transacción Fraudulenta")
    else:
        st.success("✅ Transacción Válida")
