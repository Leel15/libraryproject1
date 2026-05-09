from django.shortcuts import render ,redirect  
from django.db.models import Q,Avg, Max, Min, Sum, Count
from .models import Book , Address , Publisher , Book1 , Student,Student2,BookGallery
from .forms import BookForm , StudentForm , Student2Form , BookGalleryForm


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





def task1(request):

    books = Book.objects.all()    
    total_res = Book.objects.aggregate(total=Sum('quantity'))
    total_qty = total_res['total'] or 1
    
    for b in books:
        b.availability = (b.quantity / total_qty) * 100
        
    return render(request, 'bookmodule/lab9/task1.html', {'books': books})

def task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9/task2.html', {'publishers': publishers})

def task3(request):
    publishers = Publisher.objects.annotate(oldest_book_date=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9/task3.html', {'publishers': publishers})

def task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9/task4.html', {'publishers': publishers})

def task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4))
    )
    return render(request, 'bookmodule/lab9/task5.html', {'publishers': publishers})

def task6(request):
    publishers = Publisher.objects.annotate(
        specific_books_count=Count('book', filter=Q(book__price__gt=50, book__quantity__gte=1, book__quantity__lt=5))
    )
    return render(request, 'bookmodule/lab9/task6.html', {'publishers': publishers})

def list_books(request):
    all_books = Book1.objects.all() 
    return render(request, 'bookmodule/listbooks.html', {'books': all_books})

def add_book(request):
    if request.method == 'POST':
        t = request.POST.get('title')
        a = request.POST.get('author')
        p = request.POST.get('price')
        e = request.POST.get('edition')
        
        new_obj = Book1(title=t, author=a, price=float(p), edition=int(e))
        new_obj.save()
        
        return redirect('list_books')
        
    return render(request, 'bookmodule/addbook.html')

def edit_book(request, id):
    book_obj = Book1.objects.get(id=id)
    
    if request.method == 'POST':
        book_obj.title = request.POST.get('title')
        book_obj.author = request.POST.get('author')
        book_obj.price = float(request.POST.get('price'))
        book_obj.edition = int(request.POST.get('edition'))
        
        book_obj.save() 
        return redirect('list_books') 
    
    return render(request, 'bookmodule/addbook.html', {'book': book_obj})

def delete_book(request, id):
    book_obj = Book1.objects.get(id=id)
    book_obj.delete() 
    
    return redirect('list_books')


def list_books_p2(request):
    books = Book1.objects.all()
    return render(request, 'bookmodule/listbooks_p2.html', {'books': books})

def add_book_p2(request):
    if request.method == 'POST':
        form = BookForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('list_books_p2')
    else:
        form = BookForm() 
    return render(request, 'bookmodule/addbook_p2.html', {'form': form})

def edit_book_p2(request, id):
    book = Book1.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books_p2')
    else:
        form = BookForm(instance=book) 
    return render(request, 'bookmodule/addbook_p2.html', {'form': form})

def delete_book_p2(request, id):
    book = Book1.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books_p2')
    
    return render(request, 'bookmodule/deletebook_p2.html', {'book': book})




def student_list(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/student_list.html', {'students': students})


def manage_student(request, id=None):
    if id: 
        student = Student.objects.get(id=id)
    else: 
        student = None

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save() 
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'bookmodule/manage_student.html', {'form': form})


def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('student_list')



def student_list_p2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/student_list_p2.html', {'students': students})

def manage_student_p2(request, id=None):
    student = Student2.objects.get(id=id) if id else None

    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list_p2')
    else:
        form = Student2Form(instance=student)
    
    return render(request, 'bookmodule/manage_student_p2.html', {'form': form})

def delete_student_p2(request, id):
    student = Student2.objects.get(id=id)
    student.delete()
    return redirect('student_list_p2')


def add_book_gallery(request):
    if request.method == 'POST':
        form = BookGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('book_gallery_list')
    else:
        form = BookGalleryForm()
    return render(request, 'bookmodule/add_book_gallery.html', {'form': form})

def book_gallery_list(request):
    books = BookGallery.objects.all()
    return render(request, 'bookmodule/book_gallery_list.html', {'books': books})