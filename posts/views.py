from django.shortcuts import render, HttpResponse
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.template.html", {
        'posts':posts,
        'username': 'Friend'
    })
    
def create_post(request):
    if request.method == "POST":
        # recreate the form with the data from request.POST
        # request.POST contains what data the user has given
        form = PostForm(request.POST, request.FILES)
        form.save() # actually save the model
        return redirect(index)
    else:
        form = PostForm()
        return render(request, "post_form.template.html", {
            "form":form
        })
        
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = PostForm(instance=post)
        return render(request, "edit_post_form.template.html", {
            "form":form
        })
        
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect(index)
    
def about_us(request):
    return render(request, "profile.template.html")