from typing import Dict, List, Optional
from pathlib import Path
import json

import pandas as pd
from libs.strs import *


def read_json(path: str):
    """"
    Read json file from path
    path: str - path to json file
    return:
        dict object
    """
    with open(path, 'r') as f:
        return json.load(f)


def list_report(index_df: pd.DataFrame,
                metric_name: Optional[str] = None):
    """
    List report keys for a given metric name
    index_df: pd.DataFrame - index dataframe
    metric_name: str - metric name
    return:
        None
    """
    def list_report_keys(report, level=0):
        level_indent = '---' * level
        for k, v in report.items():
            print(f'{level_indent} {k}')
            if isinstance(v, dict):
                list_report_keys(v, level + 1)
    idf = index_df.copy()
    mask = idf[FEATURE_SET_NAME] == 'all-features'
    idf = idf[mask]
    report_path = idf[REPORT_PATH].iloc[0]
    report = read_json(str(Path(report_path, 'report.json')))
    if metric_name and metric_name in report:
        metric_report = dict()
        metric_report[metric_name] = report[metric_name]
        report = metric_report
    list_report_keys(report)


def create_label(deid_datasets: pd.DataFrame) -> List[any]:
    """
    Create a label for each deid dataset in the input dataframe.
    deid_datasets: pd.DataFrame - dataframe with index of deid datasets
    returns:
        labels: List[str] - list of labels for each deid dataset
    """
    labels: List[str] = []
    for i, row in deid_datasets.iterrows():
        # Create a label to distinguish deid datasets created using different
        # configurations.
        # We recommend to use following features from filtered index dataframe
        # to create a unique label for a deid dataset
        # List of properties for died dataset label:
        # * library name
        # * algorithm name
        # * target dataset
        # * feature set name
        # * team
        # * epsilon
        # * variant label
        # * submission number
        library_name = row[LIBRARY_NAME]
        algorithm_name = row[ALGORITHM_NAME]
        target_dataset = row[TARGET_DATASET]
        feature_set_name = row[FEATURE_SET_NAME]
        team = str(row[TEAM])  # convert to string
        epsilon = 'e' + str(row[EPSILON])  # convert to string
        variant_label = row[VARIANT_LABEL]
        submission_number = 's#' + str(row[SUBMISSION_NUMBER])  # conver to string

        # Join all labels to create a single string with each label
        # separated by a vertical bar.
        label = ' | '.join([library_name, algorithm_name, target_dataset,
                            feature_set_name, team, epsilon, variant_label,
                            submission_number])
        labels.append(label)
    return labels


def notebook_path() -> Path:
    """
    Get path to notebooks directory
    """
    notebooks_dir = Path(__file__).parent.parent
    return notebooks_dir


def index_feature_description(column_name: str):
    """
    Print the description for a given column name in the index.csv file
    column_name: str - column name in the index.csv file
    """
    cwd = Path.cwd()  # get current working directory path
    # Create path to the index.csv file
    index_desc_path = Path(cwd, 'index_definition.json')
    # Read the index_description.json file
    index_desc = read_json(str(index_desc_path))
    if column_name in index_desc:
        # Get the description for the column_name
        desc = index_desc[column_name]
        print()
        print(f'Index Column: \n-------------\n{column_name}\n\n\nDescription:\n-----------')
        for i, item in enumerate(desc):
            if i != 0:
                print()
            print(item)
    else:
        print(f'[Error] Invalid column name: {column_name}\n'
              f'column name must be one of the following:')
        for k in index_desc.keys():
            print(f'-- {k}')
