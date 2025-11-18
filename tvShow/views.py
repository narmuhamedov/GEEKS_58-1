from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator

from django.views import generic

#ListView
class FilmListView(generic.ListView):
    template_name = 'tvShow/films.html'
    model = models.Film
    context_object_name = 'film'
    ordering = ['-id']
    

#DetailView
class FilmDetailView(generic.DetailView):
    template_name = 'tvShow/film_detail.html'
    model = models.Film
    pk_url_kwarg = 'id'
    context_object_name = 'film_id'



#SEACRVIEW
class SearchView(generic.View):
    def get(self, request):
        query = request.GET.get('s', '')
        if query:
            film = models.Film.objects.filter(title__icontains=query)
        else:
            film = models.Film.objects.none
        context = {
            'film': film,
            's': query
        }
        return render(request, template_name='tvShow/films.html', context=context)


    





#search
# def searchView(request):
#     query = request.GET.get('s', '')
#     film = models.Film.objects.filter(title__icontains=query) if query else models.Film.none
#     context = {
#         'film': film,
#         's': query
#     }
#     return render(request, template_name='tvShow/films.html', context=context)



#detailView
def filmDetailView(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.Film, id=id)
        context = {
            'film_id': film_id
        }
    return render(request, template_name='tvShow/film_detail.html',
                  context=context)






#listView

def filmListView(request):
    if request.method == 'GET':
        film = models.Film.objects.all()
        paginator = Paginator(film, 2)
        page = request.GET.get("page")
        page_obj = paginator.get_page(page)        
        return render (request, 'tvShow/films.html', {"film": page_obj})



# def filmListView(request):
#     if request.method == 'GET':
#         # qwery запрос
#         film = models.Film.objects.all()
#         # контекстный ключ
#         context = {
#             "film": film,
#         }
#     return render(request, template_name='tvShow/films.html',
#                   context=context)