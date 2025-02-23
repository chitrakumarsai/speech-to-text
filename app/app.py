import streamlit as st
import streamlit_extras.add_vertical_space as avs
from streamlit_extras.switch_page_button import switch_page


# configuring home page
st.set_page_config(
    page_title="Home", page_icon=":speaking_head_in_silhouette:", layout="wide"
)
title_style = """
            <style>
            .title {
                text-align: center;
                color:#faa356;
            }
            </style>
        """
st.markdown(title_style, unsafe_allow_html=True)

# Page heading
st.markdown(
    "<h1 class='title'>Speech To Text Using Whisper<span style='color:#b3cee5'>&#x1F50A;</span>&#x1F4DC;</h1>",
    unsafe_allow_html=True,
)


# introduction markdown text
intro = """
        <h3 style="color:#a2d2fb">Introduction</h3>

        Automatic Speech Recognition (ASR) is a transformative technology that enables machines to convert spoken language into written text, facilitating seamless interaction between humans and computers.Computer algorithms facilitate this process in four steps: <span style="color:#7ce38b">analyze the audio </span>, <span style="color:#7ce38b"> break it down into parts </span>, <span style="color:#7ce38b"> convert it into a computer-readable format </span>, and <span style="color:#7ce38b"> use the algorithm again to match it into a text-readable format.</span><br>

        > <span style="color:#7ce38b">Analyze The Audio </span>:- 
        In the first step of ASR, the audio undergoes detailed analysis, extracting features like frequency patterns and acoustic characteristics. This enables the system to discern speech from background noise and capture nuances in tone and pronunciation.

        > <span style="color:#7ce38b">Break It into Parts</span> :- 
        Following analysis, the ASR system segments the audio, identifying pauses and distinct speech patterns. This step enhances recognition accuracy by breaking the input into manageable linguistic components.

        > <span style="color:#7ce38b">Convert Into Computer Readable Format</span>:- 
        Once segmented, components are transformed into a computer-readable format, often using Mel-frequency cepstral coefficients (MFCCs) or spectrograms. This conversion bridges the gap between raw audio and computational models for advanced analysis.

        > <span style="color:#7ce38b">Use Algorithm To Match Text</span>:- 
        Utilizing sophisticated algorithms, ASR matches extracted features to linguistic patterns, generating a word sequence. This final step involves probabilistic decision-making, resulting in the conversion of spoken language into written text for applications like transcription services and voice commands.

        """
st.markdown(intro, unsafe_allow_html=True)

# adding vertical spaces
avs.add_vertical_space(2)

# functionalities text for audio_file.py and youtube_video.py
functionality_audio_file = """
        <h3 style="color:#a2d2fb">Audio File Transcription</h3>

        > The <span style="color:#7ce38b">"Audio File Transcription"</span> page of the Streamlit app empowers users 
        to transcribe audio content from pre-recorded files effortlessly. Users can upload audio files in various 
        formats, such as MP3 or WAV. Upon uploading, The system offers transcripts accompanied by a play button for 
        convenient comparison between the original audio and its transcribed version. This functionality allows users 
        to validate the accuracy of the transcription process by listening to the audio while simultaneously 
        reviewing the corresponding text. 

        """

functionality_youtube_video = """
        <h3 style="color:#a2d2fb">YouTube Video Transcription</h3>

        > The <span style="color:#7ce38b">"YouTube Video Transcription"</span> page introduces a dynamic 
        functionality where users can provide the URL of a YouTube video and receive accurate transcripts of the 
        audio content. This feature is particularly useful for extracting spoken content from videos, 
        such as interviews, presentations, or educational content. Users simply input the YouTube video URL, 
        and the system processes the audio, presenting the transcribed text for easy reference. This page serves as a 
        versatile tool for extracting valuable information from YouTube videos in a text format. 

        """

# Usage in Streamlit
st.markdown(functionality_audio_file, unsafe_allow_html=True)
st.markdown(functionality_youtube_video, unsafe_allow_html=True)


# adding vertical spaces
avs.add_vertical_space(2)

# user guide markdown text
using = """
        <h3 style="color:#a2d2fb">Usage Guide</h3>
        Explore the individual pages below.
        """
st.markdown(using, unsafe_allow_html=True)
avs.add_vertical_space(2)


# main function
def main():
    pages_dict = {
        "app": "app",
        "Audio File": "Audio File",
        "Youtube Video": "Youtube Video",
    }
    option = st.selectbox(label="select one page", options=pages_dict.keys())

    if option != "app":
        switch_page(option)

    # # hiding hamburger menu while execution
    # hide_menu_style = """
    #                <style>
    #                #MainMenu {visibility: hidden;}
    #                .stApp [data-testid="stToolbar"]{display:none;}
    #                footer {visibility:hidden}
    #                </style>
    #                """
    # st.markdown(hide_menu_style, unsafe_allow_html=True)


# calling main function
if __name__ == "__main__":
    main()


