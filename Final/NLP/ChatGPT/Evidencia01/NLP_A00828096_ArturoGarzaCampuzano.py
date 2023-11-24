# This work is property of Arturo Garza Campuzano, A00828096

# Make sure to install the dependencies needed in this file before running it
import streamlit as st
import openai
import whisper
import os
import tempfile

# Set OpenAI API key
openai.api_key = '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'
model = whisper.load_model("base")

def transcribe_audio(model, file_path):
    transcript = model.transcribe(file_path)
    return transcript['text']

def save_uploaded_file(uploaded_file):
    # Save the uploaded file to a temporary location
    _, temp_file_path = tempfile.mkstemp(suffix=".m4a")
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(uploaded_file.read())
    return temp_file_path

def CustomChatGPT(user_input):
    messages = [{"role": "system", "content": "You are an office administrator, summarize the text in key points"}]
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    return ChatGPT_reply

# Streamlit app styling
st.set_page_config(
    page_title="Audio Transcription and Summarization App",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    # App title and description
    st.title("Audio Transcription and Summarization App")
    st.write("Upload an audio file, and let's transcribe and summarize it!")

    # Upload audio file
    audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"])

    if audio_file:
        # Save the uploaded file to a temporary location
        file_path = save_uploaded_file(audio_file)

        # Transcribe audio
        st.subheader("Transcription:")
        transcription = transcribe_audio(model, file_path)
        st.write(transcription)

        # Summarize using ChatGPT
        st.subheader("Summary:")
        summary = CustomChatGPT(transcription)
        st.write(summary)

        # Clean up: Delete the temporary file
        os.remove(file_path)

if __name__ == "__main__":
    main()
