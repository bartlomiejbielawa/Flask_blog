from flaskblog import app

if __name__ == "__main__":
    app.run(debug=True)


# set FLASK_APP=run.py
# flask run
# set FLASK_DEBUG=1

# for databases
# from flaskblog import db
# db.create_all()
# from flaskblog import User, Post
# user_1 = User(...)
# db.session.add(user_1)
# db.session.commit()
# User.query.all()
# User.query.filter_by(username="Bartek").all()
# user = User.query.get(1) - id
