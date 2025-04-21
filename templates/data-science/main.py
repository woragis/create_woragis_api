# main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
from pathlib import Path

# Your own modules (to be created in your project)
# from src.data_loader import load_data
# from src.analysis import run_analysis
# from src.visualization import generate_plots
# from src.modeling import train_model

DATA_PATH = Path("data/your_dataset.csv")


def load_data(path: Path) -> pd.DataFrame:
    print(f"Loading data from: {path}")
    return pd.read_csv(path)


def explore_data(df: pd.DataFrame):
    print("Dataset Head:")
    print(df.head())

    print("\nBasic Info:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe())


def visualize_data(df: pd.DataFrame):
    print("Generating plots...")

    sns.set(style="whitegrid")
    for column in df.select_dtypes(include=np.number).columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[column].dropna(), kde=True)
        plt.title(f"Distribution of {column}")
        plt.tight_layout()
        plt.savefig(f"outputs/plots/{column}_hist.png")
        plt.close()


def main(args):
    df = load_data(DATA_PATH)
    explore_data(df)

    if args.visualize:
        visualize_data(df)

    # Example model training call:
    # if args.train:
    #     model = train_model(df)
    #     model.save("outputs/model.pkl")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run data science project")
    parser.add_argument("--visualize", action="store_true",
                        help="Generate data visualizations")
    # parser.add_argument("--train", action="store_true", help="Train model")
    args = parser.parse_args()

    main(args)
