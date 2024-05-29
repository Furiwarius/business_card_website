from app.application import Application
from app.routes.pages import bp

app = Application()
app.add_blueprint(bp)

if __name__ == '__main__':
	app.run(dubug=False)
