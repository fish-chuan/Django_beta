from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import Item, Applying, Record
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    data = Item.objects.all()
    return render(request, 'index.html', {'items':data})

def apply(request):
    data = Applying.objects.all()
    return render(request, 'apply.html', {'items':data})

def send_apply(request):
    if request.method == 'POST':
        apply_user = request.POST['apply_user']
        item_name = request.POST['item_name']
        item_id = request.POST['item_id']

        check = Applying.objects.filter(item_id=item_id)
        if len(check):
            messages.info(request, "此項目已被申請！")
        else:
            app = Applying.objects.create(apply_user=apply_user, item_name=item_name, item_id=item_id)
            app.save()
            print("app save")
            itemm = Item.objects.get(item_id=item_id)
            itemm.is_apply = True
            itemm.status = 'C'
            itemm.save()
            print("item change")
        return redirect('/')
    else:
        return render(request, 'index.html')

def manage(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        result = request.POST['check']
        if result == '核准':
            itemm = Item.objects.get(item_id=item_id)
            item = Applying.objects.get(item_id=item_id)
            re = Record.objects.create(item_id=item_id, item_name=item.item_name, apply_user=item.apply_user)
            re.save()
            item.is_lent = True
            item.save()
            itemm.status = 'P'
            itemm.save()
        else:
            itemm = Item.objects.get(item_id=item_id)
            item_delete = Applying.objects.get(id=col_id)
            item_delete.delete()
            itemm.status = 'A'
            itemm.is_apply = False
            itemm.save()
        return redirect('apply')

    else:
        return render(request, 'apply.html')

def back(request):
    if request.method == 'POST':
        get_id = request.POST['item_id']
        re_check = Applying.objects.get(item_id=get_id)
        re = Record.objects.get(item_id=get_id)
        re.item_status = True
        re.save()
        itemm = Item.objects.get(item_id=get_id)
        re_check.delete()
        itemm.status = 'A'
        itemm.is_apply = False
        itemm.save()
        return redirect('back')
    else:
        data = Applying.objects.all()
        return render(request, 'back.html', {'items':data})

def record(request):
    data = Record.objects.all()
    return render(request, 'record.html', {'items': data})