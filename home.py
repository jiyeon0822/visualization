import streamlit as st

import src.home
import src.about

import src.home
import src.about

PAGES = {
  "home" : pages.home,
  "about" : pages.about
}


def main():

  st.sidebar.markdown('### Contents')
  selection = st.sidebar.radio("select", list(PAGES.keys()))
  page = PAGES[selection]
  st.write(page)
  
  
