def getAreaRectangulo(largo, ancho):
    resultado = largo * ancho
    return resultado
def getAreaTriangulo(base, altura):
    resultado = 0.5 * base * altura
    return resultado

# Función principal
def principal():
    largo = 4
    ancho = 6
    print("Largo: ", largo)
    print("Ancho: ", ancho)
    print("Área del rectángulo:", getAreaRectangulo(largo, ancho))

    base = 5
    altura = 8
    print("Base: ", base)
    print("Altura: ", altura)
    print("Área del triángulo:", getAreaTriangulo(base, altura))

principal()
