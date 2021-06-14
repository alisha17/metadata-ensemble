from app import app, db
from .models import GenomeDatabase, Genome, DataRelease, Organism
from flask import jsonify, request


@app.route("/")
def index():
    """
    Index page for the ensemble search portal
    :return welcome message
    """
    return "Welcome to the Ensemble Search Portal!"


@app.route("/get_species_databases")
def get_genes():
    """
    Endpoint to get database names for given species, release and db_type
    :return JSON returning all the database names matching the user query
    """
    species = request.args.get("species")  # species name
    db_type = request.args.get("db_type")  # db name
    release = request.args.get("release")  # release version

    queries = [Organism.name == species, DataRelease.ensembl_version == release]

    if db_type is not None:
        queries.append(GenomeDatabase.type == db_type)

    ##### Example SQL query
    # SELECT gd.dbname, gd.`type` from genome gen, data_release dr, genome_database gd, organism o
    # WHERE gen.genome_id = gd.genome_id AND dr.data_release_id = gen.data_release_id
    # AND o.organism_id = gen.organism_id
    # AND o.name = 'homo_sapiens'
    # AND dr.ensembl_version = '100';

    q = (
        db.session.query(GenomeDatabase, Genome, DataRelease, Organism)
        .filter(
            Genome.genome_id == GenomeDatabase.genome_id,
            DataRelease.data_release_id == Genome.data_release_id,
            Organism.organism_id == Genome.organism_id,
        )
        .filter(*queries)
        .all()
    )

    format_query_op = dict(
        databases=[
            dict(dbname=genome_database.dbname, type=genome_database.type)
            for genome_database, genome, data_release, organism in q
        ]
    )

    resp = jsonify(format_query_op)
    return resp
