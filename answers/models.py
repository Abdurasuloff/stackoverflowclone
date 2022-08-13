from django.db import models
from users.models import User
from questions.models import Question
from django.db.models.signals import post_save, post_delete
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Answer(models.Model):
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
      author_of_question = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='author_of_question')
      body = RichTextUploadingField()
      date_answered = models.DateTimeField(auto_now_add=True)
      likes = models.IntegerField(default=0)
      replies = models.IntegerField(default=0)
      is_seen = models.BooleanField(default=False)

      def __str__(self):
		      return str(self.body)

    
     
    

class Reply(models.Model):
      answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='replys'  )  
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      author_of_answer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='answer_owner') 
      body = models.TextField()
      date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
      is_seen = models.BooleanField(default=False)

      def __str__(self):
		      return str(self.body)


class Likes(models.Model):
      author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
      answer = models.ForeignKey(Answer  , on_delete=models.CASCADE, related_name='post_like')  
      author_of_answer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='authoranswer')
      date = models.DateTimeField(auto_now_add=True)   
      is_seen = models.BooleanField(default=False)

      def __str__(self):
		      return str(self.answer)

      

