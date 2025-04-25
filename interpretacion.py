
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interpretar_lectura(cartas, objetivo):
    resumen_cartas = []
    for carta in cartas:
        orientacion = "invertida" if carta["orientacion"] == "invertida" else ""
        nombre = carta["nombre"]
        significado = carta["significado_derecha"] if carta["orientacion"] == "normal" else carta["significado_invertida"]
        linea = f"{nombre} {f'({orientacion})' if orientacion else ''}: {significado}".strip()
        resumen_cartas.append(linea)

    prompt = f"""
Eres un lector de tarot sabio y poético. Un consultante ha preguntado: "{objetivo}".

Estas son las cartas reveladas:
{chr(10).join(resumen_cartas)}

Con base en esto, ofrece una interpretación profunda, introspectiva y simbólica que conecte las cartas entre sí y responda al objetivo del consultante.

Evita predicciones literales. Inspira, reflexiona y conecta con la sabiduría interior.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()
