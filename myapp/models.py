from myapp import db

class City(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True, index=True)
  rank = db.Column(db.Integer)
  is_visited = db.Column(db.Boolean)

  def __repr__(self):
    return f'<City {self.id}: {self.name} {self.rank}>'