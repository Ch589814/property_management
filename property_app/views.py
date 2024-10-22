from django.shortcuts import render

# Create your views here
from django.shortcuts import render, redirect
from .forms import PropertyForm

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return redirect('property_list')  # Redirect to the property list page
    else:
        form = PropertyForm()

    return render(request, 'property_app/add_property.html', {'form': form})


