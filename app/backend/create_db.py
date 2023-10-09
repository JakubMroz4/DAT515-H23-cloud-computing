import time
from app import app, db
from models import *
from werkzeug.security import generate_password_hash

time.sleep(8)

with app.app_context():
    db.create_all()

    #fill db

    test_post1 = Post(
     'Adam',
      'comment1',
    )

    test_post2 = Post(
        'Adam2',
        'comment2',
    )

    db.session.add(test_post1)
    db.session.add(test_post2)
    db.session.commit()
