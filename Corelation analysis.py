import pandas as pd
import numpy as np

# Function to calculate normalized cross-correlation with lags
def crosscorr(datax, datay, lag=0):
    shiftedy = datay.shift(-lag)  # Negative shift for forward lags
    shiftedy = shiftedy[~np.isnan(shiftedy)]
    return datax.corr(shiftedy)

# Load the data from an Excel file
def load_and_process_data(file_name):
    # Load the data
    data = pd.read_excel(file_name)
    
    # Clean the data by dropping rows with NaN values in 'Facial Covering Policy' or 'New Cases'
    clean_data = data.dropna(subset=['Facial Covering Policy', 'New Cases (7 day Rolling Average)'])
    
    return clean_data

# Calculate and print cross-correlation coefficients for forward lags up to a year
def calculate_forward_lag_correlations(clean_data):
    # Extract the series
    masking_policy = clean_data['Facial Covering Policy']
    new_cases = clean_data['New Cases (7 day Rolling Average)']
    
    # Calculate cross-correlation for each month up to 12 months forward
    for lag in range(1, 13):  # 1 to 12 month lags
        corr = crosscorr(masking_policy, new_cases, lag)
        print(f"Lag {lag} months: Correlation coefficient = {corr}")

# Main function to execute the workflow
def main(file_name):
    clean_data = load_and_process_data(file_name)
    calculate_forward_lag_correlations(clean_data)

# Example usage:
file_name = 'Combined Data for masking Analysis.xlsx' # The Excel file name
main(file_name)
