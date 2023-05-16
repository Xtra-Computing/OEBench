from pipeline import *
import logging

mkdirs("logs/")

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

log_file_name = 'logs/experiment_log-%s.log' % (datetime.datetime.now().strftime("%Y-%m-%d-%H:%M-%S"))

logging.basicConfig(
    filename=log_file_name,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M', level=logging.INFO, filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

selected_dataset = ['dataset_experiment_info/room_occupancy', 'dataset_experiment_info/electricity_prices', 'dataset_experiment_info/insects/incremental_reoccurring_balanced', 'dataset_experiment_info/beijing_multisite/shunyi', 'dataset_experiment_info/tetouan']
selected_dataset = ['dataset_experiment_info/beijing_multisite/shunyi']

for dataset_path_prefix in selected_dataset:
    logger.info(dataset_path_prefix)
    data_path, schema_path, task = schema_parser(dataset_path_prefix)

    input, target = data_preprocessing(dataset_path_prefix, data_path, schema_path, task, logger, delete_null_target=True)
    logger.info(input)
    logger.info(target)
    logger.info(input.isnull().values.any())
    logger.info(target.isnull().values.any())
