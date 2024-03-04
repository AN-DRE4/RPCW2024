
1. Quais as cidades de um determinado distrito? (Testado com o distrito de Leiria)

```sql
PREFIX : <http://www.semanticweb.org/utilizador/ontologies/2024/2/mapa-virtual/>

select ?nome where { 
	?s :distrito "Porto" .
    ?s :nome ?nome
} order by ?nome
```


2. Distribuição de cidades por distrito? (Ordenado de forma ascendente de número de cidades)


```sql
PREFIX : <http://www.semanticweb.org/utilizador/ontologies/2024/2/mapa-virtual/>

select ?distrito (COUNT(distinct ?cidade) as ?ncidades) where { 
    ?cidade :distrito ?distrito .
}
group by ?distrito order by ?ncidades
```

3. Quantas cidades se podem atingir a partir do Porto? (Diretamente)
```sql
PREFIX : <http://www.semanticweb.org/utilizador/ontologies/2024/2/mapa-virtual/>

SELECT (COUNT (DISTINCT ?cidade) AS ?numDestino) WHERE {
    ?porto :distrito "Porto" .
    ?ligacao :origem ?porto ;
    		 :destino ?cidade .
}
```


4. Quais as cidades com população acima de um determinado valor? (Testado com 50000 pessoas)


```sql
PREFIX : <http://www.semanticweb.org/utilizador/ontologies/2024/2/mapa-virtual/>

SELECT ?nome ?populacao WHERE {
    ?cidade a :cidade .
    ?cidade :nome ?nome .
    ?cidade :populacao ?populacao .
    FILTER (50000 < ?populacao).
} order by ?populacao
```