-- ranking country of origin--


use metal_bands;
select origin, SUM(fans) as nb_fans 
from metal_bands 
GROUP BY origin 
ORDER BY nb_fans DESC;