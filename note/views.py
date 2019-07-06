from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from . import models
# Create your views here.

def check_session(func):
    def login_fun(request, *args, **kwargs):
        if hasattr(request, 'session') and 'userinfo' in request.session:
            return func(request, *args, **kwargs)
        else:
            return Http404
    return login_fun

@check_session
def showall(request):
    user_id = request.session['userinfo']['id']
    user = models.User.objects.get(id=user_id)
    notes = models.Note.objects.filter(author=user)
    return render(request, 'note/showall.html', locals())

@check_session
def new(request):
    user_id = request.session['userinfo']['id']
    user = models.User.objects.get(id=user_id)

    if request.method == 'GET':
        return render(request, 'note/addnote.html')
    elif request.method == 'POST':
        note = models.Note(author=user)
        note.title = request.POST.get('note_title', '')
        note.content = request.POST.get('note_content', '')
        note.save()
        return HttpResponseRedirect('/note/all')

@check_session
def delete(request, id):
    user_id = request.session['userinfo']['id']
    user = models.User.objects.get(id=user_id)

    try:
        anote = models.Note.objects.get(author=user, id=id)
        anote.delete()
        return HttpResponseRedirect('/note/all')
    except:
        return HttpResponse('删除失败')

@check_session
def modify(request, id):
    user_id = request.session['userinfo']['id']
    user = models.User.objects.get(id=user_id)

    try:
        note = models.Note.objects.get(author=user, id=id)
        print("modify: ", note.id)
        print("id: ", id)
        if request.method == 'GET':
            return render(request, 'note/modify.html', locals())
        elif request.method == 'POST':
            try:
                title = request.POST.get('note_title', '')
                content = request.POST.get('note_content', '')
                note.title = title
                note.content = content
                note.save()
                return HttpResponseRedirect('/note/all')
            except:
                return HttpResponse("1.修改失败")

    except Exception as e:
        print("error:", e)
        return HttpResponse('2.修改失败')
