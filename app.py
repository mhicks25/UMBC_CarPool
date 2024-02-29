from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

#index
@app.route('/')
def index():
    return render_template('index.html')