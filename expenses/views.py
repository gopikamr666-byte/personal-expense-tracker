
from decimal import Decimal, InvalidOperation
from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Expense


def expense_list(request):

    expenses = Expense.objects.all().order_by('-date', '-id')

    title = request.GET.get('title', '').strip()
    category = request.GET.get('category', '').strip()
    start_date = request.GET.get('from', '').strip()
    end_date = request.GET.get('to', '').strip()

    valid_categories = dict(Expense.CATEGORY_CHOICES)

    if title:
        expenses = expenses.filter(title__icontains=title)

    if category in valid_categories:
        expenses = expenses.filter(category=category)
    elif category:
        category = ''

    if start_date:
        try:
            date.fromisoformat(start_date)
            expenses = expenses.filter(date__gte=start_date)
        except ValueError:
            start_date = ''

    if end_date:
        try:
            date.fromisoformat(end_date)
            expenses = expenses.filter(date__lte=end_date)
        except ValueError:
            end_date = ''

    today = timezone.localdate()

    monthly_expenses = Expense.objects.filter(
        date__year=today.year,
        date__month=today.month
    )

    total_spent = monthly_expenses.aggregate(
        total=Sum('amount')
    )['total'] or Decimal('0.00')

    category_summary = list(
        monthly_expenses
        .values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

  
    category_chart_labels = [
        dict(Expense.CATEGORY_CHOICES)[item['category']]
        for item in category_summary
    ]

    category_chart_values = [
        float(item['total'])
        for item in category_summary
    ]

    category_chart_colors = []

    if category_chart_values:
        highest = max(category_chart_values)
        lowest = min(category_chart_values)

        for amount in category_chart_values:
            if amount == highest:
                category_chart_colors.append('#E05252')
            elif amount == lowest:
                category_chart_colors.append('#319B65')
            else:
                category_chart_colors.append('#D9A62E')

    context = {
        'expenses': expenses,
        'categories': Expense.CATEGORY_CHOICES,
        'total_spent': total_spent,
        'category_summary': category_summary,
        'today': today,
        'search_title': title,
        'selected_category': category,
        'start_date': start_date,
        'end_date': end_date,
        'category_chart_labels': category_chart_labels,
        'category_chart_values': category_chart_values,
        'category_chart_colors': category_chart_colors,
    }

    return render(request, 'expenses/index.html', context)


@require_POST
def add_expense(request):

    title = request.POST.get('title', '').strip()
    amount = request.POST.get('amount', '').strip()
    category = request.POST.get('category', '')
    expense_date = request.POST.get('date', '')
    note = request.POST.get('note', '').strip()

    try:
        if not title or len(title) > 100:
            raise ValueError()

        amount = Decimal(amount)

        if (
            not amount.is_finite()
            or amount <= 0
            or amount > Decimal('99999999.99')
        ):
            raise ValueError()

        if category not in dict(Expense.CATEGORY_CHOICES):
            raise ValueError()

        if expense_date:
            expense_date = date.fromisoformat(expense_date)
        else:
            expense_date = timezone.localdate()

        Expense.objects.create(
            title=title,
            amount=amount,
            category=category,
            date=expense_date,
            note=note
        )

        messages.success(request, 'Expense added successfully!')

    except (ValueError, InvalidOperation, TypeError):
        messages.error(request, 'Please enter valid expense details.')

    return redirect('expense_list')


@require_POST
def edit_expense(request, pk):

    expense = get_object_or_404(Expense, pk=pk)

    title = request.POST.get('title', '').strip()
    amount = request.POST.get('amount', '').strip()
    category = request.POST.get('category', '')
    expense_date = request.POST.get('date', '')
    note = request.POST.get('note', '').strip()

    try:
        if not title or len(title) > 100:
            raise ValueError()

        amount = Decimal(amount)

        if (
            not amount.is_finite()
            or amount <= 0
            or amount > Decimal('99999999.99')
        ):
            raise ValueError()

        if category not in dict(Expense.CATEGORY_CHOICES):
            raise ValueError()

        expense_date = date.fromisoformat(expense_date)

        expense.title = title
        expense.amount = amount
        expense.category = category
        expense.date = expense_date
        expense.note = note

        expense.save()

        messages.success(request, 'Expense updated successfully!')

    except (ValueError, InvalidOperation, TypeError):
        messages.error(request, 'Please enter valid expense details.')

    return redirect('expense_list')


@require_POST
def delete_expense(request, pk):

    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()

    messages.success(request, 'Expense deleted successfully!')

    return redirect('expense_list')
