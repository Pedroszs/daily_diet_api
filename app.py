from flask import Flask, request, jsonify
from models.daily_diet_db import db
from models.diet import Diet
from models.users import User
from datetime import datetime
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import bcrypt

#CRUD: Create(POST), Read(GET), Upd(PUT), Del(DELETE)

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin123@127.0.0.1:3306/daily-diet-db"

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
# Showing with http route im using for the login
login_manager.login_view = "login" 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        #login
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "autenticação realizada com sucesso"})
    
    return jsonify({"message": "credenciais invalidos"}), 400

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})

@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user = User(username=username, password=hashed_password, role="user") 
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuario cadastrado com sucesso!"})

    return jsonify({"message": "Dados invalidos."}), 400


@app.route("/diet", methods=["POST"])
def new_register():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    date_time = data.get("date_time")
    f_diet = data.get("f_diet")

    if name and description and date_time and f_diet is not None:
        # Converte string para datetime
        date_time_obj = datetime.fromisoformat(date_time)
        
        user_diet = Diet(
            name=name,
            description=description,
            date_time=date_time_obj,
            f_diet=f_diet
        )
        db.session.add(user_diet)
        db.session.commit()
        return jsonify({"message": "Refeição registrada com sucesso!!"})
    
    return jsonify({"message": "Verifique se foram adicionadas todas as informações necessárias."}), 404

@app.route("/diet/<int:id_diet>", methods=["PUT"])
def upd_register(id_diet):
    data = request.json
    diet = Diet.query.get(id_diet)

    if diet:
        diet.name = data.get("name")
        diet.description = data.get("description")
        diet.date_time = data.get("date_time")
        diet.f_diet = data.get("f_diet")
        db.session.commit()
        return jsonify({"message": f"alterações no registro {id_diet} realizadas com sucesso"})
    
    return jsonify({"messagem": "A tarefa selecionada não existe"}), 400

@app.route("/diet/<int:id_diet>", methods=["DELETE"])
def del_register(id_diet):
    diet_del = Diet.query.get(id_diet)

    if diet_del:
        db.session.delete(diet_del)
        db.session.commit()
        return jsonify ({"message": f"Registro {id_diet} deletado com sucesso!!"})
    
    return jsonify({"message": "O registro insediro não existe"}), 400








if __name__ == "__main__":
    app.run(debug=True)