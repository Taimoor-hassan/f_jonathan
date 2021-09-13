from django.db.models.aggregates import Count
from django.shortcuts import render
from .models import card

# Create your views here.
def home (request):
    crd=card.objects.all()
    quicklink=card.objects.values('choseprogress').annotate(dcount=Count('choseprogress'))
    todo=card.objects.filter(choseprogress='todo')
    # pending=card.objects.all().annotate(progress=card.choseprogress.Count('Pending'))
    # done=card.objects.all().annotate(progress=card.choseprogress.Count('Done'))

    data={
        'crd': crd,
        'quicklink': quicklink,
        'todo': todo,
        # 'pending': pending,
        # 'done': done,
    }

    return render(request,'index.html',data)