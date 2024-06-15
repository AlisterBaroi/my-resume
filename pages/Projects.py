import streamlit as st

st.set_page_config(
    page_title="Alister Animesh Baroi - Projects", page_icon=":page_facing_up:", layout="centered", initial_sidebar_state="expanded", 
    # menu_items=None
)

def main():
  st.title("My Projects")

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



if __name__ == "__main__":
    main()
