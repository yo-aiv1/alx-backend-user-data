#!/usr/bin/env python3

""" Route module for the API """

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ welcome message """
    return jsonify({"message": "Bienvenue"})
