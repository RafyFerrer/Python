from flask import Flask, request, render_template
app = Flask ("Prueba de aplicación")
contador = 0
contador_visitas = 0
@app.route('/inicio') #Esto es un decorador, es decir, la función que venga a continuación es decorada por este
def inicio(): #Se invocará este método con ---url ----/inicio
    return '''
    <html>
    <body>
    ESTO ES UNA PRUEBA
    </body>
    </html> 
    '''
@app.route ('/hola') #Esto es un decorador, es decir, la función que venga a continuación es decorada por este
def pagina_hola():
    global contador
    contador=contador+1
    return f'''
    <html>
    <body>
    ESTO ES UNA PRUEBA vista {contador}
    </body>
    </html> 
    '''
@app.route('/suma',methods=['GET','POST'])
def suma():
    if request.method == 'GET':
        contenido = '''<html>
                <head><title>Suma - resultado</title></head> <body>
                <form action="/suma" method="POST">
                    <label>Sumando 1:</label>
                    <input type="text" name="Sumando1"/>
                    <label>Sumando 2:</label>
                    <input type="text" name="Sumando2"/><br/><br/>
                    <input type="submit" value="CALCULAR"/>
                </form>
                <body><html>'''
    elif request.method == 'POST':
        sumando1 = int(request.form.get('Sumando1'))
        sumando2 = int(request.form.get('Sumando2'))
        resultado = sumando1+sumando2
        contenido = f'Suma: {sumando1} + {sumando2} = {resultado}'
    else:
        contenido = 'Metodo no permitido'
    return contenido

@app.route('/tabla/<int:numero>')
def tabla_multiplicar(numero):
    cabecera = f'''<html>
                <head><title>Tabla del {numero}</title></head>
                <body> <table> '''
    tabla = ''
    for i in range(1,11):
        fila = f'<tr> <td> {numero} x {i} </td> <td> <b>=</b> </td> <td> {numero*i} </td></tr>'
        tabla += fila
    pie = '</table></body></html>'
    contenido = cabecera + tabla + pie
    return contenido

@app.route('/2')
def index2():
    global contador_visitas
    contador_visitas += 1
    return render_template('index2.html', contador_visitas = contador_visitas)
    # la plantilla que está rendirizando llamada index.html tiene que estar forzosamente en una carpeta llamada templates dentro del proyecto
    # si en el HTML que está renderizando hay contenido estático externo (como un logo o imagen) ha de estar forzosamente en una carpeta llamada static


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)