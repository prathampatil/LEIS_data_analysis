# This file is configured for only 2 element profiles. Later updates will come soon
import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askdirectory

def main():
    # Hide the root Tk window and prompt the user to select a folder
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    folder_path = askdirectory(title="Select Folder Containing Depth Profile .txt Files")
    root.destroy()

    if not folder_path:
        print("No folder selected. Exiting.")
        return

    # Find all .txt files in the selected folder
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    if not txt_files:
        print(f"No .txt files found in: {folder_path}")
        return

    for txt_file in txt_files:
        try:
            # Read the .txt file as tab-delimited and with latin-1 encoding
            df = pd.read_csv(txt_file, sep='\t', header=0, encoding='latin-1')
        except Exception as e:
            print(f"Error reading '{txt_file}': {e}")
            continue

        # Ensure there are at least 5 columns
        if df.shape[1] < 5:
            print(f"Skipping '{txt_file}': less than 5 columns detected.")
            continue

        # Extract:
        #   - X  = column 0
        #   - Y1 = column 3 (4th column in header)
        #   - Y2 = column 4 (5th column in header)
        x = df.iloc[:, 0]
        y1 = df.iloc[:, 3]
        y2 = df.iloc[:, 4]
        y1_name = df.columns[3]
        y2_name = df.columns[4]

        # Base filename without extension
        base_name = os.path.splitext(os.path.basename(txt_file))[0]

        # --- Plot 1: Normal scale (data points) ---
        plt.figure()
        plt.plot(x, y1, marker='o', linestyle='-', label=y1_name)
        plt.plot(x, y2, marker='o', linestyle='-', label=y2_name)
        plt.xlabel(df.columns[0])
        plt.ylabel("Value")
        plt.title(f"{base_name}")
        plt.legend()
        plt.grid(True)

        normal_fname = os.path.join(folder_path, f"{base_name}_normal.png")
        plt.savefig(normal_fname, dpi=300, bbox_inches='tight')
        plt.close()

        # --- Plot 2: Log scale for Y1 and Y2 (data points) ---
        # Replace non-positive values with NaN so log() doesn't error
        y1_log = np.log(y1.replace({0: np.nan}))
        y2_log = np.log(y2.replace({0: np.nan}))

        plt.figure()
        plt.plot(x, y1_log, marker='o', linestyle='-', label=f"log({y1_name})")
        plt.plot(x, y2_log, marker='o', linestyle='-', label=f"log({y2_name})")
        plt.xlabel(df.columns[0])
        plt.ylabel("Log(Value)")
        plt.title(f"{base_name}")
        plt.legend()
        plt.grid(True)

        log_fname = os.path.join(folder_path, f"{base_name}_log.png")
        plt.savefig(log_fname, dpi=300, bbox_inches='tight')
        plt.close()

        print(f"Processed '{txt_file}':")
        print(f"  • Saved normal plot → '{normal_fname}'")
        print(f"  • Saved log plot    → '{log_fname}'\n")

if __name__ == "__main__":
    main()