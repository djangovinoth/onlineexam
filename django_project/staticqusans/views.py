from django.shortcuts import render


from django.shortcuts import render,redirect
from .models import StaticQuestions
from .forms import StaticQuestionsForm
# Create your views here.
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.utils import timezone
import time

# Create your views here.

def staticqusans(request):
    return render(request, 'staticqusans/staticqus.html')

def showques(request,technology):
    print('showques', technology)
    c = request.GET.get('page', 1)
    jobset=StaticQuestions.objects.filter(user=request.user,technology=technology)

    paginator = Paginator(jobset, 5)

    try:
        page = paginator.page(c)

    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)


    # jobset=Questions.objects.filter(user=request.user,level=level)


    context={
    'jobset':jobset,
    'per':page,
    }

    return render(request, 'staticqusans/showques.html',context)





def addques(request):


    if request.method == 'POST':

        job_form = StaticQuestionsForm(request.POST)
        if job_form.is_valid():
            technology = job_form.cleaned_data["technology"]
            question = job_form.cleaned_data["question"]
            answer = job_form.cleaned_data["answer"]
            created_at=datetime.datetime.now()
            t=StaticQuestions(user=request.user,technology=technology,question=question,answer=answer,created_at=created_at)
            t.save()
            messages.success(request, f'new question added successfully!')

        else:
            messages.warning(request, f'sorry something went wrong please try again')

    else:

        job_form = StaticQuestionsForm()
    context={
    'job_form':job_form,
    }


    return render(request, 'staticqusans/addques.html',context)


def editquestions(request,technology,id):
    jobset=StaticQuestions.objects.filter(user=request.user,technology=technology,id=id)[0]
    print('edit')
    print(jobset)
    if request.method == 'POST':


        job_form = StaticQuestionsForm(request.POST)
        if job_form.is_valid():

            totallevel=StaticQuestions.objects.filter(user=request.user,technology=technology,id=id)[0]
            print(totallevel)


            totallevel.technology=request.POST.get("technology")
            totallevel.question=request.POST.get("question")
            totallevel.answer=request.POST.get("answer")

            totallevel.save()
            # Update data in Db
            totallevel.save(update_fields=['technology'])
            totallevel.save(update_fields=['question'])
            totallevel.save(update_fields=['answer'])
            messages.success(request, f'edited successfully !')
        else:
            print(job_form.errors)
            pass

    else:

        job_form = StaticQuestionsForm(StaticQuestions.objects.filter(user=request.user,technology=technology,id=id).values('technology','question','answer')[0])
    context={
    'job_form':job_form,
    'jobset':jobset
    }

    return render(request, 'staticqusans/editstaticquestion.html',context)



def deletequestions(request,technology,id):
    jobset=StaticQuestions.objects.filter(user=request.user,technology=technology,id=id)[0]
    if jobset:

        jobset.delete()
        return redirect('showques',technology=technology)

    return render(request, 'staticqusans/showques.html')




def showques_std(request,technology):

    c = request.GET.get('page', 1)
    jobset=StaticQuestions.objects.filter(technology=technology)



    paginator = Paginator(jobset, 5)

    try:
        page = paginator.page(c)

    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context={
    'jobset':jobset,
    'per':page,
    'technology':technology
    }

    return render(request, 'staticqusans/showques_std.html',context)
