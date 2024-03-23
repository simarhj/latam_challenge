from typing import List, Tuple
import pandas as pd
import emoji

def extract_emojis(text: str) -> List[str]:
    """Helper function to extract emojis from a text."""
    return [emoji_data['emoji'] for emoji_data in emoji.emoji_list(text)]

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """Function to find the top 10 most used emojis with their respective count (time approach)."""
    data = pd.read_json(file_path, lines=True)
    
    # Extract emojis from tweets
    data['emojis'] = data['content'].apply(extract_emojis)
    
    # Count the frequency of each emoji
    emoji_freq = [emoji for sublist in data['emojis'] for emoji in sublist]
    top_emojis = pd.Series(emoji_freq).value_counts().head(10)
    
    return [(emoji, count) for emoji, count in top_emojis.items()]