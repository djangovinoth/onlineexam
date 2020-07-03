from django.shortcuts import render

from django.contrib import messages

# Create your views here.

def labhome(request):

    return render(request, 'lab/labhome.html')

def resize(request):

    return render(request, 'actions/resize.html')


def slider(request):

    return render(request, 'actions/slider.html')


def rightclick(request):

    return render(request, 'actions/rightclick.html')


def sortable(request):

    return render(request, 'actions/sortable.html')




# js
def scroll(request):

    return render(request, 'jsscript/scroll.html')

def jsclickandtype(request):

    return render(request, 'jsscript/jsclickandtype.html')

def dom(request):

    return render(request, 'jsscript/dom.html')

def highlight(request):

    return render(request, 'jsscript/highlight.html')

def enabledOrDisabled(request):

    return render(request, 'jsscript/enabledOrDisabled.html')







def doubleclick(request):

    return render(request, 'actions/doubleclick.html')

def draganddrop(request):

    return render(request, 'actions/draganddrop.html')

def selectable(request):

    return render(request, 'actions/selectable.html')

def mousehover(request):

    return render(request, 'actions/mousehover.html')

def tooltip(request):

    return render(request, 'actions/tooltip.html')






def SingleAndMultiImage(request):

    return render(request, 'images/SingleAndMultiImage.html')

def brokenimage(request):

    return render(request, 'images/brokenimage.html')











def input(request):

    return render(request, 'elements/input.html')


def checkbox(request):

    return render(request, 'elements/checkbox.html')


def radiobutton(request):

    return render(request, 'elements/radiobutton.html')


def statictable(request):

    return render(request, 'elements/statictable.html')

def dynamictable1(request):

    return render(request, 'elements/dynamictable1.html')

def dynamictable2(request):

    return render(request, 'elements/dynamictable2.html')

def dynamictable3(request):

    return render(request, 'elements/dynamictable3.html')

def browserintent(request):

    return render(request, 'elements/browserintent.html')
def frameset(request):

    return render(request, 'elements/frameset.html')


def bootstrapalert(request,msg='no'):

    if msg=='info':
        messages.info(request, f'info alert !')
    if msg=='success':
        messages.success(request, f'success alert !')
    if msg=='warning':
        messages.warning(request, f'warning alert !')

    return render(request, 'elements/bootstrapalert.html')








def alert(request):

    return render(request, 'elements/alert.html')


def multiwindow(request):

    return render(request, 'elements/multiwindow.html')


def FileUploadDownload(request):

    return render(request, 'elements/FileUploadDownload.html')
def AddOrRemove(request):

    return render(request, 'elements/addOrRemove.html')






def keyname(request):

    return render(request, 'elements/keyname.html')
def endlessscroll(request):
    arr=[]

    for i in range(1000):
        arr.append(i)

    context={
    'arr':arr,
    }
    return render(request, 'elements/endlessscroll.html',context)


def currentlocation(request):

    return render(request, 'elements/currentlocation.html')




def dropdown(request):

    return render(request, 'elements/dropdown.html')
def autocomplete(request):

    return render(request, 'elements/autocomplete.html')

def datepicker(request):

    return render(request, 'elements/datepicker.html')
def progressbar(request):

    return render(request, 'elements/progressbar.html')
def tabs(request):

    return render(request, 'elements/tabs.html')


def simpleform(request):

    if request.method == 'POST':

        messages.success(request, f'{request.POST.get("product")} submitted successfully !')
    context={

    'max':False,

    }
    return render(request, 'framework/simpleform.html',context)

def loginform(request):
    max=False
    user=""
    checkout=False
    count=0
    if count==0:
        max=False


    if request.method == 'POST':
        if request.POST.get("username"):
            user=request.POST.get("username")
            messages.success(request, f'{request.POST.get("username")} login successfully !')
        elif request.POST.get("product"):
            count=int(request.POST.get("count"))
            count=count+1
            if count<5:
                messages.success(request, f'{request.POST.get("product")} {count} submitted successfully !')
            else:
                messages.success(request, f'{user} reached max count !')
                max=True
        elif request.POST.get("coupon"):
                messages.success(request, f'{user} You have done checkout !')
                checkout=True
        context={
        'count':count,
        'max':max,
        'checkout':checkout,
        }
        return render(request, 'framework/simpleform.html',context)

    return render(request, 'framework/loginform.html')
