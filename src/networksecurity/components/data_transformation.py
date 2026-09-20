import os
import sys

import numpy as np
import pandas as pd

from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.entity.artifact_entity import (
    DataValidationArtifact,
    DataTransformationArtifact
)
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class DataTransformation:

    def __init__(
        self,
        data_validation_artifact: DataValidationArtifact,
        data_transformation_config: DataTransformationConfig
    ):
        self.data_validation_artifact = data_validation_artifact
        self.data_transformation_config = data_transformation_config

    def initiate_data_transformation(self) -> DataTransformationArtifact:

        logging.info("Starting data transformation")

        try:
            train_df = pd.read_csv(
                self.data_validation_artifact.valid_train_file_path
            )

            test_df = pd.read_csv(
                self.data_validation_artifact.valid_test_file_path
            )

            target_column = "Result"

            X_train = train_df.drop(columns=[target_column])
            y_train = train_df[target_column]

            X_test = test_df.drop(columns=[target_column])
            y_test = test_df[target_column]

            train_arr = np.c_[
                X_train.values,
                y_train.values
            ]

            test_arr = np.c_[
                X_test.values,
                y_test.values
            ]

            # Create transformation directory
            os.makedirs(
                os.path.dirname(
                    self.data_transformation_config
                    .transformed_train_file_path
                ),
                exist_ok=True
            )

            # Save transformed arrays
            np.save(
                self.data_transformation_config
                .transformed_train_file_path,
                train_arr
            )

            np.save(
                self.data_transformation_config
                .transformed_test_file_path,
                test_arr
            )

            logging.info("Data transformation completed")

            return DataTransformationArtifact(
                transformed_train_file_path=(
                    self.data_transformation_config
                    .transformed_train_file_path
                ),
                transformed_test_file_path=(
                    self.data_transformation_config
                    .transformed_test_file_path
                ),
                preprocessor_object_file_path=(
                    self.data_transformation_config
                    .preprocessor_object_file_path
                )
            )

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    from networksecurity.components.data_ingestion import DataIngestion
    from networksecurity.components.data_validation import DataValidation

    # Data Ingestion
    data_ingestion = DataIngestion()
    data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

    # Data Validation
    data_validation = DataValidation(
        data_ingestion_artifact=data_ingestion_artifact,
        data_validation_config=__import__(
            "networksecurity.entity.config_entity",
            fromlist=["DataValidationConfig"]
        ).DataValidationConfig()
    )

    data_validation_artifact = (
        data_validation.initiate_data_validation()
    )

    # Data Transformation
    data_transformation = DataTransformation(
        data_validation_artifact=data_validation_artifact,
        data_transformation_config=DataTransformationConfig()
    )

    data_transformation_artifact = (
        data_transformation.initiate_data_transformation()
    )

    print(data_transformation_artifact)