import streamlit as st
import random

st.set_page_config(page_title="For Chehak ❤️", page_icon="💖", layout="wide")

# ---------- Theme & Custom CSS ----------
st.markdown(
    """
    <style>
    :root {
      --pink-1: #ffd8e8;
      --pink-2: #fff1f7;
      --pink-3: #ff4d88;
      --pink-4: #e6005c;
      --text-dark: #3f1a2b;
      --night-1: #0f1020;
      --night-2: #1a1b35;
    }

    .stApp {
      background: radial-gradient(circle at top left, var(--pink-1), var(--pink-2) 60%);
      color: var(--text-dark);
    }

    .topbar {
      display:flex;
      justify-content:space-between;
      align-items:center;
      padding: .25rem 0 .5rem 0;
      position: sticky;
      top: 0;
      z-index: 999;
      backdrop-filter: blur(6px);
    }

    .brand {
      font-size: 1.1rem;
      font-weight: 700;
      color: #b10f4f;
      letter-spacing: .3px;
    }

    .nav {
      font-size: .93rem;
      opacity: .9;
    }

    .hero {
      margin-top: .6rem;
      border-radius: 28px;
      padding: 3.2rem 1.5rem;
      text-align: center;
      background:
        linear-gradient(120deg, rgba(15,16,32,.85), rgba(26,27,53,.78)),
        radial-gradient(circle at 20% 20%, rgba(255,120,170,.35), transparent 40%),
        radial-gradient(circle at 80% 10%, rgba(255,190,220,.2), transparent 30%);
      color: #ffe8f2;
      box-shadow: 0 30px 60px rgba(180,20,80,.25);
      border: 1px solid rgba(255,255,255,.14);
    }

    .hero h1 {
      font-size: clamp(2rem, 5vw, 4rem);
      margin-bottom: .3rem;
      color: #ff8db8;
      text-shadow: 0 0 16px rgba(255,120,170,.55);
      font-family: "Brush Script MT", "Segoe Script", cursive;
    }

    .hero p {
      font-size: 1.15rem;
      margin: .4rem 0 1.4rem 0;
      color: #ffeef6;
    }

    .glass {
      background: rgba(255,255,255,.75);
      border: 1px solid rgba(255,255,255,.65);
      border-radius: 24px;
      padding: 1.2rem 1rem;
      box-shadow: 0 16px 35px rgba(220,40,110,.12);
      margin-bottom: 1rem;
    }

    .section-title {
      text-align:center;
      font-size: 1.85rem;
      margin: .2rem 0 .8rem;
      color: #7f2147;
      font-weight: 700;
    }

    .center {
      text-align:center;
    }

    .question {
      text-align:center;
      font-size: clamp(1.5rem, 2.8vw, 2.6rem);
      font-weight: 700;
      color: #4f1f33;
      margin: .5rem 0 1.1rem;
      line-height: 1.25;
    }

    .sub {
      text-align:center;
      opacity:.8;
      margin-bottom: .6rem;
    }

    .divider {
      text-align:center;
      color: #d0316b;
      margin: .2rem 0 1rem;
      letter-spacing:.08em;
    }

    .yes-screen {
      border-radius: 28px;
      padding: 2rem 1.2rem;
      text-align:center;
      background:
        linear-gradient(130deg, rgba(15,16,32,.9), rgba(26,27,53,.82)),
        radial-gradient(circle at 20% 20%, rgba(255,120,170,.35), transparent 40%);
      color:#ffe9f3;
      border: 1px solid rgba(255,255,255,.15);
      box-shadow: 0 26px 48px rgba(170,20,80,.25);
    }

    .no-screen {
      border-radius: 24px;
      padding: 1.6rem 1rem;
      text-align:center;
      background: rgba(255,255,255,.72);
      border: 1px solid rgba(255,180,210,.55);
    }

    .foot {
      text-align:center;
      padding: 1rem 0 .4rem;
      opacity:.82;
      color:#7b3554;
      font-size:.94rem;
    }

    /* Button polish */
    .stButton > button {
      border-radius: 999px !important;
      font-weight: 700 !important;
      border: 1px solid rgba(230,0,92,.22) !important;
      padding: .62rem 1rem !important;
      transition: .2s ease;
    }

    .stButton > button:hover {
      transform: translateY(-1px);
      box-shadow: 0 10px 24px rgba(230,0,92,.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Data ----------
QUESTIONS = [
    {
        "q": "Do you like me a little?",
        "yes": "Yes, a little! ❤️",
        "no": "Not really...",
    },
    {
        "q": "Would you love to talk to me every day?",
        "yes": "Yes, of course! 💖",
        "no": "Maybe",
    },
    {
        "q": "Can I be the one who makes you smile always?",
        "yes": "Yes, always! 💗",
        "no": "Not sure",
    },
    {
        "q": "Will you go on cute dates with me?",
        "yes": "Yes, that sounds amazing! 🌸",
        "no": "Maybe later",
    },
    {
        "q": "Will you be mine? For real this time...",
        "yes": "Yes, I'll be yours! 💞",
        "no": "Let me think...",
    },
]

NO_LINES = [
    "Even a little means a lot to me... ❤️",
    "I'll still be here, smiling for you. 🌷",
    "No is just a 'not now'... right? 💓",
    "Take your time — my feelings stay the same. ✨",
]

REASONS = [
    "Your smile is my favourite view.",
    "Talking to you makes every day brighter.",
    "You make ordinary moments magical.",
    "With you, even silence feels beautiful.",
]

MEMORIES = [
    "🌇 Sunset walks and heart-to-heart talks",
    "☕ Cozy coffee dates",
    "🎶 Songs that remind me of you",
    "💌 Tiny moments that feel like forever",
]

# ---------- State ----------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "step" not in st.session_state:
    st.session_state.step = 0
if "rejected" not in st.session_state:
    st.session_state.rejected = False
if "no_msg" not in st.session_state:
    st.session_state.no_msg = ""


def reset_all():
    st.session_state.page = "home"
    st.session_state.step = 0
    st.session_state.rejected = False
    st.session_state.no_msg = ""


# ---------- Header ----------
st.markdown(
    '<div class="topbar"><div class="brand">💖 For Chehak ❤️</div><div class="nav">Home &nbsp;&nbsp; Letters &nbsp;&nbsp; Memories &nbsp;&nbsp; Reasons &nbsp;&nbsp; Proposal</div></div>',
    unsafe_allow_html=True,
)

# ---------- Hero ----------
if st.session_state.page == "home":
    st.markdown(
        """
        <div class="hero">
          <h1>Hey Chehak ♡</h1>
          <p>A small website, for a very special person</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="glass center">', unsafe_allow_html=True)
    st.markdown("### Ready for a few cute questions? 💌")
    st.caption("No pressure, only love and smiles ✨")
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("Start Our Story ❤️", use_container_width=True):
            st.session_state.page = "proposal"
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Letters</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="center">
              Some people make the world brighter just by being in it.<br>
              You're one of them. ❤️
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Memories</div>', unsafe_allow_html=True)
        st.markdown("\n".join([f"- {m}" for m in MEMORIES]))
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Reasons I Like You</div>', unsafe_allow_html=True)
    for r in REASONS:
        st.markdown(f"- {r}")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Proposal Flow ----------
if st.session_state.page == "proposal" and not st.session_state.rejected and st.session_state.step < len(QUESTIONS):
    q = QUESTIONS[st.session_state.step]
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown(f"<div class='sub'>Question {st.session_state.step + 1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='question'>{q['q']}</div>", unsafe_allow_html=True)
    st.markdown("<div class='divider'>────────── 💗 ──────────</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1.1, 1.1, .9])
    with c1:
        if st.button(q["yes"], key=f"yes_{st.session_state.step}", use_container_width=True):
            st.session_state.step += 1
            st.rerun()
    with c2:
        if st.button(q["no"], key=f"no_{st.session_state.step}", use_container_width=True):
            st.session_state.rejected = True
            st.session_state.no_msg = random.choice(NO_LINES)
            st.rerun()
    with c3:
        if st.button("Back to Home", key=f"home_{st.session_state.step}", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Yes Ending ----------
if st.session_state.page == "proposal" and st.session_state.step >= len(QUESTIONS):
    st.markdown(
        """
        <div class="yes-screen">
          <h1 style="font-family:'Brush Script MT','Segoe Script',cursive;font-size:4rem;margin:.1rem 0;">Yay! ❤️</h1>
          <h3 style="margin:.2rem 0 1rem;">You said YES!</h3>
          <p style="font-size:1.15rem;line-height:1.7;max-width:780px;margin:auto;">
            Thank you for being the most amazing part of my life.
            I promise to make you smile, always.<br>
            Here's to our beautiful journey together! 💞
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("Forever Yours 💌", use_container_width=True):
            reset_all()
            st.rerun()

# ---------- No Ending ----------
if st.session_state.page == "proposal" and st.session_state.rejected:
    st.markdown(
        f"""
        <div class="no-screen">
          <h1 style="margin:.2rem 0;">Oh no! 🥺</h1>
          <p style="font-size:1.15rem;max-width:760px;margin:auto;line-height:1.7;">
            But I'll still be here... You might have said no,
            but you'll always be someone very special to me.<br>
            My feelings won't change. ❤️
          </p>
          <p style="margin-top:.7rem;font-weight:700;color:#7a2f4c;">{st.session_state.no_msg}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("Maybe someday? 💖", use_container_width=True):
            st.session_state.rejected = False
            st.session_state.no_msg = ""
            st.rerun()

st.markdown('<div class="foot">Made with lots of love ❤️</div>', unsafe_allow_html=True)
