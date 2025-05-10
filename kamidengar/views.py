from django.shortcuts import render

def frontpage(request):
    return render(request, 'kamidengar/frontpage.html')

def loginpage(request):
    return render(request, 'kamidengar/loginpage.html')

def dashboard(request):
    return render(request, 'kamidengar/dashboard.html')

def homepage(request):
    return render(request, 'kamidengar/homepage.html')

def forgetpassword(request):
    return render(request, 'kamidengar/forgetpassword.html')

def createaccpage(request):
    return render(request, 'kamidengar/createaccpage.html')

def communityupdate(request):
    return render(request, 'kamidengar/communityupdate.html')

def profile(request):
    return render(request, 'kamidengar/profile.html')

def hazardselection(request):
    return render(request, 'kamidengar/hazardselection.html')

def pothole(request):
    return render(request, 'kamidengar/pothole.html')

def brokentrafficlight(request):
    return render(request, 'kamidengar/brokentrafficlight.html')

def fadedroadmarking(request):
    return render(request, 'kamidengar/fadedroadmark.html')

def illegaldumping(request):
    return render(request, 'kamidengar/illegaldumping.html')

def illegalparking(request):
    return render(request, 'kamidengar/illegalparking.html')

def blockdrain(request):
    return render(request, 'kamidengar/blockdrain.html')

def thankyou(request):
    return render(request, 'kamidengar/thankyou.html')

def termsandconditions(request):
    return render(request, 'kamidengar/termsandconditions.html')