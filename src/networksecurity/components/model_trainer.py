import os
import sys

import joblib
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelTrainerArtifact
)
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class ModelTrainer:

    def __init__(
        self,
        data_transformation_artifact: DataTransformationArtifact,
        model_trainer_config: ModelTrainerConfig
    ):
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:

        logging.info("Starting model training")

        try:
            # Load transformed data
            train_arr = np.load(
                self.data_transformation_artifact
                .transformed_train_file_path
            )

            test_arr = np.load(
                self.data_transformation_artifact
                .transformed_test_file_path
            )

            # Separate features and target
            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1]

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            logging.info("Training Random Forest model")

            # Create model
            model = RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )

            # Train model
            model.fit(X_train, y_train)

            # Evaluate model
            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)

            logging.info(
                f"Random Forest accuracy: {accuracy}"
            )

            # Create model directory
            os.makedirs(
                os.path.dirname(
                    self.model_trainer_config
                    .trained_model_file_path
                ),
                exist_ok=True
            )

            # Save model
            joblib.dump(
                model,
                self.model_trainer_config
                .trained_model_file_path
            )

            logging.info("Model saved successfully")

            return ModelTrainerArtifact(
                trained_model_file_path=(
                    self.model_trainer_config
                    .trained_model_file_path
                )
            )

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    from networksecurity.components.data_ingestion import DataIngestion
    from networksecurity.components.data_validation import DataValidation
    from networksecurity.components.data_transformation import (
        DataTransformation
    )
    from networksecurity.entity.config_entity import (
        DataValidationConfig,
        DataTransformationConfig
    )

    # Data Ingestion
    data_ingestion = DataIngestion()
    data_ingestion_artifact = (
        data_ingestion.initiate_data_ingestion()
    )

    # Data Validation
    data_validation = DataValidation(
        data_ingestion_artifact=data_ingestion_artifact,
        data_validation_config=DataValidationConfig()
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

    # Model Training
    model_trainer = ModelTrainer(
        data_transformation_artifact=data_transformation_artifact,
        model_trainer_config=ModelTrainerConfig()
    )

    model_trainer_artifact = (
        model_trainer.initiate_model_trainer()
    )

    print(model_trainer_artifact)