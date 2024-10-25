-- ranking country of origin--

import './metal_bands'

select origin, SUM(fans) as nb_fans from metal_bands 
GROUP BY origin ORDER BY nb_fans DESC;