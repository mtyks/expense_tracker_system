from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from django.db.models import Sum
from django.db.models import Q
from django.core.paginator import Paginator

# หน้าหลักแสดงข้อมูล
def home(request):
    transactions = Transaction.objects.all()

    # ดึงค่าจาก GET
    sort = request.GET.get('sort', '-amount')
    category = request.GET.get('category', 'all')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    # กรองตามประเภท
    if category in ['income', 'expense']:
        transactions = transactions.filter(category=category)

    # กรองตามช่วงวันที่
    if date_from:
        transactions = transactions.filter(date__gte=date_from)
    if date_to:
        transactions = transactions.filter(date__lte=date_to)

    # เรียงลำดับ
    transactions = transactions.order_by(sort)

    # สรุปยอดตามตัวกรอง
    total_income = transactions.filter(category='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(category='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    # << ทำ pagination หลังจากกรองแล้ว >>
    paginator = Paginator(transactions, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'transactions': page_obj,  
        'page_obj': page_obj,     
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'sort': sort,
        'category': category,
        'date_from': date_from,
        'date_to': date_to,
    }

    return render(request, 'home.html', context)
 
# เพิ่มข้อมูล
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

# แก้ไขข้อมูล
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'edit_transaction.html', {'form': form, 'transaction': transaction})

# ลบข้อมูล
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('home')

# ค้นหาข้อมูล
def search_transactions(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', 'all')
    sort = request.GET.get('sort', '-amount')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    transactions = Transaction.objects.filter(
        Q(name__icontains=query) | 
        Q(amount__icontains=query) |
        Q(description__icontains=query)
    )

    if category != "all":
        transactions = transactions.filter(category=category)

    if date_from:
        transactions = transactions.filter(date__gte=date_from)
    if date_to:
        transactions = transactions.filter(date__lte=date_to)

    transactions = transactions.order_by(sort)

    paginator = Paginator(transactions, 10)  # 10 รายการต่อหน้า
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'category': category,
        'sort': sort,
        'date_from': date_from,
        'date_to': date_to,
    }
    return render(request, 'search_transactions.html', context)

def about_view(request):
    return render(request, 'about.html')
