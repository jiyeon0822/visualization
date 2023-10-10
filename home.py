import streamlit as st

import pages.sample
import pages.about

PAGES = {
  "home" : pages.sample,
  "about" : pages.about
}


def main():

  st.sidebar.markdown('### Contents')
  selection = st.sidebar.radio("select", list(PAGES.keys()))
  page = PAGES[selection]
  st.write(page)
  
  
