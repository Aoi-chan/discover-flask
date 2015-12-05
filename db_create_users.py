from app import db
from models import Users

db.create_all()

db.session.add(Users("admin", "ad@min.com", "admin"))
db.session.add(Users("foo", "foo@bar.com", "bar"))

db.session.commit()
