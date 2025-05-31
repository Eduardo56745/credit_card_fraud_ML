import streamlit as st
import joblib
import numpy as np

# Cargar el modelo
model = joblib.load("modelo_fraude.pkl")  # Ajusta si tu archivo tiene otro nombre

st.set_page_config(page_title="Detector de Fraude", page_icon="🕵️‍♂️")

st.title("🕵️ Detector de Fraude con Tarjeta de Crédito")
st.markdown("""
Este modelo usa Machine Learning para detectar si una transacción con tarjeta de crédito es fraudulenta.

🧪 **Nota:** Los datos fueron transformados con una técnica llamada *Análisis de Componentes Principales (PCA)* para proteger la identidad de los usuarios.
""")

# Lista completa de características
features = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]
input_data = []

# Botones en la barra lateral
st.sidebar.header("⚙️ Opciones")
use_random = st.sidebar.button("🎲 Usar valores aleatorios")
use_fraud_example = st.sidebar.button("🧪 Prueba de transacción fraudulenta")

# Datos corregidos de una transacción fraudulenta (30 variables)
fraud_example = [
    7526.0, 0.008430, 4.137837, -6.240697, 6.675732, 0.768307, -3.353060, -1.631735,
    0.154612, -2.795892, -6.187891, 5.664395, -9.854485, -0.306167, -10.691196,
    -0.638498, -2.041974, -1.129056, 0.116453, -1.934666, 0.488378, 0.364514,
    -0.608057, -0.539528, 0.128940, 1.488481, 0.507963, 0.735822, 0.513574, 1.0
]

st.subheader("📥 Ingresa los datos de la transacción")

# Crear inputs dinámicos
for i, feat in enumerate(features):
    if feat == "Amount":
        val = (
            np.round(np.random.uniform(0.01, 5000), 2) if use_random else
            fraud_example[i] if use_fraud_example else
            100.0
        )
        val = st.number_input(feat + " ($)", min_value=0.0, max_value=5000.0, value=val, step=0.01)
    elif feat == "Time":
        val = (
            np.round(np.random.uniform(-11, 11), 2) if use_random else
            fraud_example[i] if use_fraud_example else
            0.0
        )
        val = st.slider(feat, min_value=-11.0, max_value=11.0, value=val)
    else:
        val = (
            np.round(np.random.uniform(-11, 11), 2) if use_random else
            fraud_example[i] if use_fraud_example else
            0.0
        )
        val = st.slider(feat, min_value=-11.0, max_value=11.0, value=val)
    input_data.append(val)

# Convertir a array y predecir
input_array = np.array([input_data])

if st.button("Detectar"):
    resultado = model.predict(input_array)
    proba = model.predict_proba(input_array)[0][1]
    if resultado[0] == 1:
        st.error(f"🚨 Transacción Fraudulenta — Probabilidad: {proba:.2%}")
    else:
        st.success(f"✅ Transacción Válida — Probabilidad de fraude: {proba:.2%}")



