# Задача 1
```
Використовуючи відкритий SPARQL endpoint http://dbpedia.org/sparql,
напишіть SPARQL запит для визначення назви міста,
яке має координати (49.589443, 34.551388).
```

### Розвʼязок
```sparql
select ?city ?location
where {
	?city rdf:type dbo:City ;
	georss:point  ?location ;
	georss:point "49.589443 34.551388" .
}
```

або теж саме використовуючи оператор filter
```sparql
select ?city ?city_name ?location
where {
	?city rdf:type dbo:City ; 
	georss:point ?location ;
	foaf:name ?city_name .
	FILTER(?location = "49.589443 34.551388")
}
```

місто не знаходить, але якщо ми підставимо іншу локацію до прикладу
- "50.45 30.523333333333333"
- "46.48572222222222 30.743444444444446"
то місто знаходить. запит працює, можливо у dbpedia більше немає запису про місто з такою локацією або формат трохи змінився.
також можна спробувати використати
- `geo:lat`
- `geo:long`
- `geo:geometry` (POINT(30.523332595825 50.450000762939))
та оператор CONTAINS 