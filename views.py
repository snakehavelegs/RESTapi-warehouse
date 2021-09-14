from aiohttp import web
from webargs import fields
from webargs.aiohttpparser import use_args 
import psycopg2
import json
from elasticsearch_dsl import Q
from models import Warehouse


args = {
		'id': fields.List(fields.Int(), required=False),
		'artnum': fields.List(fields.Int(), required=False),
		'description': fields.List(fields.Str(), required=False),
		'quantity': fields.List(fields.Int(), required=False)
	}

conn = psycopg2.connect("dbname=warehouse user=admin password=admin")
cur = conn.cursor()
cur.execute("SELECT * FROM goods")

resp = json.dumps(cur.fetchall())

routes = web.RouteTableDef()

with open("warehouse.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()




	

@routes.get('/menu', name='menu')
async def menu(request):
	return web.Response(body='<h1>Menu</h1>', content_type='text/html')

@routes.get('/goods', name='goods')
async def goods(request):
	return web.Response(body='<h1>Goods Receipt</h1>', content_type='text/html')

@routes.get('/stock', name='stock')
async def stock(request):
	return web.Response(body='<h1>Stock Transfer</h1>', content_type='text/html')

@routes.get('/print', name='print')
async def printing(request):
	return web.Response(body='<h1>Printing</h1>', content_type='text/html')

@routes.get('/info', name='info')
@use_args(args, location='query')
async def info(request, args: dict):
	query = Q()
	
	if 'description' in args:
		query = query & Q('match', description={'query': args['description']})
	
	search = Warehouse.search()
	search.query = query

	result =search.execute()

	return web.json_response(data=[
		warehouse.to_dict()
		for goods in result.hits
		],
		content_type='application/json'
	)