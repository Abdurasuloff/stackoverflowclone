from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from questions.models import  Question
from answers.models import Answer, Reply
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileEditView(UpdateView):
    form_class = CustomUserChangeForm
    template_name = "edit-profile.html"
    def get_object(self):

        object = get_object_or_404(User, username=self.kwargs.get("username"))

        # only owner can view his page
        if self.request.user.username == object.username:
            return object
        else:
            # redirect to 404 page
            print("you are not the owner!!")


      
def profile(request, username):
    user = get_object_or_404(User, username=username)    
    questions = Question.objects.filter(author = user).order_by("-date")
    answers  = Answer.objects.filter(author=user).order_by("-date_answered")
    
    q = questions.count()
    a = answers.count()
    
    
    
    

    context = {'user': user,  "a":a, "q":q, 'answers':answers, 'questions':questions} 

    return render(request, 'profile.html', context)

def get_user(request):
    user = request.user

    return {'user':user}




    
    
