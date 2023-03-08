from django.shortcuts import render
from js.forms import MenuForm
from .models import Menu
from django.http import JsonResponse

def form_view(request):
    form = MenuForm()

    if request.method == 'POST':
        form = MenuForm(request.POST)
        print(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

# lf means list of food
            lf = Menu(
                item_name = cd['item_name'],
                category = cd['category'],
                description = cd['description'],
            )

            lf.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'booking.html', {'form': form})