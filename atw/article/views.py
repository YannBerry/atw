from atw.article.models import *
from django.shortcuts import render
from django.http import HttpResponse
# Export pdf
from atw.article.printers import Printer
from io import BytesIO

def article_menu(request):
    articles_m = Article.objects.all()
    return render(request, 'article/article_menu.html', {'articles_m':articles_m})

def geol(request):
    return render(request, 'article/geol.html')

def article(request, title):
    article = Article.objects.get(title=title)
    return render(request, 'article/article.html', {'a':article})

def download_articles_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Articles.pdf"'
    buffer = BytesIO()
    report = Printer(buffer,'A4') # I defined A4, Landscape and Letter in printers.py
    pdf = report.print_articles()
    response.write(pdf)
    return response

def download_article_pdf(request, title):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Article_{}.pdf"'.format(title)
    buffer = BytesIO()
    report = Printer(buffer,'A4') # I defined A4, Landscape and Letter in printers.py
    pdf = report.print_article(title)
    response.write(pdf)
    return response