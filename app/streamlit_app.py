import streamlit as st

from password_generator import (
    MemorablePasswordGenerator,
    PinGenerator,
    RandomPasswordGenerator,
)


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Password Generator",
    page_icon="🔐",
    layout="centered",
)


# --------------------------------------------------
# Custom Styling
# --------------------------------------------------

st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        .subtitle {
            text-align: center;
            color: #777;
            margin-bottom: 2rem;
        }

        .password-box {
            padding: 1.2rem;
            border-radius: 12px;
            border: 1px solid rgba(128, 128, 128, 0.3);
            text-align: center;
            font-size: 1.5rem;
            font-family: monospace;
            word-break: break-all;
            margin: 1rem 0;
        }

        .info-box {
            padding: 1rem;
            border-radius: 10px;
            background: rgba(128, 128, 128, 0.08);
            margin-top: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🔐 Password Generator</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="subtitle">
        Generate secure PINs, random passwords, and memorable passwords.
    </div>
    """,
    unsafe_allow_html=True,
)


st.divider()


# --------------------------------------------------
# Generator Type
# --------------------------------------------------

st.subheader("⚙️ Generator")

generator_type = st.selectbox(
    "Choose password type",
    [
        "Random Password",
        "PIN",
        "Memorable Password",
    ],
)


# --------------------------------------------------
# Random Password
# --------------------------------------------------

if generator_type == "Random Password":

    st.subheader("🔀 Random Password Settings")

    length = st.slider(
        "Password length",
        min_value=4,
        max_value=128,
        value=16,
        step=1,
    )

    col1, col2 = st.columns(2)

    with col1:
        include_numbers = st.checkbox(
            "Include numbers",
            value=True,
        )

    with col2:
        include_symbols = st.checkbox(
            "Include symbols",
            value=True,
        )

    st.markdown(
        """
        <div class="info-box">
        💡 Random passwords are generated using a cryptographically
        secure random source.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "🚀 Generate Password",
        use_container_width=True,
    ):

        generator = RandomPasswordGenerator(
            length=length,
            include_numbers=include_numbers,
            include_symbols=include_symbols,
        )

        st.session_state.generated_password = (
            generator.generate()
        )


# --------------------------------------------------
# PIN
# --------------------------------------------------

elif generator_type == "PIN":

    st.subheader("🔢 PIN Settings")

    length = st.slider(
        "PIN length",
        min_value=4,
        max_value=32,
        value=6,
        step=1,
    )

    st.info(
        "A PIN contains digits only."
    )

    if st.button(
        "🚀 Generate PIN",
        use_container_width=True,
    ):

        generator = PinGenerator(
            length=length,
        )

        st.session_state.generated_password = (
            generator.generate()
        )


# --------------------------------------------------
# Memorable Password
# --------------------------------------------------

elif generator_type == "Memorable Password":

    st.subheader("🧠 Memorable Password Settings")

    number_of_words = st.slider(
        "Number of words",
        min_value=2,
        max_value=10,
        value=4,
        step=1,
    )

    separator = st.text_input(
        "Separator",
        value="-",
        max_chars=5,
    )

    capitalization = st.toggle(
        "Capitalize words",
        value=False,
    )
    
    easy = st.toggle(
        "Use hard words",
        value=True,
    )

    st.markdown(
        """
        <div class="info-box">
        💡 Memorable passwords combine several random words,
        making them easier to remember.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "🚀 Generate Memorable Password",
        use_container_width=True,
    ):

        generator = MemorablePasswordGenerator(
            num_of_words=number_of_words,
            separator=separator,
            capitalization=capitalization,
            easy=easy
        )

        st.session_state.generated_password = (
            generator.generate()
        )


# --------------------------------------------------
# Generated Password
# --------------------------------------------------

if st.session_state.generated_password:

    st.divider()

    st.subheader("✨ Generated Password")

    st.markdown(
        f"""
        <div class="password-box">
            {st.session_state.generated_password}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.code(
        st.session_state.generated_password,
        language=None,
    )

    st.caption(
        "Copy the password from the box above."
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "🔐 Password Generator • Built with Python & Streamlit"
)