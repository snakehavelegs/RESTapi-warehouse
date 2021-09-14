from aiohttp import web
import views
import psycopg2
from elasticsearch_dsl import connections
from elasticsearch import Elasticsearch
connections.create_connection(
        hosts=['localhost'], ports=8080,
        timeout=20,)
app = web.Application()
app.router.add_routes(views.routes)
web.run_app(app)
