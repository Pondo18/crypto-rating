create materialized view crypto_analysed_scores as
SELECT date, crypto_currency_id, AVG(sentiment_score) as score
FROM reddit_posts p
JOIN reddit_sentimentscores s ON p.id = s.post_id
GROUP by date, crypto_currency_id;