from django.shortcuts import render

def index(request):
    return render(request,'RITCSE_codeWars/Home.html')

def all_submission(request):
    return render(request, 'RITCSE_codeWars/AllSubmissions.html')

def your_submissions(request):
    file = request.FILES['myfile']

    return render(request, 'RITCSE_codeWars/YourSubmissions.html',context={'file':file})

def your_code(request):
    return render(request,'RITCSE_codeWars/YourCode.html')