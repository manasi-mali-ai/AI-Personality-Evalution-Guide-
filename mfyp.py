# -*- coding: utf-8 -*-
"""MFYP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12FWmxupgghHqzdCw7baBvbkwcXwrBkgX
"""

!pip install openai streamlit

import streamlit as st
import openai

# Set OpenAI API Key (Replace 'YOUR_API_KEY' with your actual API key)
openai.api_key = "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"

# Define chatbot personalities
PERSONALITIES = {
    "Friendly": "You are a friendly and cheerful chatbot. You always greet users warmly and give positive responses.",
    "Professional": "You are a professional and knowledgeable chatbot. Your responses are clear, concise, and informative.",
    "Humorous": "You are a funny and witty chatbot. You always add humor to your responses and make users laugh."
}

# Streamlit UI
st.title("🧠 AI Chatbot with Evolving Personality")
st.sidebar.header("Select Personality")
selected_personality = st.sidebar.radio("Choose a chatbot personality:", list(PERSONALITIES.keys()))

# Initialize session state for memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    # Prepare prompt with selected personality
    personality_prompt = PERSONALITIES[selected_personality]
    conversation = "\n".join(st.session_state.chat_history)

    prompt = f"{personality_prompt}\n\nPrevious conversation:\n{conversation}\nUser: {user_input}\nAI:"

    # Call OpenAI GPT API
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": personality_prompt}, {"role": "user", "content": user_input}],
        max_tokens=100
    )

    bot_reply = response["choices"][0]["message"]["content"]

    # Store in chat history (short-term memory)
    st.session_state.chat_history.append(f"User: {user_input}")
    st.session_state.chat_history.append(f"AI: {bot_reply}")

    # Limit history to last 5 exchanges (for short-term memory)
    if len(st.session_state.chat_history) > 10:
        st.session_state.chat_history = st.session_state.chat_history[-10:]

    # Display chat
    st.write(f"**AI ({selected_personality}):** {bot_reply}")

# Display previous chat history
st.sidebar.subheader("Chat Memory (Recent)")
for line in st.session_state.chat_history[-6:]:
    st.sidebar.text(line)

