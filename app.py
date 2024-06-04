import streamlit as st
from streamlit_webrtc import webrtc_streamer

def main():
    st.title("Live Camera Stream")

    webrtc_streamer(key="example")

if __name__ == "__main__":
    main()
