from django.http import HttpResponse

def inicio(request):
    nombre = "Mauri"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")