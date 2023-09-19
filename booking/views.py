from django.shortcuts import render

# Create your views here.
def get_home_page(request):
    return render(request, '../templates/base.html')

def get_booking_page(request):
    return render(request, '../templates/book.html')