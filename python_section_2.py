import pandas as pd
from scipy.spatial.distance import pdist, squareform
def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic 
    

    if df.empty:
        raise ValueError("Input DataFrame is empty.")
    
    # Calculate the pairwise distances
    distances = pdist(df.values)
    
    # Convert the distances to a square form
    distance_matrix = squareform(distances)
    
    # Create a DataFrame from the distance matrix
    distance_df = pd.DataFrame(distance_matrix, index=df.index, columns=df.index)
    
    # Unroll the distance matrix to long format
    df = distance_df.stack().reset_index()
    df.columns = ['Source', 'Target', 'Distance']
    
   

    return df

from scipy.spatial.distance import pdist, squareform
def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
  

    if df.empty:
        raise ValueError("Input DataFrame is empty.")
    
    # Calculate pairwise distances using pdist
    distances = pdist(df.values)
    
    # Convert the distances to a square form
    distance_matrix = squareform(distances)
    
    # Create a DataFrame from the distance matrix
    distance_df = pd.DataFrame(distance_matrix, index=df.index, columns=df.index)
    
    # Unroll the distance matrix to long format
    df = distance_df.stack().reset_index()
    df.columns = ['Source', 'Target', 'Distance']
    
    # Remove duplicate entries by ensuring Source < Target
    unrolled_df = df[unrolled_df['Source'] < unrolled_df['Target']]
    
    

    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
   
    # Write your logic here
    

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("Input DataFrame is empty.")
    
    # Check if the reference_id exists in the DataFrame
    if reference_id not in df.index:
        raise ValueError(f"Reference ID {reference_id} not found in DataFrame.")
    
    # Get the reference value
    reference_value = df.loc[reference_id].values[0]
    
    # Calculate the lower and upper bounds
    lower_bound = reference_value * 0.90  # 10% lower
    upper_bound = reference_value * 1.10  # 10% higher
    
    # Find IDs within the threshold
    within_threshold = df[(df.values.flatten() >= lower_bound) & (df.values.flatten() <= upper_bound)]
    
    return within_threshold
    

    


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
   
    # Write your logic here
   
   
    required_columns = ['VehicleType', 'Distance']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"DataFrame must contain the following columns: {required_columns}")

    def calculate_toll(row):
        vehicle_type = row['VehicleType']
        distance = row['Distance']
        data = {}
        rate = data.get(vehicle_type, 0) 
        return rate * distance
    
  
    df['TollRate'] = df.apply(calculate_toll, axis=1)
    
    

    return df
