import pandas as pd
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Initialize an empty list to store the usernames
    usernames = []

    # Read the JSON file
    data = pd.read_json(file_path, lines=True)

    # Iterate over each row in the DataFrame
    for index, row in data.iterrows():
        # Check if 'mentionedUsers' column is not None
        if row['mentionedUsers'] is not None:
            # Iterate over the list of dictionaries in the 'mentionedUsers' column
            for user_dict in row['mentionedUsers']:
                # Extract the username from each dictionary and append it to the list
                usernames.append(user_dict['username'])

    # Count occurrences of each username
    mentions_count = pd.Series(usernames).value_counts().to_dict()

    return mentions_count
