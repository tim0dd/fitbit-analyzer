import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from app.util.paths import get_out_path

def plot_sleep_data(data: pd.DataFrame, columns: list,  out_path: str=None) -> None:
    """
    Generate and save plots for specified columns in sleep data.

    :param data: DataFrame containing the sleep score data.
    :param output_folder: Path to the folder where plots will be saved.
    :param columns: List of columns to plot.
    """
    if out_path is None:
        out_path = get_out_path()
    
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    for column in columns:
        unavailable_columns = [c for c in columns if c not in data.columns]
        if len(unavailable_columns) > 0:
            raise ValueError(f'Columns {unavailable_columns} do not exist in the loaded sleep data.\n Available columns: {data.columns}')
    
    for column in columns:
        if column in data.columns:
            plt.figure(figsize=(10, 6), dpi=300)
            sns.lineplot(data=data, x=data.index, y=column)
            plt.title(f'{column} Over Time')
            plt.ylabel(column)
            plt.xlabel('Time')
            plt.savefig(f'{out_path}/{column}_plot.png')
            plt.close()
            
