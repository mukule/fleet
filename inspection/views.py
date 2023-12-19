from django.shortcuts import render, redirect
from .models import Inspection
from .forms import InspectionForm

def inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # You can add a success message or redirect to a different page
            return redirect('success_page')
    else:
        form = InspectionForm()

    return render(request, 'inspection/index.html', {'form': form})
