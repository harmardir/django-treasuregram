from django.shortcuts import render


def index(request):
    return render(request , 'index.html',{'treasures': treasures})


class Treasure:
    def __init__(self, name, value , material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self .location = location
        self.img_url = img_url

treasures = [
    Treasure("Gold Nugget", 500.00, "gold", "Cutly's Creek, NM"),
    Treasure("Fool's Gold", 0, "pyrite", "Fools Falls, CO"),
    Treasure("Coffee Can", 20.00, "tin", "Acme, CA ")
]
