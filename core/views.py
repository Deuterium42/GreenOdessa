from django.shortcuts import render


def promo(request):
    # noinspection PyUnresolvedReferences
    return render(request, 'core_templates/promo.html')


def services(request):
    return render(request, 'core_templates/services.html')


def gallery(request):
    return render(request, 'core_templates/gallery.html')


def reviews(request):
    return render(request, 'core_templates/reviews.html')

