import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy import signal

def plot_all_files(folder_path,c):
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist.")
        return
    
    # Process all .txt files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith("properties.txt"):  # Ignore the properties files so that they dont cause error
            continue
        if filename.endswith(".txt"):  # Only process .txt files
            file_path = os.path.join(folder_path, filename)
            
            try:
                # Read the file data
                with open(file_path, 'r', encoding='utf-8') as file:
                    
                    data = pd.read_csv(file, sep='\s+', skiprows=4, header=None, names=['X','Y'])
                    X = data['X']
                    Y = data['Y']

                if c == 'y':
                    Y = signal.savgol_filter(Y, 51, 3) # window size 51, polynomial order 3
                    print("savgol")

                plt.plot(X,Y,'r')
                plt.title(str(filename))
                plt.xlabel("Energy (eV)")
                plt.ylabel("Intensity")
                plt.tight_layout()
                plt.title(str(filename))

                pltname = str(filename) + '.png'
                plt.savefig(os.path.join(folder_path, pltname))
                plt.close()
               
                print(f"Processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing .txt files: ")
    d_clean = input("Do you want to clean the data? y/n")
    plot_all_files(folder_path, d_clean)