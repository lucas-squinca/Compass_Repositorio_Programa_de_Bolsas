-- E1

select *
from livro
where publicacao > '2014-12-31'
order by cod
----------------------------------

-- E2

select titulo,
	valor
from livro
order by valor desc
LIMIT 10
----------------------------------

-- E3

SELECT
	count(titulo) as quantidade,
	edi.nome,
	ende.estado,
	ende.cidade
from livro as liv
left join editora as edi
	on liv.editora = edi.codeditora
left join endereco as ende
	on ende.codendereco = edi.endereco
group by editora
order by quantidade desc

-----------------------------------

-- E4
SELECT
	nome,
	codautor,
	nascimento,
	count(titulo) as quantidade
from autor as aut
left join livro as liv
	on liv.autor = aut.codautor
group by aut.codautor
order by aut.nome

------------------------------------

-- E5
SELECT 
	aut.nome
from autor as aut
left join livro as liv 
	on aut.codautor = liv.autor
where liv.editora <> 13 
	and liv.editora <> 23 
	and liv.editora <> 29
	and liv.editora <> 69
	and liv.editora <> 70
	and liv.editora <> 71
	and liv.editora <> 72
group by aut.nome
order by aut.nome
------------------------------------

-- E6

SELECT 
	codautor,
	aut.nome,
	count(titulo) as quantidade_publicacoes
from autor as aut
left join livro as liv
	on aut.codautor = liv.autor
group by aut.nome 
order by quantidade_publicacoes desc
limit 1
-------------------------------------

-- E7
SELECT 
	aut.nome
from autor as aut
left join livro as liv
	on liv.autor = aut.codautor 
where titulo is null
group by aut.nome 
order by aut.nome

select * from livro
select * from autor 
left join livro
	on livro.autor = autor.codautor
