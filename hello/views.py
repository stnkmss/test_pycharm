from django.shortcuts import render
from django.http import HttpResponse  # クライアントへ返す内容を管理
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm


def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)


def create(request):
    if request.method == 'POST':
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    return render(request, 'hello/create.html', params)


"""
    if request.method == 'POST':
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
"""

"""
class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'your data: ',
            'form': HelloForm()
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        msg = 'あなたは、<b>' + request.POST['name'] + \
            ' (' + request.POST['age'] + \
            ') </b>さんです。<br>メールアドレスは <b>' + request.POST['mail'] + \
            '</b> ですね。'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
"""

"""
def index(request):
    params = {
        'title': 'Hello',
        'message': 'your data:',
        'form': HelloForm()
    }
    if request.method == 'POST':
        params['message'] = '名前：' + request.POST['name'] + \
                            '<br>メール：' + request.POST['mail'] + \
                            '<br>年齢：' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html', params)


def form(request):
    msg = request.POST['msg']
    params = {
        'title': 'Hello/Form',
        'msg': 'こんにちは、' + msg + 'さん。',
    }
    return render(request, 'hello/index.html', params)
"""

"""
def index(request):
    params = {
        'title': 'Hello/Index',
        'msg': 'これは、サンプルで作ったページです。',
        'goto': 'next',
    }
    return render(request, 'hello/index.html', params)
"""

"""
def next(request):
    params = {
        'title': 'Hello/Next',
        'msg': 'これは、もう一つのページです。',
        'goto': 'index',
    }
    return render(request, 'hello/index.html', params)
"""

"""
def index(request, id, nickname):
    result = 'your id: ' + str(id) + ', name: "' + nickname + '".'
    return HttpResponse(result)
"""

"""
    if 'msg' in request.GET:
        # msg = request.GET['msg']  # paramaterを取得
        result = 'your id: ' + str(id) + ', name: "' + nickname + '".'
    else:
        result = 'please send msg paramater!'
    return HttpResponse(result)
"""
