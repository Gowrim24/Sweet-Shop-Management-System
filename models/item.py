from extensions import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }
