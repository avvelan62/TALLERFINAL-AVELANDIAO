from models.perro import Perro
from models.gato import Gato
from models.boa_constricutor import Boa_Constrictor
from models.huron import Huron
from flask import Blueprint, jsonify, render_template


animal_blueprint = Blueprint('animal_bp', __name__, url_prefix="/animal")

@animal_blueprint.route('/')
def index():
    return render_template("index.html")

@animal_blueprint.route('/perro', methods=['GET'])
def hacer_sonido_perro():
    perro = Perro("Booster", 2, 25)
    return jsonify({"nombre": perro.nombre, "edad": perro.edad, "sonido": perro.hacer_sonido()}), 201
    
    
@animal_blueprint.route('/gato', methods=['GET'])
def hacer_sonido_gato():
    gato = Gato("Michi", 3, 4)
    return jsonify({"nombre": gato.nombre, "edad": gato.edad, "sonido": gato.hacer_sonido()}), 201


@animal_blueprint.route('/huron', methods=['GET'])
def hacer_sonido_huron():
    huron = Huron("Bobby", 1, 2, "Colombia", 12.5)
    return jsonify({"nombre": huron.nombre, "edad": huron.edad, "sonido": huron.hacer_sonido()}), 201
 
    
@animal_blueprint.route('/boa_constrictor', methods=['GET'])
def hacer_sonido_boa():
    boa = Boa_Constrictor("Snake", 5, 10, "Argentina", 20.6)
    return jsonify({"nombre": boa.nombre, "edad": boa.edad, "sonido": boa.hacer_sonido()}), 201
    