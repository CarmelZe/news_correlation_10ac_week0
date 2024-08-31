CREATE TABLE IF NOT EXISTS ml_features (
    id SERIAL PRIMARY KEY,
    article_id INTEGER NOT NULL,
    source_id INTEGER NOT NULL,
    topic_id INTEGER,
    event_id INTEGER,
    feature_1 FLOAT,
    feature_2 FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
