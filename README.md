# LEIS_data_analysis
This repository deals with the data analysis and plotting protocols used for data from the qTac100 Low Energy Ion Scattering Spectroscopy. The current code can convert all the commas to decimal points and plot the files. This can be done together with ```LEIS_convert_and_plot.py``` or separately using ```commadotconverter.py``` and ```plot_all_leis.py``` respectively. 

# Insructions to use
* Open terminal and the change directory to the path you stored the codes to using ```cd <path here>```
* First check if you have python installed by inputting ```python --version``` in your terminal. The version should be >3.9. If not update it.
* Download the whole folder or clone the repository locally whichever you choose
* Check if you have ```pip``` installed using ```python3 -m pip --version```
* If you don't have, install ```pip``` using ```python3 -m ensurepip --default-pip```
* Install the requirements file using ```pip install -r requirements.txt```
* Run the code using ```python3 <filename>.py``` and insert the folder path by copypasting the path from the folder info
* When asked if you want to clean the data, input y or n depending on whether you want to clean the data using the Savitzky-Golay filter
* You can change the parameters for the filter in the code, just make sure the second number is less than the first number.
* Once the data is converted, you should see ```Processed <filename>``` appear in the terminal
* Once the filter is applied, you should see ```savgol filter applied``` appear in the terminal
* Once the plotting is done you should see ```Plotted <filename>``` appear in the terminal
* Once all of this is done, the plots will be stored as ```<filename>,png``` in the folder where the data files are

