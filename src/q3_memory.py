import pandas as pd
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Initialize a dictionary to store the counts
    mentions_count = {}

    # Read the JSON file
    data = pd.read_json(file_path, lines=True)

    # Iterate over each row in the DataFrame
    for index, row in data.iterrows():
        # Check if 'mentionedUsers' column is not None
        if row['mentionedUsers'] is not None:
            # Iterate over the list of dictionaries in the 'mentionedUsers' column
            for user_dict in row['mentionedUsers']:
                # Extract the username from each dictionary
                username = user_dict.get('username')
                if username:
                    # Update the count in the dictionary
                    mentions_count[username] = mentions_count.get(username, 0) + 1

    # Convert the dictionary to a list of tuples and return
    return list(mentions_count.items())

