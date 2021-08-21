from django.shortcuts import render

# Create your views here.


def posts(request):
    return render(request, "posts/allPosts.html")


def post_details(request):
    pass