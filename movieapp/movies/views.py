from django.shortcuts import render
from .models import Category,Movie

kategori_list = ['macera', 'romantik', 'dram',"bilim kurgu"]
film_list = [
    {
        "id":1,
        "film_adi":"film1",
        "aciklama":"film1 aciklama",
        "image" : "1.jpeg",
        "anasayfa": True
    },
    {
        "id":2,
        "film_adi":"film2",
        "aciklama":"film2 aciklama",
        "image" : "2.jpeg",
        "anasayfa": True
    },
    {
        "id":3,
        "film_adi":"film3",
        "aciklama":"film3 aciklama",
        "image" : "3.jpeg",
        "anasayfa": False
    },
    {
        "id":4,
        "film_adi":"film4",
        "aciklama":"film4 aciklama",
        "image" : "4.jpeg",
        "anasayfa": False
    },
]

def  home(request):
    data = {
        # "kategoriler":kategori_list,
        "kategoriler":Category.objects.all(),
        # "filmler": film_list,
        "filmler": Movie.objects.filter(anasayfa=True)
    }
    return render(request, "index.html", data)


def  movies(request):
    data = {
        #  "kategoriler":kategori_list,
        "kategoriler":Category.objects.all(),
        # "filmler": film_list,
        "filmler": Movie.objects.all()
    }
    return render(request, "movies.html", data)

def  moviedetails(request,id):
    data = {
        # "id": id,
        "movie": Movie.objects.get(id=id)
    }
    return render(request, "details.html", data)
