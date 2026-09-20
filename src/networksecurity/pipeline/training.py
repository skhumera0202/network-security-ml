import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.model_evaluation import ModelEvaluation

from networksecurity.entity.config_entity import (
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig
)

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class TrainingPipeline:

    def __init__(self):
        pass

    def start_data_ingestion(self):
        logging.info("Starting Data Ingestion")

        data_ingestion = DataIngestion()

        data_ingestion_artifact = (
            data_ingestion.initiate_data_ingestion()
        )

        return data_ingestion_artifact

    def start_data_validation(self, data_ingestion_artifact):
        logging.info("Starting Data Validation")

        data_validation = DataValidation(
            data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config=DataValidationConfig()
        )

        data_validation_artifact = (
            data_validation.initiate_data_validation()
        )

        return data_validation_artifact

    def start_data_transformation(self, data_validation_artifact):
        logging.info("Starting Data Transformation")

        data_transformation = DataTransformation(
            data_validation_artifact=data_validation_artifact,
            data_transformation_config=DataTransformationConfig()
        )

        data_transformation_artifact = (
            data_transformation.initiate_data_transformation()
        )

        return data_transformation_artifact

    def start_model_training(self, data_transformation_artifact):
        logging.info("Starting Model Training")

        model_trainer = ModelTrainer(
            data_transformation_artifact=data_transformation_artifact,
            model_trainer_config=ModelTrainerConfig()
        )

        model_trainer_artifact = (
            model_trainer.initiate_model_trainer()
        )

        return model_trainer_artifact

    def start_model_evaluation(
        self,
        data_transformation_artifact,
        model_trainer_artifact
    ):
        logging.info("Starting Model Evaluation")

        model_evaluation = ModelEvaluation(
            data_transformation_artifact=data_transformation_artifact,
            model_trainer_artifact=model_trainer_artifact,
            model_evaluation_config=ModelEvaluationConfig()
        )

        model_evaluation_artifact = (
            model_evaluation.initiate_model_evaluation()
        )

        return model_evaluation_artifact

    def run_pipeline(self):

        try:
            logging.info("========== Training Pipeline Started ==========")

            # 1. Data Ingestion
            data_ingestion_artifact = (
                self.start_data_ingestion()
            )

            # 2. Data Validation
            data_validation_artifact = (
                self.start_data_validation(
                    data_ingestion_artifact
                )
            )

            if not data_validation_artifact.validation_status:
                raise Exception(
                    "Data validation failed."
                )

            # 3. Data Transformation
            data_transformation_artifact = (
                self.start_data_transformation(
                    data_validation_artifact
                )
            )

            # 4. Model Training
            model_trainer_artifact = (
                self.start_model_training(
                    data_transformation_artifact
                )
            )

            # 5. Model Evaluation
            model_evaluation_artifact = (
                self.start_model_evaluation(
                    data_transformation_artifact,
                    model_trainer_artifact
                )
            )

            logging.info(
                f"Model accepted: "
                f"{model_evaluation_artifact.is_model_accepted}"
            )

            logging.info(
                f"Test accuracy: "
                f"{model_evaluation_artifact.test_accuracy}"
            )

            logging.info("========== Training Pipeline Completed ==========")

            return model_evaluation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    pipeline = TrainingPipeline()

    artifact = pipeline.run_pipeline()

    print("\nTraining Pipeline Result:")
    print(artifact)