from django.shortcuts import render,redirect
from .models import Expense
from .forms import ExpenseForm
from django.http import HttpResponse

# Create your views here.
def my_expense(request):
    budget=0
    expenses = Expense.objects.all()
    total_amount =Expense.objects.raw('SELECT total_amount FROM cost_management_expense')
    return HttpResponse(total_amount)
    context = {'expenses': expenses,'total_budget':budget}

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

def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('cost-list')



