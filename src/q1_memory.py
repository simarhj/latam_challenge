import json
from typing import List, Tuple
from datetime import datetime

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Initialize a dictionary to store the date and the user with the most posts
    top_users_per_date = {}

    # Iterate over the JSON file to find the dates with the most posts
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            date_str = tweet['date'][:10]  # Take only the date part
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            username = tweet['user']['username']
            
            # Update the user with the most posts for this date
            if date not in top_users_per_date:
                top_users_per_date[date] = {'user': username, 'count': 1}
            else:
                top_users_per_date[date]['count'] += 1

    # Sort the dictionary by the count of posts and take the top 10 dates
    top_10_dates = sorted(top_users_per_date.items(), key=lambda x: x[1]['count'], reverse=True)[:10]

    # Create the output list with the dates and the users with most posts
    result = [(date, data['user']) for date, data in top_10_dates]

    return result