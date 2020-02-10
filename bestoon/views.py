from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import User, Income, Expense, Token

# Create your views here.
@csrf_exempt
def submit_expense(request):
    """submit an expense"""
    print(request.POST)

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']
    Expense.objects.create(user = this_user, amount = request.POST['amount'],
            text = request.POST['text'], date = date)
    return JsonResponse({
        'status' : 'ok',
    }, encoder=JSONEncoder)

@csrf_exempt
def submit_income(request):
    """submit an income"""
    print(request.POST)

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.Post['date']
    Income.objects.create(user = this_user, amount = request.POST['amount'],
                          text = request.POST['text'], date = date)
    return JsonResponse({
        'status' : 'ok',
    }, encoder=JSONEncoder)
