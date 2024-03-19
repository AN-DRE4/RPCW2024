import requests
import json
from icecream import ic

sparql_endpoint = "http://dbpedia.org/sparql"

# Query to get all movies
sparql_query = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?movie ?title ?abstract ?runtime
WHERE {
    ?movie rdf:type dbo:Film .
    ?movie rdfs:label ?title .

    OPTIONAL {
        ?movie dbo:abstract ?abstract .
        FILTER (lang(?abstract) = 'en')
    }

    OPTIONAL {
        ?movie dbo:runtime ?runtime .
    }
    
    FILTER (lang(?title) = 'en')
}
"""

headers = {
    'Accept': 'application/sparql-results+json'
}

params = {
    'format': 'json', 
    'query': sparql_query
}

# Send the SPARQL query using the requests library
response = requests.get(sparql_endpoint, params=params, headers=headers)
ic("Headers sent: ") 
ic(response.request.headers)

ic("\nParams sent: ") 
ic(response.request.url)

movies = { "movies": [] }
# Check if the request was successful
if response.status_code == 200:
    # Parse the response in JSON
    response_json = response.json()
    # Extract the movies from the response
    for binding in response_json['results']['bindings']:
        movie = {}
        movie['uri'] = binding['movie']['value']
        movie['title'] = binding['title']['value']
        if 'abstract' in binding:
            movie['abstract'] = binding['abstract']['value']
        if 'runtime' in binding:
            movie['runtime'] = binding['runtime']['value']
        movies["movies"].append(movie)
    f = open("filmes.json", "w")
    f.write(json.dumps(movies, indent=4))
    f.close()
else:
    ic("Error executing the query. HTTP Status Code: " + response.status_code)
    ic(response.text)

# CaLculate num of movies
ic("Number of movies: " + str(len(movies["movies"])))