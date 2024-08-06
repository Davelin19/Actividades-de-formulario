from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/')
def inicio ():
    return render_template('index.html')
@app.route ('/formu1')
def formu():
    return render_template('formu1.html')
@app.route ('/respuesta', methods = ['POST'])
def respuesta():
    if request.method == 'POST':
        A = int(request.form['A'])
        B = int(request.form['B'])
        C = int(request.form['C'])

        if A > B and A > C: # type: ignore
            return render_template('formu1.html', respuesta = 'el mayor es A', A=A, B=B, C=C)
        elif B > A and B > C: # type: ignore
             return render_template('formu1.html', respuesta ='el mayor es B', A=A, B=B, C=C)
        elif C > A and C > B: # type: ignore
             return render_template('formu1.html', respuesta = 'el mayor es C', A=A, B=B, C=C)
        else:
             return render_template('formu1.html', respuesta = 'los valores son iguales', A=A, B=B, C=C)

@app.route('/formu2', methods=['GET', 'POST'])
def formu2():
    mensaje = None  
    mensaje_error = None  

    if request.method == 'POST':
        try:
            nota = int(request.form['nota'])

            if nota < 0 or nota > 20:
                mensaje_error = "Fallo"
            elif nota >= 19:
                mensaje = "A"
            elif nota >= 16:
                mensaje = "B"
            elif nota >= 14:
                mensaje = "C"
            elif nota >= 11:
                mensaje = "D"
            else:
                mensaje = "E"
        except ValueError:
            mensaje_error = "Fallo"
    return render_template('formu2.html', mensaje=mensaje, mensaje_error = mensaje_error)

@app.route('/formu3', methods=['GET', 'POST'])
def formu3():
    peso = None  
    mensaje_error = None 
    if request.method == 'POST':
        try:
            resultado1 = int(request.form.get('resultado1', 0))
            resultado2 = int(request.form.get('resultado2', 0))
            resultado3 = int(request.form.get('resultado3', 0))
            resultado4 = int(request.form.get('resultado4', 0))
            resultado5 = int(request.form.get('resultado5', 0))

            dolares = resultado1 + resultado2 + resultado3 + resultado4 + resultado5
            peso = dolares * 4154
        except ValueError:
            mensaje_error = "Fallo"
    return render_template('formu3.html', pesos = peso, mensaje_error = mensaje_error)


@app.route('/formu4', methods=['GET', 'POST'])
def formu4():
    producto = None 
    if request.method == 'POST':
        try:
            num = int(request.form['numero'])
            doble = num * 2
            triple = num * 3
            producto = {'doble': doble,'triple': triple}
        except ValueError:
            producto = "Fallo"
    return render_template('formu4.html', producto = producto)
       
            
@app.route('/formu5', methods=['GET', 'POST'])
def areformu5():
    figura = None
    calcular_area = None
    error = None

    if request.method == 'POST':
        figura = request.form['figura']
        try:
            if figura == 'cuadrado':
                radio = float(request.form['radio'])
                calcular_area = 3.14159 * (radio ** 2)
            elif figura == 'triangulo':
                lado = float(request.form['lado'])
                calcular_area = lado ** 2
            elif figura == 'circulo':
                largo = float(request.form['largo'])
                ancho = float(request.form['ancho'])
                calcular_area = largo * ancho
            elif figura == 'rectangulo':
                base = float(request.form['base'])
                altura = float(request.form['altura'])
                calcular_area = 0.5 * base * altura
            else:
                error = "Figura no existente"
        except ValueError:
            error = "ingrese valores válidos para calcular"

    return render_template('formu5.html', figura = figura, area = calcular_area, error = error)
    
if __name__=='__main__':
    app.run(debug=True)

