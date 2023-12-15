from django.shortcuts import render, redirect
from .models import News
from django.db.models import Q
from .forms import NewsForm
from django.urls import reverse
# Create your views here.

# Bosh sahifa uchun views
def home(request):
    query = request.GET.get("q", "")
    if query:
        news = News.objects.filter(Q(title__icontains=query) | Q(subtitle__icontains=query) | Q(body__icontains=query))
    else:
        news = News.objects.all().order_by("-created_at")
    context = {
        "news": news,
        "q": query
    }
    return render(request, "pages/home.html", context)

# har bir yangilik uchun view
def detail_page(request, slug):
    try:
        news = News.objects.get(slug=slug)
        query = request.GET.get("news_id")
        if query:
            news_id = int(query)
            news = News.objects.get(id=news_id)
            news.delete()
            return redirect("home")
        return render(request, "pages/detail.html", {"news": news})
    except:
        return render(request, "pages/detail.html")
    
# yangilik yaratish uchun view
def create_news(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "pages/create.html", {"form": form})
    else:
        return render(request, "pages/create.html", {"form": form})

# ma'lumotlarni o'zgartirish uchun view
def change_news(request, id):
    news = News.objects.get(id=id)
    if request.method == 'POST':
        form = NewsForm(instance=news, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("detail", slug=news.slug)
        else:
            return render(request, "pages/edit.html", {"form": form})
    else:
        form = NewsForm(instance=news)
        return render(request, "pages/edit.html", {"form": form})