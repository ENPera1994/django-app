from django.shortcuts import render, redirect
from .models import Product, Category, Face, Architect
from django.contrib import messages
#from django.contrib.auth import authenticate, login, logout


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})


def home(request):
    products = Product.objects.all()[:4]
    faces = Face.objects.all()[:4]
    architects = Architect.objects.all()[:4]
    return render(request, 'home.html', {'products':products, 'faces':faces, 'architects':architects})


def about(request):
   return render(request, 'about.html', {})


def products(request):
    categoria_filtro = request.GET.get('categoria', '')
    ancho_terreno_filtro = request.GET.get('ancho_terreno', '')
    metros_cuadrados_filtro = request.GET.get('metros_cuadrados', '')
    dormitorios_filtro = request.GET.get('dormitorios', '')
    pisos_filtro = request.GET.get('pisos', '')

    products = Product.objects.all()

    if categoria_filtro:
        products = products.filter(category=categoria_filtro)
    
    if ancho_terreno_filtro:
        if ancho_terreno_filtro == '1':
            products = products.filter(width__range=(0, 10))
        elif ancho_terreno_filtro == '2':
            products = products.filter(width__range=(10, 20))
        elif ancho_terreno_filtro == '3':
            products = products.filter(width__range=(20, 30))
        elif ancho_terreno_filtro == '4':
            products = products.filter(width__range=(30, 40))
        elif ancho_terreno_filtro == '5':
            products = products.filter(width__range=(40, 50))
        elif ancho_terreno_filtro == '6':
            products = products.filter(width__range=(50, 60))
        elif ancho_terreno_filtro == '7':
            products = products.filter(width__range=(60, 70))
        elif ancho_terreno_filtro == '8':
            products = products.filter(width__range=(70, 80))
        elif ancho_terreno_filtro == '9':
            products = products.filter(width__range=(80, 90))
        elif ancho_terreno_filtro == '10':
            products = products.filter(width__range=(90, 100))

    if metros_cuadrados_filtro:
        if metros_cuadrados_filtro == '1':
            products = products.filter(dimension__range=(0, 10))
        elif metros_cuadrados_filtro == '2':
            products = products.filter(dimension__range=(10, 20))
        elif metros_cuadrados_filtro == '3':
            products = products.filter(dimension__range=(20, 30))
        elif metros_cuadrados_filtro == '4':
            products = products.filter(dimension__range=(30, 40))
        elif metros_cuadrados_filtro == '5':
            products = products.filter(dimension__range=(40, 50))
        elif metros_cuadrados_filtro == '6':
            products = products.filter(dimension__range=(50, 60))
        elif metros_cuadrados_filtro == '7':
            products = products.filter(dimension__range=(60, 70))
        elif metros_cuadrados_filtro == '8':
            products = products.filter(dimension__range=(70, 80))
        elif metros_cuadrados_filtro == '9':
            products = products.filter(dimension__range=(80, 90))
        elif metros_cuadrados_filtro == '10':
            products = products.filter(dimension__range=(90, 100))
        # products = products.filter(dimension=int(metros_cuadrados_filtro))

    if dormitorios_filtro:
        products = products.filter(cantRoom=int(dormitorios_filtro))

    if pisos_filtro:
        products = products.filter(cantFloor=int(pisos_filtro))

    categories = Category.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories})


def fachadas(request):
    categoria_filtro = request.GET.get('categoria', '')
    faces = Face.objects.all()
    if categoria_filtro:
        faces = faces.filter(category=categoria_filtro)
    categories = Category.objects.all()
    return render(request, 'fachadas.html', {'faces':faces, 'categories': categories})

def architects(request):
    architects = Architect.objects.all()
    architects = architects.filter(checked=True)
    return render(request, 'architects.html', {'architects':architects})


def registerArchitect(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        qualification = request.POST['qualification']
        positions = request.POST['positions']
        experience = request.POST['experience']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        architect = Architect(name=name, password=password, qualification=qualification, positions=positions, experience=experience, email=email, phone=phone, city=city)
        architect.save()
        return redirect('home')
    else:
        return render(request, 'register.html', {})


# def loginArchitect(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, ("You Have Been Logged In!"))
#             return redirect('home')
#         else:
#             messages.success(request, ("There was an error, please try again..."))
#             return redirect('login')

#     else:
#         return render(request, 'login.html', {})

# def logoutArchitect(request):
#     logout(request)
#     return redirect('home')

