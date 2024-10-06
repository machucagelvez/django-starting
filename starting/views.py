from django.http import HttpResponse
import datetime
from django.template import Template, Context


# Cada función que se crea en views.py es una vista
def saludo(request):
    # Se abre el documento html que se va a utilizar:
    doc_externo = open("C:/ds/django/starting/templates/saludo.html")

    # Se crea la plantilla:
    plantilla = Template(doc_externo.read())
    doc_externo.close()

    # Se crea el contexto:
    ctx = Context()

    # Se renderiza la plantilla y se le pasa el contexto:
    documento = plantilla.render(ctx)

    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Ahí se ven!")


def obtenerFecha(request):
    fechaActual = datetime.datetime.now()
    return HttpResponse("Fecha y hora actuales: %s" % fechaActual)


def calcularEdad(request, edad, anio):
    periodo = anio - 2024
    edadFutura = periodo + edad
    documento = """
        <html>
            <body>
                <h2>En el año %s tendrás %s años</h2>
            </body>
        </html>
""" % (
        anio,
        edadFutura,
    )

    return HttpResponse(documento)
