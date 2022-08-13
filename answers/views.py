from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from questions.models import Question




@login_required
def like(request, answer_id):
	user = request.user
	answer = Answer.objects.get(id=answer_id)
	current_likes = answer.likes
	liked = Likes.objects.filter(author=user, answer=answer).count()
	author_of_answer = answer.author
      

	if not liked:
		like = Likes.objects.create(author=user, answer=answer, author_of_answer=author_of_answer)
		#like.save()
		current_likes = current_likes + 1
            

	else:
		Likes.objects.filter(author=user, answer=answer).delete()
		current_likes = current_likes - 1

	answer.likes = current_likes
	answer.save()

      
      

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def nots_like(request):
	author = request.user
	answer = Answer.objects.filter(author=author)
	likes  =  Likes.objects.filter(answer__in = answer).order_by('-date')
	Likes.objects.filter(answer__in = answer, is_seen=False).update(is_seen=True)
	
      
	context = {
		'likes': likes,
		'answer':answer
	}

	return render(request, 'like_nots.html', context)

@login_required
def nots_reply(request):
	author = request.user
	answer = Answer.objects.filter(author=author)
	replies  =  Reply.objects.filter(answer__in = answer).order_by('-date')
	Reply.objects.filter(answer__in = answer, is_seen=False).update(is_seen=True)

	context = {
		'replies': replies,
		'answer':answer
	}

	return render(request, 'reply_nots.html', context)

@login_required
def nots_answer(request):
	author = request.user
	question = Question.objects.filter(author=author)
	answers  = Answer.objects.filter(question__in = question).order_by('-date_answered')
	Answer.objects.filter(question__in = question, is_seen=False).update(is_seen=True)

	context = {
		
		'answers':answers
	}

	return render(request, 'answer_nots.html', context)	


def countanswernotifications(request):
	notifications = 0
	if request.user.is_authenticated:
		notifications = Answer.objects.filter(author_of_question=request.user, is_seen=False).count()

	return  {'notifications':notifications}


def countreplynotifications(request):
	notifications = 0
	if request.user.is_authenticated:
		notifications = Reply.objects.filter(author_of_answer=request.user, is_seen=False).count()

	return  {'replynotifications':notifications}

	
def countlikenotifications(request):
	notifications = 0
	if request.user.is_authenticated:
		notifications = Likes.objects.filter(author_of_answer=request.user, is_seen=False).count()

	return  {'likenotifications':notifications}

