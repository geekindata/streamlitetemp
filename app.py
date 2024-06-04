import streamlit as st
from streamlit_webrtc import webrtc_streamer

def main():
    st.title("Live Camera Stream")
    
    rtc_configuration = {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}

    media_stream_constraints = {
        "video": True,
        "audio": False,
    }
    
    webrtc_ctx = webrtc_streamer(
        key="example",
        rtc_configuration=rtc_configuration,
        media_stream_constraints=media_stream_constraints,
    )

    if webrtc_ctx.video_stream:
        st.write("Live Camera Stream")
        st.write(webrtc_ctx.video_stream)

if __name__ == "__main__":
    main()
