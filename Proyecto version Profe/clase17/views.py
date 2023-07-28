from django.http import HttpResponse
from django.template import template, context


def bienvenida(request):
    return HttpResponse ("Bienvenido a mi primer saludo!!!!")

def bienvenida_html(request):
    response = """
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h1>Comision 55630!!</h1>
    </html>
    """

    return HttpResponse (response)

def saludar(request, nombre):
    response = f"Hola, Bienvenido {nombre} al curso de django"
    return HttpResponse(response)


def bienvenida_template(request):
    miHtml = open("C:/Users/Arlette/Desktop/Codehouse%20Python/Clase%2017%20jueves%2027-07-23/clase17/clase17/plantillas/bienvenido.html")
    plantilla = miHtml.read()
    miHtml.close()
    micontexto = context()
    documento = plantilla.render(micontexto)
    return HttpResponse(documento)

