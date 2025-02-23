import librosa
from src.logger import ProjectLogger


class AudioProcessor:
    def __init__(self, file_path):
        """
        Initialize the AudioProcessor.

        Parameters:
        - file_path (str): Path to the audio file.
        """
        self.file_path = file_path
        self.logger = ProjectLogger().get_logger()

    def load_audio(self):
        """
        Load audio file using librosa.

        Returns:
        - tuple: A tuple containing the audio signal and sampling rate.
            - np.ndarray: Audio signal.
            - int: Sampling rate.
        """
        self.logger.info(f"Entered load_audio() in {self.__class__.__name__} file")
        try:
            self.logger.info("Loading audio file using librosa")

            audio_signal, sampling_rate = librosa.load(self.file_path)

            self.logger.info("Exiting load_audio()")

            return audio_signal, sampling_rate
        except Exception as e:
            self.logger.exception("Error loading audio", e)
            self.logger.info("Exiting load_audio()")
            return None, None

    def get_audio_duration(self):
        """
        Get the duration of the loaded audio.

        Returns:
        - float: Audio duration in seconds.
        """
        self.logger.info(f"Entered duration() in {self.__class__.__name__} file")

        audio_signal, sampling_rate = self.load_audio()
        if audio_signal is not None:
            duration = librosa.get_duration(y=audio_signal, sr=sampling_rate)

            self.logger.info("Exiting duration()")
            return duration
        return None
