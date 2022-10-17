import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

total_v = 0
# Helper function for the Total Return calculation
def calculate(value):
    global total_v
    if total_v == 0:
        total_v = value
    else:
        total_v *= value
    return (total_v - 1) * 100

def main():

    # --- Data formatting 

    # Read data into DataFrame object.
    data = pd.read_csv('rawdata.csv')
    # Drop the name column because it is the same for every row.
    data = data.drop(columns=['Name'])
    # Create the add1PercentSpace column for total return calculation
    data['Add1InPercentSpace'] = 1 + data['DailyReturn']/100

    data['Total Return'] = data['Add1InPercentSpace'].map(calculate)

    #-------------

    data.plot(x=0, y=3, title="Total Return", xlabel="", legend=False, figsize=(10, 5))

    # X-ticks
    REFERENCE_DATA = list(data['ReferenceDate'])
    REFERENCE_DATA_LENGTH = len(REFERENCE_DATA)
    steps = np.arange(0, REFERENCE_DATA_LENGTH, 253)
    labels = [REFERENCE_DATA[x] for x in steps]
    plt.xticks(steps, labels, fontsize=7, rotation=50)

    # Y-ticks
    plt.yticks([0.0, 500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3000.0], 
    ["0%", "500%", "1000%", "1500%", "2000%", "2500%", "3000%"])

    # Create solid color for data.
    plt.fill_between(REFERENCE_DATA, data['Total Return'])
    plt.show()

main()