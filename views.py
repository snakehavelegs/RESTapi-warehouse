from aiohttp import web
from webargs import fields
from webargs.aiohttpparser import use_args 
import psycopg2
import json
from psycopg2.extras import RealDictCursor
args = {
		'id': fields.Int(required=False),
		'artnum': fields.Int(required=False),
		'description': fields.Str(required=False),
		'quantity': fields.Int(required=False)
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
@use_args(args, location='query')
async def menu(request, args: dict):
	return web.json_response(data=jsonObject, content_type='application/json')
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
async def information(request):
	return web.Response(body='<h1>Information</h1>', content_type='text/html')