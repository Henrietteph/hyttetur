import streamlit as st

# --- Init Session State ---
if "players" not in st.session_state:
    st.session_state.players = {}
if "agenda" not in st.session_state:
    st.session_state.agenda = {
        "Fredag": ["18:00 - Velkommen", "19:00 - Middag"],
        "Lørdag": ["10:00 - Frokost", "12:00 - Spillturnering", "18:00 - Grillfest"]
    }

# --- Page Config ---
st.set_page_config(page_title="Poengtavle", layout="centered")

# --- Header Image ---
st.title("Hyttetur")
#uploaded_image = st.file_uploader("Last opp toppbilde", type=["jpg", "jpeg", "png"])
#if uploaded_image:
#    st.image(uploaded_image, use_column_width=True)

# --- Legg til deltaker ---
st.subheader("➕ Legg til deltaker")
new_name = st.text_input("Navn på deltaker")
if st.button("Legg til"):
    if new_name and new_name not in st.session_state.players:
        st.session_state.players[new_name] = 0
    elif new_name in st.session_state.players:
        st.warning(f"{new_name} finnes allerede!")

# --- Vis poengtavle ---
st.subheader("🏆 Poengtavle")
if not st.session_state.players:
    st.info("Ingen deltakere enda.")
else:
    for name, score in st.session_state.players.items():
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        with col1:
            st.write(f"**{name}**")
        with col2:
            st.write(f"{score}")
        with col3:
            if st.button("+1", key=f"plus_{name}"):
                st.session_state.players[name] += 1
        with col4:
            if st.button("-1", key=f"minus_{name}"):
                st.session_state.players[name] -= 1

# --- Fjern deltaker ---
st.subheader("❌ Fjern deltaker")
remove_name = st.selectbox("Velg deltaker", [""] + list(st.session_state.players.keys()))
if st.button("Fjern"):
    if remove_name:
        del st.session_state.players[remove_name]

# --- Agenda ---
st.subheader("📅 Agenda")
for day, items in st.session_state.agenda.items():
    st.markdown(f"### {day}")
    for item in items:
        st.write(f"• {item}")
