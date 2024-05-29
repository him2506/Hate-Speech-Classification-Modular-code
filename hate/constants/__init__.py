import os

from datetime import datetime

# Get the current file's directory (directory of a.py)
current_file_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the current file's directory (parent of x)
parent_directory = os.path.dirname(current_file_directory)

# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME = 'hate_speech'
ZIP_FILE_NAME = 'Data.zip'
LABEL = 'label'
TWEET = 'tweet'
MODEL_NAME = 'model.h5'
APP_HOST = "0.0.0.0"
APP_PORT = 8080

# Data ingestion constants
# DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_ARTIFACTS_DIR = os.path.join(parent_directory, 'datasets')

# DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_IMBALANCE_DATA_DIR = "train.csv"

# DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "labeled_data.csv"

# Data transformation constants 
DATA_TRANSFORMATION_ARTIFACTS_DIR = 'DataTransformationArtifacts'
TRANSFORMED_FILE_NAME = "final.csv"
DATA_DIR = "data"
ID = 'id'
AXIS = 1
INPLACE = True
DROP_COLUMNS = ['Unnamed: 0','count','hate_speech','offensive_language','neither']
CLASS = 'class'


# Model training constants
MODEL_TRAINER_ARTIFACTS_DIR = 'ModelTrainerArtifacts'
TRAINED_MODEL_DIR = 'trained_model'
TRAINED_MODEL_NAME = 'model.h5'
X_TEST_FILE_NAME = 'x_test.pickle'
Y_TEST_FILE_NAME = 'y_test.pickle'

X_TRAIN_FILE_NAME = 'x_train.pickle'

RANDOM_STATE = 42
EPOCH = 2
BATCH_SIZE = 128
VALIDATION_SPLIT = 0.2


# Model Architecture constants
MAX_WORDS = 10000
MAX_LEN = 100
LOSS = 'binary_crossentropy'
METRICS = ['accuracy']
ACTIVATION = 'sigmoid'


# Model  Evaluation constants
MODEL_EVALUATION_ARTIFACTS_DIR = 'ModelEvaluationArtifacts'
BEST_MODEL_DIR = "best_Model"
MODEL_EVALUATION_FILE_NAME = 'loss.csv'


# Model pusher to final loaction folder
BEST_FINAL_MODEL_FOLDER = 'Best_Model_folder'