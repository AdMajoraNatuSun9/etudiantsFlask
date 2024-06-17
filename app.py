# app.py

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager
from charity.web_charity_bp import web_charity_bp
from charity.api_charity_bp import api_charity_bp
from accounts.auth_bp import auth_bp
from extensions import db
from charity.controllers.DonController import don_bp  # Importez le Blueprint
from charity import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# app = Flask(__name__)

CORS(app, origins="*")

app.register_blueprint(web_charity_bp, url_prefix='/charity')
app.register_blueprint(api_charity_bp, url_prefix='/api/charity')
#app.register_blueprint(auth_bp, url_prefix='/auth')
#app.register_blueprint(don_bp, url_prefix='/api/charity')  # Enregistrez le Blueprint

app.config['SECRET_KEY'] = 'charity_secret'
app.config['BASE_TEMPLATE_FOLDER'] = 'charity/templates'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1850@localhost:3306/charity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

from charity.models.categorie import Categorie
from charity.models.projet import Projet
from accounts.models.user import User
from charity.models.don import Don

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

"""
with app.app_context():
    db.create_all()
"""

if __name__ == '__main__':
    app.run(debug=True)












# from flask import Flask, render_template
# from flask_cors import CORS
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from charity import web_charity_bp, api_charity_bp
# from accounts import auth_bp
# from extensions import db
# from charity.controllers.don_controller import don_bp  # Importez le Blueprint
#
# app = Flask(__name__)
#
# CORS(app, origins="*")
#
# app.register_blueprint(web_charity_bp, url_prefix='/charity')
# app.register_blueprint(api_charity_bp, url_prefix='/api/charity')
# app.register_blueprint(auth_bp, url_prefix='/auth')
# app.register_blueprint(don_bp, url_prefix='/api/charity')  # Enregistrez le Blueprint
#
# app.config['SECRET_KEY'] = 'charity_secret'
# app.config['BASE_TEMPLATE_FOLDER'] = 'charity/templates'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1850@localhost:3306/charity'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db.init_app(app)
# migrate = Migrate(app, db)
#
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'auth.login'
#
# from charity.models.categorie import Categorie
# from charity.models.projet import Projet
# from accounts.models.user import User
# from charity.models.don import Don
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
#
# """
# with app.app_context():
#     db.create_all()
# """
#
# if __name__ == '__main__':
#     app.run(debug=True)

# ----------------


# # import flask
# from flask import Flask, render_template
# from flask_cors import CORS
# from charity import web_charity_bp, api_charity_bp
# from accounts import auth_bp
# from extensions import db
# from flask_migrate import Migrate
# from flask_login import LoginManager
#
# app = flask.Flask(__name__)
#
# CORS(app, origins="*")
#
# app.register_blueprint(web_charity_bp, url_prefix='/charity')
# app.register_blueprint(api_charity_bp, url_prefix='/api/charity')
# app.register_blueprint(auth_bp, url_prefix='/auth')
#
# app.config['SECRET_KEY'] = 'charity_secret'
#
# app.config['BASE_TEMPLATE_FOLDER'] = 'charity/templates'
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1850@localhost:3306/charity'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db.init_app(app)
#
# migrate = Migrate(app, db)
#
# login_manager = LoginManager()
# login_manager.init_app(app)
#
# #Specifier la vue de connexion
# # with app.app_context():
# #   db.create_all()
# login_manager.login_view = 'auth.login'
#
# from charity.models.categorie import Categorie
# from charity.models.projet import Projet
# from accounts.models.User import User
# from accounts.models.don import Don
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
#
## """
# with app.app_context():
#     db.create_all()
# """

# db.init_app(app)
#

