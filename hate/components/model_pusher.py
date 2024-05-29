import sys,os
from hate.logger import logging
from hate.exception import CustomException
from hate.configuration.gcloud_syncer import GCloudSync
from hate.entity.config_entity import ModelPusherConfig
from hate.entity.artifact_entity import ModelPusherArtifacts

# # Get the current file's directory (directory of a.py)
# current_file_directory = os.path.dirname(os.path.abspath(__file__))
# print('current_file_directory------> ',current_file_directory)
# # Get the parent directory of the current file's directory (parent of x)
# parent_directory = os.path.dirname(current_file_directory)
# print('parent_directory ---------->',parent_directory)

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig):
        """
        :param model_pusher_config: Configuration for model pusher
        """
        self.model_pusher_config = model_pusher_config
        # self.gcloud = GCloudSync()
    
    def write_to_file(self,file_path, text):
        try:
            with open(file_path, 'w') as file:
                file.write(text)
            logging.info(f"Successfully wrote to {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    
    
    def initiate_model_pusher(self) -> ModelPusherArtifacts:
        """
            Method Name :   initiate_model_pusher
            Description :   This method initiates model pusher.

            Output      :    Model pusher artifact
        """
        logging.info("Entered initiate_model_pusher method of ModelTrainer class")
        try:
            # Uploading the model to gcloud storage

            # self.gcloud.sync_folder_to_gcloud(self.model_pusher_config.BUCKET_NAME,
            #                                   self.model_pusher_config.TRAINED_MODEL_PATH,
            #                                   self.model_pusher_config.MODEL_NAME)
            
            # need code for puting the best model to certain folder
            
            current_file_directory = os.path.dirname(os.path.abspath(__file__))
            parent_directory = os.path.dirname(current_file_directory)
            model_saving_path = os.path.join(parent_directory,'best_model_location','best_model_location.txt')
            logging.info("Writing the best model path at file -->")
            logging.info(model_saving_path)
        
            self.write_to_file(model_saving_path, self.model_pusher_config.TRAINED_MODEL_PATH)

            logging.info("Uploaded best model to gcloud storage at --->")
            logging.info(self.model_pusher_config.TRAINED_MODEL_PATH)

            # Saving the model pusher artifacts
            model_pusher_artifact = ModelPusherArtifacts(
                best_final_model_folder=self.model_pusher_config.TRAINED_MODEL_PATH
            )
            logging.info("Exited the initiate_model_pusher method of ModelTrainer class")
            return model_pusher_artifact

        except Exception as e:
            raise CustomException(e, sys) from e
