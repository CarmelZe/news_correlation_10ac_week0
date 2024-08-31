import psycopg2
from config import config
import pandas as pd

# Function to insert sources
def insert_sources(data_df):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        sources = data_df['source_name'].unique()
        for source in sources:
            cur.execute("INSERT INTO sources (source_name) VALUES (%s) ON CONFLICT DO NOTHING", (source,))

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Function to insert articles
def insert_articles(data_df):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for index, row in data_df.iterrows():
            cur.execute("""
                INSERT INTO articles 
                (source_id, published_at, content_length, title_word_count, 
                 title_sentiment, title_sentiment_numeric, dominant_topic, 
                 category, event_cluster, title_keywords, content_keywords, keyword_similarity)
                VALUES (
                    (SELECT source_id FROM sources WHERE source_name = %s),
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
                """, (
                    row['source_name'], row['published_at'], row['content_length'], 
                    row['title_word_count'], row['title_sentiment'], row['title_sentiment_numeric'], 
                    row['dominant_topic'], row['category'], row['event_cluster'], 
                    ','.join([kw[0] for kw in row['title_keywords']]), 
                    ','.join([kw[0] for kw in row['content_keywords']]), 
                    row['keyword_similarity']
                ))

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # Load your data
    data_df = pd.read_csv('../data/rating.csv')
    
    # Insert sources first
    insert_sources(data_df)
    
    # Insert articles after sources have been inserted
    insert_articles(data_df)
