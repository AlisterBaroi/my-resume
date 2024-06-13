import streamlit as st

st.set_page_config(
    page_title="Alister Animesh Baroi - Resume", page_icon=":page_facing_up:", layout="centered"
)

def main():
  row0 = st.columns([1,1])

  with row0[0]:
     st.image("./images/Profile.png",width=360, caption="Holla")
     
  with row0[1]:
    st.title("Alister Animesh Baroi")
    st.write("Cloud Architect, DevOps Engineer, AI Engineer, Backend Engineer.")
    with open("./images/Alister_Baroi_Resume.pdf", "rb") as file:
      st.download_button("Download Resume", type="primary", data=file, file_name="Alister_Baroi_Resume.pdf", mime="application/pdf")

  row1 = st.columns([1,1,1,1])
  # git = st.image("https://static-00.iconduck.com/assets.00/github-icon-512x497-oppthre2.png")
  row1[0].link_button(":globe_with_meridians: Website", url="https://alisterbaroi.streamlit.io", help="alisterbaroi.streamlit.io", use_container_width=True)
  row1[1].link_button(":blue-background[in] LinkedIn", url="https://www.linkedin.com/in/alisterbaroi", help="linkedin.com/in/alisterbaroi", use_container_width=True)
  row1[2].link_button(":cat: GitHub", url="https://github.com/alisterbaroi", help="github.com/alisterbaroi", use_container_width=True)
  row1[3].link_button(":red[@] Email", url="mailto:alister.baroi@gmail.com", help="alister.baroi@gmail.com", use_container_width=True)







if __name__ == "__main__":
    main()
