from datetime import datetime
from extensions import db

class Test(db.Model):

    __tablename__ = "Messages"

    id = db.Column(db.Integer, primary_key=True)

    test_text = db.Column(db.String(76))

    def data(self):

        return {
            "id": self.id,
            "test_text": self.test_text,
            "email": self.email,
            "message": self.message,
        }
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).all()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()