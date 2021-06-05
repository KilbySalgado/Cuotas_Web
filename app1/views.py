from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

calculadora = [
    {
        'monto': 1000,
        'tasa': 21,
        'plazo':24,
        'cuota':51.39,
        'total':1233.36

    },
    {
        'monto': 2500,
        'tasa': 21,
        'plazo':36,
        'cuota':94.19,
        'total':3390.84
    }
]


def calculo(request):
        if request.method == 'POST':
            monto = int(request.POST.get('monto'))
            tasa = int(request.POST.get('tasa'))
            plazo = int(request.POST.get('plazo'))
            cuota = (monto*((tasa/100)/12)/(1-(1+((tasa/100)/12))**(-plazo*12)))
            total = cuota*(plazo*12)


            ctx = {
                'calculadora': calculadora
            }

            calculadora.append({
                'monto': monto,
                'tasa': tasa,
                'plazo': plazo,
                'cuota': cuota,
                'total':total,
            })

            return render(request, 'cuota/index.html', ctx)
        else:
            ctx = {
                'calculadora': calculadora
            }

            return render(request, 'cuota/index.html', ctx)