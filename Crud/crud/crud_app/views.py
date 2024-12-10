# crud_app/views.py
from django.shortcuts import render, redirect
from .forms import PersonForm

def person_create_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_success')  # Redirect after saving
    else:
        form = PersonForm()
    return render(request, 'crud_app/person_form.html', {'form': form})

def person_success_view(request):
    return render(request, 'crud_app/person_success.html')
