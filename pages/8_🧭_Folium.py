import streamlit as st
import athigeo.foliumap as athigeo 

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/Dmutai/map-templater>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.gifer.com/embedded/download/4j.gif"
st.sidebar.image(logo)

st.title("Athigeo Map")

with st.expander("See source code"):
    with st.echo():
        m = athigeo.Map()
        m.add_basemap("OpenTopoMap")
        m.add_basemap("Esri.WorldImagery")
        m.add_basemap("Strava.Ride")
        m.add_basemap("Strava.Run")
        m.add_layer_control()



m.to_streamlit(width=1000, height=700)
