
# 🔮 Oráculo de Tarot - Proyecto Streamlit

Bienvenido al **Oráculo de Tarot**, una aplicación web interactiva construida en **Python** usando **Streamlit**.

Este proyecto permite realizar una tirada de cartas de tarot personalizada, interpretar la tirada mediante inteligencia artificial, y explorar temas como amor, salud, trabajo o simplemente realizar una consulta abierta al universo.

---

## 🚀 ¿Qué incluye esta app?

- **Selección de tirada**: elige entre 1, 3, 4 o 5 cartas.
- **Definición de objetivo**: pregunta específica, tema, o lectura general.
- **Visualización de cartas**: muestra imágenes locales de las cartas, en posición normal o invertida.
- **Significado breve** de cada carta.
- **Interpretación final personalizada** con IA (OpenAI API).
- **Flujo limpio y controlado**: sin recargas dobles, sin errores, sin repeticiones.

---

## 🛠 Requisitos

Antes de correr la app, asegúrate de instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

---

## 📂 Estructura del Proyecto

```
oraculum/
├── app.py               # Aplicación principal
├── cartas.json          # Datos de todas las cartas (nombre, imágenes, significados)
├── images/              # Carpeta con las imágenes de todas las cartas
├── interpretacion.py    # Módulo para generar la interpretación final usando OpenAI
├── requirements.txt     # Lista de librerías necesarias
└── README.md            # Este archivo
```

---

## 🎯 Cómo ejecutar

1. Clona o descarga este repositorio.
2. Asegúrate de tener las imágenes en la carpeta `/images`.
3. Ejecuta:

```bash
streamlit run app.py
```

4. Abre el navegador en [http://localhost:8501](http://localhost:8501) y comienza tu consulta.

---

## 🌟 Créditos

- Proyecto original desarrollado en colaboración contigo, Carlos.
- Inspiración mágica: la tradición eterna del Tarot y la exploración del destino.

---
