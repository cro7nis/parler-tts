import streamlit as st
from PIL import Image
from loguru import logger
from tts import ParlerTTS
from dynaconf import Dynaconf

st.set_page_config(page_title="TTS", page_icon=':speaking_head_in_silhouette:', layout="wide")

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['configs/settings.yaml'],
    environments=True,
    load_dotenv=True,
)


@st.cache_resource
def init_model():
    parler = ParlerTTS(**settings.tts)
    return parler


def main(parler):
    st.write("# Text-to-Speech with Parler-TTS :speaking_head_in_silhouette:")

    img = Image.open('assets/akash.png')
    st.image(img, width=200)
    st.markdown(
        "###### Made with :heart: by [@cro7nis](https://twitter.com/cro7nis)",
        unsafe_allow_html=True)

    st.write(
        "The code is open source and available "
        "on [GitHub](https://github.com/cro7nis/parler-tts.git). "
        "Special thanks to the [parler-tts library](https://github.com/huggingface/parler-tts) :grin:"
    )

    st.write("Please add an input text for speech conversion and provide a description of the speaker")

    input_text = st.text_input("Input text:",
                               value="Hey, how are you doing today?")

    description = st.text_input("Description:",
                                value="A female speaker with a slightly low-pitched voice delivers her words quite"
                                      " expressively, in a very confined sounding environment with clear audio quality.")

    button = st.button("Generate Audio")
    if button:
        if input_text and description:
            try:
                with st.spinner('Generating'):
                    audio_array = tts.generate(input_text, description)
                    st.audio(audio_array, sample_rate=tts.sampling_rate)
            except Exception as e:
                logger.error(e)
                st.error("Something went wrong. Please try again")
        else:
            st.error("Please insert a youtube link")


if __name__ == "__main__":
    tts = init_model()
    main(tts)
