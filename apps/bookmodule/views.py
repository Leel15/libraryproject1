from django.shortcuts import render 
from django.db.models import Q,Avg, Max, Min, Sum, Count
from .models import Book , Address , Student


def index(request): 
    return render(request, "bookmodule/index.html") 

def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 

def viewbook(request, bookId): 
    return render(request, 'bookmodule/one_book.html') 

def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/html5/links.html')

def formatting(request):
    return render(request, 'bookmodule/html5/text/formatting.html')

def listing(request):
    return render(request, 'bookmodule/html5/listing.html')

def tables(request):
    return render(request, 'bookmodule/html5/tables.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            
            if isTitle and string in item['title'].lower():
                contained = True
                
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
                
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    
    mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition= 1)
    mybook = Book.objects.create(title = 'Continuous Delivery', author = 'J.Humble and D.Farley', edition = 1)
    mybook.save()

    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})  

def lookup_query(request):
    mybooks=books=Book.objects.filter(author__isnull =
    False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

# Task 1: Price <= 80
def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books, 'title': 'Task 1'})

# Task 2: Edition > 3 AND (Title or Author contains 'qu')
def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books, 'title': 'Task 2'})

# Task 3: Opposite of Task 2
def task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books, 'title': 'Task 3'})

# Task 4: Order by Title
def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books, 'title': 'Task 4'})


# Task 5:
def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/stats.html', {'stats': stats})

# task7
def task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/city_stats.html', {'cities': cities})