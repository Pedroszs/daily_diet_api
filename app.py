from flask import Flask, request, jsonify
from models.daily_diet_db import db
from models.diet import Diet
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin123@127.0.0.1:3306/daily-diet-db"
db.init_app(app)

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




if __name__ == "__main__":
    app.run(debug=True)