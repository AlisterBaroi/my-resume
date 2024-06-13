import streamlit as st

st.set_page_config(
    page_title="Alister Animesh Baroi - Resume", page_icon=":page_facing_up:", layout="centered"
)

def main():
  row0 = st.columns([1,1])

  with row0[0]:
     st.image("./images/Profile.png",width=360)
     
  with row0[1]:
    st.header("Alister Animesh Baroi", anchor=False)
    st.write("Cloud Architect, DevOps Engineer, AI Engineer, Backend Engineer.")
    with open("./images/Alister_Baroi_Resume.pdf", "rb") as file:
      st.download_button(":page_facing_up: Download Resume", type="primary", data=file, file_name="Alister_Baroi_Resume.pdf", mime="application/pdf")

  row1 = st.columns([1,1,1,1])
  row1[0].link_button(":orange[@ Email]", url="mailto:alister.baroi@gmail.com", help="alister.baroi@gmail.com", use_container_width=True)
  row1[1].link_button(":red[:globe_with_meridians: Website]", url="https://alisterbaroi.streamlit.io", help="alisterbaroi.streamlit.io", use_container_width=True)
  row1[2].link_button(":blue-background[in] :blue[LinkedIn]", url="https://www.linkedin.com/in/alisterbaroi", help="linkedin.com/in/alisterbaroi", use_container_width=True)
  row1[3].link_button(":computer: :green[GitHub]", url="https://github.com/alisterbaroi", help="github.com/alisterbaroi", use_container_width=True)

  st.subheader("Summary", anchor=False)
  st.markdown(""" 
- 3+ years experience,
- 👔 Lead Cloud Architect (current job),
- 🏆 Computer Science (Honours) graduate from Taylors University (Malaysia),
  - 🔥 Majored in AI & minored in FinTech,

""")







if __name__ == "__main__":
    main()
