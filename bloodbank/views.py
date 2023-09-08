from django.shortcuts import render, redirect
from .forms import BloodDonorForm
from .models import BloodDonor

def home(request):
    if request.method == 'POST':
        form = BloodDonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = BloodDonorForm()

    context = {'form': form}
    return render(request, 'home.html', context)

def display(request):
    donors = BloodDonor.objects.all()
    print(donors)
    context = {'donors': donors}
    return render(request, 'display.html', context)





# from django.shortcuts import render, redirect
# from .forms import BloodDonorForm
# from .models import BloodDonor

# def home(request):
#     if request.method == 'POST':
#         form = BloodDonorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('display')
#     else:
#         form = BloodDonorForm()

#     context = {'form': form}
#     return render(request, 'home.html', context)

# def display(request):
#     donors = BloodDonor.objects.all()
#     print(donors)
#     context = {'donors': donors}
#     return render(request, 'display.html', context)

# def landing(request):
#         return render(request,'register.html')