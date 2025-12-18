import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler

def clean_and_scale(df):
    """
    Standardizes 'Time' and 'Amount' using RobustScaler 
    to handle financial outliers.
    """
    rob_scaler = RobustScaler()
    
    df['scaled_amount'] = rob_scaler.fit_transform(df['Amount'].values.reshape(-1,1))
    df['scaled_time'] = rob_scaler.fit_transform(df['Time'].values.reshape(-1,1))
    
    # Remove original unscaled columns
    df.drop(['Time', 'Amount'], axis=1, inplace=True)
    
    return df

def get_balanced_subsample(df):
    """
    Creates a 50/50 balanced dataset for training 
    to address severe class imbalance.
    """
    # Shuffle the data
    df = df.sample(frac=1)
    
    fraud_df = df.loc[df['Class'] == 1]
    non_fraud_df = df.loc[df['Class'] == 0][:len(fraud_df)]
    
    balanced_df = pd.concat([fraud_df, non_fraud_df])
    
    # Shuffle the final subsample
    return balanced_df.sample(frac=1, random_state=42)
