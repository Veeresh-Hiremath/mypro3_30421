from django.http import HttpResponse
import os
def my1(request):
    return HttpResponse("<h1>hii good morning</h1>")
def my2(request):
    a='''<h2>hey mams</h2>
    <h1>how are you</h1></a>'''
    return HttpResponse(a)
a1=os.path.abspath(__file__)
a2=os.path.dirname(os.path.dirname(a1))
def my3(request):
    f=os.path.join(a2,"html.html")
    w=open(f)
    e=w.read()
    return HttpResponse(e)