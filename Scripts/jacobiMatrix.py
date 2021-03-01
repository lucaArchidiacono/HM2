import sympy as sym

def createJacobiMatrix(v_str, f_list):
    #liste aller definierten Variablen
    vars = sym.symbols(v_str)
    #liste aller definierten Funktionen mit den vordefinierten Variablen drin
    f = sym.sympify(f_list)
    #Matrix mit 0-en erstellen, welche als Platzhalter dienen um spaeter mit Werte ersetzt zu werden
    J = sym.zeros(len(f),len(vars))
    #Hier wird durch die Liste von Funkionen iteriert
    for i, fi in enumerate(f):
        #Hier wird durch die Liste von Variablen iteriert (innerhalb der momentanen Funktion)
        for j, s in enumerate(vars):
            #Hier wird die momentane Variable (in unserem Beispiel x1 oder x2) genommen und dementsprechend abgeleitet.
            #Anschliessend wird der Platzhalter (0) ersetzt, durch die neu abgeleitete Funktion. 
            J[i,j] = sym.diff(fi, s)
    return J

jacobiMatrix = createJacobiMatrix('x1 x2', ['x1**2 + x2 - 11','x1 + x2**2 - 7'])
print(jacobiMatrix)