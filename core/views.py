from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Comment


def reviews(request):
    template_name = 'reviews.html'
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {
        'new_comment': new_comment,
        'comment_form': comment_form})


def promo(request):
    # noinspection PyUnresolvedReferences
    return render(request, 'core_templates/promo.html')


def services(request):
    return render(request, 'core_templates/services.html')


def gallery(request):
    return render(request, 'core_templates/gallery.html')


def lawns(request):
    return render(request, 'core_templates/lawns.html')


def garden_design(request):
    return render(request, 'core_templates/garden-design.html')


def auto_watering(request):
    return render(request, 'core_templates/auto_watering.html')


def trimming(request):
    return render(request, 'core_templates/trimming.html')


def work_system(request):
    return render(request, 'core_templates/work_system.html')
