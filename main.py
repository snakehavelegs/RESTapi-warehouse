from aiohttp import web
import views
import psycopg2

conn = psycopg2.connect("dbname=warehouse user=admin password=admin")
cur = conn.cursor()
cur.execute("SELECT * FROM goods")
resp = cur.fetchall()

app = web.Application()
app.router.add_routes(views.routes)


web.run_app(app)
