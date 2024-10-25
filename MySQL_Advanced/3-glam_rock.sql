-- ranked by their longevity .
SELECT band_name, 
COALESCE(split, 2020) - formed as lifespan
FROM metal_bands
where 
 style LIKE '%Glam rock%';