from db import db
from flask_restful import Resource, reqparse
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine import reflection
from ast import literal_eval

metadata = db.MetaData(db.engine)
def init_table(name):
  return db.Table(name, meta, autoload = True, schema='public')

class StatView(Resource):

  insp = reflection.Inspector.from_engine(db.engine) 
  print(insp.get_view_names())

  MyView = db.Table("stat_by_date", metadata,
                    db.Column("score_id", db.Integer, primary_key=True), 
                    extend_existing=True, autoload=True)

  print(MyView)
