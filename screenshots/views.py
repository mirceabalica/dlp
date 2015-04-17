from .models import Screenshot
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    screenshots_list = Screenshot.objects.all()
    paginator = Paginator(screenshots_list, 2)
    page = request.GET.get('page')
    try:
        screenshots = paginator.page(page)
    except PageNotAnInteger:
        screenshots = paginator.page(1)
    except EmptyPage:
        screenshots = paginator.page(paginator.num_pages)

    context = {'on_page_screenshots': screenshots,}
    return render(request, 'screenshots/index.html', context)


def get_id(current, other):
    if other is not None:
        return other.id, 'enabled'
    else:
        return current.id, 'disabled'


def detail(request, domain_id):
    domain = get_object_or_404(Screenshot, pk=domain_id)
    next_domain = Screenshot.objects.all().filter(id__gt=domain.id).order_by(
        'id').first()
    previous_domain = Screenshot.objects.all().filter(
        id__lt=domain.id).order_by(
        'id').last()
    return render(request, 'screenshots/detail.html',
                  {'domain_item': domain,
                   'next_domain_id': get_id(domain, next_domain),
                   'previous_domain_id': get_id(domain, previous_domain)})