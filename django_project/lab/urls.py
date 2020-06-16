from django.urls import path
from . import views


urlpatterns = [

    path('labhome/', views.labhome, name='labhome'),
    path('resize/', views.resize, name='resize'),
    path('slider/', views.slider, name='slider'),
    path('rightclick/', views.rightclick, name='rightclick'),
    path('doubleclick/', views.doubleclick, name='doubleclick'),
    path('draganddrop/', views.draganddrop, name='draganddrop'),
    path('selectable/', views.selectable, name='selectable'),
    path('mousehover/', views.mousehover, name='mousehover'),
    path('tooltip/', views.tooltip, name='tooltip'),
    path('sortable/', views.sortable, name='sortable'),


    path('scroll/', views.scroll, name='scroll'),
    path('jsclickandtype/', views.jsclickandtype, name='jsclickandtype'),
    path('dom/', views.dom, name='dom'),
    path('highlight/', views.highlight, name='highlight'),
    path('enabledOrDisabled/', views.enabledOrDisabled, name='enabledOrDisabled'),



    path('SingleAndMultiImage/', views.SingleAndMultiImage, name='SingleAndMultiImage'),
    path('brokenimage/', views.brokenimage, name='brokenimage'),


    path('input/', views.input, name='input'),
    path('checkbox/', views.checkbox, name='checkbox'),
    path('radiobutton/', views.radiobutton, name='radiobutton'),
    path('statictable/', views.statictable, name='statictable'),
    path('dynamictable1/', views.dynamictable1, name='dynamictable1'),
    path('dynamictable2/', views.dynamictable2, name='dynamictable2'),
    path('dynamictable3/', views.dynamictable3, name='dynamictable3'),
    path('alert/', views.alert, name='alert'),
    path('multiwindow/', views.multiwindow, name='multiwindow'),
    path('FileUploadDownload/', views.FileUploadDownload, name='FileUploadDownload'),
    path('AddOrRemove/', views.AddOrRemove, name='AddOrRemove'),
    path('browserintent/', views.browserintent, name='browserintent'),
    path('frameset/', views.frameset, name='frameset'),
    path('bootstrapalert/<str:msg>/', views.bootstrapalert, name='bootstrapalert'),
    path('dropdown/', views.dropdown, name='dropdown'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('datepicker/', views.datepicker, name='datepicker'),
    path('progressbar/', views.progressbar, name='progressbar'),
    path('tabs/', views.tabs, name='tabs'),









    path('keyname/', views.keyname, name='keyname'),
    path('endlessscroll/', views.endlessscroll, name='endlessscroll'),
    path('currentlocation/', views.currentlocation, name='currentlocation'),




]
