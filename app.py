import requests
import streamlit as st
import typing
from typing_extensions import Literal
from typing import Literal
from streamlit_lottie import st_lottie
import json
from PIL import Image


# Find more emocjis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="georgios_orfanidis", page_icon="random:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
with open("animation_datascience.json", "r") as f:
    lottie_coding = json.load(f)
#img_contact_form = Image.open("images/yt_contact_form.png")
#img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    image = Image.open('me.png')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.title("Georgios Orfanidis")
    with col3:
        st.image(image, caption='', width=200)
    #st.subheader("CV")

    st.write(
        """
        As a dedicated mathematician with a profound passion for Quantitative Risk Analysis and Data Science,
         I bring a dynamic blend of analytical prowess and innovation to the table. My professional journey 
         has been driven by a relentless curiosity for unraveling complex problems and translating data into 
         actionable insights. In addition to my work in the field, I invest my free time backtesting various 
         investment strategies and leveraging the power of Python to automate processes. With a strong 
         foundation in mathematics and a commitment to continuous learning, I am poised to contribute my 
         expertise to challenging projects and further advance the realm of data-driven decision-making.
        """
    )
    st.write("[Learn more about my projects >](https://github.com/georgosqlab)")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I can  do:")
        st.write("##")
        st.write(
            """
            By leveraging the computer power of languages like Python, I can assist companies or 
            individuals with:
            - Quantitative Risk Analysis: Offering data-driven risk assessments and modeling to enhance decision-making 
            and mitigate potential financial pitfalls.
            - Data Science Solutions: Providing data analysis, predictive modeling, and actionable insights to help 
            businesses harness the full potential of their data.
            - Investment Strategy Optimization: Backtesting and fine-tuning investment strategies, optimizing 
            portfolios, and identifying opportunities for maximizing returns while minimizing risks.
            - Process Automation: Streamlining workflows and automating repetitive tasks, improving efficiency and 
            freeing up valuable time and resources.
            - Machine Learning Applications: Building machine learning models for predictive analytics, 
            natural language processing, image recognition, and more.

            If this rings a bell to you, feel free to get in touch with me.
            """
        )
        st.write("[LinkedIn profile >](https://www.linkedin.com/in/georgios-orfanidis-aa797a10a/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# ---- CONTACT ----
with st.container():
    st.write("---")
    #st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/georgeorfa90@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()