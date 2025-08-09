from django.core.paginator import Paginator
from django.shortcuts import render
from .models import EmailEntry

def email_list(request):
    emails = EmailEntry.objects.all().order_by('-timestamp')
    
    paginator = Paginator(emails, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "webapp/email_list.html", {"page_obj": page_obj})

