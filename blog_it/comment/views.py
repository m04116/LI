from django.shortcuts import render, get_object_or_404, redirect
from . models import Comment
from .forms import CommentForm
from django.utils import timezone


def authorization_page(request):
    if request.user.is_authenticated():
            return redirect('message_page')
    return render(request,
            'blog/authorization_page.html',
            {'message_page': message_page})


def message_page(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
        form.published_date = timezone.now()
        form.save()
        return redirect('message_page')
    context = {'nodes':Comment.objects.all(), 'form': form}
    return render (request, 'blog/message_page.html', context)


def add_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.parent = comment = get_object_or_404(Comment, pk=pk)
            form.post = comment
            form.published_date = timezone.now()
            form.save()
            return redirect ('message_page')
    else:
        form = CommentForm()
    context ={'comment': comment, 'form': form}
    return render (request, 'blog/add_comment.html', context)


def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
#            form.published_date = timezone.now()  # If change pub. date nessesary
            form.save()
            return redirect('message_page')
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'blog/edit.html', context)


def del_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('message_page')
