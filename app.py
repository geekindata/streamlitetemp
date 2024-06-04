import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, ClientSettings

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        return frame

def main():
    st.title("Live Camera Stream")
    
    client_settings = ClientSettings(
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={
            "video": True,
            "audio": False,
        },
    )
    
    webrtc_ctx = webrtc_streamer(
        key="example",
        video_processor_factory=VideoProcessor,
        rtc_configuration=client_settings.rtc_configuration,
        media_stream_constraints=client_settings.media_stream_constraints,
    )

    if webrtc_ctx.video_processor:
        st.video(webrtc_ctx.video)

if __name__ == "__main__":
    main()
