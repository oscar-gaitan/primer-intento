from flask import Flask, jsonify,


app = Flask(__name__)


cliente = [
   {
   
      'id':'1',
      'nombre':'andres',
      'apellido':'perez',
      'correo' : 'andres-perez@gmail.com',
      'telefono':'+523456786589',
      'comentarios':'Deseo recibir mas informacion sobre sus servicios'
   },
   {
      'id':'2',
      'nombre':'miguel',
      'apellido':'gomez',
      'correo' : 'miguel-gomez@gmail.com',
      'telefono': '+527690428569',
      'comentarios':'Deseo recibir mas informacion sobre sus servicios'
   }
]

@app.route('/')
def index():
    return "hola"


@app.route('/registro')
def obteter_cliente():
   return jsonify(cliente)


@app.route('/enviar', methods=['GET','POST'])
def obtener_envio():
   resp = {
      "msg":"ok"
   }


   return jsonify(resp)


if __name__ =='__main__':
    app.run(debug= True)