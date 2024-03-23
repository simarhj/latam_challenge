from typing import List, Tuple
import pandas as pd
import emoji

def extract_emojis(text: str) -> List[str]:
    """Helper function to extract emojis from a text."""
    return [emoji_data['emoji'] for emoji_data in emoji.emoji_list(text)]

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """Function to find the top 10 most used emojis with their respective count (memory approach)."""
    data = pd.read_json(file_path, lines=True)
    
    # Extract emojis from tweets and count their frequency
    emoji_freq = data['content'].apply(lambda x: pd.Series(extract_emojis(x))).stack().value_counts().head(10)
    
    return [(emoji, count) for emoji, count in emoji_freq.items()]