from elasticsearch_dsl import Document, Text, Keyword, Integer, analyzer, tokenizer

description_analyzer = analyzer(
	'description_analyzator',
	tokenizer=tokenizer('standard'),
	filter=['lowercase', 'stop', 'trim', 'classic'],
	)



class Warehouse(Document):

	id = Keyword()
	artnum = Integer()
	description = Text(analyzer=description_analyzer)
	quantity = Integer()

	class Index:
		name = 'warehouse'
