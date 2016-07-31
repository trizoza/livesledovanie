from flask import Blueprint, jsonify
from flask.ext.login import LoginManager, login_user , logout_user , current_user , login_required
from flask import Flask, session, request, flash, url_for, redirect, render_template, abort, g, send_from_directory
from pymongo import MongoClient
from bson import json_util
import json
import os

places = Blueprint('places', __name__, template_folder='templates')

client = MongoClient("mongodb://admin:51dBVLs4ZLpi@%s:%s/" \
                           %(os.environ['OPENSHIFT_MONGODB_DB_HOST'],os.environ['OPENSHIFT_MONGODB_DB_PORT']))
db = client.sledovanie
poi = db.poi

    #
    #"mongo":        "mongodb://admin:51dBVLs4ZLpi@%s:%s/" \
    #                       %(os.environ['OPENSHIFT_MONGODB_DB_HOST'],os.environ['OPENSHIFT_MONGODB_DB_PORT'])
    #"mongo":        "mongodb://admin:51dBVLs4ZLpi@%s:%s/" %("127.0.0.1","27017")

@places.route('/ajax/pois', methods=['GET'])
#@login_required
def pois():
    if request.method == 'GET':
        pois = poi.find()
        pois = str(json.dumps(list(pois),default=json_util.default))
        return pois
    
@places.route('/scitaj')
#@login_required
def vysledok():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    c = request.args.get('c', 0, type=float)
    return jsonify(result=c + b)


@places.route('/mapa', methods=['GET'])
#@login_required
def mapa():
    if request.method == 'GET':
        return render_template('mapa.html')