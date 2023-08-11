-- EXERCÍCIOS ########################################################################

-- (Exercício 1) Crie uma coluna calculada com o número de visitas realizadas por cada
-- cliente da tabela sales.customers


with visita as (

	select
		count(*) as numero_visita,
		customer_id
	from sales.funnel 
	group by customer_id
) 

select
	numero_visita,
	cus.*
from sales.customers as cus
left join visita as vist
	on cus.customer_id = vist.customer_id
order by customer_id

-- Correto:
with numero_de_visitas as (

	select customer_id, count(*) as n_visitas
	from sales.funnel
	group by customer_id

)

select
	cus.*,
	n_visitas

from sales.customers as cus
left join numero_de_visitas as ndv
	on cus.customer_id = ndv.customer_id