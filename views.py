from aiohttp import web
from webargs import fields
from webargs.aiohttpparser import use_args 
import psycopg2
from psycopg2 import sql 
import jinja2
import aiohttp_jinja2
import json
from operations import input_analyzer, con_to_db



args = {
		'id': fields.List(fields.Int(), required=False),
		'artnum': fields.List(fields.Int(), required=False),
		'description': fields.List(fields.Str(), required=False),
		'quantity': fields.List(fields.Int(), required=False)
	}




routes = web.RouteTableDef()


@routes.get('', name='basic')
async def basic(request):
	return web.Response(body='<h1> go to /goods </h1>', content_type='text/html')
@routes.get('/menu', name='menu')
async def menu(request):
	return web.Response(body='<h1>Menu</h1>', content_type='text/html')

@routes.get('/goods', name='goods')
@aiohttp_jinja2.template("base.html")
async def goods(request):
	data = await request.post()
	#DISCLAIMER!!! Here I've got a problem to solve it in future check my problemsolved.txt :) [1]
	if data:
		item = data['item']
		init_analyzer = input_analyzer()
		init_analyzer.analyzer(item)

		conn = psycopg2.connect("dbname=warehouse user=admin password=admin")
		cur = conn.cursor()
		query = sql.SQL("INSERT INTO goods (id, artnum, description, quantity) VALUES (%s, %s, %s, %s)")
		cur.execute(query, init_analyzer.analyzed)
		conn.commit()
		cur.close()
		conn.close()

	#declare func of class which will analyse our data (we need: 4 columns splitted by colons)
	

@routes.get('/stock', name='stock')
async def stock(request):
	return web.Response(body='<h1>Stock Transfer</h1>', content_type='text/html')

@routes.get('/print', name='print')
async def printing(request):
	return web.Response(body='<h1>Printing</h1>', content_type='text/html')

@routes.get('/info', name='info')
@use_args(args, location='query')
async def info(request, args: dict):
	return web.Response(body='<h1> Info </h1>', content_type='text/html')

