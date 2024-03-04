import json

f = open("mapa.json", encoding='utf-8')

bd = json.load(f)

f.close()

ttl = ""
for cidade in bd['cidades']:
    ttl += f"""
###  http://www.semanticweb.org/utilizador/ontologies/2024/2/mapa-virtual#{cidade["id"]}
:{cidade["id"]} rdf:type owl:NamedIndividual ,
                :cidade ;
         :descricao "{cidade["descrição"]}" ;
         :distrito "{cidade["distrito"]}" ;
         :id "{cidade["id"]}" ;
         :nome "{cidade["nome"]}" ;
         :populacao {cidade["população"]} .
    """

for ligacao in bd['ligacoes']:
    ttl += f"""
###  http://www.semanticweb.org/utilizador/ontologies/2024/2/mapa-virtual#{ligacao["id"]}
:{ligacao["id"]} rdf:type owl:NamedIndividual ,
                :ligacao ;
         :destino :{ligacao["destino"]} ;
         :origem :{ligacao["origem"]} ;
         :distancia {ligacao["distância"]} ;
         :id "{ligacao["id"]}" .
    """

f = open("out.ttl", "w", encoding='utf-8')

f.write(ttl)

f.close()