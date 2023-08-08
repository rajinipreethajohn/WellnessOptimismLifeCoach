
import streamlit as st
import replicate
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Import API key from your file

os.environ["REPLICATE_API_TOKEN"] = api_key

# Streamlit app
def main():
    st.title("Optimism Coach")

    # User input prompt
    prompt_input = st.text_area("Enter your question:", "How can I be more optimistic in life?")

    if st.button("Generate Response"):
        # Define pre_prompt
        pre_prompt = "You are a helpful, respectful and honest wellness and life 'Coach'. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.."
        # Generate LLM response
        output = replicate.run("replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
                               input={"prompt": f"{pre_prompt} {prompt_input} Coach: ",
                                      "temperature": 0.1, "top_p": 0.9, "max_length": 128, "repetition_penalty": 1})

        full_response = ""
        for item in output:
            full_response += item

        st.subheader("Generated Response:")
        st.write(full_response)

if __name__ == "__main__":
    main()