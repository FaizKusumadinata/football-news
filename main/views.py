from django.shortcuts import render, redirect, get_object_or_404
from main.forms import NewsForm
from main.models import News
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406426196',
        'name': 'Faiz Kusumadinata',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)

def create_news(request):
    form = NewsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_news.html", context)

def show_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.increment_views()

    context = {
        'news': news,
        'news.title':'How can Martinelli find his form for Arsenal to silence critics?',
        'news.thumbnail': 'https://ichef.bbci.co.uk/ace/standard/800/cpsprodpb/ccd5/live/163a03f0-8da0-11f0-bcbf-f3fb3e8bb0a7.jpg.webp',
        'news.content': 'Arsenal return to Premier League action this weekend with the visit of Ange Postecoglous Nottingham Forest - their first league game since the defeat by Liverpool at Anfield before the international break.'
    }

    return render(request, "news_detail.html", context)

def show_xml(request):
     news_list = News.objects.all()
     xml_data = serializers.serialize("xml", news_list)
     return HttpResponse(xml_data, content_type="application/xml")
 
def show_json(request):
    news_list = News.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, news_id):
   try:
       news_item = News.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", news_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except News.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, news_id):
   try:
       news_item = News.objects.get(pk=news_id)
       json_data = serializers.serialize("json", [news_item])
       return HttpResponse(json_data, content_type="application/json")
   except News.DoesNotExist:
       return HttpResponse(status=404)