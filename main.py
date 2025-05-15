from flask import Flask, request, render_template

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











if __name__=="__main__":
    app.run(debug=True)