from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406426196',
        'name': 'Faiz Kusumadinata',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)