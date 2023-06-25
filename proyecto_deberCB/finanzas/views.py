from django.shortcuts import render
from finanzas.models import EntidadFinanzas

# Create your views here.
def listar_coop(request):
    las_cooperativas = EntidadFinanzas.objects.all()
    num_cooperativas = len(EntidadFinanzas)
    informacion_template = {"la_cooperativas": las_cooperativas, "numero_cooperativas": num_cooperativas}
    return render(request, "cooperativas.html", informacion_template)
