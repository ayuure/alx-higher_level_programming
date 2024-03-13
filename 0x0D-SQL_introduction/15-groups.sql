-- list the records of scores with same number 
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;