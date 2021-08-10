from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from sqlalchemy_serializer import SerializerMixin

class Food(db.Model, SerializerMixin):
    __tablename__ = 'food'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    razdel = db.Column(db.String)
    weight = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def get_all_food(cls):
        foods = cls.query.all()
        if not foods:
            return []
        return foods


    @classmethod
    def edit_food(cls, id, data):
        cls.query.filter(cls.id==id).update(data)
        db.session.commit()


    @classmethod
    def change_activity(cls, id, data: bool):
        food = cls.query.filter_by(id=id).first()
        if not food:
            return []
        food.is_active=data
        return food

    @classmethod
    def delete(cls, id):
        food = cls.query.filter_by(id=id).first()
        if not food:
            return []
        db.session.delete(food)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'name': self.name, "description": self.description, "price": self.price, 'razdel': self.razdel, 'weight': self.weight, 'is_active': self.is_active}
