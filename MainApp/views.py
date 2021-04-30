from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Pizza


# Create your views here.


def index(request):
    """The home page for the pizzeria"""
    return render(request, "MainApp/index.html")


def pizzas(request):
    pizzas = Pizza.objects.order_by("date_added")

    context = {"pizzas": pizzas}
    return render(request, "MainApp/pizzas.html", context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by("-date_added")

    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "MainApp/pizza.html", context)


def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            form.save()
            return redirect("MainApp:pizza", pizza_id=pizza_id)

    context = {"form": form, "pizza": pizza}
    return render(request, "MainApp/new_comment.html", context)
