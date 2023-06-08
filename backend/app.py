from flask import Flask
from models.database import db, init_db
from controllers.routes import need_routes

app = Flask(__name__)

# Db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:post_123@localhost:5432/autopay"
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

# Once connectivity is established create the tables
with app.app_context():
    db.create_all()

app.register_blueprint(need_routes)

@app.route("/")
def home():
    return {"check": "Checking if the route works"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8000, debug=True)