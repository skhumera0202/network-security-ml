from dataclasses import dataclass
from pathlib import Path


@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = "network_security"
    artifact_dir: str = "Artifacts"


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = "data_ingestion"
    feature_store_file_path: str = "feature_store/phisingData.csv"
    training_file_path: str = "Artifacts/data_ingestion/train.csv"
    testing_file_path: str = "Artifacts/data_ingestion/test.csv"
    data_source_url: str = ""


@dataclass
class DataValidationConfig:
    validation_status: bool = True
    valid_data_dir: str = "valid_data"
    invalid_data_dir: str = "invalid_data"
    valid_train_file_path: str = "valid_data/train.csv"
    valid_test_file_path: str = "valid_data/test.csv"
    invalid_train_file_path: str = "invalid_data/train.csv"
    invalid_test_file_path: str = "invalid_data/test.csv"
    drift_report_file_path: str = "Artifacts/data_validation/drift_report.yaml"

@dataclass
class DataTransformationConfig:
    transformed_train_file_path: str = (
        "Artifacts/data_transformation/train.npy"
    )

    transformed_test_file_path: str = (
        "Artifacts/data_transformation/test.npy"
    )

    preprocessor_object_file_path: str = (
        "Artifacts/data_transformation/preprocessor.pkl"
    )

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = (
        "Artifacts/model_trainer/trained_model.pkl"
    )

@dataclass
class ModelEvaluationConfig:
    model_evaluation_file_path: str = (
        "Artifacts/model_evaluation/evaluation.yaml"
    )