# Data processing pipeline under open environment setting

This data processing pipeline is specifically designed for open environment learning, providing a comprehensive analysis of datasets, including missing values statistics, anomaly detection, multi-dimensional and one-dimensional drift detection, and concept drift detection. The pipeline is designed to process multiple datasets and provide a detailed report on various metrics.

The whole project can be downloaded from https://drive.google.com/file/d/14I-QaquIefdaEChEXg_mxDHVlfHHiO9y/view?usp=share_link

## Table of Contents

- [Dependencies](#dependencies)
- [Usage](#usage)
- [Adding a New Dataset](#adding-a-new-dataset)
- [Function: run_pipeline](#function-run_pipeline)


## Dependencies

This project requires the following Python packages:

- numpy
- pandas
- scikit-learn
- scipy
- pyod
- Keras
- tensorflow
- torch
- rtdl
- delu
- lightgbm
- xgboost
- catboost
- copulas
- menelaus

To install these packages, you can use pip:

\```bash
pip install scikit-learn
\```

## Usage

1. Prepare `info.json` and `schema.json` for your datasets and place them in a folder named `dataset_experiment_info` in the same directory as this script. For each dataset, create a subfolder with the dataset's name.

2. If only the statistics for selected datasets are desired, in the script, update the `dataset_prefix_list` variable to include the desired dataset subfolders' names from the `dataset_experiment_info` folder. statistics for all datasets are desired, current code can remain unchanged as all dataset subfolders under the `dataset_experiment_info` folder will be iterated.

3. Run the script, and the pipeline will process each dataset in the specified list, generating various statistics and saving the results in separate CSV files within each dataset's subfolder. An `overall_stats.csv` file will also be generated, containing aggregated statistics for all datasets.


\```bash
python3 pipeline.py
\```

## Adding a New Dataset

To add a new dataset to the pipeline, follow these steps:

1. Create a new subfolder within the `dataset_experiment_info` folder, named after the dataset.
2. Place the dataset file (e.g., CSV or Excel) in the `dataset` folder.
3. Create a schema file `schema.json` and an dataset information file `info.json` for the dataset and place it in the same subfolder. 

4. If needed, add the dataset subfolder's name to the `dataset_prefix_list` variable in the script.

For example, to add a dataset called `my_new_dataset`, you should:

- Create a subfolder named `my_new_dataset` inside the `dataset_experiment_info` folder.
- Place the `my_new_dataset.csv` file (or any other supported format) inside the `dataset` subfolder.
- Create a schema file `schema.json` and a information file `info.json` and place them inside the `my_new_dataset` subfolder.
- If needed, manually add 'my_new_dataset' to the `dataset_prefix_list` variable in the script.

Template of `schema.json` of a dataset is as follows:
\```json
{
    "numerical": ["num1", "num2"],
    "categorical": ["cat1", "cat2"],
    "target": ["target"],
    "timestamp": ["date", "time"],
    "replace_with_null": ["column_to_be_replaced_by_null"],
    "window size": 0,
    "unnecessary": ["unnecessary1", "unnecessary2"]
}
\```

Template of `info.json` of a dataset is as follows:
\```json
{
    "schema": "schema.json",
    "data": "dataset/my_new_.csv",
    "task": "classification"
}
\```

## Function: run_pipeline

### Parameters

- `dataset_prefix_list`: A list of dataset path prefixes to process.
- `done`: A list of already processed datasets.

### Description

The `run_pipeline` function iterates through each dataset path prefix in the `dataset_prefix_list` and processes the dataset. For each dataset, the function performs the following steps:

1. Pre-processes the dataset and extracts its schema.
2. Processes missing values and calculates various missing value statistics.
3. Detect outliers using IForest and ECOD methods.
4. Detect multi-dimensional data drift using HDDDM, kdqTree and KS Statistics.
5. Detect one-dimensional data drift using KS Statistics, HDDDM, kdsTree, CBDB, and PCA-CD methods.
6. Detect concept drift using the PERM, ADWIN, DDM and EDDM method.

After processing each dataset, the function saves the calculated statistics in separate CSV files within each dataset's subfolder. Additionally, the `overall_stats.csv` file is generated, containing aggregated statistics for all datasets.




