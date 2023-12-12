from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Trubi
import logging

from .templates.forms import AppointmentForm

logger = logging.getLogger(__name__)


def base(request):
    form = AppointmentForm(request.POST)
    if form.is_valid():
        namef = form.cleaned_data['name']
        from_email = form.cleaned_data['email']
        adress = form.cleaned_data['adr']
        Phone = form.cleaned_data['phone']
        inform = form.cleaned_data['info']
        text = EmailMultiAlternatives('Заявка на покупку', f'Имя: {namef}'
                                                           f'Почта отправителя: {from_email}'
                                                           f'Адрес: {adress}'
                                                           f'Телефон: {Phone}'
                                                           f'Дополнительная информация: {inform}',
                                      to=['sergey.fomin.90@inbox.ru'])
        text.send()

        return render(request, 'djapp/base.html', {'form': form})

    return render(request, 'djapp/base.html', {'form': form})


def index(request):
    logger.info('Index page accessed')
    return render(request, 'djapp/index.html', )


def about_us(request):
    return render(request, 'djapp/about.html')


def FAQ(request):
    return render(request, 'djapp/FAQs.html')


def products(request):
    Trub = Trubi.objects.all()
    return render(request, 'djapp/products.html', {'Trub': Trub})


def steeltubes(request):
    return render(request, 'djapp/Stubes/steeltubes.html')


def btubes(request):
    return render(request, 'djapp/Stubes/bezshovtubes.html')


def svartubes(request):
    return render(request, 'djapp/Stubes/weldtubes.html')


def Ugltubes(request):
    return render(request, 'djapp/Stubes/UglerodTubes.html')


def Nershavtubes(request):
    return render(request, 'djapp/Stubes/NershavTubes.html')


def CentTubes(request):
    return render(request, 'djapp/SHtubes/CentTubes.html')


def EmptyTubes(request):
    return render(request, 'djapp/SHtubes/EmptyTubes.html')


def IndusTubes(request):
    return render(request, 'djapp/SHtubes/IndusTubes.html')


def RecreatTubes(request):
    return render(request, 'djapp/SHtubes/RecreatTubes.html')


def StatTubes(request):
    return render(request, 'djapp/SHtubes/StatTubes.html')


def ShelezTubes(request):
    return render(request, 'djapp/SHtubes/ShelezTubes.html')


def angle(request):
    return render(request, 'djapp/angles/angle.html')


def angle25(request):
    return render(request, 'djapp/angles/angle25.html')


def angle323(request):
    return render(request, 'djapp/angles/angle323.html')


def angle324(request):
    return render(request, 'djapp/angles/angle324.html')


def angle40(request):
    return render(request, 'djapp/angles/angle40.html')


def angle504(request):
    return render(request, 'djapp/angles/angle504.html')


def angle505(request):
    return render(request, 'djapp/angles/angle505.html')


def angle63(request):
    return render(request, 'djapp/angles/angle63.html')


def angle75(request):
    return render(request, 'djapp/angles/angle75.html')


def angle90(request):
    return render(request, 'djapp/angles/angle90.html')


def Shvellers(request):
    return render(request, 'djapp/Shvellers/Shvellers.html')


def P18(request):
    return render(request, 'djapp/Shvellers/18P.html')


def U18(request):
    return render(request, 'djapp/Shvellers/18U.html')


def U20(request):
    return render(request, 'djapp/Shvellers/20p.html')


def P20(request):
    return render(request, 'djapp/Shvellers/20u.html')


def P24(request):
    return render(request, 'djapp/Shvellers/24p.html')


def U24(request):
    return render(request, 'djapp/Shvellers/24u.html')


def Shvellers(request):
    return render(request, 'djapp/Shvellers/Shvellers.html')


def P18(request):
    return render(request, 'djapp/Shvellers/18P.html')


def U18(request):
    return render(request, 'djapp/Shvellers/18U.html')


def U20(request):
    return render(request, 'djapp/Shvellers/20p.html')


def P20(request):
    return render(request, 'djapp/Shvellers/20u.html')


def P24(request):
    return render(request, 'djapp/Shvellers/24p.html')


def U24(request):
    return render(request, 'djapp/Shvellers/24u.html')


def Lsteel(request):
    return render(request, 'djapp/Lsteel/Lsteel.html')


def L16(request):
    return render(request, 'djapp/Lsteel/L16.html')


def L17(request):
    return render(request, 'djapp/Lsteel/L17.html')


def L36(request):
    return render(request, 'djapp/Lsteel/L36.html')


def L39(request):
    return render(request, 'djapp/Lsteel/L39.html')


def L155(request):
    return render(request, 'djapp/Lsteel/L155.html')


def L165(request):
    return render(request, 'djapp/Lsteel/L165.html')


def Isteel(request):
    return render(request, 'djapp/Isteel/Isteel.html')


def I13(request):
    return render(request, 'djapp/Isteel/I13.html')


def I14(request):
    return render(request, 'djapp/Isteel/I14.html')


def I16(request):
    return render(request, 'djapp/Isteel/I16.html')


def I135(request):
    return render(request, 'djapp/Isteel/I135.html')


def I145(request):
    return render(request, 'djapp/Isteel/I145.html')
