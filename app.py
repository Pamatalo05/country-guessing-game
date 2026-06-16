import streamlit as st
import random

st.set_page_config(page_title="Country Guessing Game", page_icon="🌎")

countries = [
    {
        "country": "Ecuador",
        "capital": "Quito",
        "population": "18 millones",
        "region": "South America"
    },
    {
        "country": "Japan",
        "capital": "Tokyo",
        "population": "125 millones",
        "region": "Asia"
    },
    {
        "country": "Canada",
        "capital": "Ottawa",
        "population": "40 millones",
        "region": "North America"
    },
    {
        "country": "Brazil",
        "capital": "Brasilia",
        "population": "216 millones",
        "region": "South America"
    },
    {
        "country": "France",
        "capital": "Paris",
        "population": "68 millones",
        "region": "Europe"
    }
]

if "current_country" not in st.session_state:
    st.session_state.current_country = random.choice(countries)

st.title("🌎 Country Guessing Game")

st.write("Adivina el país usando las pistas:")

country = st.session_state.current_country

st.info(f"🏛️ Capital: {country['capital']}")
st.info(f"👥 Población: {country['population']}")
st.info(f"🌍 Región: {country['region']}")

guess = st.text_input("¿Qué país es?")

if st.button("Verificar respuesta"):
    if guess.strip().lower() == country["country"].lower():
        st.success("✅ ¡Correcto!")
    else:
        st.error(f"❌ Incorrecto. La respuesta era {country['country']}.")

if st.button("Nuevo país"):
    st.session_state.current_country = random.choice(countries)
    st.rerun()