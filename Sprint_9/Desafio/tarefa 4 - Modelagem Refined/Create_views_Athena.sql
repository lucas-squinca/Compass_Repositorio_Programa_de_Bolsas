CREATE view filmesPopularesFantasy as 
select distinct
    mov.titulo_principal as titulo,
    fat.popularidade as popularidade
from fatofilmes as fat
right join dimmovies as mov on mov.id_movie = fat.id_movies
order by popularidade desc


Create view maioresProdutores as 
select distinct
    prod.produtores as produtor,
    count(prod.produtores) as maiores_produtores
from fatofilmes as fat
inner join dimprodutores as prod on prod.id_produtor = fat.id_produtores
group by prod.produtores
order by maiores_produtores desc

Create view faturamento as 
select distinct
    mov.titulo_principal as titulo,
    fat.orcamento as orcamento,
    fat.receita as receita,
    (fat.receita - fat.orcamento) as faturamento
from fatofilmes as fat
right join dimmovies as mov on mov.id_movie = fat.id_movies

