from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Cloud_s
from django.contrib import messages

# Create your views here.


@login_required(login_url="/authentication/login")
def index(request):
    categories = Category.objects.all()
    cloud_s = Cloud_s.objects.filter(owner=request.user)

    context = {"cloud_s": cloud_s}
    return render(request, "cloud_s/index.html", context)


def add_cloud_s(request):
    categories = Category.objects.all()
    context = {"categories": categories, "values": request.POST}
    if request.method == "GET":
        return render(request, "cloud_s/add_cloud_s.html", context)

    if request.method == "POST":
        amount = request.POST["amount"]
        description = request.POST["description"]
        date = request.POST["cloud_date"]
        category = request.POST["category"]

        if not amount:
            messages.error(request, "amount is required")
            return render(request, "cloud_s/add_cloud_s.html", context)

        if not description:
            messages.error(request, "Description is required")
            return render(request, "cloud_s/add_cloud_s.html", context)

    Cloud_s.objects.create(
        owner=request.user,
        amount=amount,
        date=date,
        category=category,
        description=description,
    )
    messages.success(request, "Cloud saved succesfully")

    return redirect("cloud_s")


def cloud_edit(request, id):
    cloud_s = Cloud_s.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        "cloud_s": cloud_s,
        "values": cloud_s,
        "categories": categories,
    }
    if request.method == "GET":
        return render(request, "cloud_s/cloud-edit.html", context)
    if request.method == "POST":
        amount = request.POST["amount"]

        if not amount:
            messages.error(request, "amount is required")
            return render(request, "cloud_s/cloud-edit.html", context)

        description = request.POST["description"]
        date = request.POST["cloud_date"]
        category = request.POST["category"]

        if not description:
            messages.error(request, "Description is required")
            return render(request, "cloud_s/cloud-edit.html", context)

    cloud_s.owner = request.user
    cloud_s.amount = amount
    cloud_s.date = date
    cloud_s.category = category
    cloud_s.description = description

    cloud_s.save()
    messages.success(request, "Cloud updated succesfully")

    return redirect("cloud_s")
