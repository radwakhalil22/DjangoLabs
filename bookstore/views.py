from django.shortcuts import render, redirect
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from .forms import BookForm

# def index(request): 
#     return HttpResponse('Radwa')

# Create your views here.
def index(request):
    all_books = Book.objects.all()
    return render(request, 'bookstore/bookList.html', context={"books": all_books})



# book_list = [
#     {
#         'index': 0,
#         'id': 1,
#         'name': 'TASK-1',
#         'priority': 1,
#         'description': "Learning Learnin gJSfffjk dfjdklg jkdgjdkgjdkgjd kgjdkgjdglk jdgkljfjfjejekgjekgjekgjekgjgekjgekLearningJSfffjkdfjdklgjkdgjdkgjdkgjdkgjdkgjdglkjdgkljfjfjejekgjekgjekgjekgjgekjgekLearningJSfffjkdfjdklgjkdgjdkgjdkgjdkgjdkgjdglkjdgkljfjfjejekgjekgjekgjekgjgekjgek",
#     },
#     {
#         'index': 1,
#         'id': 2,
#         'name': 'TASK-2',
#         'priority': 4,
#         'description': "Learning LearningJS fffjkdfjd klgjkdgjdkgjdkgjdkgjd kgjdglkjdgk ljfj fjejekgjekgjekgjekgjgekjgek",
#     },
#     {
#         'index': 2,
#         'id': 3,
#         'name': 'TASK-3',
#         'priority': 2,
#         'description': "LearningJS fffjk dfjdklgjkdg jdkgjdkgjd kgjdkgjdglkjdgkl jfjfjejekg jekgjekgjekgjgekjgek",
#     },
# ]


# def _get_book(book_id):
#     for book in book_list:
#         if 'id' in book and book['id'] == book_id:
#             return book
#     return None
    
def books_list(request):
    all_books = Book.objects.all()
    return render(request, 'bookstore/bookList.html', context={"books": all_books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'bookstore/bookDetails.html', context={"book": book})


def book_delete(request, pk):
    Book.objects.get(pk=pk).delete()
    return redirect("bookstore:book-list")
    

def book_update(request,pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookstore:book-update", pk=book.id)
        
    return render(request, 'bookstore/book_update.html', context={
        'form': form, 
        'book': book
    })
def create_book(request):
        form = BookForm()
        if request.method == "POST":
            form = BookForm(data=request.POST)
            if form.is_valid():
                form.save()
            return redirect("bookstore:index")
        return render(request, 'bookstore/book_create.html', context={
            'form': form
    })