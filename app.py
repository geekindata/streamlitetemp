import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("Live Camera Stream")

    # HTML code to display video
    html_code = """
    <div>
        <video autoplay playsinline muted id="videoElement"></video>
    </div>
    <script>
        var video = document.querySelector("#videoElement");

        if (navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(function(stream) {
                    video.srcObject = stream;
                })
                .catch(function(error) {
                    console.error("Error accessing camera:", error);
                });
        }
    </script>
    """

    # Display the HTML code
    components.html(html_code, height=400)

if __name__ == "__main__":
    main()
