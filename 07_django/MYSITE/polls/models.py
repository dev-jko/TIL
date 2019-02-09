from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.id} {self.question_text}'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(day=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} {self.choice_text} {self.question}'


"""

Choice.objects.create(choice_text='text1', question_id=1)

c = Choice()
c.choice_text = 'choice'
c.question = q
c.save()

q = Question(question_text='text')
q.choice_set.create(choice_text='text2')

c.question
q.choice_set
q.choice_set.all()
q.choice_set.count()


"""









