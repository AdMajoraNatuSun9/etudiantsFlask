# charity/controllers/DonController.py
from flask import Blueprint, jsonify, request
from charity.models.don import Don
from extensions import db

# Création du Blueprint
don_bp = Blueprint('don_bp', __name__)

class DonController:
    def __init__(self):
        self.don_model = Don

    def all(self):
        try:
            dons = self.don_model.query.all()
            result = [{'id': don.id, 'montant': don.montant, 'identifiant': don.identifiant,
                       'telephone': don.telephone, 'modePayement': don.modePayement,
                       'projet_id': don.projet_id} for don in dons]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def create(self):
        try:
            data = request.get_json()
            if not all(k in data for k in ('montant', 'identifiant', 'telephone', 'modePayement', 'projet_id')):
                return jsonify({'message': 'Données manquantes'}), 400

            don = self.don_model(
                montant=data['montant'],
                identifiant=data['identifiant'],
                telephone=data['telephone'],
                modePayement=data['modePayement'],
                projet_id=data['projet_id']
            )

            db.session.add(don)
            db.session.commit()
            return jsonify({'message': 'Don créé avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500

    def update(self, don_id):
        try:
            data = request.get_json()
            don = self.don_model.query.get(don_id)
            if don:
                don.montant = data['montant']
                don.identifiant = data['identifiant']
                don.telephone = data['telephone']
                don.modePayement = data['modePayement']
                don.projet_id = data['projet_id']
                db.session.commit()
                return jsonify({'message': 'Don mis à jour avec succès'}), 200
            else:
                return jsonify({'message': 'Don non trouvé'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500

    def delete(self, don_id):
        try:
            don = self.don_model.query.get(don_id)
            if don:
                db.session.delete(don)
                db.session.commit()
                return jsonify({'message': 'Don supprimé avec succès'}), 200
            else:
                return jsonify({'message': 'Don non trouvé'}), 404
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500

# don_controller = DonController()
#
# @don_bp.route('/listDons', methods=['GET'])
# def list_dons():
#     return don_controller.all()
#
# @don_bp.route('/createDon', methods=['POST'])
# def create_don():
#     return don_controller.create()
#
# @don_bp.route('/updateDon/<int:don_id>', methods=['PUT'])
# def update_don(don_id):
#     return don_controller.update(don_id)
#
# @don_bp.route('/deleteDon/<int:don_id>', methods=['DELETE'])
# def delete_don(don_id):
#     return don_controller.delete(don_id)
#
#
#
#


#
# from flask import Blueprint, jsonify, request
# from charity.models.don import Don
# from extensions import db
#
# # Création du Blueprint
# don_bp = Blueprint('don_bp', __name__)
#
# class DonController:
#     def __init__(self):
#         self.don_model = Don
#
#     def all(self):
#         try:
#             dons = self.don_model.query.all()
#             result = [{'id': don.id, 'montant': don.montant, 'identifiant': don.identifiant,
#                        'telephone': don.telephone, 'modePayement': don.modePayement,
#                        'projet_id': don.projet_id} for don in dons]
#             return jsonify(result), 200
#         except Exception as e:
#             return jsonify({'message': str(e)}), 500
#
#     def create(self):
#         try:
#             data = request.get_json()
#             if not all(k in data for k in ('montant', 'identifiant', 'telephone', 'modePayement', 'projet_id')):
#                 return jsonify({'message': 'Données manquantes'}), 400
#
#             don = self.don_model(
#                 montant=data['montant'],
#                 identifiant=data['identifiant'],
#                 telephone=data['telephone'],
#                 modePayement=data['modePayement'],
#                 projet_id=data['projet_id']
#             )
#
#             db.session.add(don)
#             db.session.commit()
#             return jsonify({'message': 'Don créé avec succès'}), 201
#         except KeyError:
#             return jsonify({'message': 'Données manquantes'}), 400
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({'message': str(e)}), 500
#
#     def update(self, don_id):
#         try:
#             data = request.get_json()
#             don = self.don_model.query.get(don_id)
#             if don:
#                 don.montant = data['montant']
#                 don.identifiant = data['identifiant']
#                 don.telephone = data['telephone']
#                 don.modePayement = data['modePayement']
#                 don.projet_id = data['projet_id']
#                 db.session.commit()
#                 return jsonify({'message': 'Don mis à jour avec succès'}), 200
#             else:
#                 return jsonify({'message': 'Don non trouvé'}), 404
#         except KeyError:
#             return jsonify({'message': 'Données manquantes'}), 400
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({'message': str(e)}), 500
#
#     def delete(self, don_id):
#         try:
#             don = self.don_model.query.get(don_id)
#             if don:
#                 db.session.delete(don)
#                 db.session.commit()
#                 return jsonify({'message': 'Don supprimé avec succès'}), 200
#             else:
#                 return jsonify({'message': 'Don non trouvé'}), 404
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({'message': str(e)}), 500
#
# don_controller = DonController()
#
# @don_bp.route('/listDons', methods=['GET'])
# def list_dons():
#     return don_controller.all()
#
# @don_bp.route('/createDon', methods=['POST'])
# def create_don():
#     return don_controller.create()
#
# @don_bp.route('/updateDon/<int:don_id>', methods=['PUT'])
# def update_don(don_id):
#     return don_controller.update(don_id)
#
# @don_bp.route('/deleteDon/<int:don_id>', methods=['DELETE'])
# def delete_don(don_id):
#     return don_controller.delete(don_id)
#



# # controllers/don_controller.py
#
# from flask import jsonify, request
# from charity.models.don import Don
# from extensions import db
#
#
# class DonController:
#     def __init__(self):
#         self.don_model = Don
#
#     def all(self):
#         try:
#             dons = self.don_model.query.all()
#             result = [{'id': don.id, 'montant': don.montant, 'identifiant': don.identifiant,
#                        'telephone': don.telephone, 'modePayement': don.modePayement,
#                        'projet_id': don.projet_id} for don in dons]
#             return jsonify(result), 200
#         except Exception as e:
#             return jsonify({'message': str(e)}), 500
#
#     def create(self):
#         try:
#             data = request.form
#
#             # Validation des données
#             if not all(k in data for k in ('montant', 'identifiant', 'telephone', 'modePayement', 'projet_id')):
#                 return jsonify({'message': 'Données manquantes'}), 400
#
#             don = self.don_model(
#                 montant=data['montant'],
#                 identifiant=data['identifiant'],
#                 telephone=data['telephone'],
#                 modePayement=data['modePayement'],
#                 projet_id=data['projet_id']
#             )
#
#             db.session.add(don)
#             db.session.commit()
#             return jsonify({'message': 'Don créé avec succès'}), 201
#         except KeyError:
#             return jsonify({'message': 'Données manquantes'}), 400
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({'message': str(e)}), 500
#
#     def update(self, don_id):
#         try:
#             data = request.get_json()
#             don = self.don_model.query.get(don_id)
#             if don:
#                 don.montant = data['montant']
#                 don.identifiant = data['identifiant']
#                 don.telephone = data['telephone']
#                 don.modePayement = data['modePayement']
#                 don.projet_id = data['projet_id']
#                 db.session.commit()
#                 return jsonify({'message': 'Don mis à jour avec succès'}), 200
#             else:
#                 return jsonify({'message': 'Don non trouvé'}), 404
#         except KeyError:
#             return jsonify({'message': 'Données manquantes'}), 400
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({'message': str(e)}), 500
#
#     def delete(self, don_id):
#         try:
#             don = self.don_model.query.get(don_id)
#             if don:
#                 db.session.delete(don)
#                 db.session.commit()
#                 return jsonify({'message': 'Don supprimé avec succès'}), 200
#             else:
#                 return jsonify({'message': 'Don non trouvé'}), 404
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({'message': str(e)}), 500