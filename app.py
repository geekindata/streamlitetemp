import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, ClientSettings

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
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
        video_transformer_factory=VideoTransformer,
        client_settings=client_settings,
    )

    if webrtc_ctx.video_transformer:
        st.video(webrtc_ctx.state.object)

if __name__ == "__main__":
    main()
