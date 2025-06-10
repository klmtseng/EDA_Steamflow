# Exploratory Data Analysis tool with file selection
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def select_file():
    """Open a dialog to select a data file."""
    root = Tk()
    root.withdraw()
    file_path = askopenfilename()
    root.destroy()
    return file_path


def load_data(path):
    """Load data according to file extension."""
    ext = os.path.splitext(path)[1].lower()
    if ext == '.csv':
        return pd.read_csv(path)
    if ext in ['.xls', '.xlsx']:
        return pd.read_excel(path)
    if ext == '.json':
        return pd.read_json(path)
    raise ValueError(f'Unsupported file type: {ext}')


def perform_basic_eda(df):
    """Display basic EDA outputs."""
    print("Shape:", df.shape)
    print("\nHead:\n", df.head())
    print("\nInfo:")
    print(df.info())
    print("\nDescribe:\n", df.describe(include='all'))
    print("\nMissing values:\n", df.isnull().sum())
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:
        sns.pairplot(df[numeric_cols])
        plt.show()
        corr = df[numeric_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.show()


def main():
    path = select_file()
    if not path:
        print('No file selected.')
        return
    df = load_data(path)
    perform_basic_eda(df)


if __name__ == '__main__':
    main()
