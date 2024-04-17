import json
import xml.etree.ElementTree as ET
from rdflib import Graph, Literal, Namespace, URIRef, RDF, OWL

g = Graph()
g.parse('familia-base.ttl')

root = ET.parse('biblia.xml')

familia = Namespace('http://rpcw.di.uminho.pt/2024/familia/')

people_dict = {}

for person in root.findall('person'):
    id = person.find('id').text
    name = person.find('namegiven').text
    sex = person.find('sex').text
    parents = []
    for parent in person.findall('parent'):
        parents.append({'id': parent.get('ref'), 'name': parent.text})
    people_dict[id] = {'name': name, 'sex': sex, 'parents': parents}
    g.add((URIRef(f'{familia}{id}'), RDF.type, OWL.NamedIndividual))
    g.add((URIRef(f'{familia}{id}'), RDF.type, familia.Pessoa))
    g.add((URIRef(f'{familia}{id}'), familia.nome, Literal(name)))

for person in people_dict:
    for parent in people_dict[person]['parents']:
        if parent['id'] in people_dict:
            if people_dict[parent['id']]['sex'] == 'M':
                g.add((URIRef(f'{familia}{person}'), familia.temPai, URIRef(f'{familia}{parent["id"]}')))
            elif people_dict[parent['id']]['sex'] == 'F':
                g.add((URIRef(f'{familia}{person}'), familia.temMae, URIRef(f'{familia}{parent["id"]}')))
            else:
                print(f'Error: {people_dict[parent["id"]]["name"]} sex not defined')
        else:
            print(f'Error: {parent["name"]} not found')

people_json = json.dumps(people_dict)
print(g.serialize())
            