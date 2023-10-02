import time
from app import app, db
from models import User

time.sleep(12)

with app.app_context():
    db.create_all()

    #fill db
    user_exists = User.query.filter_by(email="adam@adam.com").first() is not None

    if (not user_exists):
        test_user = User(
            'Adam',
            'adam@adam.com',
            'adam'
        )

        db.session.add(test_user)
        db.session.commit()