
import streamlit as st
import random
import json
from interpretacion import interpretar_lectura

st.set_page_config(page_title="Oráculo de Tarot", layout="centered")

# Inicializar sesión si no existen variables
st.session_state.setdefault("etapa", "bienvenida")
st.session_state.setdefault("num_cartas", 3)
st.session_state.setdefault("cartas", [])
st.session_state.setdefault("objetivo", "")
st.session_state.setdefault("volver_a_tirar", False)

# ✅ Manejar si se debe reiniciar antes de mostrar cualquier cosa
if st.session_state.volver_a_tirar:
    st.session_state.cartas = []
    st.session_state.etapa = "tirada"
    st.session_state.volver_a_tirar = False
    st.rerun()

# Cargar cartas
with open("cartas.json", "r", encoding="utf-8") as f:
    todas_las_cartas = json.load(f)

def mostrar_bienvenida():
    st.title("🔮 Oráculo de Tarot")
    st.write("Descubre lo que te depara el destino a través de las cartas. Tu lectura comienza aquí.")
    if st.button("Comenzar Lectura"):
        st.session_state.etapa = "tirada"

def elegir_tirada():
    st.header("Elige el tipo de tirada")
    tirada = st.radio("¿Cuántas cartas deseas que el oráculo revele?", ["3 cartas", "4 cartas", "5 cartas", "1 carta del día"])
    st.session_state.num_cartas = int(tirada[0])
    if st.button("Continuar"):
        st.session_state.etapa = "objetivo"

def definir_objetivo():
    st.header("¿Qué deseas explorar hoy?")
    objetivo = st.radio("Selecciona una opción o escribe tu pregunta:", ["Pregunta específica", "Tema (Amor, Salud, Trabajo)", "Lectura abierta"])
    pregunta = ""
    if objetivo == "Pregunta específica":
        pregunta = st.text_input("Escribe tu pregunta aquí")
    elif objetivo == "Tema (Amor, Salud, Trabajo)":
        tema = st.selectbox("Elige un tema", ["Amor", "Trabajo", "Salud", "Propósito"])
        pregunta = f"Tema: {tema}"
    else:
        pregunta = "Lectura abierta"

    if st.button("Realizar Tirada"):
        st.session_state.objetivo = pregunta
        st.session_state.etapa = "tirada_cartas"

def hacer_tirada():
    st.header("Tirada del Tarot")
    if not st.session_state.cartas:
        seleccion = random.sample(todas_las_cartas, k=st.session_state.num_cartas)
        for carta in seleccion:
            orientacion = random.choice(["normal", "invertida"])
            carta['orientacion'] = orientacion
            carta['img_mostrar'] = carta['img'] if orientacion == "normal" else carta['img_invertida']
            carta['significado'] = carta['significado_derecha'] if orientacion == "normal" else carta['significado_invertida']
        st.session_state.cartas = seleccion

    for i, carta in enumerate(st.session_state.cartas):
        st.subheader(f"Carta {i+1}: {carta['nombre']} {'(invertida)' if carta['orientacion'] == 'invertida' else ''}")
        st.image(carta['img_mostrar'], width=150)
        st.caption(carta['significado'])

    if st.button("Interpreta mis cartas"):
        st.session_state.etapa = "interpretacion"

def mostrar_interpretacion():
    st.header("🔍 Interpretación del Oráculo")

    with st.spinner("Consultando los misterios del universo..."):
        resumen = interpretar_lectura(st.session_state.cartas, st.session_state.objetivo)

    st.markdown(resumen)
    st.write("---")

    if st.button("🔄 Vuelve a tirar las cartas", key="volver_btn"):
        st.session_state.volver_a_tirar = True
        st.rerun()

# Enrutamiento principal
if st.session_state.etapa == "bienvenida":
    mostrar_bienvenida()
elif st.session_state.etapa == "tirada":
    elegir_tirada()
elif st.session_state.etapa == "objetivo":
    definir_objetivo()
elif st.session_state.etapa == "tirada_cartas":
    hacer_tirada()
elif st.session_state.etapa == "interpretacion":
    mostrar_interpretacion()
