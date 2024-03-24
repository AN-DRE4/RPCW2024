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