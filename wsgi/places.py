from flask import Blueprint, jsonify
from flask.ext.login import LoginManager, login_user , logout_user , current_user , login_required
from flask import Flask, session, request, flash, url_for, redirect, render_template, abort, g, send_from_directory, current_app
from pymongo import MongoClient
from bson import json_util
import json
import os
from cestadb import *
from ftpcopy import resize_and_copy_to_cesta_ftp
from functools import wraps


places = Blueprint('places', __name__, template_folder='templates')

"""
client = MongoClient("mongodb://admin:51dBVLs4ZLpi@%s:%s/" \
                           %(os.environ['OPENSHIFT_MONGODB_DB_HOST'],os.environ['OPENSHIFT_MONGODB_DB_PORT']))
db = client.sledovanie

poi = db.poi
"""
    #
    #"mongo":        "mongodb://admin:51dBVLs4ZLpi@%s:%s/" \
    #                       %(os.environ['OPENSHIFT_MONGODB_DB_HOST'],os.environ['OPENSHIFT_MONGODB_DB_PORT'])
    #"mongo":        "mongodb://admin:51dBVLs4ZLpi@%s:%s/" %("127.0.0.1","27017")


def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f().data) + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function


@places.route('/mapa', methods=['GET'])
#@login_required
def mapa():
    if request.method == 'GET':
        return render_template('mapa.html')


# koli moznosti mat mapu verejne
#@login_required
@places.route('/ajax/pois', methods=['GET'])
def pois():
    if request.method == 'GET':
        pois = poi.find()
        pois = str(json.dumps(list(pois),default=json_util.default))
        return pois



@places.route('/ajax/pois/onroute', methods=['GET'])
#@login_required
@support_jsonp
def icons():
    if request.method == 'GET':
        pois = poi.find()
        pois = str(json.dumps(list(pois),default=json_util.default))
        return pois