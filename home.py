import streamlit as st

import src.home
import src.about

import pages.home
import pages.about

PAGES = {
  "home" : pages.home,
  "about" : pages.about
}


def main():

  st.sidebar.markdown('### Contents')
  selection = st.sidebar.radio("select", list(PAGES.keys()))
  page = PAGES[selection]
  st.write(page)
  
  
