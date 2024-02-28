from django.shortcuts import render, redirect
from news.forms import CreateCategoryForm, CreateNewsForm
from rest_framework import viewsets
from news.models import News, Category, User
from news.serializers import CategorySerializer, UserSerializer, NewsSerializer


def home(request):
    news = News.objects.all()
    context = {"news": news}

    return render(request, "home.html", context=context)


def news_details(request, id):
    news = News.objects.get(pk=id)
    context = {"news": news}

    return render(request, "news_details.html", context=context)


def categories_form(request):
    form = CreateCategoryForm()

    if request.method == "POST":
        form = CreateCategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home-page")

    context = {"form": form}
    return render(request, "categories_form.html", context)


def news_form(request):
    form = CreateNewsForm()

    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)

        if form.is_valid():
            news_instance = form.save(commit=False)
            news_instance.image = form.cleaned_data["image"]
            news_instance.save()
            return redirect("home-page")

    context = {"form": form}
    return render(request, "news_form.html", context)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
