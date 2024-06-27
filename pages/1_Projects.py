import streamlit as st

st.set_page_config(
    page_title="Alister Animesh Baroi - Projects", page_icon=":page_facing_up:", layout="centered", initial_sidebar_state="expanded", 
    # menu_items=None
)

def main():
  st.title("Projects —")
  st.write("Here are all my AI/ML, Web Development, and cloud related projects — Enjoy!!")
  st.subheader(":red[Work in progress...]")
  # Dark mode
  with st.sidebar:
    if st.toggle("Dark Mode", value=True) is False:
      st._config.set_option(f'theme.base', "light")
    else:
      st._config.set_option(f'theme.base', "dark")
    
    # Refresh button  
    if st.button("Refresh", help="Refresh page if something isn't updating accordingly", use_container_width=True):
      st.rerun()

    # Clear button  
    if st.button("Clear Session", help="Clears session, cache, and cookie data", use_container_width=True):
      st._config.set_option(f'theme.base', "dark")
      st.cache_data.clear()
      st.session_state.clear()
      st.cache_resource.clear()
      st.rerun()
    st.markdown("Copyright ©️ 2024 :blue[Alister Animesh Baroi.]<br>All rights reserved.", unsafe_allow_html=True)

  # Project: Ecommerce store
  with st.container(border=True):
    jobcol = st.columns([2, 5, 2]) 
    a = {"name": "E-Commerce Store", "tech":"HTML, CSS, JavaScript, Bootstrap 4, PHP, SQL", "date":"04/2021", "platform": "MySQL Database, XAMPP Server", "des":"A full-fledged ecommerce store built with PHP, MySQL, & Bootstrap using the MVC architecture. The project is to showcase a fictional e-commerce to showcase and sell plants and pottery accessories.", "link":"https://github.com/AlisterBaroi/ecommerce-php", "image":"https://alisterbaroi.github.io/img/work.png", "video":None}
    jobcol[0].write(a["name"])
    jobcol[1].write(f":gray[A fictional e-commerce store to showcase and sell plants and pottery accessories. :green[Date: {a['date']}]]")
    if jobcol[2].button(":red[View Details]", use_container_width=True, key="Ecommerce"):
      project(a["name"], a["date"], a["tech"], a["platform"], a["des"], a["link"], a["image"], a["video"])

  # Project: Escape from Maze
  with st.container(border=True):
    jobcol = st.columns([2, 5, 2]) 
    a = {"name": "Escape from Maze - PC Game", "tech":"Visual Scripting, C++", "date":"07/2019", "platform":"Unreal Engine 4.20, Sketchup", "des":"This is one of the first games I created using Unreal Engine 4. The objective of this game is simple; collect 3 keys to unlock a door and escape the maze that you're in.", "link":"https://baroiall.itch.io/escape-from-maze", "image":"https://img.itch.zone/aW1nLzIyOTQxMTEucG5n/315x250%23c/Z5c6dp.png", "video":"https://youtu.be/hX1eFkL11_o"}
    jobcol[0].write(a["name"])
    jobcol[1].write(f":gray[One of the first games I created using Unreal Engine 4.20 and sketchup. :green[Date: {a['date']}]]")
    if jobcol[2].button(":red[View Details]", use_container_width=True, key="Escape"):
      project(a["name"], a["date"], a["tech"], a["platform"], a["des"], a["link"], a["image"], a["video"])
    
  # Project: Netflix Clone
  with st.container(border=True):
    jobcol = st.columns([2, 5, 2]) 
    a = {"name": "Netflix Clone", "tech":"HTML, CSS, JavaScript, Bootstrap 4", "date":"05/2019", "platform":None, "des":"A complete bootstrap clone of the front-end of Netflix.", "link":"https://alisterbaroi.github.io/Netflix/", "image":"https://img.itch.zone/aW1nLzIyOTQxMTEucG5n/315x250%23c/Z5c6dp.png", "video":None}
    jobcol[0].write(a["name"])
    jobcol[1].write(f":gray[A complete bootstrap clone of the front-end of Netflix. :green[Date: {a['date']}]]")
    if jobcol[2].button(":red[View Details]", use_container_width=True, key="Netflix"):
      project(a["name"], a["date"], a["tech"], a["platform"], a["des"], a["link"], a["image"], a["video"])
    
    


@st.experimental_dialog("Project Details —", width="large")
def project(item, item2, item3, item4, item5, item6, item7, item8):
    modal1 = st.columns([2, 3])
    with modal1[0]:
      if item8 is None:
        st.image(item7)
      else:
        st.video(item8)
        
    with modal1[1]: 
      modal2 = st.columns([6, 2])
      modal2[0].write(f""":green[Project Name:]   
                  {item}""")
      modal2[1].write(f""" :green[Date:]   
                      {item2}""")
      details = st.columns([1, 1])
      details[0].write(f""":green[Languages/Frameworks:]   
                      {item3}""")
      details[1].write(f""":green[Platforms/Tools Used:]   
                      {item4}""")
      st.write(f""":green[Description:]   
              {item5}""")
      if item6 is None:
        if st.button("Close"):
          st.rerun()
      else:
        modalbtn = st.columns(2)
        modalbtn[0].link_button("Go to Project ➚", url=item6, type="primary", use_container_width=True)
        if modalbtn[1].button("Close", use_container_width=True):
          st.rerun()

if __name__ == "__main__":
    main()
