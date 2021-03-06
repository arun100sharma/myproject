from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import BlogForm
from .models import Blog

def add_blog(request):
	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			blog_item = form.save(commit=False)
			blog_item.save()
			return redirect('/blog/' + str(blog_item.id) + '/')
	else:
		form = BlogForm()
	return render(request, 'blog/blog_form.html', {'form' : form})

def edit_blog(request, id=None):
	item = get_object_or_404(Blog, id=id)
	form = BlogForm(request.POST or None, instance=item)
	if form.is_valid():
		form.save()
		return redirect('/blog/' + str(item.id) + '/')
	return render(request, 'blog/blog_form.html', {'form' : form})

def blog(request, id=None):
	blog = Blog.objects.get(id=id)
	return render(request, 'blog/blog.html', {'blog' : blog})