from django.shortcuts import render


def home(request):
    return render(request, 'magazine/home.html')


def trends(request):
    context = {
        'headline': 'Leather in Summer? Yes, Please!',
        'para1': 'Fashion houses are breaking rules: lightweight leather skirts and cropped jackets are taking over street style.',
        'para2': 'Pair them with sneakers for day or strappy sandals for night. Flamboyant loves rebels who bend the season.',
    }
    return render(request, 'magazine/section.html', context)


def celebrity_style(request):
    context = {
        'headline': 'Zendaya Does It Again',
        'para1': 'At Paris Fashion Week, Zendaya stepped out in a sharp power suit with metallic detailing.',
        'para2': 'Minimal jewelry, bold eyeliner, max confidence. The internet is still buzzing — and so are we.',
    }
    return render(request, 'magazine/section.html', context)


def street_style(request):
    context = {
        'headline': 'Sneakers Meet Sequins',
        'para1': 'Forget saving sequins for night — they’re hitting the sidewalks.',
        'para2': 'Think chunky sneakers, oversized denim jackets, and a glittery skirt. Comfort + drama = the new casual.',
    }
    return render(request, 'magazine/section.html', context)


def beauty(request):
    context = {
        'headline': 'Gloss Is Back',
        'para1': 'Matte lips had their moment, but gloss is staging a shiny return.',
        'para2': 'Paired with natural brows and dewy skin, it’s the ultimate fresh look. Flamboyant tip: clear gloss works over any lipstick.',
    }
    return render(request, 'magazine/section.html', context)


def picks(request):
    context = {
        'headline': '3 Must-Haves This Month',
        'picks': ['Neon mini bag', 'Oversized sunglasses', 'Chunky silver hoops'],
    }
    return render(request, 'magazine/picks.html', context)

# Create your views here.
