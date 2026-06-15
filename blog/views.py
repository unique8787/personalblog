from django.shortcuts import HttpResponse, render

def bloghome(request):
    return render(request, 'blog/blogHome.html')
    #return HttpResponse("Hello Welcome to this bloghome.we will keep all the blog")

def blogpost(request, slug):
    return render(request, 'blog/blogPost.html')
   # return HttpResponse(f'This is blogpost:{slug}')

