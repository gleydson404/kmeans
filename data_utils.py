import numpy as np


def load_dataset(dataset_name):
    return np.loadtxt(f"data/{dataset_name}")
