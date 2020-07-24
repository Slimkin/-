from collections import Counter

from django.shortcuts import render_to_response
from django.http import Http404

counter_show = Counter()
counter_click = Counter()


def index(request):
    from_landing = request.GET.get('from-landing')
    counter_click[from_landing] += 1
    
    return render_to_response('index.html')


def landing(request):
    ab_test_arg = request.GET.get('ata')
    counter_show[ab_test_arg] +=1
    
    if ab_test_arg == 'original':
        template = 'landing.html'
    elif ab_test_arg == 'test':
        template = 'landing_alternate.html'
    else:
        raise Http404

    return render_to_response(template)


def stats(request):
    try:
        tc = counter_click['test'] / counter_show['test']
    except ZeroDivisionError:
        tc = 0

    try:
        oc = counter_click['original'] / counter_show['original']
    except ZeroDivisionError:
        oc = 0

    return render_to_response('stats.html', context={
        'test_conversion': tc,
        'original_conversion': oc,
    })
