import streamlit as st



def main():
  st.set_page_config(
    page_title="Alister Animesh Baroi - Resume", page_icon=":page_facing_up:", layout="centered"
)

  # Load css file
  with open("./styles/main.css", "rb") as s:
    st.markdown("<style>{}</style>".format(s.read()), unsafe_allow_html=True)

  row0 = st.columns([2,4], gap="medium")

  # Hero Section
  with row0[0]:
     st.image("./assets/profile-pic (1).png", width=230)
     
  with row0[1]:
    st.header("Alister Animesh Baroi", anchor=False)
    st.write("""
             :blue[Cloud Architect, DevOps Engineer, AI Engineer, Backend Engineer]
             *Driving business success with AI-powered workflows & cloud solutions*
              """)
    with open("./assets/Alister_Baroi_Resume.pdf", "rb") as file:
      st.download_button(":page_facing_up: Download Resume", type="primary", data=file, file_name="Alister_Baroi_Resume.pdf", mime="application/pdf")



    # row1 = st.columns([0.8, 1, 1.05, 0.9])
    row1 = st.columns([1, 1, 1])
    row1[0].link_button(":orange[@ Email]", url="mailto:alister.baroi@gmail.com", help="alister.baroi@gmail.com", use_container_width=True)
    # row1[1].link_button(":red[:globe_with_meridians: Website]", url="https://alisterbaroi.streamlit.io", help="alisterbaroi.streamlit.io", use_container_width=True)
    row1[1].link_button(":blue-background[in] :blue[LinkedIn]", url="https://www.linkedin.com/in/alisterbaroi", help="linkedin.com/in/alisterbaroi", use_container_width=True)
    row1[2].link_button(":computer: :green[GitHub]", url="https://github.com/alisterbaroi", help="github.com/alisterbaroi", use_container_width=True)
  st.divider()

