from django.shortcuts import render,redirect
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def my_expense(request):
    expenses = Expense.objects.all()
    total_amount = Expense.total_amount
    context = {'expenses': expenses,'total_amount':total_amount}

    return render(request, 'cost/expense.html', context)


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.save()
        return redirect('cost-list')
        #return redirect('cost-list/')

    else:
        form = ExpenseForm
    return render(request, 'cost/add_expense.html', {'form': form})
