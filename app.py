import streamlit as st
import language_tool_python
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="GrammarGenius AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD LANGUAGE TOOL
# =========================================================

@st.cache_resource
def load_tool():
    return language_tool_python.LanguageTool('en-US')

tool = load_tool()

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
GOOGLE FONT
========================================================= */

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

/* =========================================================
BACKGROUND
========================================================= */

.stApp {
    background: #050505;
    overflow: hidden;
}

.stApp::before,
.stApp::after {
    content: '';
    position: fixed;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    filter: blur(120px);
    z-index: -1;
    animation: float 20s infinite alternate ease-in-out;
}

.stApp::before {
    background: radial-gradient(circle, rgba(139,92,246,0.25) 0%, rgba(0,0,0,0) 70%);
    top: -100px;
    left: -100px;
}

.stApp::after {
    background: radial-gradient(circle, rgba(6,182,212,0.25) 0%, rgba(0,0,0,0) 70%);
    bottom: -100px;
    right: -100px;
    animation-delay: -10s;
}

@keyframes float {
    0% {
        transform: translate(0,0) scale(1);
    }
    50% {
        transform: translate(100px,100px) scale(1.1);
    }
    100% {
        transform: translate(-50px,150px) scale(0.9);
    }
}

/* =========================================================
HIDE STREAMLIT
========================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* =========================================================
MAIN CONTAINER
========================================================= */

.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 1000px;
}

/* =========================================================
GLASS EFFECT
========================================================= */

.glass {
    background: rgba(20,20,25,0.4);
    border: 1px solid rgba(255,255,255,0.05);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 40px;
    box-shadow:
        0 20px 40px rgba(0,0,0,0.4),
        inset 0 0 0 1px rgba(255,255,255,0.05);
}

/* =========================================================
TITLE
========================================================= */

.main-title {
    text-align: center;
    font-size: 4.5rem;
    font-weight: 800;
    background: linear-gradient(to right, #a855f7, #06b6d4, #a855f7);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
    animation: gradientFlow 5s linear infinite;
}

@keyframes gradientFlow {
    to {
        background-position: 200% center;
    }
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1.2rem;
    margin-bottom: 40px;
}

/* =========================================================
TEXT AREA
========================================================= */

.stTextArea textarea {
    background: rgba(10,10,15,0.6) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 16px !important;
    color: #f8fafc !important;
    font-size: 1.1rem !important;
    padding: 20px !important;
    min-height: 220px !important;
}

.stTextArea textarea:focus {
    border-color: #8b5cf6 !important;
    box-shadow:
        0 0 0 4px rgba(139,92,246,0.1) !important;
}

/* =========================================================
BUTTON
========================================================= */

.stButton button {
    width: 100%;
    height: 56px;
    border: none;
    border-radius: 16px;
    background: linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%);
    color: white;
    font-size: 1.1rem;
    font-weight: 600;
    transition: 0.3s;
    box-shadow: 0 4px 15px rgba(139,92,246,0.3);
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(139,92,246,0.5);
}

/* =========================================================
METRIC CARD
========================================================= */

.metric-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 24px;
    text-align: center;
}

.metric-title {
    color: #94a3b8;
    font-size: 0.9rem;
}

.metric-value {
    font-size: 2rem;
    font-weight: 700;
    color: white;
}

/* =========================================================
RESULT BOX
========================================================= */

.result-box {
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.2);
    border-radius: 16px;
    padding: 20px;
    margin-top: 24px;
    color: #34d399;
    font-size: 1.2rem;
    text-align: center;
}

/* =========================================================
CORRECTED BOX
========================================================= */

.corrected-box {
    background: rgba(30,41,59,0.5);
    border-left: 4px solid #10b981;
    padding: 24px;
    border-radius: 16px;
    margin-top: 20px;
    font-size: 1.1rem;
    line-height: 1.8;
    color: #f1f5f9;
}

/* =========================================================
ERROR CARD
========================================================= */

.error-card {
    background: rgba(239,68,68,0.05);
    border-left: 4px solid #ef4444;
    border-radius: 12px;
    padding: 16px;
    margin-top: 16px;
    color: #fca5a5;
}

/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background-color: #0a0a0f;
}

