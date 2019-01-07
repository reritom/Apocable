from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@csrf_exempt
def login_user(request):
    if request.method == 'GET':
        return JsonResponse({'logged_in': request.user.is_authenticated()})

    elif request.method == 'POST':
        if request.user.is_authenticated:
            return JsonResponse({'ko':"User already logged in"})

        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            return JsonResponse({'ko':"Username doesn't exist"})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message':'User successfully logged in'})
        else:
            return JsonResponse({'ko':"Unsuccessful login"})

    else:
        return JsonResponse({'ko':"Unsupported request method"})

def logout_user(request):
    logout(request)
    return JsonResponse({'hello':'out'})

@csrf_exempt
def signup_user(request):
    if request.user.is_authenticated:
        return JsonResponse({"ko":"ko"})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            return JsonResponse({"ko":"This username already exists"})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
    return JsonResponse({'hello':'up'})

