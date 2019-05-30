from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def paciente_list(request):
    return render(request, 'paciente/list.html')
def paciente_show(request, paciente_id):
    return render(request, 'paciente/show.html', {'id':paciente_id})

# Create your views here.


   # def home(request):
 #   return render(request, 'home.html')
   # def time(request, time):
  #  return render(request, 'time.html', {'time':time})
    #def jogador(request, time, jogador):
    #return render(request, 'jogador.html', { 'jogador':jogador})
#def melhor(request, time, jogador, melhor):
#    return render(request, 'melhor.html', {'melhor':melhor})