from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at questions {0}." .format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {0}." .format(question_id)
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question {0}" .format(question_id))
