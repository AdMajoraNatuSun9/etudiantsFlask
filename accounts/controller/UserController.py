# controllers/user_controller.py

from flask import jsonify, request
from charity.models.user import User
from extensions import db


class UserController:
    def __init__(self):
        self.user_model = User

    def all(self):
        try:
            users = self.user_model.query.all()
            result = [{'id': user.id, 'nom': user.nom, 'prenom': user.prenom,
                       'username': user.username} for user in users]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def create(self):
        try:
            nom = request.form['nom']
            prenom = request.form['prenom']
            username = request.form['username']
            password = request.form['password']

            if self.user_model.query.filter_by(username=username).first():
                return jsonify({'message': 'Nom d\'utilisateur déjà pris'}), 400

            user = self.user_model(nom=nom, prenom=prenom, username=username)
            user.set_password(password)

            db.session.add(user)
            db.session.commit()

            return jsonify({'message': 'Utilisateur créé avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500

    def update(self, user_id):
        try:
            data = request.get_json()
            user = self.user_model.query.get(user_id)
            if user:
                user.nom = data.get('nom', user.nom)
                user.prenom = data.get('prenom', user.prenom)
                db.session.commit()
                return jsonify({'message': 'Utilisateur mis à jour avec succès'}), 200
            else:
                return jsonify({'message': 'Utilisateur non trouvé'}), 404
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500

    def delete(self, user_id):
        try:
            user = self.user_model.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return jsonify({'message': 'Utilisateur supprimé avec succès'}), 200
            else:
                return jsonify({'message': 'Utilisateur non trouvé'}), 404
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500
