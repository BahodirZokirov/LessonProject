from django.shortcuts import render, redirect, get_object_or_404
from .models import Categories, News
from .forms import NewsForm
# Create your views here.


def categories(request):
    all_categories = Categories.objects.all()
    context = {
        "categories": all_categories
    }
    return render(request, 'category.html', context)


def categories_all(request):
    if 'search' in request.GET:
        all_news = News.objects.filter(news_title__icontains=request.GET['search']) | News.objects.filter(news_body__icontains=request.GET['search'])
    else:
        all_news = News.objects.all()
    context = {
        "news": all_news
    }
    return render(request, "category_all.html", context)


def category_all_detail(request, pk):
    certain_new = News.objects.get(id=pk)
    context = {
        "certain_new": certain_new
    }
    return render(request, 'category_all_detail.html', context)


def category_sport(request):
    if 'search' in request.GET:
        all_news = News.objects.filter(news_body__icontains=request.GET['search']) | News.objects.filter(news_title__icontains=request.GET['search'])
        # SELECT * FROM media WHERE news_title LIKE % keyword %
    else:
        all_news = News.objects.all()
    context = {
        "news": all_news
    }
    return render(request, 'sport/category_sport.html', context)


def category_politic(request):
    if 'search' in request.GET:
        all_news = News.objects.filter(news_body__icontains=request.GET['search']) | News.objects.filter(news_title__icontains=request.GET['search'])
        # SELECT * FROM media WHERE news_title LIKE % keyword %
    else:
        all_news = News.objects.all()
    context = {
        "news": all_news
    }
    return render(request, 'politic/category_politic.html', context)


def category_business(request):
    if 'search' in request.GET:
        all_news = News.objects.filter(news_body__icontains=request.GET['search']) | News.objects.filter(news_title__icontains=request.GET['search'])
        # SELECT * FROM media WHERE news_title LIKE % keyword %
    else:
        all_news = News.objects.all()
    context = {
        "news": all_news
    }
    return render(request, 'business/category_business.html', context)


#Detail views


def category_sport_detail(request, pk):
    certain_new = News.objects.get(id=pk)
    context = {
        "certain_new": certain_new
    }
    return render(request, 'sport/category_sport_detail.html', context)


def category_politic_detail(request, pk):
    certain_new = News.objects.get(id=pk)
    context = {
        "certain_new": certain_new
    }
    return render(request, 'politic/category_politic_detail.html', context)


def category_business_detail(request, pk):
    certain_new = News.objects.get(id=pk)
    context = {
        "certain_new": certain_new
    }
    return render(request, 'business/category_business_detail.html', context)



#CRUD


def news_add (request):
    categories = Categories.objects.filter(pk__in=[1, 2, 3])
    context = {
        "categories": categories
    }
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        image = request.POST['image']
        category_id = Categories.objects.get(pk=request.POST['category'])
        news = News(news_title=title, news_body=body, news_image=image, news_category=category_id)
        news.save()
        return redirect('HomePage')
    else:
        return render(request, "CRUD/news_add.html", context)


def news_edit(request, pk):
    categories = Categories.objects.filter(pk__in=[1, 2, 3])
    news = News.objects.get(id=pk)
    context = {
        "categories": categories,
        "news": news
    }

    if request.method == "POST":
        news.news_title = request.POST['title']
        news.news_body = request.POST['body']
        news.news_image = request.POST['image']
        news.news_category = Categories.objects.get(pk=request.POST['category'])
        news.save()
        return redirect("HomePage")
    else:
        return render(request, 'CRUD/news_edit.html', context)


def news_delete(request, pk):
    news = News.objects.get(id=pk)
    context = {
        "news": news
    }
    if request.method == "POST":
        news.delete()
        return redirect("categories_all")
    else:
        return render(request, "CRUD/news_delete_confirmation.html", context)


    #-----forms-----


def news_add_form(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("HomePage")
    else:
        form = NewsForm()
        context = {
            "form": form
        }
        return render(request, 'forms/news_add_form.html', context)
