from flask import Flask,session,redirect,render_template,url_for,request
from api import api_blueprint
from config import Config
from models import db
from flask_migrate import Migrate
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api_blueprint)
CORS(app, supports_credentials=True)
Session(app)

with app.app_context():
    db.init_app(app)
    db.create_all()


migrate = Migrate(app)
migrate.init_app(app)




if __name__ == '__main__':

    app.run(debug=True)
