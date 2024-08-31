import psycopg2
from config import config


def create_tables():
    """create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS sources (
            source_id SERIAL PRIMARY KEY,
            source_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS articles (
            article_id SERIAL PRIMARY KEY,
            source_id INTEGER NOT NULL,
            published_at TIMESTAMP,
            content_length INTEGER,
            title_word_count INTEGER,
            title_sentiment VARCHAR(10),
            title_sentiment_numeric INTEGER,
            dominant_topic INTEGER,
            category VARCHAR(255),
            event_cluster INTEGER,
            title_keywords TEXT,
            content_keywords TEXT,
            keyword_similarity FLOAT,
            FOREIGN KEY (source_id)
                REFERENCES sources (source_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS events (
            event_id SERIAL PRIMARY KEY,
            event_name VARCHAR(255)
        )
        """,
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    create_tables()
