import streamlit as st

from gemini_client import ask_gemini
from openai_client import ask_openai
from evaluator import ai_evaluate


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Dual-LLM AI Assistant",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* Global */
    .stApp {
        background: #0b0f19;
        color: #f5f7fa;
    }

    .main {
        padding: 2rem 3rem 3rem 3rem;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #1f2937;
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #f9fafb;
    }

    /* Main heading */
    .hero-title {
        font-size: 42px;
        font-weight: 700;
        letter-spacing: -1.5px;
        margin-bottom: 8px;
        color: #ffffff;
    }

    .hero-subtitle {
        font-size: 16px;
        color: #9ca3af;
        max-width: 720px;
        line-height: 1.6;
        margin-bottom: 30px;
    }

    /* Section titles */
    .section-title {
        font-size: 18px;
        font-weight: 600;
        color: #f3f4f6;
        margin: 20px 0 12px 0;
    }

    /* Cards */
    .info-card {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 18px;
    }

    .card-title {
        font-size: 14px;
        color: #9ca3af;
        margin-bottom: 8px;
    }

    .card-value {
        font-size: 24px;
        font-weight: 600;
        color: #ffffff;
    }

    /* Response container */
    .response-container {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 14px;
        padding: 24px;
        margin-top: 10px;
        line-height: 1.7;
        color: #e5e7eb;
    }

    /* Model labels */
    .model-label {
        font-size: 16px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 10px;
    }

    /* Text area */
    textarea {
        background-color: #111827 !important;
        color: #ffffff !important;
        border: 1px solid #374151 !important;
        border-radius: 12px !important;
    }

    textarea:focus {
        border: 1px solid #6b7280 !important;
        box-shadow: none !important;
    }

    /* Select box */
    div[data-baseweb="select"] > div {
        background-color: #111827;
        border: 1px solid #374151;
        border-radius: 10px;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 48px;
        border-radius: 10px;
        border: 1px solid #374151;
        background: #ffffff;
        color: #111827;
        font-weight: 600;
        font-size: 15px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #e5e7eb;
        border-color: #6b7280;
    }

    /* Divider */
    hr {
        border-color: #1f2937;
    }

    /* Sidebar text */
    .sidebar-description {
        color: #9ca3af;
        font-size: 13px;
        line-height: 1.6;
    }

    .feature-item {
        color: #d1d5db;
        font-size: 13px;
        padding: 5px 0;
    }

    /* Status */
    .status {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 20px;
        background: #172554;
        color: #93c5fd;
        font-size: 12px;
        font-weight: 500;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 12px;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #1f2937;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div style="font-size:22px;font-weight:700;color:#ffffff;">
            Dual-LLM
        </div>

        <div class="sidebar-description">
            Multi-model AI assistant for generating,
            comparing and evaluating responses.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### Model Configuration")

    model = st.selectbox(
        "AI Mode",
        [
            "Gemini",
            "ChatGPT",
            "Compare Both"
        ]
    )

    st.divider()

    st.markdown("### System")

    st.markdown(
        '<span class="status">Application Ready</span>',
        unsafe_allow_html=True
    )

    st.markdown("")

    st.markdown(
        """
        <div class="feature-item">Gemini integration</div>
        <div class="feature-item">ChatGPT integration</div>
        <div class="feature-item">Multi-model comparison</div>
        <div class="feature-item">AI response evaluation</div>
        <div class="feature-item">Fallback handling</div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <div class="sidebar-description">
            Built with Python, Streamlit and modern
            large language model APIs.
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="hero-title">Dual-LLM AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-subtitle">
        A multi-model AI workspace that allows you to interact
        with different language models, compare their responses,
        and evaluate response quality.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Ask your question</div>',
    unsafe_allow_html=True
)

prompt = st.text_area(
    "Question",
    placeholder=(
        "Ask a technical question, request an explanation, "
        "generate code, or explore an idea..."
    ),
    height=160,
    label_visibility="collapsed"
)

st.markdown("")

ask_button = st.button(
    "Generate Response",
    use_container_width=True
)


# --------------------------------------------------
# GEMINI MODE
# --------------------------------------------------

if ask_button and prompt.strip() and model == "Gemini":

    with st.spinner("Generating response..."):

        try:

            response = ask_gemini(prompt)

            st.markdown(
                '<div class="section-title">Gemini Response</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="response-container">{response}</div>',
                unsafe_allow_html=True
            )

        except Exception as error:

            st.error(
                f"Gemini request failed: {error}"
            )


# --------------------------------------------------
# CHATGPT MODE
# --------------------------------------------------

elif ask_button and prompt.strip() and model == "ChatGPT":

    with st.spinner("Generating response..."):

        try:

            response = ask_openai(prompt)

            st.markdown(
                '<div class="section-title">ChatGPT Response</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="response-container">{response}</div>',
                unsafe_allow_html=True
            )

        except Exception as error:

            st.error(
                f"ChatGPT request failed: {error}"
            )


# --------------------------------------------------
# COMPARE BOTH
# --------------------------------------------------

elif ask_button and prompt.strip() and model == "Compare Both":

    st.markdown(
        '<div class="section-title">Model Comparison</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    gemini_response = None
    chatgpt_response = None

    # Gemini
    with col1:

        st.markdown(
            '<div class="model-label">Gemini</div>',
            unsafe_allow_html=True
        )

        with st.spinner("Gemini is generating..."):

            try:

                gemini_response = ask_gemini(prompt)

                st.markdown(
                    f'<div class="response-container">'
                    f'{gemini_response}'
                    f'</div>',
                    unsafe_allow_html=True
                )

            except Exception as error:

                st.error(
                    f"Gemini request failed: {error}"
                )

    # ChatGPT
    with col2:

        st.markdown(
            '<div class="model-label">ChatGPT</div>',
            unsafe_allow_html=True
        )

        with st.spinner("ChatGPT is generating..."):

            try:

                chatgpt_response = ask_openai(prompt)

                st.markdown(
                    f'<div class="response-container">'
                    f'{chatgpt_response}'
                    f'</div>',
                    unsafe_allow_html=True
                )

            except Exception:

                st.warning(
                    "ChatGPT is currently unavailable."
                )

    # Evaluation
    if gemini_response and chatgpt_response:

        st.divider()

        st.markdown(
            '<div class="section-title">'
            'AI Evaluation'
            '</div>',
            unsafe_allow_html=True
        )

        with st.spinner("Evaluating responses..."):

            try:

                evaluation = ai_evaluate(
                    gemini_response,
                    chatgpt_response
                )

                st.markdown(
                    f'<div class="response-container">'
                    f'{evaluation}'
                    f'</div>',
                    unsafe_allow_html=True
                )

            except Exception as error:

                st.error(
                    f"Evaluation failed: {error}"
                )

    elif gemini_response:

        st.info(
            "Gemini responded successfully, but ChatGPT is "
            "currently unavailable. Both models are required "
            "for response comparison."
        )


# --------------------------------------------------
# EMPTY INPUT
# --------------------------------------------------

elif ask_button:

    st.warning(
        "Please enter a question before generating a response."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Dual-LLM AI Assistant · Multi-model AI experimentation
    </div>
    """,
    unsafe_allow_html=True
)