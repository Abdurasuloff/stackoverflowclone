from django.shortcuts import render, redirect  
from .models import Question, Category
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from answers.models import Answer, Reply
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

# Create your views here.

def home(request):

      category = Category.objects.all()
      if 'q' in request.GET:
            q = request.GET['q']
            questions = Question.objects.filter(title__icontains=q).order_by("-date")
      else:
            try:
                  pro = request.user.pro.id
                  cat = Question.objects.all()
                  questions = Question.objects.filter(category_id=pro).order_by("-date")
            except:
                  questions = Question.objects.all().order_by("-date")

      return render(request, 'home.html', {"object_list": questions, 'category':category})     

@login_required
def askquestion(request):
      user = request.user
      
      if  request.method == "POST":
            author = user
            body = request.POST['body']
            category_id = request.POST['category']
            title = request.POST['title']
           
            Question.objects.create(
           
                body = body,
                title = title,
                author = author ,
                slug = title.replace(" ", "-") ,
                category= Category.objects.get(id=category_id)
                
                )
            redirect('home')
                
     
      return render(request, 'askquestion.html', )          

def detail(request, slug,  id ):
      questions = Question.objects.filter(slug=slug)
      question = questions.get(id=id)
      related_questions = Question.objects.filter(category = question.category)
      hit_count = get_hitcount_model().objects.get_for_object(question)
      hits = hit_count.hits
      hit_count_response = HitCountMixin.hit_count(request, hit_count)
      if hit_count_response.hit_counted:
            hits =+  1
       
      if  request.method == "POST":
            if request.POST.get("body"):
                author = request.user
                body = request.POST['body']
                Answer.objects.create(
           
                body = body,
                question = question,
                author = author ,
                author_of_question = question.author,
                )
                answers = question.answers
                answers =+ answers + 1
                question.answers = answers
                question.save()


            elif request.POST.get("bodycomment") and request.POST.get("answer_id") :
                  author = request.user
                  bodycomment = request.POST['bodycomment']
                  answer_id = request.POST.get("answer_id")
                  answer=Answer.objects.get(id=answer_id)
                  

                  Reply.objects.create(
           
                  body = bodycomment,
                  author = author,
                  answer = answer,
                  author_of_answer = answer.author, 
                  )
                  replies = answer.replies
                  replies = replies + 1
                  answer.replies = replies
                  answer.save()
           
      
      answers=Answer.objects.filter(question=question).order_by('-likes') 
      comments = Reply.objects.filter(answer = answers).order_by("-date") 
      context = {
            "object":question, 
            "hits":hits,
            "answers": answers,   
            "comments" : comments,
            "related_questions":related_questions,
      }

      return render(request, "detail.html", context)


def category(request, slug):
      category = Category.objects.get(slug=slug)
      questions = Question.objects.filter(category=category).order_by('-date')
      context = {"category":category, "questions":questions }
      
      return render(request, 'category.html', context)

def get_category(request):
      category = Category.objects.all()
      
      return {'category': category}
