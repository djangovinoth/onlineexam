from django.shortcuts import render,redirect
from blog.models import Questions,Answers
from blog.forms import QuestionsForm
# Create your views here.
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

def addquestions(request):
    jobset=Questions.objects.filter(user=request.user)

    if request.method == 'POST':

        job_form = QuestionsForm(request.POST)
        if job_form.is_valid():
            totallevel=Questions.objects.filter(user=request.user,level=job_form.cleaned_data["level"]).count()
            print(totallevel)
            if totallevel<10:


                x = datetime.datetime.now()

                print(x.strftime("%m%d%Y%H%M%S%f"))

                qid=x.strftime("%m%d%Y%H%M%S%f")
                level = job_form.cleaned_data["level"]
                technology = job_form.cleaned_data["technology"]
                question = job_form.cleaned_data["question"]
                answera = job_form.cleaned_data["answera"]
                answerb = job_form.cleaned_data["answerb"]
                answerc = job_form.cleaned_data["answerc"]
                answerd = job_form.cleaned_data["answerd"]
                correctanswer = job_form.cleaned_data["correctanswer"]

                t=Questions(user=request.user,level=level,technology=technology,question=question,answera=answera,
                answerb=answerb,answerc=answerc,answerd=answerd,correctanswer=correctanswer,qid=qid)
                t.save()
                messages.success(request, f'added success fully !')

                # return redirect('java-questions')
            else:
                messages.success(request, f'{job_form.cleaned_data["level"]} and {job_form.cleaned_data["technology"]} reached max count of 10 questions. Please choose another level')

        else:
            pass

    else:

        job_form = QuestionsForm()
    context={
    'job_form':job_form,
    'jobset':jobset
    }

    return render(request, 'exam/addquestion.html',context)

def editquestions(request,level,technology,qid):
    jobset=Questions.objects.filter(user=request.user,level=level,technology=technology,qid=qid)[0]
    print('edit')
    print(jobset)
    if request.method == 'POST':


        job_form = QuestionsForm(request.POST)
        if job_form.is_valid():

            totallevel=Questions.objects.filter(user=request.user,level=job_form.cleaned_data["level"],technology=technology,qid=qid)[0]
            print(totallevel)


            totallevel.level=request.POST.get("level")
            totallevel.technology=request.POST.get("technology")
            totallevel.question=request.POST.get("question")
            totallevel.answera=request.POST.get("answera")
            totallevel.answerb=request.POST.get("answerb")
            totallevel.answerc=request.POST.get("answerc")
            totallevel.answerd=request.POST.get("answerd")
            totallevel.correctanswer=request.POST.get("correctanswer")

            totallevel.save()
            # Update data in Db
            totallevel.save(update_fields=['level'])
            totallevel.save(update_fields=['technology'])
            totallevel.save(update_fields=['question'])
            totallevel.save(update_fields=['answera'])
            totallevel.save(update_fields=['answerb'])
            totallevel.save(update_fields=['answerc'])
            totallevel.save(update_fields=['answerd'])
            totallevel.save(update_fields=['correctanswer'])
            messages.success(request, f'edited success fully !')
        else:
            print(job_form.errors)
            pass

    else:

        job_form = QuestionsForm()
    context={
    'job_form':job_form,
    'jobset':jobset
    }

    return render(request, 'exam/editquestion.html',context)


def view_java_questions(request,level,technology):

    print(technology)
    c = request.GET.get('page', 1)
    jobset=Questions.objects.filter(user=request.user,level=level,technology=technology)

    paginator = Paginator(jobset, 1)

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

    return render(request, 'exam/viewjavaquestion.html',context)





def show_levels(request,technology):

    print(technology)
    jobset=Questions.objects.filter(technology=technology).values('level').order_by('level').distinct()


    context={
    'jobset':jobset,
    'technology':technology,

    }

    return render(request, 'exam/showlevels.html',context)

def student_show_levels(request,technology):

    print(technology)
    jobset=Questions.objects.filter(technology=technology).values('level').order_by('level').distinct()


    context={
    'jobset':jobset,
    'technology':technology,

    }

    return render(request, 'exam/studentshowlevels.html',context)



def deletequestions(request,level,technology,qid):
    jobset=Questions.objects.filter(user=request.user,level=level,technology=technology,qid=qid)[0]
    if jobset:

        jobset.delete()
        return redirect('view-java-questions',level=level,technology=technology)

    return render(request, 'exam/viewjavaquestion.html')


def student_view_java_questions(request,level,technology,qid='NONE'):


    if request.method == 'POST':
        if request.POST.get("stdans") is None:
            messages.info(request, f'Please select any options!')
        else:

            add=Answers.objects.filter(user=request.user,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid")).count()
            print(Answers.objects.filter(user=request.user,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid")))
            if add==0:
                t=Answers(user=request.user,attemptid='1',level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"),stdanswer=request.POST.get("stdans"))
                t.save()
                messages.success(request, f'added success fully !')
            else:
                update=Answers.objects.filter(user=request.user,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"))[0]
                print(update)


                update.attemptid='1'
                update.level=request.POST.get("level")
                update.technology=request.POST.get("technology")
                update.qid=request.POST.get("qid")
                update.stdanswer=request.POST.get("stdans")

                update.save()
                # Update data in Db
                update.save(update_fields=['attemptid'])
                update.save(update_fields=['level'])
                update.save(update_fields=['technology'])

                update.save(update_fields=['qid'])
                update.save(update_fields=['stdanswer'])


                messages.success(request, f'Updated Successfully  !')

            # print(request.POST.get("stdans"))
            # print(request.POST.get("qid"))

    c = request.GET.get('page', 1)
    jobset=Questions.objects.filter(level=level,technology=technology)

    paginator = Paginator(jobset, 1)

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
    'level':level,
    'technology':technology,

    }

    return render(request, 'exam/studentviewjavaquestion.html',context)