#   # Summary Section
#   st.subheader("Summary", anchor=False)
#   st.markdown(""" 
# - 3+ years experience,
# - 👔 Lead Cloud Architect (current job),
# - 🏆 Computer Science (Honours) graduate from Taylors University (Malaysia),
#   - 🔥 Majored in AI & minored in FinTech,
# """)

  # Skills Section
  st.subheader("Skills", anchor=False)
  with st.expander("Programming Languages"):
    st.multiselect(
      "Programming Languages",
      ["Python", "JavaScript", "Git", "YAML", "HCL", "SQL", "PHP",  "C++", "Java", "Bash", "PowerShell", "HTML", "CSS"],
      ["Python", "JavaScript", "Git", "YAML", "HCL", "SQL", "PHP",  "C++", "Java", "Bash", "PowerShell", "HTML", "CSS"], disabled=False, label_visibility="collapsed")
  
  with st.expander("Frameworks & Libraries"):  
    st.multiselect(
      "Frameworks & Libraries",
      ["FastAPI", "Streamlit", "Docker", "Terraform", "Django", "Seaborn", "Keras", "Next.js", "Anaconda", "TensoFlow", "Scikit-learn", "Matplotlib", "React Native"],
      ["FastAPI", "Streamlit", "Docker", "Terraform", "Django", "Seaborn", "Keras", "Next.js", "Anaconda", "TensoFlow", "Scikit-learn", "Matplotlib", "React Native"], disabled=False, label_visibility="collapsed")
    
  with st.expander("Platforms & Tools"):  
    st.multiselect(
      "Platforms & Tools",
      ["Google Cloud", "GitHub", "GitHub Actions", "Docker", "Linux", "Figma", "MySQL", "PostgreSQL", "Google Colab", "Jupyter Notebooks"],
      ["Google Cloud", "GitHub", "GitHub Actions", "Docker", "Linux", "Figma", "MySQL", "PostgreSQL", "Google Colab", "Jupyter Notebooks"], disabled=False, label_visibility="collapsed")
  
  with st.expander("Technology Concepts"):  
    st.multiselect(
      "Technology Concepts",
      ["Microservices", "DevOps", "CI/CD", "AI", "Backend", "Data Anaalysis", "Data Science", "Machine Learning", "Software Architecture", "Frontend"],
      ["Microservices", "DevOps", "CI/CD", "AI", "Backend", "Data Anaalysis", "Data Science", "Machine Learning", "Software Architecture", "Frontend"], disabled=False, label_visibility="collapsed")

  with st.expander("Soft skills"):
    st.multiselect(
      "List of Soft Skills",
      ["Python", "JavaScript", "Git", "YAML", "SQL", "PHP",  "C++", "Java", "Bash", "PowerShell", "HTML", "CSS"],
      ["Python", "JavaScript", "Git", "YAML", "SQL", "PHP",  "C++", "Java", "Bash", "PowerShell", "HTML", "CSS"], disabled=False, label_visibility="collapsed")
  
  # Experience Section
  st.subheader("Experience", anchor=False)
  with st.expander("Read Global Consultants :gray[(*Oct 2023 - Present*)]"):
    with st.container(border=True):
      jobcol = st.columns([1.5, 1.5, 1]) 
      jobcol[0].write(":blue[Lead Cloud Architect]")
      jobcol[1].write(":grey[London, England, UK (Remote)]")
      jobcol[2].write(":gray[*Mar 2024 - Present*]")
      st.write("""
              - Created AI-driven APIs and systems to streamline the automated workflows which significantly increased company's internal efficiency,
              - Built different backend microservices to connect with Google Cloud to perform variety automations for the company's internal and external operations
              - Designed, implimented, and maintained CI/CD pipelines.
               """)
    with st.container(border=True):
      jobcol = st.columns([1.5, 1.5, 1]) 
      jobcol[0].write(":blue[Solutions Architect]")
      jobcol[1].write(":grey[London, England, UK (Remote)]")
      jobcol[2].write(":grey[*Mar 2024 - Present*]")
      st.write("""
              - Acquired Google Cloud :green[Startup Funding] as Cloud Credits to enable the company to access Google Cloud for two years at no cost,
              - Did R&D on designing, implementing, and overseeing the :green[cloud infrastructure] of the company,
              - Designed, implimented, and maintained CI/CD pipelines.
               """)
  
  with st.expander("Kambyan Network :gray[(*Aug 2022 - Jun 2023*)]"):
    with st.container():
      with st.container(border=True):
        jobcol = st.columns([1.5, 1.5, 1]) 
        jobcol[0].write(":blue[DevOps Engineer]")
        jobcol[1].write(":grey[Petaling Jaya, KL, Malaysia]")
        jobcol[2].write(":grey[*Aug 2022 - Jun 2023*]")
        st.write("""
              - Designed, built and monitored the CI/CD pipeline which reduced the company's code-to-production interval from 1 hour to 4 minutes,
              - Monitored, analyzed, and optimized the cloud infrastructure which resulted in a 65% reduction of the daily cloud operations cost,
              - Designed the microservice architecture, its integration with the cloud, and compliance with the SDLC and Cloud Standards,
              - Designed, implemented, and oversaw the VPC network and the company's cloud infrastructure.
               """)
  
  with st.expander("Google Developers Student Club at Taylor's University :gray[(*Oct 2021 - Oct 2022*)]"):
    with st.container():
      with st.container(border=True):
        jobcol = st.columns([1.5, 1.5, 1]) 
        jobcol[0].write(":blue[Technical Associate (Mentor)]")
        jobcol[1].write(":grey[Subang Jaya, Selangor, Malaysia]")
        jobcol[2].write(":grey[*Oct 2021 - Oct 2022*]")
        st.write("""
              - Was responsible for hosting technical events and crash courses on :green[Machine Learning], and :green[Google Cloud Platform], at the university,
              - :green[Conducted webinars and technical events] on cloud computing fundamentals and teaching Google Cloud Platform to and junior students/newcomers.
               """)
  st.markdown("To see the full list of my work experience (from LinkedIn), [click here](https://www.linkedin.com/in/alisterbaroi/details/experience/)", unsafe_allow_html=True)

  # Education Section
  st.subheader("Education", anchor=False)
  with st.expander("Bachelor of Computer Science (Hons) :gray[(*Aug 2020 - Aug 2023*)]"):
      with st.container(border=True):
        jobcol = st.columns([1.5, 1.5, 1]) 
        jobcol[0].write(":blue[Bachelor of Computer Science (Hons)]")
        jobcol[1].write(":grey[Taylor' University - Selangor, Malaysia]")
        jobcol[2].write(":grey[*Aug 2020 - Aug 2023*]")
        st.write("""
              - Major/specilization in :green[Artificial Intelligence] (AI),
              - Minor in :green[Financial Technology] (FinTech),
              - CGPA: :green[3.54/4.0],
              - Achievements: :green[Deans List] letters of recommendation, :green[Taylor's SHINE Gold Award], :green[Taylor's Excellence Award Scholarship] 
                 """)
  
      with st.container(border=True):
        jobcol = st.columns([1.5, 1.5, 1]) 
        jobcol[0].write(":blue[Bachelor of Science in Computer Science (Hons)]")
        jobcol[1].write(":grey[University of the West of England (UWE) - Bristol, UK]")
        jobcol[2].write(":grey[*Aug 2020 - Aug 2023*]")
        st.write("""
              - Dual award program with Taylor's University,  
              - CGPA: :green[3.54/4.0]
               """)
  with st.expander("Foundation in Computing :gray[(*Aug 2019 - Aug 2020*)]"):
    with st.container(border=True):
        jobcol = st.columns([1.5, 1.5, 1]) 
        jobcol[0].write(":blue[Foundation in Computing]")
        jobcol[1].write(":grey[Taylor' College - Selangor, Malaysia]")
        jobcol[2].write(":grey[*Aug 2019 - Aug 2020*]")
        st.write("""  
              - CGPA: :green[3.44/4.0],
              - Achievements: :green[Deans List] letters of recommendation
               """)
  
  with st.expander("A Levels :gray[(*June 2016 - June 2018*)]"):
    with st.container(border=True):
        jobcol = st.columns([1.5, 1.5, 1]) 
        jobcol[0].write(":blue[Cambridge Advanced Levels]")
        jobcol[1].write(":grey[British Council Bangladesh - Dhaka, Bangladesh]")
        jobcol[2].write(":grey[*June 2016 - June 2018*]")
        st.write("""
              - :green[Subjects:] Physics, Chemistry, Mathematics, 
              - :green[Reg. Type:] Private Student 
               """)
  
  with st.expander("O Levels :gray[(*June 2014 - Jun 2015*)]"):
    with st.container(border=True):
        jobcol = st.columns([1.5, 1.5, 1]) 
        jobcol[0].write(":blue[Cambridge Ordinary Levels]")
        jobcol[1].write(":grey[Bacha English Medium School (BEMS) - Dhaka, Bangladesh]")
        jobcol[2].write(":grey[*June 2014 - Jun 2015*]")
        st.write("""
              - :green[Subjects:] English Language, Mathematics, Chemistry, Physics, Bengali, Geography, 
              - :green[Reg. Type:] School Student
               """)
  




if __name__ == "__main__":
    main()
