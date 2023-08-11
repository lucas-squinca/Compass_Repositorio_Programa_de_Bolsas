select * from tbvendedor
select * from tbestoqueproduto
select * from tbvendas
-- E8

select
	vendedor.cdvdd,
	nmvdd
from tbvendedor as vendedor
left join tbvendas as vendas
	on vendedor.cdvdd = vendas.cdvdd
where status = 'Concluído'
group by vendedor.nmvdd
order by count(vendas.nmpro) desc
limit 1 
---------------------------------------

-- E9

select
	vendas.cdpro,
	vendas.nmpro
from tbvendas as vendas
where status = 'Concluído' 
	and dtven >= '2014-02-03' 
	and dtven <= '2018-02-02'
group by vendas.nmpro
order by count(vendas.nmpro) desc
limit 1
--------------------------------------

-- E10

select
	vendedors.nmvdd as vendedor,
	sum(vendas.qtd * vendas.vrunt) as valor_total_vendas,
	sum(vendas.qtd * vendas.vrunt) * vendedors.perccomissao/100 as comissao
from tbvendedor as vendedors
left join tbvendas as vendas
	on vendas.cdvdd = vendedors.cdvdd
where status = 'Concluído'
group by vendedor
order by comissao desc
--------------------------------------

-- E11
SELECT 
	cdcli,
	nmcli,
	count(cdven) * (qtd * vrunt) as gasto
from tbvendas as vendas
where status = 'Concluído'
group by cdcli
order by gasto desc
limit 1
--------------------------------------

-- E12
SELECT 
	cddep,
	nmdep,
	dtnasc,
	sum(vendas.qtd * vendas.vrunt) as valor_total_vendas

from tbdependente as dep
left join tbvendas as vendas
	on dep.cdvdd = vendas.cdvdd
where status = 'Concluído'
group by nmdep
order by valor_total_vendas
limit 1
--------------------------------------

-- E13
select * from tbvendas
select * from tbestoqueproduto
select 
	cdpro,
	nmcanalvendas,
	nmpro,
	sum(vendas.qtd) as quantidade_vendas
from tbvendas as vendas
where status = 'Concluído'
group by vendas.cdpro, nmcanalvendas
order by quantidade_vendas
--------------------------------------

-- E14
SELECT 
	vendas.estado,
	(avg(qtd * vrunt):DECIMAL, 2) as gastomedio
from tbvendas as vendas
where status= 'Concluído'
group by estado 
order by gastomedio
--------------------------------------

-- E15
select * from tbvendas

select
	vendas.cdven,
	vendas.deletado
from tbvendas as vendas
where deletado is not 0
order by cdven
--------------------------------------

-- E16
select
	estado,
	vendas.nmpro,
	round(avg(vendas.qtd), 4) as quantidade_media
from tbvendas as vendas
where status = 'Concluído'
group by estado, vendas.nmpro
order by estado