from django.shortcuts import render, get_object_or_404
from . import models


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
        return render (request, 'tvShow/films.html', {"film": film})



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