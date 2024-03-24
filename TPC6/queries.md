# Quantos filmes existem no repositório?
-------------------------
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