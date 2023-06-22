import streamlit as st
import openai

# Set up OpenAI API
openai.api_key = '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'

# Title and description
st.title('Content Generator')
st.markdown('Enter up to 50 words to generate content.')

# Input form
input_text = st.text_area('Input text:', max_chars=50, height=100)

# Generate button
if st.button('Generate'):
    if input_text:
        with st.spinner('Generating...'):
            # Generate content using ChatGPT
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=input_text,
                max_tokens=300,
                temperature=0.7,
                n=1,
                stop=None
            )
            
            generated_content = response.choices[0].text.strip()
            
            # Display generated content
            st.subheader('Generated Content')
            st.write(generated_content)
    else:
        st.warning('Please enter some input text.')
