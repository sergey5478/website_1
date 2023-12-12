from django.urls import path
from . import views

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.index, name='main_page'),
    path('about-us', views.about_us, name='about_page'),
    path('FAQ', views.FAQ, name='FAQ_page'),
    path('products', views.products, name='products_page'),

    path('tubes1', views.steeltubes, name='Stalnie_Trubi'),
    path('tubes1_1', views.btubes, name='Bezshovnie_Trubi'),
    path('tubes1_2', views.svartubes, name='Svarochnie_Trubi'),
    path('tubes1_3', views.Nershavtubes, name='NershavTubes'),
    path('tubes1_4', views.Ugltubes, name='UglerodTubes'),

    path('tubes2', views.ShelezTubes, name='ShelezobetTubes'),
    path('tubes2_1', views.EmptyTubes, name='PustotelieTubes'),
    path('tubes2_2', views.IndusTubes, name='IndustrialTubes'),
    path('tubes2_3', views.RecreatTubes, name='RecreatTubes'),
    path('tubes2_4', views.StatTubes, name='StaticTubes'),
    path('tubes2_5', views.CentTubes, name='CentriFugeTubes'),

    path('angle', views.angle, name='angle'),
    path('angle25', views.angle25, name='angle25'),
    path('angle323', views.angle323, name='angle323'),
    path('angle324', views.angle324, name='angle324'),
    path('angle40', views.angle40, name='angle40'),
    path('angle504', views.angle504, name='angle504'),
    path('angle505', views.angle505, name='angle505'),
    path('angle63', views.angle63, name='angle63'),
    path('angle75', views.angle75, name='angle75'),
    path('angle90', views.angle90, name='angle90'),

    path('Shvellers', views.Shvellers, name='Shvellers'),
    path('18P', views.P18, name='18P'),
    path('18U', views.U18, name='18U'),
    path('20p', views.P20, name='20p'),
    path('20u', views.U20, name='20u'),
    path('24p', views.P24, name='24p'),
    path('24u', views.U24, name='24u'),

    path('Lsteel', views.Lsteel, name='Lsteel'),
    path('I13', views.I13, name='I13'),
    path('I14', views.I14, name='I14'),
    path('I16', views.I16, name='I16'),
    path('I135', views.I135, name='I135'),
    path('I145', views.I145, name='I145'),

    path('Isteel', views.Isteel, name='Isteel'),
    path('L16', views.L16, name='L16'),
    path('L17', views.L17, name='L17'),
    path('L36', views.L36, name='L36'),
    path('L39', views.L39, name='L39'),
    path('L155', views.L155, name='L155'),
    path('L165', views.L165, name='L165'),

]
