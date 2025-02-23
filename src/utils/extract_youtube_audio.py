import os
import yt_dlp
from src.logger import ProjectLogger

logger = ProjectLogger().get_logger()

class YouTubeAudioExtractor:
    def __init__(self):
        """
        Initialize the YouTubeAudioExtractor.
        """
        self.audio_file = "data/uploaded/youtube_audio.mp3"  # Save as MP3 for better compatibility

    def extract_audio(self, url):
        """
        Extract audio from a YouTube video and save it as an MP3 file.

        Parameters:
        - url (str): The URL of the YouTube video.

        Raises:
        - Exception: If there is an error during the extraction process.
        """
        logger.info(f"Entered extract_audio() in {self.__class__.__name__} class")

        # Create the directory if it doesn't exist
        os.makedirs("data/uploaded", exist_ok=True)

        try:
            # Set options for yt-dlp
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': 'data/uploaded/youtube_audio',  # Output without extension
                'quiet': False,
                'postprocessor_args': ['-y'],  # Overwrite if exists
            }

            # Extract audio using yt-dlp
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # Rename file to have the correct extension
            if os.path.exists('data/uploaded/youtube_audio.mp4.mp3'):
                os.rename('data/uploaded/youtube_audio.mp4.mp3', self.audio_file)
            elif os.path.exists('data/uploaded/youtube_audio.mp3'):
                self.audio_file = 'data/uploaded/youtube_audio.mp3'

            # Confirm the file was created
            if os.path.exists(self.audio_file):
                logger.info(f"Audio downloaded and saved as {self.audio_file}")
            else:
                logger.error("Audio file was not saved correctly.")

        except Exception as e:
            logger.exception(f"Error extracting audio: {e}")

        logger.info("Exiting extract_audio()")
