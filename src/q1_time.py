import pandas as pd
from typing import List, Tuple
from datetime import datetime

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Read the JSON file
    data = pd.read_json(file_path, lines=True)

    # Convert the 'date' column to datetime type
    data['date'] = pd.to_datetime(data['date']).dt.date

    # Calculate the number of tweets per date
    tweets_per_date = data.groupby('date').size().reset_index(name='number_of_tweets')

    # Find the top 10 dates with the most tweets
    top_10_dates = tweets_per_date.nlargest(10, 'number_of_tweets')

    result = []

    # Iterate over the top 10 dates
    for date in top_10_dates['date']:
        # Filter tweets for the current date
        tweets_for_date = data[data['date'] == date]
        
        # Find the user with the most publications for the current date
        top_user = tweets_for_date['user'].apply(lambda x: x['username']).value_counts().idxmax()
        
        # Add the date and user to the result list
        result.append((datetime.strptime(str(date), '%Y-%m-%d').date(), top_user))

    return result
    

