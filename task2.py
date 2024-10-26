"""#
Використовуючи бібліотеки RdfLib, SPARQLWrapper та відкритий endpoint написати Python-скрипт,
який буде повертати компанії України, які мають відношення до IT галузі.
Компанії необхідно впорядкувати за кількістю співробітників.
#"""
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://dbpedia.org/sparql')

# TODO clean numEmployees, remove symbols and words >, +, Approx, Approximately, globally. force to integer
query = '''
    select ?company ?name ?numEmployees
    where {
        ?company rdf:type schema:Organization ;
        dbp:industry ?industry ;
        dbo:locationCity ?city ;
        dbp:numEmployees ?numEmployees ;
        foaf:name ?name .
        FILTER(CONTAINS(lcase(str(?industry)), "computer") || CONTAINS(lcase(str(?industry)), "development"))
        FILTER(CONTAINS(lcase(str(?city)), "ukraine"))
    } order by DESC (?numEmployees)
'''

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
query_res = sparql.query().convert()
print(query_res)

for value in query_res['results']['bindings']:
    name = value['name']['value']
    # company = value['company']['value']
    numEmployees = value['numEmployees']['value']
    print(name, '(', numEmployees, ')')