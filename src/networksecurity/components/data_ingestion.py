import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class DataIngestion:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self) -> DataIngestionArtifact:

        logging.info("Entered data ingestion component")

        try:
            # Read dataset
            data_path = os.path.join("data", "phisingData.csv")

            df = pd.read_csv(data_path)

            logging.info("Dataset loaded successfully")
            logging.info(f"Dataset shape: {df.shape}")

            # Create directories
            os.makedirs(
                os.path.dirname(
                    self.data_ingestion_config.training_file_path
                ),
                exist_ok=True
            )

            os.makedirs(
                os.path.dirname(
                    self.data_ingestion_config.testing_file_path
                ),
                exist_ok=True
            )

            # Train-test split
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # Save train data
            train_set.to_csv(
                self.data_ingestion_config.training_file_path,
                index=False
            )

            # Save test data
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,
                index=False
            )

            logging.info("Train-test split completed")

            return DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )

        except Exception as e:
            raise NetworkSecurityException(e, sys) 
if __name__ == "__main__":

    data_ingestion = DataIngestion()

    artifact = data_ingestion.initiate_data_ingestion()

    print(artifact)