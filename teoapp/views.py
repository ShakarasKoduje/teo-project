from django.shortcuts import render
from teoapp.models import PostData, PostAuthor, PostContent
# Create your views here.


def index(request):
    listaWpisow = PostData.objects.all()
    #mymodels = MyModel.objects.all().order_by('-id')[:4] #zwraca cztery ostatnie obiekty z bazy danych
    listaAutorow = PostAuthor.objects.all()
    caloscBlog = PostContent.objects.get(id=1)
    #print(f"To jest zawartość całego bloga {str(caloscBlog.content)[:50]}")
    return render(request, 'teoapp/index.html',  {'posts' : listaWpisow,
                                                  'authors' : listaAutorow,
                                                  'calosc':caloscBlog})
