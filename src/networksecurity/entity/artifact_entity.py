from dataclasses import dataclass
from typing import Optional


@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str


@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: Optional[str] = None
    valid_test_file_path: Optional[str] = None
    invalid_train_file_path: Optional[str] = None
    invalid_test_file_path: Optional[str] = None
    drift_report_file_path: Optional[str] = None

@dataclass
class DataTransformationArtifact:
    transformed_train_file_path: str
    transformed_test_file_path: str
    preprocessor_object_file_path: str

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str

@dataclass
class ModelEvaluationArtifact:
    is_model_accepted: bool
    trained_model_path: str
    test_accuracy: float