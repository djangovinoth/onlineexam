from django.shortcuts import render,redirect
from blog.models import Questions,Answers
from blog.forms import QuestionsForm
# Create your views here.
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.utils import timezone
import time

def addquestions(request):
    jobset=Questions.objects.filter(user=request.user)

    if request.method == 'POST':

        job_form = QuestionsForm(request.POST)
        if job_form.is_valid():
            totallevel=Questions.objects.filter(user=request.user,level=job_form.cleaned_data["level"],technology = job_form.cleaned_data["technology"]).count()
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


def student_view_java_questions(request,level,technology,attemptcount,qid='NONE'):

    c = request.GET.get('page', 1)
    jobset=Questions.objects.filter(level=level,technology=technology)

    paginator = Paginator(jobset, 1)

    try:
        page = paginator.page(c)

    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)


    if request.method == 'POST':

        if request.POST.get("stdans") is None:
            messages.info(request, f'Please select any options!')
        else:

            add=Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid")).count()
            # print(Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid")))
            if add==0:
                if request.POST.get("status")=='completed':
                    completed=Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"))
                    for c in completed:
                        c.status='completed'
                        c.complted_at=datetime.datetime.now()
                        c.save()
                        c.save(update_fields=['status'])
                        c.save(update_fields=['complted_at'])
                    t=Answers(user=request.user,attemptid=attemptcount,due_at=datetime.datetime.now() + datetime.timedelta(hours=1),complted_at=datetime.datetime.now(),updated_at=datetime.datetime.now(),created_at=datetime.datetime.now(),level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"),stdanswer=request.POST.get("stdans"),status=request.POST.get("status"))
                    t.save()
                    messages.success(request, f'You have submitted your answers thanks for your time!')
                    # completed.status='completed'
                    # completed.save()
                    # completed.save(update_fields=['status'])


                else:
                    t=Answers(user=request.user,attemptid=attemptcount,updated_at=datetime.datetime.now(),created_at=datetime.datetime.now(),level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"),stdanswer=request.POST.get("stdans"),status=request.POST.get("status"))
                    t.save()

                    messages.success(request, f'added success fully !')





            else:
                update=Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"))[0]

                update.attemptid=attemptcount

                update.status=request.POST.get("status")
                update.level=request.POST.get("level")
                update.technology=request.POST.get("technology")
                update.qid=request.POST.get("qid")
                update.stdanswer=request.POST.get("stdans")
                update.updated_at=datetime.datetime.now()
                update.save()
                update.save(update_fields=['attemptid'])
                update.save(update_fields=['level'])
                update.save(update_fields=['technology'])
                update.save(update_fields=['qid'])
                update.save(update_fields=['stdanswer'])
                update.save(update_fields=['status'])

                update.save(update_fields=['updated_at'])

                messages.success(request, f'Updated Successfully  !')

            # print(request.POST.get("stdans"))
            # print(request.POST.get("qid"))




    # jobset=Questions.objects.filter(user=request.user,level=level)


    context={
    'jobset':jobset,
    'per':page,
    'level':level,
    'technology':technology,


    }

    return render(request, 'exam/studentviewjavaquestion.html',context)

def student_attempts(request, level,technology):
    totalqus=Questions.objects.filter(level=level,technology=technology).count()




    attempts=Answers.objects.filter(user=request.user,level=level,technology=technology).values('attemptid').order_by('-attemptid').distinct()
    dic=[]
    for a in attempts:
        totalans=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=a['attemptid']).count()
        ans=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=a['attemptid'])
        qus=Questions.objects.filter(level=level,technology=technology)

        crtcount=0
        for an in ans:
            crt=Questions.objects.filter(level=level,technology=technology,qid=an.qid)[0]
            if an.stdanswer==crt.correctanswer:
                crtcount=crtcount+1
            else:
                pass

        status=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=a['attemptid']).values('status').order_by('-status').distinct()
        created=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=a['attemptid']).values('created_at').distinct()
        updated=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=a['attemptid']).values('updated_at').distinct()
        completed=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=a['attemptid']).values('complted_at').distinct()

        s=status[len(status)-1]

        case={'status':s['status'],'attemptid':a['attemptid'],'created':created[0]['created_at'],
                'updated':updated[len(updated)-1]['updated_at'],'completed':completed[len(completed)-1]['complted_at'],
                'ratio':str(totalans)+'/'+str(totalqus),'score':round((totalans/totalqus)*100),'totalscore':round((crtcount/qus.count())*100)}
        dic.append(case)


    # print(dic)
    attemptcount=int(attempts.count())+1
    context={
    'technology':technology,
    'level':level,
    'attempts':attempts,
    'attemptcount':attemptcount,
    'dic':dic,
    }

    return render(request,'exam/attempts.html',context)





