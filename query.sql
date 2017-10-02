-- https://bigquery.cloud.google.com/results/test-mail-project:bquijob_1c2f26cb_15eb57c3e19
-- Query to select top-level comments to /r/DailyProgrammer
SELECT 
    c.id, c.body, c.author, c.created_utc, c.parent_id, p.title AS parent_title 
FROM 
    [fh-bigquery:reddit_comments.2017_06] c 
JOIN 
    (SELECT CONCAT('t3_', id) AS id, title, created_utc FROM [fh-bigquery:reddit_posts.2017_06]) p 
ON
    c.parent_id = p.id
WHERE 
    c.subreddit = 'dailyprogrammer' AND c.parent_id LIKE 't3_%' AND body <> '[deleted]';
