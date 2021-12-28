from django.shortcuts import render


def main_page(request):
    return render( request, "main_page.html")


def my_account(request):
    return render( request, "my_account.html")
