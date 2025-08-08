from models import Grupo
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def paginacao(request, grupos):

    paginacao = Paginator(grupos, 20)

    try:
        pagina = int(request.GET.get('pagina', '1'))
    except ValueError:
        pagina = 1

    try:
        grupos = paginacao.page(pagina)
    except (EmptyPage, InvalidPage):
        grupos = paginacao.page(paginacao.num_pages)

    return grupos
