import streamlit as st

st.set_page_config(
    page_title="Alister Baroi", page_icon=":page_facing_up:", layout="centered", initial_sidebar_state="expanded", 
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


  # Project: Resume Parser API
  with st.container(border=True):
    jobcol = st.columns([2, 5, 2]) 
    a = {"name": "Resume Parser API", "tech":"Python, FastAPI, GCloud SDK", "date":"12/2023", "platform": "OpenAI, GCP DocumentAI, Google Cloud Platform", "des":"An AI-based API, designed to accept API request with resumes/CVs (PDF file) as argument, process them with computer vision and LLM, and send back the parsed (extracted) data as a JSON response.", "link":"https://resume-parser-api-2otwbg7hbq-nw.a.run.app/docs", "image":"./assets/Resume_parser.jpeg", "video":None}
    jobcol[0].write(a["name"])
    jobcol[1].write(f":gray[API to accept resumes, process with computer vision & LLM, & send back parsed data as JSON. :green[Date: {a['date']}]]")
    if jobcol[2].button(":red[View Details]", use_container_width=True, key="Resume"):
      project(a["name"], a["date"], a["tech"], a["platform"], a["des"], a["link"], a["image"], a["video"])
  
  # Project: Cat & Dog Classifier
  with st.container(border=True):
    jobcol = st.columns([2, 5, 2]) 
    a = {"name": "Cat & Dog Classifier", "tech":"Python, Keras, TensorFlow, Scikit-Learn, Streamlit", "date":"11/2023", "platform": "Docker, Google Cloud Platform", "des":"A robust image classification web app, wrapped around my previosuly-built Deep Learning (Convolutional Neural Network) model that I trained with a dataset cat and dog images (in 2022), that allows users to upload images of cats or dogs, and get the classification prediction, with high accuracy.", "link":"https://cat-and-dog-classifier-5b4x24knra-uc.a.run.app/", "image":"https://raw.githubusercontent.com/AlisterBaroi/cat_and_dog_classifier/c011b26cadaf6047329622a6730a4a6de8ee107f/.github/workflows/demo.png", "video":None}
    jobcol[0].write(a["name"])
    jobcol[1].write(f":gray[A web app wrapped around an CNN model to clasify between images of cats and dogs. :green[Date: {a['date']}]]")
    if jobcol[2].button(":red[View Details]", use_container_width=True, key="Cat&dog"):
      project(a["name"], a["date"], a["tech"], a["platform"], a["des"], a["link"], a["image"], a["video"])

  # Project: time-speaker
  with st.container(border=True):
    jobcol = st.columns([2, 5, 2]) 
    a = {"name": "Time Speaker", "tech":"Python", "date":"10/2023", "platform": None, "des":"A simple program to print time in words from numeral inputs. This is a problem from the 'Turing Coding Challenge 2020'. The challange name is 'The Time in Words' (Challenge 7).", "link":"https://github.com/AlisterBaroi/time-speaker", "image":"https://raw.githubusercontent.com/AlisterBaroi/time-speaker/main/img/demo.gif", "video":None}
    jobcol[0].write(a["name"])
    jobcol[1].write(f":gray[A simple program to print time in words from numeric inputs. Build during coding challenge.  :green[Date: {a['date']}]]")
    if jobcol[2].button(":red[View Details]", use_container_width=True, key="time-speaker"):
      project(a["name"], a["date"], a["tech"], a["platform"], a["des"], a["link"], a["image"], a["video"])

   # Project: Breast Cancer Diagnosis Predictor
  with st.container(border=True):
    jobcol = st.columns([2, 5, 2]) 
    a = {"name": "Breast Cancer Diagnosis Predictor ", "tech":"Python, Scikit-learn, Keras", "date":"02/2022", "platform": "Google Colab, Jupyter Notebook", "des":"A simple Deep Learning (Artificial Neural Network) model, trained with real breast cancer data, that can predict the outcome for breast cancer diagnosis. Built it as a semester project.", "link":"https://github.com/AlisterBaroi/breast-cancer-diagnosis-predictor", "image":"https://private-user-images.githubusercontent.com/44337842/343929947-1fd52485-99af-4e0b-a629-74a7de701695.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTk1MTcyNzMsIm5iZiI6MTcxOTUxNjk3MywicGF0aCI6Ii80NDMzNzg0Mi8zNDM5Mjk5NDctMWZkNTI0ODUtOTlhZi00ZTBiLWE2MjktNzRhN2RlNzAxNjk1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MjclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjI3VDE5MzYxM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBkMzVmOGRiNTVhNWNkMzMwNmM5N2YwMWM1ZmNiYTRjZTExNGY3OTdhMTc3Y2YyYWZjNTAxZjZjYjg1MzIyN2EmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.PdQwsdknX3AqkIH29d4yIuaiq5kLaFwF7aQXRhHFWR8", "video":None}
    jobcol[0].write(a["name"])
    jobcol[1].write(f":gray[A simple Deep Learning (ANN) model to predict breast cancer diagnosis. :green[Date: {a['date']}]]")
    if jobcol[2].button(":red[View Details]", use_container_width=True, key="ANN"):
      project(a["name"], a["date"], a["tech"], a["platform"], a["des"], a["link"], a["image"], a["video"])
   
  # Project: Property Consultancy Mobile App
  with st.container(border=True):
    jobcol = st.columns([2, 5, 2]) 
    a = {"name": "MyKay - Mobile App", "tech":"JavaScript, React Native", "date":"08/2021", "platform": "React Native Expo", "des":"A property consultancy mobile app, build using React Native. The main functionality of this app is the offline login system created using the Asynchronous Storage. Aside from that the app is mostly UI", "link":"https://github.com/AlisterBaroi/My-Kay", "image":"https://alisterbaroi.github.io/img/work.png", "video":None}
    jobcol[0].write(a["name"])
    jobcol[1].write(f":gray[A Property Consultancy Mobile App made using React Native. :green[Date: {a['date']}]]")
    if jobcol[2].button(":red[View Details]", use_container_width=True, key="MyKay"):
      project(a["name"], a["date"], a["tech"], a["platform"], a["des"], a["link"], a["image"], a["video"])

  # Project: Bookstore Inventory Management System
  with st.container(border=True):
    jobcol = st.columns([2.2, 5, 2]) 
    a = {"name": "Bookstore Inventory Management System", "tech":"C++", "date":"06/2021", "platform": None, "des":"A simple inventory management system (terminal) for book stores, with the ability to add/edit/remove records of books and customer order transactions.", "link":"https://github.com/AlisterBaroi/bookstore-inventory-system", "image":"https://private-user-images.githubusercontent.com/44337842/343895418-e5311460-a465-4f56-b336-8f60d0b95d80.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTk1MTE5MjEsIm5iZiI6MTcxOTUxMTYyMSwicGF0aCI6Ii80NDMzNzg0Mi8zNDM4OTU0MTgtZTUzMTE0NjAtYTQ2NS00ZjU2LWIzMzYtOGY2MGQwYjk1ZDgwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MjclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjI3VDE4MDcwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTg5NTFiMWNmOWNiNDllMTI0ZGU3OTZiNWE3ZDk0NGUyMmM0M2FhN2U1M2U3MDk5N2Y2ZTUwMTA5YzY3Y2Q5NWQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.jo0KiD4x0f0FGdPwhkz0swFIl-VX6I4qqvmn8zyTFLA", "video":None}
    jobcol[0].write(a["name"])
    jobcol[1].write(f":gray[A terminal application for executing CRUD operations for book inventory management. :green[Date: {a['date']}]]")
    if jobcol[2].button(":red[View Details]", use_container_width=True, key="Inventory"):
      project(a["name"], a["date"], a["tech"], a["platform"], a["des"], a["link"], a["image"], a["video"])
 
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
    a = {"name": "Netflix Clone", "tech":"HTML, CSS, JavaScript, Bootstrap 4", "date":"05/2019", "platform":None, "des":"A complete bootstrap clone of the front-end of Netflix.", "link":"https://alisterbaroi.github.io/Netflix/", "image":"https://raw.githubusercontent.com/AlisterBaroi/Netflix/2726b21ebad33c710f21a82542f8563afa1b8f6a/images/branding.jpeg", "video":None}
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
