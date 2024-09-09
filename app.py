import os
from lyzr_agent import LyzrAgent
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LYZR_API_KEY = os.getenv("LYZR_API_KEY")
AGENT_ID = os.getenv("AGENT_ID")

# Streamlit page configuration
st.set_page_config(
    page_title="WebSite to Sales EMail Generator",
    layout="wide",  # Set the layout to wide for better use of space
    initial_sidebar_state="expanded",
    page_icon="lyzr-logo-cut.png",
)

# Display Lyzr logo
image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# Set up layout with columns
col1, col2 = st.columns([1, 1])

# Title
st.markdown("## 🚀 WebSite to Sales EMail Generator")

# Sidebar for inputs
with st.sidebar:
    st.markdown("### Input Information")
    website_url = st.text_input("🌐 Enter Website URL")
    product_description = st.text_area("🛍️ Enter Product Description", height=150)

    # Choose tone of email
    email_tone = st.selectbox("🎯 Choose Email Tone", ["Formal", "Casual", "Humorous", "Persuasive"])

    # Add a slider for length preference
    email_length = st.slider("📝 Preferred Email Length (Words)", 50, 300, 150)

    # Generate button
    generate_button = st.button("Generate")

if generate_button:
    if website_url and product_description:
        with st.spinner("🕵🏼‍ Scraping website..."):
            # Initialize the LyzrAgent
            Agent = LyzrAgent(api_key=LYZR_API_KEY, llm_api_key=OPENAI_API_KEY)
            with st.spinner("⚙️ Executing Your Tasks..."):
                response = Agent.send_message(
                    agent_id=AGENT_ID,
                    user_id="7422",
                    session_id="IITV",
                    message=f"Scrape this Website: {website_url} and write a {email_tone} sales email for our product: {product_description}."
                )
                st.markdown("🤯 Website Scraping Completed")
                st.markdown("✅ Task Completed")

                st.markdown("### ✉️ Generated Sales Email")
                st.markdown(f"{response['response']}")

    else:
        st.warning("Please provide the website URL and product description.")

# Optional footer
st.sidebar.markdown("---")
st.sidebar.markdown("Powered by **Lyzr** and **OpenAI**")
