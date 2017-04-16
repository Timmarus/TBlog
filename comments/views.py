from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CommentForm


def comment_box(request):
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = CommentForm()

    return render(request, 'commentbox.html', {'form': form})