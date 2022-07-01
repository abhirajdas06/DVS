from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Services view

def services(request):
    # return HttpResponse("Hello Services")
    return render(request, "services/services.html")


# vicisoft view

def vicisoft(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "vicisoft/vicisoft.html")

def doc_m(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "vicisoft/doc_management.html")

def workflow(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "vicisoft/workflow.html")


# eScan view

def escan(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "escan/escan.html")

def enterprise_edition(request):
    # return HttpResponse("Hello enterprise_edition")
    return render(request, "escan/enterprise_edition.html")

def total_security(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "escan/total_security.html")


# Sharp Education view

def sharp_education(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "sharp_education/sharp_education.html")

def classroom_management(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "sharp_education/classroom_management.html")

def touch_boards(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "sharp_education/touch_boards.html")

def sharp_signage(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "sharp_education/sharp_signage.html")

def learning_management(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "sharp_education/learning_management.html")

def interactive_content(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "sharp_education/interactive_content.html")


# NetCore Cloud view

def netcore_cloud(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "netcore_cloud/netcore_cloud.html")

def email_security(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "netcore_cloud/email_security.html")

def email_archive(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "netcore_cloud/email_archive.html")


# D-link Networking view

def networking(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "networking/networking.html")

def cable(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "networking/cable.html")

def router(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "networking/router.html")

def switch(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "networking/switch.html")


# End-point Security view

def endpoint_security(request):
    # return HttpResponse("Hello vicisoft")
    return render(request, "endpoint_security/endpoint_security.html")
