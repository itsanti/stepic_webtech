from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.models import Question
from django.views.decorators.http import require_GET, require_POST
from django.core.paginator import Paginator, EmptyPage
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

@require_GET
def main_list(request, *args, **kwargs):
  questions = Question.objects.all().order_by('-added_at')
  try:
    page = int(request.GET.get('page', 1))
  except ValueError:
    raise Http404
  limit = request.GET.get('limit', 10)
  paginator = Paginator(questions, limit)
  paginator.baseurl = '/?page='
  try:
    page = paginator.page(page)
  except EmptyPage:
    page = paginator.page(paginator.num_pages)
  return render(request, 'main_list.html', {
    'questions': page.object_list,
    'paginator': paginator,
    'page': page,
  })

@require_GET
def popular_list(request, *args, **kwargs):
  questions = Question.objects.all().order_by('-rating')
  try:
    page = int(request.GET.get('page', 1))
  except ValueError:
    raise Http404
  limit = request.GET.get('limit', 10)
  paginator = Paginator(questions, limit)
  paginator.baseurl = '/popular/?page='
  try:
    page = paginator.page(page)
  except EmptyPage:
    page = paginator.page(paginator.num_pages)
  return render(request, 'popular_list.html', {
    'questions': page.object_list,
    'paginator': paginator,
    'page': page,
    'path': request.path,
  }) 
 
def question_details(request, id):
  if request.method == "POST":
    return render('OK')
  try:
    # question = get_object_or_404(Question, id=id)
    question = Question.objects.get(id=id)
  except Question.DoesNotExist:
    raise Http404
  return render(request, 'question.html', {
    'question': question,
    'form': AnswerForm(),
  })
  
def ask_form(request):
  if request.method == "POST":
    form = AskForm(request.POST)
    form._user = request.user
    if form.is_valid():
      question = form.save()
      return HttpResponseRedirect(question.get_url())
  else:
    form = AskForm()
  return render(request, 'askform.html', {
    'form': form,
    'path': request.path,
  }) 

@require_POST
def post_answer(request):
  form = AnswerForm(request.POST)
  form._user = request.user
  if form.is_valid():
    answer = form.save()
    return HttpResponseRedirect(answer.question.get_url())

def signup_form(request):
  if request.method == "POST":
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      user = authenticate(username=user.username, password=user.password)
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/')
  else:
    form = SignupForm()
  return render(request, 'signupform.html', {
    'form': form,
    'path': request.path,
  })
  
def login_form(request):
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      user = form.save()
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/')
  else:
    form = LoginForm()
  return render(request, 'loginform.html', {
    'form': form,
    'path': request.path,
  })