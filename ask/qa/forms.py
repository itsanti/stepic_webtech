from django import forms
from qa.models import Question, Answer
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class AskForm(forms.Form):
  ''' add question '''
  title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
  
  # def clean(self):
    # '''
      # if is_spam(self.clean_data):
        # raise forms.ValidationError(
          # 'spam detected!!',
          # code='spam'
        # )
    # '''
    # pass
  
  def clean_title(self):
    title = self.cleaned_data['title']
    return title
  
  def clean_text(self):
    text = self.cleaned_data['text']
    return text
    
  def save(self):
    data = {
      'title': self.cleaned_data['title'],
      'text': self.cleaned_data['text'],
      'added_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      'rating': 0,
      'author_id': self._user.id,
    }
    question = Question(**data)
    question.save()
    return question
    

class AnswerForm(forms.Form):
  ''' add answer '''
  text = forms.CharField(label='New answer', widget=forms.Textarea(attrs={'class':'form-control'}))
  question = forms.IntegerField()

  def clean_text(self):
    text = self.cleaned_data['text']
    return text
  
  def clean_question(self):
    question = self.cleaned_data['question']
    return question
  
  def save(self):
    data = {
      'text': self.cleaned_data['text'],
      'added_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      'question_id': int(self.cleaned_data['question']),
      'author_id': self._user.id,
    }
    answer = Answer(**data)
    answer.save()
    return answer 

class SignupForm(forms.Form):
  username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class':'form-control'}))
  email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
  password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  
  def clean_password(self):
    password = self.cleaned_data['password']
    return password  
  
  def save(self):
    username = self.cleaned_data['username']
    email = self.cleaned_data['email']
    password = self.cleaned_data['password']
    user = User.objects.create_user(username, email, password)
    return user 
    
class LoginForm(forms.Form):
  username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class':'form-control'}))
  password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  
  def save(self):
    username = self.cleaned_data['username']
    password = self.cleaned_data['password']
    user = authenticate(username=username, password=password)
    return user 