import pandas as pd

def load_news_data(file_path):
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        raise Exception(f"The file at {file_path} was not found.")

    data.dropna(subset=['article_id', 'source_name', 'title', 'content'], inplace=True)
    
    if 'published_at' in data.columns:
        data['published_at'] = pd.to_datetime(data['published_at'], errors='coerce')
    
    if 'title_sentiment' in data.columns:
        data['title_sentiment'] = pd.Categorical(data['title_sentiment'], categories=['negative', 'neutral', 'positive'])
    
    return data
