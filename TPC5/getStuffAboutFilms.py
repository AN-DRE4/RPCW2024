import requests
import json
from icecream import ic

sparql_endpoint = "http://dbpedia.org/sparql"

def sendSPARQLQuery(sparql_query,propriedade):
    headers = {
        "Accept": "application/sparql-results+json"
    }
    # Define the parameters
    params = {
        "query": sparql_query,
        "format": "json"
    }
    # Send the SPARQL query using requests
    response = requests.get(sparql_endpoint, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()
        cenas = []
        for cena in results["results"]["bindings"]:
            cenas.append(cena[propriedade]["value"])
        return cenas
    else:
        print("Error:", response.status_code)
        print(response.text)
        return []


def getActors(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?actor 
WHERE {{
    <{uri}> dbo:starring ?actorName .
    ?actorName rdfs:label ?actor .
    FILTER (lang(?actor) = 'en')
}}
"""
    return sendSPARQLQuery(sparql_query,"actor")

def getComposers(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?composer
WHERE {{
    <{uri}> dbo:musicComposer ?composerName .
    ?composerName dbp:name ?composer .
    FILTER (lang(?composer) = 'en')
}}
"""
    return sendSPARQLQuery(sparql_query,"composer")

def getDirectors(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?director
WHERE {{
    <{uri}> dbo:director ?directorName .
    ?directorName dbp:name ?director .
    FILTER (lang(?director) = 'en')
}}
"""
    return sendSPARQLQuery(sparql_query,"director")

def getProducers(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?producer
WHERE {{
    <{uri}> dbo:producer ?producerName .
    ?producerName dbp:name ?producer .
    FILTER (lang(?producer) = 'en')
}}
"""
    return sendSPARQLQuery(sparql_query,"producer")

def getCountrys(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?country
WHERE {{
    <{uri}> dbp:country ?country .
    FILTER (lang(?country) = 'en')
}}
"""
    return sendSPARQLQuery(sparql_query,"country")

def getGenres(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?genre
WHERE {{
    <{uri}> dbp:genre ?genre .
    FILTER (lang(?genre) = 'en')
}}
"""
    return sendSPARQLQuery(sparql_query,"genre")

def getWriters(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?writer
WHERE {{
    <{uri}> dbo:writer ?writerName .
    ?writerName dbp:name ?writer .
    FILTER (lang(?writer) = 'en')
}}
"""
    return sendSPARQLQuery(sparql_query,"writer")


'''f = open("films.json")
movies = json.load(f)
actors = []
composers = [] 
directors = [] 
producers = [] 
countrys = [] 
genres = [] 
writers = [] 
#for movie in movies:
for movie in movies["movies"]:
    print(movie["title"])
    #query para ir buscar atores
    movie["actors"] = getActors(movie["uri"])
    #query para ir buscar músicos
    movie["composers"] = getComposers(movie["uri"])
    #query para ir buscar realizadores
    movie["directors"] = getDirectors(movie["uri"])
    
    #query para ir bbuscar produtores
    movie["producers"] = getProducers(movie["uri"])

    #query para ir buscar paises
    movie["countrys"] = getCountrys(movie["uri"])
    
    #query para ir buscar genres
    movie["genres"] = getGenres(movie["uri"])
    
    #query para ir buscar escritores
    movie["writers"] = getWriters(movie["uri"])   

f = open("filmsInfo.json","w")
json.dump(movies,f)
f.close()'''

import concurrent.futures

f = open("films.json")
movies = json.load(f)

def fetch_movie_data(movie):
    movie["actors"] = getActors(movie["uri"])
    movie["composers"] = getComposers(movie["uri"])
    movie["directors"] = getDirectors(movie["uri"])
    movie["producers"] = getProducers(movie["uri"])
    movie["countrys"] = getCountrys(movie["uri"])
    movie["genres"] = getGenres(movie["uri"])
    movie["writers"] = getWriters(movie["uri"])
    ic(f"Finished processing movie: {movie['uri']}")
    return movie

with concurrent.futures.ThreadPoolExecutor() as executor:
    movies["movies"] = list(executor.map(fetch_movie_data, movies["movies"]))

f = open("filmsInfo.json","w")
json.dump(movies,f)
f.close()