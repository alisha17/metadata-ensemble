from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_user = "anonymous"
db_name = "ensembl_metadata_104"
db_host = "ensembldb.ensembl.org"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{db_user}@{db_host}/{db_name}"
db = SQLAlchemy(app)

from app import routes, models
