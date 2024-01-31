from django.http import Http404
from django.shortcuts import render

ice_cream_catalog = [
    {
        'id': 0,
        'title': 'Классический пломбир',
        'description': 'Настоящее мороженое, для истинных ценителей вкуса. '
                       'Если на столе появляется пломбир — это не надолго.',
    },
    {
        'id': 1,
        'title': 'Мороженое с кузнечиками',
        'description': 'В колумбийском стиле: мороженое '
                       'с добавлением настоящих карамелизованных кузнечиков.',
    },
    {
        'id': 2,
        'title': 'Мороженое со вкусом сыра чеддер',
        'description': 'Вкус настоящего сыра в вафельном стаканчике.',
    },
]

ICE_CREAM_ID = {item['id']: item for item in ice_cream_catalog}


def ice_cream_detail(request, pk):
    try:
        return render(request,
                      'ice_cream/ice_cream_detail.html',
                      {'ice_cream': ICE_CREAM_ID[pk],
                       })
    except KeyError:
        raise Http404("Page not found")


def ice_cream_list(request):
    return render(request,
                  'ice_cream/ice_cream_list.html',
                  {'ice_cream_list': ice_cream_catalog,
                   })