[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

/* =========================================================
FOOTER
========================================================= */

.footer {
    text-align: center;
    margin-top: 40px;
    color: #64748b;
    font-size: 0.9rem;
}

/* =========================================================
RESPONSIVE
========================================================= */

@media (max-width: 768px) {

    .main-title {
        font-size: 2.5rem;
    }

    .glass {
        padding: 20px;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("✨ GrammarGenius AI")

    st.markdown("---")

    st.markdown("## 🤖 About")

    st.write("""
    AI-powered writing assistant using NLP.

    Features:
    - Grammar correction
    - Spelling correction
    - Punctuation fixing
    - Writing enhancement
    """)

    st.markdown("---")

    st.markdown("## 🚀 Technologies")

    st.write("""
    ✅ Streamlit  
    ✅ Python  
    ✅ NLP  
    ✅ LanguageTool  
    """)

    st.markdown("---")

    st.success("✨ Smart Writing Assistant")

# =========================================================
# MAIN CONTAINER
# =========================================================

st.markdown("<div class='glass'>", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.markdown("""
<div class='main-title'>
✨ GrammarGenius AI
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Fix grammar, spelling, punctuation and improve writing instantly using AI
</div>
""", unsafe_allow_html=True)

# =========================================================
# METRIC CARDS
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class='metric-card'>
        <div class='metric-title'>Grammar Engine</div>
        <div class='metric-value'>🧠 NLP</div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='metric-card'>
        <div class='metric-title'>Correction Type</div>
        <div class='metric-value'>✨ AI</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =========================================================
# EXAMPLE BUTTONS
# =========================================================

col1, col2 = st.columns(2)

with col1:

    if st.button("❌ Try Incorrect Example"):

        st.session_state.example = (
            "He go to school everyday and dont likes homework."
        )

with col2:

    if st.button("✅ Try Correct Example"):

        st.session_state.example = (
            "He goes to school every day and doesn't like homework."
        )

default_text = ""

if "example" in st.session_state:
    default_text = st.session_state.example

# =========================================================
# TEXT AREA
# =========================================================

input_text = st.text_area(
    "✍️ Enter your text",
    value=default_text,
    height=220,
    placeholder="Type or paste your paragraph here..."
)

# =========================================================
# STATS
# =========================================================

word_count = len(input_text.split())
char_count = len(input_text)

col1, col2 = st.columns(2)

with col1:
    st.info(f"📝 Words: {word_count}")

with col2:
    st.info(f"🔠 Characters: {char_count}")

st.write("")

# =========================================================
# CHECK BUTTON
# =========================================================

if st.button("🚀 Check Grammar"):

    if input_text.strip() == "":

        st.warning("Please enter some text.")

    else:

        with st.spinner("🤖 AI is analyzing your text..."):

            time.sleep(1)

            try:

                # Grammar Check
                matches = tool.check(input_text)

                # Correct Text
                corrected_text = language_tool_python.utils.correct(
                    input_text,
                    matches
                )

                # =================================================
                # RESULT
                # =================================================

                st.markdown("""
                <div class='result-box'>
                ✨ AI Analysis Completed Successfully
                </div>
                """, unsafe_allow_html=True)

                # =================================================
                # CORRECTED TEXT
                # =================================================

                st.markdown(f"""
                <div class='corrected-box'>

                <b>✅ Corrected Text</b>

                <br><br>

                {corrected_text}

                </div>
                """, unsafe_allow_html=True)

                # =================================================
                # DETECTED ISSUES
                # =================================================

                if len(matches) > 0:

                    st.write("## ⚠️ Detected Issues")

                    for match in matches[:10]:

                        wrong_text = input_text[
                            match.offset:
                            match.offset + match.errorLength
                        ]

                        suggestions = ", ".join(
                            match.replacements[:5]
                        )

                        st.markdown(f"""
                        <div class='error-card'>

                        <b>❌ Wrong Text:</b> {wrong_text}

                        <br><br>

                        <b>⚠️ Issue:</b> {match.message}

                        <br><br>

                        <b>✅ Suggestions:</b> {suggestions}

                        </div>
                        """, unsafe_allow_html=True)

                else:

                    st.success("🎉 No grammar mistakes found.")

            except Exception as e:

                st.error(f"Error: {e}")

# =========================================================
# CLOSE CONTAINER
# =========================================================

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class='footer'>
Built with ❤️ using Streamlit & NLP
</div>
""", unsafe_allow_html=True)