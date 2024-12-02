from Training.configration_manager.configuration import ConfigurationManager
from Training.Components.Common.data_validation import DataValidation
from Training.custom_logging import info_logger
import sys

PIPELINE = "Data Validation Training Pipeline"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        # Load the data validation configuration object
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        # Passing the data validation configuration obj to the component
        data_validation = DataValidation(config=data_validation_config)
        data_validation.check_all_data_is_categorical_numerical()
            


if __name__ == "__main__":
    info_logger.info(f">>>>>>>> {PIPELINE} sttarted <<<<<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    info_logger.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")