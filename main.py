from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

usuario=[]
id_contador=1

@app.route("/", methods=["GET", "POST"])
def crud():
    global id_contador
    if request.method=="POST":
        nombre=request.form["nombre"]
        correo=request.form["correo"]
        usuario.append({"id": id_contador, "nombre": nombre, "correo": correo})
        id_contador+=1
        # print(usuario)
    eliminar_id=request.args.get("eliminar")
    if eliminar_id:
        for diccionario in usuario:
            if str(diccionario["id"])==eliminar_id:
                usuario.remove(diccionario)
                break
    return render_template("crud.html", usuario=usuario)

# ruta para editar la informacion del usuario
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    # TODO: capturar y buscar el usuario a editar
    for diccionario in usuario: # para cada diccionario centro de la lista evalue:
        if diccionario["id"]==id: # si el id convertido a string es igual al id que me pasan por parametro
            usuario_a_editar=diccionario # hemos identificado el usario a editar
            break
    # print(usuario_a_editar)
    # TODO: actualizar la informacion del usuario seleccionado
    if request.method=="POST":
        usuario_a_editar["nombre"]=request.form.get("nombre") # el nombre nuevo sera el que llegue por un nuevo formulario
        usuario_a_editar["correo"]=request.form.get("correo") # el correo nuevo sera el que llegue por un nuevo formulario
        return redirect(url_for("crud")) # redirecciona la aplicacion a la ruta de la funcion crud
    
    return render_template("editar.html", usuario_a_editar=usuario_a_editar)







if __name__=="__main__":
    app.run(debug=True)