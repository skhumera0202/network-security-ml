import os
import sys

import pandas as pd
import yaml

from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact
)
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class DataValidation:

    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig
    ):
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_validation_config = data_validation_config

    def validate_number_of_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            with open("data_schema/schema.yaml", "r") as file:
                schema = yaml.safe_load(file)

            expected_columns = len(schema["columns"])
            actual_columns = len(dataframe.columns)

            logging.info(
                f"Expected columns: {expected_columns}, "
                f"Actual columns: {actual_columns}"
            )

            return expected_columns == actual_columns

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def validate_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            with open("data_schema/schema.yaml", "r") as file:
                schema = yaml.safe_load(file)

            expected_columns = set(schema["columns"].keys())
            actual_columns = set(dataframe.columns)

            return expected_columns == actual_columns

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:

        logging.info("Starting data validation")

        try:
            train_df = pd.read_csv(
                self.data_ingestion_artifact.trained_file_path
            )

            test_df = pd.read_csv(
                self.data_ingestion_artifact.test_file_path
            )

            train_columns_valid = (
                self.validate_number_of_columns(train_df)
                and self.validate_columns(train_df)
            )

            test_columns_valid = (
                self.validate_number_of_columns(test_df)
                and self.validate_columns(test_df)
            )

            validation_status = (
                train_columns_valid and test_columns_valid
            )

            logging.info(
                f"Data validation status: {validation_status}"
            )

            return DataValidationArtifact(
                validation_status=validation_status,
                valid_train_file_path=(
                    self.data_ingestion_artifact.trained_file_path
                    if train_columns_valid
                    else None
                ),
                valid_test_file_path=(
                    self.data_ingestion_artifact.test_file_path
                    if test_columns_valid
                    else None
                )
            )

        except Exception as e:
            raise NetworkSecurityException(e, sys)
if __name__ == "__main__":

    from networksecurity.components.data_ingestion import DataIngestion

    data_ingestion = DataIngestion()
    data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

    data_validation = DataValidation(
        data_ingestion_artifact=data_ingestion_artifact,
        data_validation_config=DataValidationConfig()
    )

    data_validation_artifact = data_validation.initiate_data_validation()

    print(data_validation_artifact)