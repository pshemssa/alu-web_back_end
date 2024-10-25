-- ranking country of origin--
select origin, SUM(fans) as nb_fans from metal_bands where 
GROUP BY origin ORDER BY nb_fans DESC;