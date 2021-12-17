from django.db.models.query import QuerySet
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseBadRequest
from django.db.models.query import QuerySet
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .forms import SearchForm
from .models import BookModel


def QueryView(request:request.HttpRequest)->HttpResponse:
    form = SearchForm

    if ("keyward" in request.GET):
        form = form(request.GET)
        if form.is_valid():
            keyward = form.cleaned_data.get("keyward")
            # matched_results:QuerySet = BookModel.objects.filter(title__icontains=keyward).explain(analyze=True) # provides info about the query exec time
            
            # searchvector allows us to search multiple fields
            # matched_results:QuerySet = BookModel.objects.annotate(search=SearchVector('title', 'authors')).filter(search=keyward)

            """
            SEARCH RANK
            vector = SearchVector("title")
            query = SearchQuery(keyward)
            matched_results = BookModel.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")
            """

            """
            WEIGHTING

            # A=1, B=0.4 C=0.2 D=0.1
            """
            vector = SearchVector("title", weight="B") + SearchVector("authors", weight="A")
            query = SearchQuery(keyward)
            matched_results = BookModel.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")
            # print(vector, query)
            
            return render(request, "index.html", {"results": matched_results})

        return HttpResponseBadRequest()

    return render(request, "index.html", {'form':form})