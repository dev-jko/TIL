from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# Create your views here.


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:3]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(
            id=request.POST.get('choice'))
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:question_results', args=(question.id, )))
    except (KeyError, Choice.DoesNotExist):
        context = {'question': question, 'error_message': 'Pick right choice'}
        return render(request, 'polls/detail.html', context)
    return redirect(resolve_url('polls:question_detail', question_id=question.id))
