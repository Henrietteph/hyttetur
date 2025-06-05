import streamlit as st

# --- Init Session State ---
if "players" not in st.session_state:
    st.session_state.players = {}
if "agenda" not in st.session_state:
    st.session_state.agenda = {
        "Fredag": ["15:00 - Ankomst og apertiff", "15:30 - Romfordeling og Agenda", "16:00 - Pynte oss", "17:00 - Quiz", "18:00 - Middag", "20:00 - Skifte til chill", "20:30 - Mimeleik", "21:00 - Fritid"],
        "Lørdag": ["11:00 - Frokost og fyre i stampen", "12:30 - Spele kubb og/eller brettspill", "14:00 - Kortskalle og/eller anna hemmelig leik", "16:00 - Badestamp", "17:00 - Stelle seg", "18:00 - Middag", "19:30 - Ulike leika", "??:?? - Kåring av vinner🤴"],
        "Søndag": ["11:00 - Frokost", "12:30 - Pakke, rydde, vaske", "??:?? - Chill og avreise"]
    }

# --- Page Config ---
st.set_page_config(page_title="Poengtavle", layout="centered")

# --- Header Image ---
st.title("🔥Hyttetur🔥")
#uploaded_image = st.file_uploader("Last opp toppbilde", type=["jpg", "jpeg", "png"])
#if uploaded_image:
#    st.image(uploaded_image, use_column_width=True)

# --- Agenda ---
st.subheader("📅 Agenda")
col_fredag, col_lordag, col_sondag = st.columns(3)

with col_fredag:
    st.markdown("### Fredag")
    for item in st.session_state.agenda["Fredag"]:
        st.write(f"• {item}")

with col_lordag:
    st.markdown("### Lørdag")
    for item in st.session_state.agenda["Lørdag"]:
        st.write(f"• {item}")

with col_sondag:
    st.markdown("### Søndag")
    for item in st.session_state.agenda["Søndag"]:
        st.write(f"• {item}")
        

# --- Legg til deltaker ---
new_name = st.text_input("Legg til deltaker")
if st.button("Legg til"):
    st.session_state.players[new_name] = 0


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
#st.subheader("❌ Fjern deltaker")
#remove_name = st.selectbox("Velg deltaker", [""] + list(st.session_state.players.keys()))
#if st.button("Fjern"):
#    if remove_name:
#        del st.session_state.players[remove_name]

