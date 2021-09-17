from aiohttp import web
import views
import psycopg2
import jinja2
import aiohttp_jinja2
import os

app = web.Application()
aiohttp_jinja2.setup(
    app, loader=jinja2.FileSystemLoader(os.path.join(os.getcwd(), "templates"))
)

app.router.add_route('POST', '/goods', views.goods)
app.router.add_routes(views.routes)
web.run_app(app)
