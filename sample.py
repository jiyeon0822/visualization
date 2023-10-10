import streamlit as st
import awesome_streamlit as ast

import src.home
import src.about




PAGES = {
  "home" : src.home,
  "about" : src.about
}


def main():

  st.sidebar.markdown('### Contents')
  selection = st.sidebar.radio("select", list(PAGES.keys()))
  page = PAGES[selection]
  
  with st.spinner(f"Loading {selection} ..."):
    ast.shared.components.write_page(page)
  
  
