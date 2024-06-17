from flask import render_template, Blueprint, request, redirect, url_for, flash, jsonify
from charity import web_charity_bp
from charity.models.projet import Projet
from charity.models.don import Don
import requests
from extensions import db


# Route pour la page d'accueil, affiche tous les projets
@web_charity_bp.route("/")
def index():
    projets = Projet.query.all()
    return render_template('index.html', projets=projets)


# Route pour afficher les détails d'un projet spécifique
@web_charity_bp.route("/details/<int:projetId>")
def details(projetId):
    projet = Projet.query.get_or_404(projetId)
    total_dons = calculer_total_dons(projetId)
    return render_template('details.html', projet=projet, total_dons=total_dons)


# Fonction pour calculer le total des dons pour un projet spécifique
def calculer_total_dons(projetId):
    projet = Projet.query.get_or_404(projetId)
    dons = projet.dons
    total_dons = sum(don.montant for don in dons)
    return total_dons


# Route pour la page de don, et traitement des dons
@web_charity_bp.route("/don", methods=['GET', 'POST'])
def don():
    if request.method == 'POST':
        try:
            identifiant = request.form['identifiant']
            montant = request.form['montant']
            telephone = request.form['telephone']
            modePayement = request.form['modePayement']
            projet_id = request.form['projet_id']

            don = Don(identifiant=identifiant,
                      montant=montant,
                      telephone=telephone,
                      modePayement=modePayement,
                      projet_id=projet_id)

            paygate_url = "https://paygateglobal.com/api/v1/pay"
            response = requests.post(paygate_url,
                                     json={
                                         'auth_token': '5b2a5ed8-7764-4f51-a0fc-f3f49980d54e',
                                         'phone_number': telephone,
                                         'amount': montant,
                                         'identifiant': identifiant,
                                         'network': modePayement
                                     })
            response_data = response.json()
            print('reponse', response_data)

            db.session.add(don)
            db.session.commit()

            total_dons = calculer_total_dons(projet_id)
            return jsonify({'success': True, 'total_dons': total_dons})
        except Exception as e:
            print(e)
            return jsonify({'success': False})
    else:
        return render_template('don.html')

# from flask import render_template, jsonify
# from charity.data import projets
# from charity import web_charity_bp
#
#
# @web_charity_bp.route("/")
# def index():
#     return render_template('index.html', projets=projets)
#
#
# @web_charity_bp.route("/details/<int:projetId>")
# def details(projetId):
#     details = next((projet for projet in projets if projet["id"] == projetId), None)
#     return render_template('details.html', retour = details)
#
#
# @web_charity_bp.route("/don")
# def don():
#     return render_template('don.html')
#
# @web_charity_bp.route("/")
# def index():
#     return render_template('index.html', projets=projets)
#
#
# @web_charity_bp.route("/details/<int:projetId>")
# def details(projetId):
#     details = next((projet for projet in projets if projet["id"] == projetId), None)
#     return render_template('details.html', retour = details)