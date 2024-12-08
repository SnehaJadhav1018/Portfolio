import streamlit as st
from PIL import Image

# Portfolio Data
portfolio = {
    "name": "Sneha Tukaram Jadhav",
    "about": "Aspiring Data Scientist passionate about leveraging technology to solve real-world problems.",
    "skills": ["Data Science","Data Analytics","Python", "Machine Learning", "SQL", "Data Visualization", "Networking"],
    "projects": [
        {
            "title": "IoT-Based Women's Safety System",
            "description": "Developed an IoT system for women's safety with real-time location tracking.",
            "technologies": ["Raspberry Pi", "GPS Module", "Python"],
            "link": "https://github.com/username/iot-safety-system"
        },
        {
            "title": "House Price Prediction",
            "description": "Implemented a machine learning model to predict house prices based on multiple features.",
            "technologies": ["Python", "scikit-learn", "pandas"],
            "link": "https://github.com/username/house-price-prediction"
        },
    ],
    "education": "B.E. in Computer Engineering- Ajinkya D.Y. patil School of Engineering,Lohegaon,Pune(2024)",
    "contact": {
        "Email": "Sneha3020jadhav@gmail.com",
        "LinkedIn": "https://linkedin.com/in/snehajadhav",
        "GitHub": "https://github.com/username",
    },
    "resume": "Sneha Jadhav Resume new.pdf",  # Path to your resume
}

# Streamlit App
st.set_page_config(page_title=f"{portfolio['name']}'s Portfolio", layout="wide")

# Profile Picture (Optional)
st.sidebar.image("WB img.jpg", caption=portfolio["name"], width=150)  # Replace with your profile picture
st.sidebar.write(f"### {portfolio['name']}")
st.sidebar.write(portfolio["about"])

# Tabs for Organization
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "💡 Skills", "📂 Projects", "🎓 Education & Contact"])

# Home Tab
with tab1:
    st.header("Welcome!")
    st.write(portfolio["about"])
    st.write("### 📥 Download My Resume")
    with open(portfolio["resume"], "rb") as f:
        st.download_button(
            label="Download Resume",
            data=f,
            file_name="Sneha Jadhav Resume new.pdf",
            mime="application/pdf",
        )

# Skills Tab
with tab2:
    st.header("My Skills")
    selected_skill = st.selectbox("Select a skill to learn more:", portfolio["skills"])
    st.write(f"### {selected_skill}")
    st.write(f"I have hands-on experience in {selected_skill}. It has been crucial in several projects.")

# Projects Tab
with tab3:
    st.header("My Projects")
    for project in portfolio["projects"]:
        with st.expander(f"📌 {project['title']}"):
            st.write(project["description"])
            st.write(f"**Technologies Used:** {', '.join(project['technologies'])}")
            st.write(f"[View Project on GitHub]({project['link']})")

# Education & Contact Tab
with tab4:
    st.header("Education")
    st.write(portfolio["education"])

    st.header("Contact")
    st.write(f"- 📧 **Email:** [Send Email](mailto:{portfolio['contact']['Email']})")
    st.write(f"- 🌐 **LinkedIn:** [Visit LinkedIn](https://linkedin.com/in/johndoe)")
    st.write(f"- 🐙 **GitHub:** [Visit GitHub](https://github.com/username)")

# Interactive Section: Upload Profile Picture
st.sidebar.write("---")
st.sidebar.write("Sneha Jadhav")
uploaded_file = st.sidebar.file_uploader("WB img.jpg", type=["jpg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.sidebar.image(image, caption="Uploaded Profile Picture", use_column_width=True)
