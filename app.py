import streamlit as st
import google.generativeai as genai
import random


api_key = "AIzaSyC7fuV17plvn7-CRulU1p1DRH8K7O059TI"
genai.configure(api_key=api_key)


def get_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)



def recipe_generation(user_input, word_count):
    st.write("### Generating your recipe...")
    st.write(f"While I work on creating your blog, here's a little joke to keep you entertained:\n\n*{get_joke()}*")

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Write a detailed recipe about {user_input} in {word_count} words.")
        st.success("Your recipe is ready!")
        return response.text
    except Exception as e:
        st.error(f"Error generating recipe: {e}")
        return None



st.title("Flavour Fusion: AI-Driven Recipe Blogging")
st.write("### Hello! Let's create a fantastic recipe together!")

user_input = st.text_input("Enter Recipe Topic", placeholder="E.g., Vegan Chocolate Cake")
word_count = st.number_input("Enter Word Count", min_value=100, max_value=2000, step=50)

if st.button("Generate Recipe"):
    if user_input and word_count:
        blog_content = recipe_generation(user_input, word_count)
        if blog_content:
            st.write("## Generated Recipe")
            st.write(blog_content)
    else:
        st.warning("Please enter both a recipe topic and word count.")
