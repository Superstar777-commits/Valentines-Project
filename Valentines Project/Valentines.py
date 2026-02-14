import streamlit as st
from datetime import datetime, date
import os

st.set_page_config(page_title="Thando ❤️", page_icon="❤️", layout="centered")

# ---------------- THEME ----------------
st.markdown("""
<style>

body {
    background-color: #fff5f7;
}

.title {
    text-align:center;
    font-size:48px;
    color:#d90429;
    font-weight:bold;
    margin-top:30px;
}

.subtitle {
    text-align:center;
    font-size:22px;
    color:#444;
    margin-bottom:30px;
}

.section {
    background-color:white;
    padding:25px;
    border-radius:20px;
    margin-top:25px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

.stButton>button {
    border-radius:25px;
    height:65px;
    font-size:22px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

if "accepted" not in st.session_state:
    st.session_state.accepted = False

# ---------------- HEADER ----------------
st.markdown('<p class="title">Thando ❤️</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">I made a tiny website just to ask you something important...</p>', unsafe_allow_html=True)

# ---------------- COUNTDOWN ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)

target_date = date(date.today().year, 2, 28)
today = date.today()
days_left = (target_date - today).days

if days_left >= 0:
    st.subheader(f"⏳ Countdown to our date: {days_left} days")
else:
    st.subheader("The day has arrived ❤️")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- QUESTION ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)

st.subheader("Will you be my Valentine?")

no_messages = [
    "Are you sure? 🥺",
    "Think carefully...",
    "This button is getting nervous",
    "I believe in you",
    "The YES button looks better now right?",
    "Destiny is calling..."
]

col1, col2 = st.columns(2)

with col1:
    if st.button("YES 💖"):
        st.session_state.accepted = True

with col2:
    if st.button("NO 💔"):
        st.session_state.no_clicks += 1

if st.session_state.accepted:
    st.balloons()
    st.success("You just made me the happiest person alive ❤️")

    st.markdown("""
    ### 🌹 Date Details
    - 📅 28 February
    - 😊 Happiness: Guaranteed
    - 🍽️ Food: You choose
    - 💭 Memory: Pending creation
    """)

elif st.session_state.no_clicks > 0:
    msg = no_messages[min(st.session_state.no_clicks-1, len(no_messages)-1)]
    st.warning(msg)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PHOTO GALLERY ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("📸 Our Memories")

photo_folder = "Photos"

if os.path.exists(photo_folder):
    Photos = os.listdir(photo_folder)

    cols = st.columns(2)
    for i, photo in enumerate(photos):
        with cols[i % 2]:
            st.image(os.path.join(photo_folder, photo), use_container_width=True)
else:
    st.info("Add pictures into a folder named 'photos'")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<br>
<p style='text-align:center;color:gray'>
Made with courage ❤️
</p>
""", unsafe_allow_html=True)



