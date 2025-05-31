import streamlit as st
import joblib
import numpy as np

# Cargar el modelo
model = joblib.load("xgb_model_credit_card_fraud.pkl")  # Cambia el nombre si es diferente

st.set_page_config(page_title="Detector de Fraude", page_icon="🕵️‍♂️")

st.title("🕵️ Detector de Fraude con Tarjeta de Crédito")
st.markdown("""
Este modelo utiliza técnicas avanzadas de Machine Learning para detectar si una transacción puede ser fraudulenta.

🧪 **Nota:** Los datos han sido transformados mediante *Análisis de Componentes Principales (PCA)* para proteger la identidad de los usuarios.
""")

# Lista de características
features = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]
input_data = []

# Botón para valores aleatorios
st.sidebar.header("🔧 Generar valores aleatorios")
use_random = st.sidebar.button("🎲 Usar valores aleatorios")

st.subheader("📥 Ingresa los datos de la transacción")

# Crear sliders o inputs para cada variable
for feat in features:
    if feat == "Amount":
        val = np.round(np.random.uniform(0.01, 5000), 2) if use_random else 100.0
        val = st.number_input(feat + " ($)", min_value=0.0, max_value=5000.0, value=val, step=0.01)
    elif feat == "Time":
        val = np.round(np.random.uniform(-11, 11), 2) if use_random else 0.0
        val = st.slider(feat, min_value=-11.0, max_value=11.0, value=val)
    else:
        val = np.round(np.random.uniform(-11, 11), 2) if use_random else 0.0
        val = st.slider(feat, min_value=-11.0, max_value=11.0, value=val)
    input_data.append(val)

# Convertir a array y predecir
input_array = np.array([input_data])

if st.button("Detectar"):
    resultado = model.predict(input_array)
    if resultado[0] == 1:
        st.error("🚨 Transacción Fraudulenta")
    else:
        st.success("✅ Transacción Válida")