def student_view_java_questions0(request,level,technology,attemptcount,qid='NONE'):
    print(attemptcount,'....',qid)
    jobset=Questions.objects.filter(level=level,technology=technology)
    submit=False
    c = request.GET.get('page', 1)
    print(c,'....','your c is ')
    Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"))
    final=Answers.objects.filter(user=request.user,attemptid=attemptcount,level=level,technology=technology)
    compstatus=False
    for f in final:
        if f.status in 'completed':
            print('f.status',f.status)
            compstatus=True
    try:
        mode=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=attemptcount,qid=jobset[int(c)-int(1)].qid)[0]

        print('mode','.....>',mode)
        print('mode id','.....>',mode.qid)
    except:
        print('error')
        mode=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=attemptcount)


    paginator = Paginator(jobset, 1)

    try:
        page = paginator.page(c)

    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)


    if request.method == 'POST':

        if request.POST.get("stdans") is None:
            messages.info(request, f'Please select any options!')
        else:

            add=Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid")).count()

            # print(Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid")))
            if add==0:
                if request.POST.get("status")=='completed':
                    completed=Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"))
                    for c in completed:
                        c.status='completed'
                        c.complted_at=datetime.datetime.now()
                        c.save()
                        c.save(update_fields=['status'])
                        c.save(update_fields=['complted_at'])
                    t=Answers(user=request.user,attemptid=attemptcount,due_at=datetime.datetime.now() + datetime.timedelta(hours=1),complted_at=datetime.datetime.now(),updated_at=datetime.datetime.now(),created_at=datetime.datetime.now(),level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"),stdanswer=request.POST.get("stdans"),status=request.POST.get("status"))
                    t.save()

                    messages.success(request, f'You have submitted your answers thanks for your time!')
                    # mode=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=attemptcount,qid=jobset[int(c)-int(1)].qid)[0]


                    # completed.status='completed'
                    # completed.save()
                    # completed.save(update_fields=['status'])


                else:
                    t=Answers(user=request.user,attemptid=attemptcount,updated_at=datetime.datetime.now(),created_at=datetime.datetime.now(),level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"),stdanswer=request.POST.get("stdans"),status=request.POST.get("status"))
                    t.save()

                    messages.success(request, f'Your selected answer - "{request.POST.get("stdans")}" is added successfully, Click "Next Question" to continue or Select another option and save again to update !')
                    mode=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=attemptcount,qid=jobset[int(c)-int(1)].qid)[0]
                    submit=True





            else:
                update=Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"))[0]

                update.attemptid=attemptcount

                update.status=request.POST.get("status")
                update.level=request.POST.get("level")
                update.technology=request.POST.get("technology")
                update.qid=request.POST.get("qid")
                update.stdanswer=request.POST.get("stdans")
                update.updated_at=datetime.datetime.now()
                update.save()
                update.save(update_fields=['attemptid'])
                update.save(update_fields=['level'])
                update.save(update_fields=['technology'])
                update.save(update_fields=['qid'])
                update.save(update_fields=['stdanswer'])
                update.save(update_fields=['status'])

                update.save(update_fields=['updated_at'])

                messages.success(request, f'Updated Successfully  !')
                mode=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=attemptcount,qid=jobset[int(c)-int(1)].qid)[0]
                submit=True

            # print(request.POST.get("stdans"))
            # print(request.POST.get("qid"))




    # jobset=Questions.objects.filter(user=request.user,level=level)


    context={
    'jobset':jobset,
    'per':page,
    'level':level,
    'technology':technology,
    'submit':submit,
    'mode':mode,
    'compstatus':compstatus,


    }

    return render(request, 'exam/studentviewjavaquestion0.html',context)



    def student_view_java_questions00(request,level,technology,attemptcount,qid='NONE'):
        print(attemptcount,'....',qid)

        submit=False
        c = request.GET.get('page', 1)
        print(c,'....','your c is ')
        try:
            index=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=attemptcount).count()
            print('index','----',index)
            mode=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=attemptcount)[index]
            print(mode)
        except:
            mode=Answers.objects.filter(user=request.user,level=level,technology=technology,attemptid=attemptcount)

        jobset=Questions.objects.filter(level=level,technology=technology)
        print('jobset---',jobset[int(c)-int(1)].qid)

        print(jobset)
        paginator = Paginator(jobset, 1)


        try:
            page = paginator.page(c)

        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)


        if request.method == 'POST':

            if request.POST.get("stdans") is None:
                messages.info(request, f'Please select any options!')
            else:

                add=Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid")).count()

                # print(Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid")))
                if add==0:
                    if request.POST.get("status")=='completed':
                        completed=Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"))
                        for c in completed:
                            c.status='completed'
                            c.complted_at=datetime.datetime.now()
                            c.save()
                            c.save(update_fields=['status'])
                            c.save(update_fields=['complted_at'])
                        t=Answers(user=request.user,attemptid=attemptcount,due_at=datetime.datetime.now() + datetime.timedelta(hours=1),complted_at=datetime.datetime.now(),updated_at=datetime.datetime.now(),created_at=datetime.datetime.now(),level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"),stdanswer=request.POST.get("stdans"),status=request.POST.get("status"))
                        t.save()
                        messages.success(request, f'You have submitted your answers thanks for your time!')
                        # completed.status='completed'
                        # completed.save()
                        # completed.save(update_fields=['status'])


                    else:
                        t=Answers(user=request.user,attemptid=attemptcount,updated_at=datetime.datetime.now(),created_at=datetime.datetime.now(),level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"),stdanswer=request.POST.get("stdans"),status=request.POST.get("status"))
                        t.save()

                        messages.success(request, f'Your selected answer - "{request.POST.get("stdans")}" is added successfully, Click "Next Question" to continue or Select another option and save again to update !')
                        submit=True




                else:
                    update=Answers.objects.filter(user=request.user,attemptid=attemptcount,level=request.POST.get("level"),technology=request.POST.get("technology"),qid=request.POST.get("qid"))[0]

                    update.attemptid=attemptcount

                    update.status=request.POST.get("status")
                    update.level=request.POST.get("level")
                    update.technology=request.POST.get("technology")
                    update.qid=request.POST.get("qid")
                    update.stdanswer=request.POST.get("stdans")
                    update.updated_at=datetime.datetime.now()
                    update.save()
                    update.save(update_fields=['attemptid'])
                    update.save(update_fields=['level'])
                    update.save(update_fields=['technology'])
                    update.save(update_fields=['qid'])
                    update.save(update_fields=['stdanswer'])
                    update.save(update_fields=['status'])

                    update.save(update_fields=['updated_at'])

                    messages.success(request, f'Updated Successfully  !')
                    submit=True

                # print(request.POST.get("stdans"))
                # print(request.POST.get("qid"))




        # jobset=Questions.objects.filter(user=request.user,level=level)


        context={
        'jobset':jobset,
        'per':page,
        'level':level,
        'technology':technology,
        'submit':submit,
        'mode':mode,

        }

        return render(request, 'exam/studentviewjavaquestion0.html',context)
