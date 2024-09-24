from django.shortcuts import render

# Create your views here.
import random
quotes = [
    "The struggle itself is enough to fill a man's heart.",
    "I can feel this heart inside me and I conclude it exists",
    "I'm filled with a desire for clarity and meaning within a world and condition that offers neither"
]

images = [
    "/static/images/albert_camus1.jpg.webp",
    "/static/images/albert_camus2.jpg",
    "/static/images/albert_camus3.jpg.webp"
]

def quote(request):
    selected_quote = random.choice(quotes)
    selected_image = random.choice(images)
    
    context = {
        'quote': random.choice(quotes),
        'image': random.choice(images)
    }

    return render(request, 'quotes/quote.html', context)

def show_all(request):
    context = {
        'quotes': quotes,
        'images': images
    }

    return render(request, 'quotes/show_all.html', context)

def about(request):
    return render(request, 'quotes/about.html')
