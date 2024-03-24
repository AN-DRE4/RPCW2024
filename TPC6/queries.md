# Quantos filmes existem no repositório?

```
PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT (COUNT(?s) AS ?count)
WHERE {
    ?s a :Film .
}
```

# Qual a distribuição de filmes por ano de lançamento?

```
PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?year (COUNT(?s) AS ?count)
WHERE {
    ?s a :Film .
    ?s :date ?yearString .
    bind(str(year(xsd:date(?yearString))) as ?year)
}
GROUP BY ?year
ORDER BY ?year
```

# Qual a distribuição de filmes por género?
```
PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?genre (COUNT(?s) AS ?count)
WHERE {
    ?s a :Film .
    ?s :hasGenre ?genre .
}
GROUP BY ?genre
ORDER BY DESC(?count)
```

# Em que filmes participou o ator 'Burt Reynolds'?
```
PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?actor
WHERE {
    ?s a :Film .
    ?s :hasActor ?actor .
}
```

# Produz uma lista de realizadores com o seu nome e o número de filmes que realizou.
```
PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?producerName (COUNT(?s) AS ?count)
WHERE {
    ?s a :Film .
    ?s :hasProducer ?producer .
    ?producer :name ?producerName .
}
GROUP BY ?producerName
ORDER BY DESC(?count)
```

# Qual o título dos livros que aparecem associados aos filmes?
```
PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?title
WHERE {
    ?s a :Film .
    ?s :movie_title ?title .
}
```