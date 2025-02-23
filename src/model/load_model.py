import whisper
from src.logger import ProjectLogger
import os

logger = ProjectLogger().get_logger()

class WhisperModelManager:
    def __init__(self):
        """Initialize the WhisperModelManager."""
        pass

    def load_model(self, model_name):
        """
        Load or download a Whisper model.

        Parameters:
        - model_name (str): The name of the Whisper model. Valid values: 
          ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 
          'large-v1', 'large-v2', 'large-v3', 'large']

        Returns:
        - whisper.Whisper: The loaded Whisper model.
        """
        logger.info(f"Entered load_model() in {self.__class__.__name__}")

        try:
            # Let Whisper handle the model loading and downloading
            model = whisper.load_model(model_name)
            logger.info(f"Model '{model_name}' loaded successfully.")
            return model
        
        except Exception as e:
            logger.exception(f"Error occurred while loading model '{model_name}': {e}")
            return None


    def save_model_as_zip(self, model, model_name, model_folder_path):
        """Save the downloaded model as a zip file."""

        model_zip_path = model_folder_path + f"/{model_name}_model.zip"
        # model_zip_path = "../../models/"
        try:
            with zipfile.ZipFile(model_zip_path, "w") as zipf:
                logger.info("Opening zip file")
                # Add all files in the model folder to the zip file
                for root, _, files in os.walk(model_folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arc_name = os.path.relpath(file_path, model_folder_path)
                        zipf.write(file_path, arcname=arc_name)
        except Exception as e:
            logger.exception("Failed to save model", e)

    def load_model_from_zip(self, model_zip_path, model_extracted_path):
        """Load the model from the zip file."""
        logger.info("About to load model using zip")

        with zipfile.ZipFile(model_zip_path, "r") as zipf:
            logger.info("Extracting the model from zip")
            # Extract the zip file to a temporary directory
            zipf.extractall(model_extracted_path)

            # Load the model from the temporary directory
            model = whisper.load_model("base", download_root=model_extracted_path)

            return model
