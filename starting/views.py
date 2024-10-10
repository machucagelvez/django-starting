from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# Cada función que se crea en views.py es una vista
def saludo(request):
    persona = Persona("Stevie", "Nicks")
    # nombre = "Ozzy"
    # apellido = "Osbourne"
    temas = ["plantillas", "modelos", "formularios", "vistas", "despliegue"]
    ahora = datetime.datetime.now()

    # Se abre el documento html que se va a utilizar:
    # doc_externo = open("C:/ds/django/starting/templates/saludo.html")

    # Se crea la plantilla:
    # plantilla = Template(doc_externo.read())
    # doc_externo.close()

    # Se abre el documento html que se va a utilizar:
    # En settings.py se debe configurar la ruta de las plantillas en TEMPLATES[0]["DIRS"]
    # doc_externo = loader.get_template("saludo.html")

    # Se crea el contexto:
    # Se pueden enviar datos a la plantilla a través de un diccionario:
    # ctx = Context(
    #     {
    #         "nombre_persona": persona.nombre,
    #         "apellido_persona": persona.apellido,
    #         "fecha_actual": ahora,
    #         "temas": temas,
    #     },
    # )

    # Se renderiza la plantilla y se le pasa el contexto:
    # documento = plantilla.render(ctx)

    # Si se usa loader.get_template se debe pasar el contexto en un diccionario:
    # documento = doc_externo.render(
    # {
    #     "nombre_persona": persona.nombre,
    #     "apellido_persona": persona.apellido,
    #     "fecha_actual": ahora,
    #     "temas": temas,
    # },
    # )

    # return HttpResponse(documento)

    # Con el método render no es necesario cargar el documento html previamente, se puede renderizar directamente
    return render(
        request,
        "saludo.html",
        {
            "nombre_persona": persona.nombre,
            "apellido_persona": persona.apellido,
            "fecha_actual": ahora,
            "temas": temas,
        },
    )


def curso_python(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "curso_python.html", {"fecha_actual": fecha_actual})


def curso_css(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "curso_css.html", {"fecha_actual": fecha_actual})


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
