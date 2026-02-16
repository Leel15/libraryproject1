from django.http import HttpResponse
from django.shortcuts import render  

#Task 1 
#def index(request): 
 #   return HttpResponse("Hello, world!") 

#task 2
#def index(request): 
 
   #name = request.GET.get("name") or "world!" 
  # return HttpResponse("Hello, "+name) 

#task 3
#def index2(request, val1=0):
 
 #   return HttpResponse("value1 = " + str(val1))

#task 4
#def index(request):  
 #   name = request.GET.get("name") or "world!" 
 #   return render(request, "bookmodule/index.html") 

#task 5 
#def index(request): 
 #   name = request.GET.get("name") or "world!" 
  #  return render(request, "bookmodule/index.html" , {"name": name})

#task 6 
#def index(request): 
 #   name = request.GET.get("name") or "world!" 
  #  return HttpResponse("Hello, "+name) 

#task 6
def index2(request, val1=0):
    if isinstance(val1, int):
        return HttpResponse("value1 = " + str(val1))
    else:
        return HttpResponse("error, expected val1 to be integer")


def index(request): 
   name = request.GET.get("name") or "world!"  #add this line 
   return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name 

def viewbook(request, bookId): 
# assume that we have the following books somewhere (e.g. database) 
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'} 
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    targetBook = None 
    if book1['id'] == bookId: targetBook = book1 
    if book2['id'] == bookId: targetBook = book2 
    context = {'book':targetBook} # book is the variable name accessible by the template 
    return render(request, 'bookmodule/show.html', context) 

 