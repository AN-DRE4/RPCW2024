import json
from icecream import ic

f = open("db.json", encoding='utf-8')

bd = json.load(f)

f.close()

ttl = ""
for instrument in bd['instrumentos']:
    instrument["#text"] = instrument["#text"].replace(" ", "_")
    ttl += f"""

###  http://www.semanticweb.org/utilizador/ontologies/2024/1/music#{instrument["#text"]}
:{instrument["#text"]} rdf:type owl:NamedIndividual ,
                :instrumento ;
             :nome_instrumento "{instrument["#text"]}" .
        """
    
for curso in bd['cursos']:
    curso["instrumento"]["#text"] = curso["instrumento"]["#text"].replace(" ", "_")    
    curso["designacao"] = curso["designacao"].replace(" ", "_")
    ttl += f"""

###  http://www.semanticweb.org/utilizador/ontologies/2024/1/music#{curso["id"]}
:{curso["id"]} rdf:type owl:NamedIndividual ,
                    :curso ;
             :ensina :{curso["instrumento"]["#text"]} ;
             :designacao "{curso["designacao"]}" ;
             :duracao "{curso["duracao"]}" ;
             :id "{curso["id"]}" .

        """
    
for aluno in bd['alunos']:
    aluno["nome"] = aluno["nome"].replace(" ", "_")
    aluno["instrumento"] = aluno["instrumento"].replace(" ", "_")
    ttl += f"""

###  http://www.semanticweb.org/utilizador/ontologies/2024/1/music#{aluno["id"]}
:{aluno["id"]} rdf:type owl:NamedIndividual ,
                    :aluno ;
             :pertence :{aluno["curso"]} ;
             :toca :{aluno["instrumento"]} ;
             :ano_curso "{aluno["anoCurso"]}" ;
             :data_nascimento "{aluno["dataNasc"]}" ;
             :id "{aluno["id"]}" ;
             :nome "{aluno["nome"]}" .

        """

f = open("out.ttl", "w", encoding='utf-8')

f.write(ttl)

f.close()