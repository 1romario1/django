from django.http import HttpResponse
import datetime

def introduccion(request):
    documento="""<html>
    <body>
    <h1>Esta es mi primera pagina con django<h1>
    <body>
    <style>
    h1{
        color:blue}
    <style>
    <html>"""
    return HttpResponse(documento)
def saludo(request):
    return HttpResponse('hola')

def despedir(request):
    return HttpResponse('Adios')

def fecha(request):
    fechas=datetime.datetime.now()
    fecha_actual="""
    <html>
    <body>
    <h2>Fecha alctual= %s<h2>
    <body>
    <html>"""%fechas
    return HttpResponse(fecha_actual)

def calcularEdad(request,edad,agno):
    periodo=agno-2023
    edadFutura=edad+periodo
    documento="""<html>
    <body>
    <h2>En el año %s tendras %s años""" %(agno,edadFutura)
    return HttpResponse(documento)
    
