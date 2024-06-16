import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Alister Animesh Baroi - About", page_icon=":page_facing_up:", layout="centered", initial_sidebar_state="expanded", 
    # menu_items=None
)


# st.markdown("<script src='https://platform.linkedin.com/badges/js/profile.js?embed=True' type='text/javascript'></script>", unsafe_allow_html=True)
# code = """<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="alisterbaroi" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://bd.linkedin.com/in/alisterbaroi?trk=profile-badge"></a></div>"""
# st.html(code)
# st.markdown("""<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="alisterbaroi" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://bd.linkedin.com/in/alisterbaroi?trk=profile-badge&&embed=True">Alister Animesh Baroi</a></div>""", unsafe_allow_html=True)

def main():
  
  # Dark mode
  with st.sidebar:
    if st.toggle("Dark Mode", value=True) is False:
      st._config.set_option(f'theme.base', "light")
    else:
      st._config.set_option(f'theme.base', "dark")

    # Clear button  
    if st.button("Clear Session", help="Clears session, cache, and cookie data", use_container_width=True):
      st.cache_data.clear()
      st.session_state.clear()
      st.cache_resource.clear()
      st.rerun()

  st.title("Contact —")
  st.markdown(
      """This is the :green[***Contacts***] page, where you can contact me using the :green[contact form] below, or reach out to me at my :blue[LinkedIn] profile.  
              :green[— Alister Baroi, with ♥]"""
  )

  form_sec = st.columns([5, 8])
  # form_sec = st.columns([2, 3])
  with form_sec[0]:
    #  st.write("Use this form to contact me")
     components.html("""<script src='https://platform.linkedin.com/badges/js/profile.js' type='text/javascript'></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="small" data-theme="light" data-type="VERTICAL" data-vanity="alisterbaroi" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://bd.linkedin.com/in/alisterbaroi?embed=True"></a></div>
                """, height=330)
  with form_sec[1]:
    with st.form(key="contact"):
      st.subheader("Contact Form —")
      contact_form_col = st.columns(2)
      contact_form_col[0].text_input("Email Address", placeholder="e.g. john.doe@example.com")
      contact_form_col[1].text_input("Full Name", placeholder="e.g. John Doe")
      st.text_area("Message", placeholder="Write your message here")
      st.form_submit_button("Send message")


  st.divider()
  # Feedbacks & Reports Section
  st.subheader(":red[Feedbacks & Reports]")
  st.markdown(
      """This is the :red[***Feedbacks & Reports***] section, for you, to submit your user feedbacks, and report any bugs or other technical issues/difficulties that you may be facing. Please feel free to use this to let us know of any improvements/issues we can bring/fix.  
              :blue[— Thank you, with ♥]"""
  )
  # st.divider()
  row = st.columns([1, 1])
  # st.markdown("<style>hr{margin: 0;}</style>", unsafe_allow_html=True)
  # Subsection to leave user feedbacks
  with row[0]:
      st.subheader(":blue[User Feedback]")
      st.write(
          "Please feel free to leave your user feedbacks by clicking the button below. Share your :blue[user experience], suggested :blue[improvements] — Thank you."
      )
      feedbacks = st.button("Leave a feedback")
      if feedbacks:
        report("report_feedback")
      # st.divider()

  # Subsection to leave a bug report
  with row[1]:
      st.subheader(":red[Report Bugs]")
      st.write(
          "If facing any :red[bugs], :red[errors] or :red[technical issues], report them immediately by clicking the button below. I take bug reports very seriously — Thank you."
      )
      bugs = st.button("Report a bug")
      if bugs:
        report("report_bugs")
  st.divider()
  
  # Terms & Ccndition statements setion
  st.write(
      "Keep in mind that all submitted feedbacks and reports are governed by these :blue[Terms & Conditions] and :blue[Privacy Policy] statements."
  )

  
  
# Report form (Modal)
@st.experimental_dialog("Submit Report", width="small")
def report(item):
      st.write(
          "Submit your :blue[user feedback] here.."
          if item == "report_feedback"
          else "Please report here the :red[bug/issue] you are facing.."
      )
      with st.form(str(item), border=True):
          row1 = st.columns([1, 1])
          with row1[0]:
              name = st.text_input("Name", placeholder="e.g. John Doe", key="name")
          with row1[1]:
              email = st.text_input(
                  "Email", placeholder="e.g. john.doe@email.com", key="email"
              )
          feedback_txt = st.text_area(
              "Feedback" if item == "report_feedback" else "Bug description",
              placeholder=(
                  "User experience, improvement suggestions, feature reuests, etc."
                  if item == "report_feedback"
                  else "Describe the bug/error/issue you are facing. If possible, write the exact step-by-step process to recreate it."
              ),
              key="report_des",
          )
          if item == "report_bugs":
              uploaded_file = st.file_uploader(
                  "Upload images", type=["jpg", "png"],
                  accept_multiple_files=True, label_visibility="collapsed"
              )

          if st.form_submit_button(
              "Submit feedback" if item == "report_feedback" else "Report issue"
          ):
              st.session_state.reported = {"item": item}
              st.rerun()






if __name__ == "__main__":
    main()
