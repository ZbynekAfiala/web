from flask import Flask, render_template
from forms import PoptatForm

app = Flask(__name__)

app.secret_key = "AsEfGG1123p"
