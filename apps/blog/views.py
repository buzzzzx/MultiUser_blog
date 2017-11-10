from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from taggit.models import Tag

from .models import Post
from .forms import PostWriteForm
from operation.models import PostComment
from operation.forms import CommentForm
from utils.randstr import generate_code


# Create your views here.

def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    # paginate
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts': posts, 'page': page, 'section': 'post', 'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, uu_id=post, status='published',
                             publish__year=year, publish__month=month, publish__day=day)
    # List of active comments
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # a new comment was posted

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()

    comment_form = CommentForm()

    return render(request, 'blog/post/detail.html',
                  {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


@login_required
def post_write(request):
    form = PostWriteForm()

    if request.method == "POST":
        form = PostWriteForm(request.POST)
        if form.is_valid():
            post = Post()
            cd = form.cleaned_data
            title = cd['title']
            body = cd['body']
            author = request.user
            post.title = title
            post.body = body
            post.author = author
            post.uu_id = generate_code()
            post.save()

            return render(request, 'blog/post/detail.html', {'post': post})
        else:
            return render(request, 'blog/post/post_write.html', {'form': form})

    return render(request, 'blog/post/post_write.html', {'form': form})
