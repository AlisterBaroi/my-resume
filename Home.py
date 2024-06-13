import streamlit as st



def main():
  st.set_page_config(
    page_title="Alister Animesh Baroi - Resume", page_icon=":page_facing_up:", layout="centered"
)

  # Load css file
  with open("./styles/main.css", "rb") as s:
    st.markdown("<style>{}</style>".format(s.read()), unsafe_allow_html=True)

  row0 = st.columns([2,4], gap="small")

  with row0[0]:
     st.image("./assets/profile-pic (1).png", width=220)
     
  with row0[1]:
    st.header("Alister Animesh Baroi", anchor=False)
    st.write("Cloud Architect, DevOps Engineer, AI Engineer, Backend Engineer.")
    with open("./assets/Alister_Baroi_Resume.pdf", "rb") as file:
      st.download_button(":page_facing_up: Download Resume", type="primary", data=file, file_name="Alister_Baroi_Resume.pdf", mime="application/pdf")



    # row1 = st.columns([0.8, 1, 1.05, 0.9])
    row1 = st.columns([1, 1, 1])
    row1[0].link_button(":orange[@ Email]", url="mailto:alister.baroi@gmail.com", help="alister.baroi@gmail.com", use_container_width=True)
    # row1[1].link_button(":red[:globe_with_meridians: Website]", url="https://alisterbaroi.streamlit.io", help="alisterbaroi.streamlit.io", use_container_width=True)
    row1[1].link_button(":blue-background[in] :blue[LinkedIn]", url="https://www.linkedin.com/in/alisterbaroi", help="linkedin.com/in/alisterbaroi", use_container_width=True)
    row1[2].link_button(":computer: :green[GitHub]", url="https://github.com/alisterbaroi", help="github.com/alisterbaroi", use_container_width=True)
  st.divider()

  st.subheader("Summary", anchor=False)
  st.markdown(""" 
- 3+ years experience,
- 👔 Lead Cloud Architect (current job),
- 🏆 Computer Science (Honours) graduate from Taylors University (Malaysia),
  - 🔥 Majored in AI & minored in FinTech,
""")
  st.subheader("Skills", anchor=False)
#   st.markdown(""" 
# - 3+ years experience,
# - 👔 Lead Cloud Architect (current job),
# - 🏆 Computer Science (Honours) graduate from Taylors University (Malaysia),
#   - 🔥 Majored in AI & minored in FinTech, 
# """)
  st.multiselect(
    "Programming Languages",
    ["Python", "JavaScript", "Git", "YAML", "SQL", "PHP",  "C++", "Java", "Bash", "PowerShell", "HTML", "CSS"],
    ["Python", "JavaScript", "Git", "YAML", "SQL", "PHP",  "C++", "Java", "Bash", "PowerShell", "HTML", "CSS"], disabled=False, label_visibility="visible")
  
  st.multiselect(
    "Frameworks & Libraries",
    ["FastAPI", "Streamlit", "Docker", "Next.js", "Django", "Keras", "Seaborn", "Anaconda", "TensoFlow", "Scikit-learn", "Matplotlib", "React Native"],
    ["FastAPI", "Streamlit", "Docker", "Next.js", "Django", "Keras", "Seaborn", "Anaconda", "TensoFlow", "Scikit-learn", "Matplotlib", "React Native"], disabled=False, label_visibility="visible")
  
  st.multiselect(
    "Platforms & Tools",
    ["Google Cloud", "GitHub Actions", "Docker", "Linux", "Figma", "MySQL", "PostgreSQL", "Google Colab", "Jupyter Notebooks"],
    ["Google Cloud", "GitHub Actions", "Docker", "Linux", "Figma", "MySQL", "PostgreSQL", "Google Colab", "Jupyter Notebooks"], disabled=False, label_visibility="visible")

  st.multiselect(
    "Technology Concepts",
    ["Microservices", "DevOps", "CI/CD", "AI", "Data Anaalysis", "Data Science", "Machine Learning", "Software Architecture", "Frontend", "Backend"],
    ["Microservices", "DevOps", "CI/CD", "AI", "Data Anaalysis", "Data Science", "Machine Learning", "Software Architecture", "Frontend", "Backend"], disabled=False, label_visibility="visible")







if __name__ == "__main__":
    main()
