from django.shortcuts import render
from main.models import Item
from main.models import Applying
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    data = Item.objects.all()
    return render(request, 'index.html', {'items':data})

def apply(request):
    if request.method == "POST":
        apply_user = request.POST['apply_user']
        item_id = request.POST['item_id']

        app = Applying.objects.create(apply_user=apply_user, item_num=item_id, is_pass=False)
        app.save()
        print("apply done")
        return ('/')
    else:
        return render(request, 'apply.html')