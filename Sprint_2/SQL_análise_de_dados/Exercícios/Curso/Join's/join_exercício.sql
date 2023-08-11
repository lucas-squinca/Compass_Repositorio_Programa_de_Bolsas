-- EXERCÍCIOS ########################################################################

-- (Exercício 1) Identifique quais as marcas de veículo mais visitada na tabela sales.funnel

-- Minha tentativa (correto!)
select 
	modelo.brand, count(visitas.visit_id) as contagem
from sales.products as modelo
left join sales.funnel as visitas
	on modelo.product_id = visitas.product_id
group by modelo.brand
order by contagem desc


-- Correto:
select 
	pro.brand,
	count(*) as visitas

from sales.funnel as fun
left join sales.products as pro
	on fun.product_id = pro.product_id
group by pro.brand
order by visitas desc
-- (Exercício 2) Identifique quais as lojas de veículo mais visitadas na tabela sales.funnel

-- Minha tentativa (correto!)
select
	loja.store_name, count(visitas.visit_id) as visits
from sales.stores as loja
left join sales.funnel as visitas
	on loja.store_id = visitas.store_id
group by loja.store_name
order by visits desc

-- Correto:
select 
	sto.store_name,
	count(*) as visitas

from sales.funnel as fun
left join sales.stores as sto
	on fun.store_id = sto.store_id
group by sto.store_name
order by visitas desc
-- (Exercício 3) Identifique quantos clientes moram em cada tamanho de cidade (o porte da cidade
-- consta na coluna "size" da tabela temp_tables.regions)

-- Minha tentativa: (Não consta o "null")
select tamanho.size, count(clientes.customer_id) as clients
from temp_tables.regions as tamanho
left join sales.customers as clientes
	on lower(tamanho.city) = lower(clientes.city)
	and lower(tamanho.state) = lower(clientes.state)
group by tamanho.size
order by clients desc

-- Correto:
select
	reg.size,
	count(*) as contagem
from sales.customers as cus
left join temp_tables.regions as reg
	on lower(cus.city) = lower(reg.city)
	and lower(cus.state) = lower(reg.state)
group by reg.size
order by contagem desc
