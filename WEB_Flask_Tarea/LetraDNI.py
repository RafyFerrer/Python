from flask import Flask,render_template,request

app=Flask("Cálculo de la letra del DNI")
letra=""
n_DNI=0

def calcula_letra_dni (numero):
    codigo ="TRWAGMYFPDXBNJZSQVHLCKE"
    clave = numero % 23
    return codigo[clave]

@app.route("/",methods=['GET','POST'])
def principal():
    global letra
    global n_DNI
    pagina="calculaletra.html"
    if request.method =="POST":
        n_DNI = int(request.form.get('DNI'))
        letra = calcula_letra_dni(int(n_DNI))
        pagina="calculaletrarespuesta.html"
    return render_template(pagina,letradni=letra,numerodni=n_DNI)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)