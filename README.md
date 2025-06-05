# 💳 Detección de Fraude con Tarjetas de Crédito

Este proyecto fue desarrollado para demostrar cómo el **Machine Learning** puede ayudar a detectar transacciones fraudulentas en tiempo real ⚠️. A partir de un conjunto de datos de tarjetas de crédito anonimizados, se entrenó un modelo capaz de identificar patrones sospechosos y prevenir fraudes financieros 🕵️‍♂️💰.

Forma parte de mis proyectos personales como **Data Scientist**, y el modelo ha sido desplegado como una app interactiva.

---

## 🔗 Prueba la App

Puedes probar el modelo en acción a través de esta aplicación desarrollada con **Streamlit** y desplegada en **Render**:

👉 [https://credit-card-fraud-ml.onrender.com](https://credit-card-fraud-ml.onrender.com)

> ⏳ *Nota: Puede tardar algunos segundos en iniciar si ha estado inactiva.*

---

## 📌 Objetivo del Proyecto

Detectar de forma automática si una transacción con tarjeta de crédito es **fraudulenta o legítima**, utilizando datos reales anonimizados. Este tipo de modelo puede integrarse en sistemas financieros para evitar pérdidas económicas significativas.

---

## ⚙️ Proceso de Desarrollo

### 🧹 Preparación de Datos
- Limpieza del conjunto de datos.
- Balanceo de clases con técnicas como **undersampling**.
- Separación entre variables numéricas y categóricas.

### ⚙️ Entrenamiento de Modelos
Se entrenaron diferentes modelos de clasificación, incluyendo:
- **Regresión Logística**
- **Random Forest**
- **LightGBM** (modelo final seleccionado)

### 📊 Evaluación
Debido al desbalance extremo en las clases, se usaron métricas especializadas:
- **F1-score** de 0.83
- **ROC AUC** de 0.99

---

## 🔍 Resultados

- 🔐 **Modelo final:** LightGBM
  - Alta capacidad para identificar fraudes sin generar demasiados falsos positivos.
  - Optimización enfocada en la clase minoritaria (transacciones fraudulentas).
  - Rendimiento superior en pruebas con datos no vistos.

---

## 🧰 Tecnologías Utilizadas

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- LightGBM ⚡
- Matplotlib & Seaborn
- Streamlit 🌐
- Render (despliegue web)

---

## 🚀 Aplicaciones Reales

- **Seguridad financiera:** detección automatizada de actividades sospechosas en tiempo real.
- **Integración con bancos o pasarelas de pago** 💳.
- **Escalabilidad:** adaptable a otros tipos de fraude o dominios transaccionales.

---

## ✨ Conclusión

Este proyecto demuestra el potencial del análisis de datos y el Machine Learning para prevenir fraudes financieros y proteger tanto a usuarios como a instituciones bancarias. La app desplegada permite probar el modelo de forma sencilla, simulando una predicción en tiempo real de transacciones sospechosas.

---

📫 ¿Dudas, ideas o sugerencias? ¡Estoy abierto a colaboración!
