from flask import Flask, redirect, url_for
from controllers.animal_controller import animal_blueprint

app = Flask(__name__, template_folder='views')

app.register_blueprint(animal_blueprint)

# Redirigir la raíz al blueprint
@app.route('/')
def home():
    return redirect(url_for('animal_bp.index')) 

if __name__ == "__main__":
    app.run()