import streamlit as st
import random

st.set_page_config(page_title="Romantic Proposal 💖", page_icon="💘", layout="centered")

# ---------- Styles ----------
st.markdown("""
<style>
.main {
    background: radial-gradient(circle at top left, #ffd6e8, #ffeef6 60%);
}
.block-container {
    padding-top: 2rem;
}
.card {
    background: rgba(255,255,255,0.78);
    border: 1px solid rgba(255,255,255,0.7);
    border-radius: 24px;
    padding: 1.4rem 1.2rem 1.8rem 1.2rem;
    box-shadow: 0 20px 45px rgba(230,0,92,0.18);
}
h1, h2, h3, p {
    text-align: center;
    color: #4a1c2c;
}
.small {
    text-align:center;
    opacity:.8;
}
.stButton > button {
    border-radius: 999px;
    font-weight: 700;
    border: none;
    padding: 0.6rem 1rem;
}
.yesBtn button {
    background: linear-gradient(135deg, #ff4d88, #e6005c) !important;
    color: white !important;
}
.noMsg {
    text-align: center;
    color: #8c3756;
    font-weight: 600;
    margin-top: 0.5rem;
}
.success {
    background: rgba(255,255,255,0.9);
    border: 1px dashed rgba(255,77,136,.6);
    border-radius: 18px;
    padding: 1rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- Data ----------
follow_ups = [
    {
        "q": "Aww 💞 When should we go out?",
        "options": ["This weekend 🌷", "Tonight 🌙", "Soon please 🥹"]
    },
    {
        "q": "What sounds perfect for our date?",
        "options": ["Coffee ☕", "Dinner 🍝", "Long walk 🌆"]
    },
    {
        "q": "Final question: Will you let me spoil you with love? ❤️",
        "options": ["Yes, always 😘", "Absolutely 💕", "100% yes 💗"]
    }
]

no_lines = [
    "Really? 🙃",
    "Think again 😘",
    "No is disabled 😌",
    "Try Yes maybe? 💘"
]

# ---------- State ----------
if "started" not in st.session_state:
    st.session_state.started = False
if "step" not in st.session_state:
    st.session_state.step = 0
if "done" not in st.session_state:
    st.session_state.done = False
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "no_msg" not in st.session_state:
    st.session_state.no_msg = ""

def reset():
    st.session_state.started = False
    st.session_state.step = 0
    st.session_state.done = False
    st.session_state.no_count = 0
    st.session_state.no_msg = ""

# ---------- UI ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<h1>Hey, beautiful ✨</h1>", unsafe_allow_html=True)
st.markdown('<p class="small">I have something special to ask you...</p>', unsafe_allow_html=True)

if not st.session_state.started:
    st.markdown("<h3>Would you like to go on a date with me? 💌</h3>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="yesBtn">', unsafe_allow_html=True)
        if st.button("Yes 💖", use_container_width=True):
            st.session_state.started = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        if st.button("No 🙈", use_container_width=True):
            st.session_state.no_count += 1
            st.session_state.no_msg = random.choice(no_lines)
            st.rerun()

    if st.session_state.no_msg:
        st.markdown(f'<p class="noMsg">{st.session_state.no_msg}</p>', unsafe_allow_html=True)

elif not st.session_state.done:
    current = follow_ups[st.session_state.step]
    st.markdown(f"<h3>{current['q']}</h3>", unsafe_allow_html=True)

    cols = st.columns(len(current["options"]))
    for i, opt in enumerate(current["options"]):
        with cols[i]:
            if st.button(opt, key=f"opt_{st.session_state.step}_{i}", use_container_width=True):
                st.session_state.step += 1
                if st.session_state.step >= len(follow_ups):
                    st.session_state.done = True
                st.rerun()

if st.session_state.done:
    st.markdown("""
    <div class="success">
      <h2>Yay!!! 🎉💞</h2>
      <p>You just made my day the happiest ever! 🌸</p>
      <p>Can’t wait for our cute date! 🥰</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Ask Again 💫", use_container_width=True):
        reset()
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
