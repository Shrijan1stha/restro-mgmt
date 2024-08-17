from django.shortcuts import render, redirect, get_object_or_404
from .models import Table, Menu, Category, Order, Waiter, Reception


# Create your views here.


def home(request):
    return render(request, 'base.html')

def table_list(request):
    table = Table.objects.all()
    data = {'table':table}
    return render(request, 'table/table.html', context=data)

def create_table(request):
    if request.method == 'POST':
        table = request.POST.get('table_no')
        capacity = request.POST.get('capacity')
        status = request.POST.get('status')
        Table.objects.create(table=table, capacity=capacity, status=status)
        return redirect('table')
    return render(request, 'table/create.html')

def edit_table(request, pk):
    edit_obj = Table.objects.get(id=pk)
    if request.method == 'POST':
        table = request.POST.get('table_no')
        capacity = request.POST.get('capacity')
        status = request.POST.get('status')
        
        edit_obj.table = table
        edit_obj.capacity = capacity
        edit_obj.status = status
        edit_obj.save()
        return redirect('table')
    data = {'edit': edit_obj}
    return render(request, 'table/edit.html', context=data)

def delete_table(request,pk):
    delete_obj = Table.objects.get(id=pk)
    delete_obj.delete()
    return redirect('table')

# Menu

def menu(request):
    menu = Menu.objects.all()
    catagori = Category.objects.all()
    cat = catagori.filter()
    data = {'menu_list':menu, 'cat':cat}
    return render(request,'menu/menu.html', context=data)

def create_menu(request):
    categories = Category.objects.all()
    context = {'cat_list': categories}

    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')

        # Validate form data
        if not item_name or not price or not category_id:
            context['error'] = 'All fields are required.'
            return render(request, 'menu/create.html', context)

        # Ensure the price is a valid number
        try:
            price = float(price)
        except ValueError:
            context['error'] = 'Price must be a number.'
            return render(request, 'menu/create.html', context)

        # Get the category instance
        category = get_object_or_404(Category, id=category_id)

        # Create the menu item
        Menu.objects.create(items=item_name, price=price, category=category)
        return redirect('menu')

    return render(request, 'menu/create.html', context=context)

def edit_menu(request,pk):
    edit_obj = Menu.objects.get(id=pk)
    categories = Category.objects.all()
    data = {'menu': edit_obj, 'cat_list': categories}
    if request.method == 'POST':
        category_name = request.POST.get('category')
        itemname = request.POST.get('item_name')
        price = request.POST.get('price')
        category_instance = get_object_or_404(Category, category=category_name)

        edit_obj.category = category_instance
        edit_obj.items = itemname
        edit_obj.price = price
        edit_obj.save()
        return redirect('menu')

    return render(request, 'menu/edit.html', context=data)

def delete_menu(request,pk):
    delete_obj = Menu.objects.get(id=pk)
    delete_obj.delete()
    return redirect('menu')



# Category

def category(request):
    category = Category.objects.all()
    data = {'categories':category}
    return render(request,'category/category_list.html',context=data)

def create_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category')
        Category.objects.create(category=category_name)
        return redirect('category')
    return render(request,'category/create.html')

def edit_category(request,pk):
    edit_obj = Category.objects.get(id=pk)
    if request.method == 'POST':
        categories = request.POST.get('category')

        edit_obj.category = categories
        edit_obj.save()
        return redirect('category')
    data = {'edit_cat':edit_obj}
    return render(request,'category/edit.html',context=data)

def delete_category(request,pk):
    del_cat = Category.objects.get(id=pk)
    del_cat.delete()
    return redirect('category')

# Order

def order(request):
    order = Order.objects.all()
    data = {'orders':order}
    return render(request,'order/order.html', context=data)

def create_order(request):
    tables = Table.objects.all()
    items = Menu.objects.all()
    data = {
        'tables':tables,
        'items':items,
        }

    if request.method == 'POST':
        table_no = request.POST.get('table_no')
        item_name = request.POST.get('items')
        quantity = request.POST.get('quantity')
        
        table_instance = get_object_or_404(Table, id=table_no)
        item_instance = get_object_or_404(Menu, id=item_name)

        Order.objects.create(table_no=table_instance, items=item_instance, quantity=quantity)
        return redirect('order_list')
    return render(request, 'order/create.html', context=data)

def edit_order(request, pk):
    edit_order = get_object_or_404(Order, pk=pk)
    tables = Table.objects.all()
    items = Menu.objects.all()
    data = {
        'edit_order': edit_order,
        'tables': tables,
        'items': items,
    }

    if request.method == 'POST':
        table_id = request.POST.get('table_no')
        item_id = request.POST.get('item_name')
        quantity = request.POST.get('quantity')

        table_instance = get_object_or_404(Table, id=table_id)
        item_instance = get_object_or_404(Menu, id=item_id)

        edit_order.table_no = table_instance
        edit_order.items = item_instance
        edit_order.quantity = quantity
        edit_order.save()
        return redirect('order_list')

    return render(request, 'order/edit.html', context=data)

def delete_order(request,pk):
    del_order = Order.objects.get(id=pk)
    del_order.delete()
    return render(request, 'order/order.html')


# Waiter

def waiter_list(request):
    waiter = Waiter.objects.all()
    data = {'waiters':waiter}
    return render(request, 'waiter/waiter_list.html',context=data)

def create_waiter(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        middlename = request.POST.get('middle_name')
        lastname = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        Waiter.objects.create(first_name=firstname,middle_name=middlename,last_name=lastname,gender=gender,address=address)
        return redirect('waiter_list')
    return render(request, 'waiter/create.html')

def edit_waiter(request,pk):
    waiter_obj = Waiter.objects.get(id=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        waiter_obj.first_name = first_name
        waiter_obj.middle_name = middle_name
        waiter_obj.last_name = last_name
        waiter_obj.gender = gender
        waiter_obj.address = address
        waiter_obj.save()
        return redirect('waiter_list')
    data = {'edit':waiter_obj}
    return render(request,'waiter/edit.html',context=data)

def delete_waiter(request,pk):
    del_waiter = Waiter.objects.get(id=pk)
    del_waiter.delete()
    return redirect('waiter_list')

# Reception

def reception_list(request):
    reception = Reception.objects.all()
    data = {'receptions':reception}
    return render(request,'reception/reception.html', context=data)

def create_reception(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        middlename = request.POST.get('middle_name')
        lastname = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        Reception.objects.create(first_name=firstname, middle_name=middlename, last_name=lastname, gender=gender, address=address,
                                 phone=phone)
        return redirect('reception_list')
    return render(request,'reception/create.html')

def edit_reception(request,pk):
    reception_obj = Reception.objects.get(id=pk)
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        middlename = request.POST.get('middle_name')
        lastname = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        reception_obj.first_name = firstname
        reception_obj.middle_name = middlename
        reception_obj.last_name = lastname
        reception_obj.gender = gender
        reception_obj.address = address
        reception_obj.phone = phone
        reception_obj.save()
        return redirect('reception_list')
    data = {'edit':reception_obj}
    return render(request,'reception/edit.html',context=data)

def delete_reception(request,pk):
    delete_rec = Reception.objects.get(id=pk)
    delete_rec.delete()
    return redirect('reception_list')