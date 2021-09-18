class input_analyzer:
	def analyzer(self, item):
		self.analyzed = item.split(',')
		counter = 0
		for items in self.analyzed:
			counter = counter + 1
		if counter == 4:
			print(f'Finish! Added {self.analyzed}')
			return self.analyzed
		else:
			print("there's not 4 columns")
	
def con_to_db():
	conn = psycopg2.connect("dbname=warehouse user=admin password=admin")
	cur = conn.cursor()

