class input_analyzer:
	def analyzer(item):
		input_analyzer.analyzer.oneitem = item.split(',') 
		counter = 0
		for items in input_analyzer.analyzer.oneitem:
			counter = counter + 1
		if counter == 4:
			print(f'Finish! Added {input_analyzer.analyzer.oneitem}')
			return input_analyzer.analyzer.oneitem
		else:
			print("there's not 4 columns")

def con_to_db():
	conn = psycopg2.connect("dbname=warehouse user=admin password=admin")
	cur = conn.cursor()

