from app import db


class GenomeDatabase(db.Model):
    """
    Mapping for table 'genome_database'
    """

    __tablename__ = "genome_database"

    genome_database_id = db.Column(db.Integer, primary_key=True)
    genome_id = db.Column(db.Integer)
    type = db.Column(db.String(20))
    dbname = db.Column(db.String(128))


class Genome(db.Model):
    """
    Mapping for table 'genome'
    """
    __tablename__ = "genome"

    genome_id = db.Column(db.Integer, primary_key=True)
    organism_id = db.Column(db.Integer)
    data_release_id = db.Column(db.Integer)


class DataRelease(db.Model):
    """
    Mapping for table 'data_release'
    """
    __tablename__ = "data_release"

    data_release_id = db.Column(db.Integer, primary_key=True)
    ensembl_version = db.Column(db.Integer)


class Organism(db.Model):
    """
    Mapping for table 'organism'
    """
    __tablename__ = "organism"

    organism_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), primary_key=True)
