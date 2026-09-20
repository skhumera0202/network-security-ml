import os
import sys
import yaml
import joblib
import numpy as np

from sklearn.metrics import accuracy_score

from networksecurity.entity.config_entity import ModelEvaluationConfig
from networksecurity.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact
)
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class ModelEvaluation:

    def __init__(
        self,
        data_transformation_artifact: DataTransformationArtifact,
        model_trainer_artifact: ModelTrainerArtifact,
        model_evaluation_config: ModelEvaluationConfig
    ):
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_artifact = model_trainer_artifact
        self.model_evaluation_config = model_evaluation_config

    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:

        logging.info("Starting model evaluation")

        try:
            # Load test data
            test_arr = np.load(
                self.data_transformation_artifact
                .transformed_test_file_path
            )

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            # Load trained model
            model = joblib.load(
                self.model_trainer_artifact.trained_model_file_path
            )

            # Make predictions
            y_pred = model.predict(X_test)

            # Calculate accuracy
            accuracy = accuracy_score(y_test, y_pred)

            logging.info(
                f"Model evaluation accuracy: {accuracy}"
            )

            # Accept model if accuracy >= 0.90
            is_model_accepted = accuracy >= 0.90

            # Create directory
            os.makedirs(
                os.path.dirname(
                    self.model_evaluation_config
                    .model_evaluation_file_path
                ),
                exist_ok=True
            )

            # Save evaluation result
            evaluation_result = {
                "accuracy": float(accuracy),
                "is_model_accepted": is_model_accepted
            }

            with open(
                self.model_evaluation_config
                .model_evaluation_file_path,
                "w"
            ) as file:
                yaml.safe_dump(
                    evaluation_result,
                    file
                )

            return ModelEvaluationArtifact(
                is_model_accepted=is_model_accepted,
                trained_model_path=(
                    self.model_trainer_artifact
                    .trained_model_file_path
                ),
                test_accuracy=float(accuracy)
            )

        except Exception as e:
            raise NetworkSecurityException(e, sys)
if __name__ == "__main__":

    from networksecurity.components.data_ingestion import DataIngestion
    from networksecurity.components.data_validation import DataValidation
    from networksecurity.components.data_transformation import DataTransformation

    from networksecurity.entity.config_entity import (
        DataValidationConfig,
        DataTransformationConfig
    )

    # 1. Data Ingestion
    data_ingestion = DataIngestion()
    data_ingestion_artifact = (
        data_ingestion.initiate_data_ingestion()
    )

    # 2. Data Validation
    data_validation = DataValidation(
        data_ingestion_artifact=data_ingestion_artifact,
        data_validation_config=DataValidationConfig()
    )

    data_validation_artifact = (
        data_validation.initiate_data_validation()
    )

    # 3. Data Transformation
    data_transformation = DataTransformation(
        data_validation_artifact=data_validation_artifact,
        data_transformation_config=DataTransformationConfig()
    )

    data_transformation_artifact = (
        data_transformation.initiate_data_transformation()
    )

    # 4. Model Training
    from networksecurity.components.model_trainer import ModelTrainer
    from networksecurity.entity.config_entity import ModelTrainerConfig

    model_trainer = ModelTrainer(
        data_transformation_artifact=data_transformation_artifact,
        model_trainer_config=ModelTrainerConfig()
    )

    model_trainer_artifact = (
        model_trainer.initiate_model_trainer()
    )

    # 5. Model Evaluation
    model_evaluation = ModelEvaluation(
        data_transformation_artifact=data_transformation_artifact,
        model_trainer_artifact=model_trainer_artifact,
        model_evaluation_config=ModelEvaluationConfig()
    )

    model_evaluation_artifact = (
        model_evaluation.initiate_model_evaluation()
    )

    print(model_evaluation_artifact)