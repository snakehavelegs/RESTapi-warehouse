from aiohttp import web
import views
import psycopg2

app = web.Application()
app.router.add_routes(views.routes)
web.run_app(app)
