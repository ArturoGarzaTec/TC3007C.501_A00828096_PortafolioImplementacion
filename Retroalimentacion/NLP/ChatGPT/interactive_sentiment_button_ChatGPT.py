import streamlit as st
import openai

openai.api_key = "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"


st.title("Sentiment Analyzer Based On Text Analysis ")
st.subheader("Paras Patidar - MLAIT")
st.write('\n\n')

sentence = st.text_input("Enter a Sentence","Write Here...")
prompt = "Tell me if this sentence is positive, negative or neutral: " + sentence


if st.button('Predict Sentiment'):
	response = openai.Completion.create(engine="text-davinci-003",
                                                prompt=prompt,
                                                max_tokens=256,
                                                temperature=0,
                                                top_p=1.0,
                                                frequency_penalty=0.0,
                                                presence_penalty=0.0)
	st.write("Sentiment: " + response["choices"][0]["text"])
else:
	st.write("Press the above button..")

