from flask import request, jsonify
from charity.data import projets
from charity import api_charity_bp
from charity.controllers.CategorieController import CategorieController
from charity.controllers.ProjetController import ProjetController
from charity.controllers.DonController import DonController
from accounts.controller.UserController import UserController


@api_charity_bp.route("/api/list")
def api_list():
    return jsonify(projets)


categorieController = CategorieController()
projetController = ProjetController()
donController = DonController()
userController = UserController


# Catégorie route
@api_charity_bp.route("/categories", methods=["POST"])
def add_categories():
    return categorieController.create()


@api_charity_bp.route("/listCategories", methods=["GET"])
def list_categories():
    return categorieController.all()


@api_charity_bp.route("/update/<int:id>", methods=["PUT"])
def update_categorie(id):
    return categorieController.update(id)


@api_charity_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_categorie(id):
    return categorieController.delete(id)


# project route
@api_charity_bp.route("/projects", methods=["POST"])
def add_project():
    return projetController.create()


@api_charity_bp.route("/listProject", methods=["GET"])
def list_project():
    return projetController.all()


@api_charity_bp.route("/update/<int:id>", methods=["PUT"])
def update_project(id):
    return projectController.update(id)


@api_charity_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_project(id):
    return projectController.delete(id)



# # Routes pour les dons (DonController)
#
@api_charity_bp.route("/dons", methods=["POST"])
def add_don():
     return donController.create()

@api_charity_bp.route("/listDons", methods=["GET"])
def list_dons():
   return donController.all()
#
@api_charity_bp.route("/updateDon/<int:id>", methods=["PUT"])
def update_don(id):
     return donController.update(id)
#
@api_charity_bp.route("/deleteDon/<int:id>", methods=["DELETE"])
def delete_don(id):
    return donController.delete(id)
#


# Routes pour les utilisateurs (UserController)

@api_charity_bp.route("/users", methods=["POST"])
def add_user():
    return userController.create()

@api_charity_bp.route("/listUsers", methods=["GET"])
def list_users():
    return userController.all()

@api_charity_bp.route("/updateUser/<int:id>", methods=["PUT"])
def update_user(id):
    return userController.update(id)

@api_charity_bp.route("/deleteUser/<int:id>", methods=["DELETE"])
def delete_user(id):
    return userController.delete(id)