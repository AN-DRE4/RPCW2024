import json

f = open("tpc1.json", encoding='utf-8')
bd = json.load(f)
f.close()

ruas = set()
ttl = ""
for plant in bd:
    if plant["Código de rua"]!="" or plant["Rua"]!="":

        ttl+=f"""
###  http://www.semanticweb.org/utilizador/ontologies/2024/1/plants#plant_{plant["Id"]}
:planta_{plant["Id"]} rdf:type owl:NamedIndividual ;
                 :temRua :rua_{plant["Código de rua"]} ;
                 :caldeira "{plant["Caldeira"]}" ;
                 :data_atualizacao "{plant["Data de actualização"]}" ;
                 :data_plantacao "{plant["Data de Plantação"]}" ;
                 :especie "{plant["Espécie"]}" ;
                 :estado "{plant["Estado"]}" ;
                 :gestor "{plant["Gestor"]}" ;
                 :id {plant["Id"]} ;
                 :implantacao "{plant["Implantação"]}" ;
                 :nome_cientifico "{plant["Nome Científico"]}" ;
                 :numero_intervencoes {plant["Número de intervenções"] if plant["Número de intervenções"]!="" else 0 } ;
                 :numero_registo {plant["Número de Registo"]} ;
                 :origem "{plant["Origem"]}" ;
                 :tutor "{plant["Tutor"]}" .
                 """
        if plant["Código de rua"] not in ruas:
            ruas.add(plant["Código de rua"])
            ttl+=f"""
###  http://rpcw.di.uminho.pt/2024/plants#rua_{plant["Código de rua"]}
:rua_{plant["Código de rua"]} rdf:type owl:NamedIndividual ;
             :codigo_rua {plant["Código de rua"]} ;
             :freguesia "{plant["Freguesia"]}" ;
             :local "{plant["Local"]}" ;
             :rua "{plant["Rua"]}" .
    """
print(ttl)

'''f = open("out.ttl", "w", encoding='utf-8')
f.write(ttl)
f.close()
'''
