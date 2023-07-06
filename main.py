from CNNclassifier import logger
from CNNclassifier.pipeline.stage_01_data_ingesation import DataIngestionTrainingPipeline



STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e