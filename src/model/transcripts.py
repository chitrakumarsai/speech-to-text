import time
from src.logger import ProjectLogger

logger = ProjectLogger().get_logger()


class TranscriptProcessor:
    def __init__(self, transcription_engine):
        """
        Initialize the TranscriptProcessor.

        Parameters:
        - transcription_engine: The engine used for audio transcription.
        """
        self.transcription_engine = transcription_engine

    def get_transcripts(self, audio_file_path):
        """
        Get transcripts from an audio file.

        Parameters:
        - audio_file_path (str): Path to the audio file.

        Returns:
        - tuple: A tuple containing transcripts obtained from the audio file and the time taken for transcription.
            - str: Transcripts obtained from the audio file.
            - float: Time taken for transcription in seconds.
        """
        try:
            # Assuming some hypothetical library for audio transcription
            start_time = time.time()
            transcripts = self.transcription_engine.transcribe(
                audio_file_path, fp16=False
            )
            end_time = time.time()
            time_taken = end_time - start_time
            return transcripts, time_taken
        except Exception as e:
            logger.exception("Error Transcribing Audio", e)
            return None

