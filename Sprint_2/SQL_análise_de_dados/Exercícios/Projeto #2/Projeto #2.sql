-- (Query 1) Gênero dos leads
-- Colunas: gênero, leads(#)

select
	case
		when ibge.gender = 'male' then 'homens'
		when ibge.gender = 'female' then 'mulheres'
		end as "gênero",
	count(*) as "leads (#)"

from sales.customers as cus
left join temp_tables.ibge_genders as ibge
	on lower(cus.first_name) = lower(ibge.first_name)
group by ibge.gender
-- (Query 2) Status profissional dos leads
-- Colunas: status profissional, leads (%)

--select distinct professional_status
--from sales.customers

select
	case
		when professional_status = 'freelancer' then 'freelancer'
		when professional_status = 'retired' then 'aposentado'
		when professional_status = 'clt' then 'clt'
		when professional_status = 'self_employed' then 'autônomo'
		when professional_status = 'other' then 'outro'
		when professional_status = 'businessman' then 'empresário'
		when professional_status = 'civil_servant' then 'funcionário público'
		when professional_status = 'student' then 'estudante'
		end as "status profissional",
	(count(*)::float)/(select count(*) from sales.customers) as "leads (%)"
		
from sales.customers
group by professional_status
order by "leads (%)"

-- (Query 3) Faixa etária dos leads
-- Colunas: faixa etária, leads (%)

select
	case
		when datediff('y', birth_date, current_date) < 20 then '0-20'
		when datediff('y', birth_date, current_date) < 40 then '20-40'
		when datediff('y', birth_date, current_date) < 60 then '40-60'
		when datediff('y', birth_date, current_date) < 80 then '60-80'
		else '80+' end "faixa etária",
		count(*)::float/(select count(*) from sales.customers) as "leads (%)"

from sales.customers
group by "faixa etária"
order by "faixa etária" desc
-- (Query 4) Faixa salarial dos leads
-- Colunas: faixa salarial, leads (%), ordem

select
	case
		when income < 5000 then '0-5000'
		when income < 10000 then '5000-10000'
		when income < 15000 then '10000-15000'
		when income < 20000 then '15000-20000'
		else '20000+' end "faixa etária",
		count(*)::float/(select count(*) from sales.customers) as "leads (%)",
		case
			when income < 5000 then 1
			when income < 10000 then 2
			when income < 15000 then 3
			when income < 20000 then 4
			else 5 end "ordem"

from sales.customers
group by "faixa etária", "ordem"
order by "ordem" desc

-- (Query 5) Classificação dos veículos visitados
-- Colunas: classificação do veículo, veículos visitados (#)
-- Regra de negócio: Veículos novos tem até 2 anos e seminovos acima de 2 anos
with
	classificacao_veiculos as (
		
		select
			fun.visit_page_date,
			pro.model_year,
			extract('y' from visit_page_date) - pro.model_year::int as idade_veiculo,
			case
				when extract('y' from visit_page_date) - pro.model_year::int <= 2 then 'novo'
				else 'semi novo' end as "classificação do veículo"
		from sales.funnel as fun
		left join sales.products as pro
			on fun.product_id = pro.product_id
	)

select
	"classificação do veículo",
	count(*) as "veículos visitados (#)"
from classificacao_veiculos
group by "classificação do veículo"

-- (Query 6) Idade dos veículos visitados
-- Colunas: Idade do veículo, veículos visitados (%), ordem
with
	faixa_de_idade_dos_veículos as (
		
		select
			fun.visit_page_date,
			pro.model_year,
			extract('y' from visit_page_date) - pro.model_year::int as idade_veiculo,
			case
				when extract('y' from visit_page_date) - pro.model_year::int <= 2 then 'até dois anos'
				when extract('y' from visit_page_date) - pro.model_year::int <= 4 then 'de dois a quatro anos'
				when extract('y' from visit_page_date) - pro.model_year::int <= 6 then 'de quatro a seis anos'
				when extract('y' from visit_page_date) - pro.model_year::int <= 8 then 'de seis a oito anos'
				when extract('y' from visit_page_date) - pro.model_year::int <= 10 then 'de oito a dez anos'
				else 'acima de dez anos'
				end as "idade_do_veículo",
			case
				when extract('y' from visit_page_date) - pro.model_year::int <= 2 then 1
				when extract('y' from visit_page_date) - pro.model_year::int <= 4 then 2
				when extract('y' from visit_page_date) - pro.model_year::int <= 6 then 3
				when extract('y' from visit_page_date) - pro.model_year::int <= 8 then 4
				when extract('y' from visit_page_date) - pro.model_year::int <= 10 then 5
				else 6
				end as "ordem"
		from sales.funnel as fun
		left join sales.products as pro
			on fun.product_id = pro.product_id
	)

select
	"idade_do_veículo",
	count(*)::float/(select count(*) from sales.funnel) as "veículos visitados (%)",
	ordem
from faixa_de_idade_dos_veículos
group by "idade_do_veículo", ordem
order by ordem



-- (Query 7) Veículos mais visitados por marca
-- Colunas: brand, model, visitas (#)
select
	pro.brand,
	pro.model,
	count(*) as "visitas (#)"

from sales.funnel as fun
left join sales.products as pro
	on fun.product_id = pro.product_id
group by pro.brand, pro.model
order by pro.brand, pro.model, "visitas (#)"









