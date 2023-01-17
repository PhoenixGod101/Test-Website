from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash

views = Blueprint(__name__, "views")

@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/about")
def about():
    return render_template("about.html")