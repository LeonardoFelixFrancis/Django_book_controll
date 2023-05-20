from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BooksForm, BooksFilterForm
from django.contrib.auth.models import User
from .models import BookModel

# Create your views here.

class LibraryIndexView(View):
    def get(self, request):

        form = BooksForm()
        field_form = BooksFilterForm

        if request.user.is_authenticated:
            books = BookModel.objects.all().filter(user=request.user)
            return render(request, "library/index.html", {"user": request.user, "form":form, "books":books, "filter_form":field_form})
        else:
            return HttpResponseRedirect(reverse("login"))
    def post(self, request):
        form = BooksForm(request.POST)
        field_form = BooksFilterForm
        books = BookModel.objects.all().filter(user=request.user)
        if request.user.is_authenticated:
            if form.is_valid():
                book = BookModel(book_name=request.POST["book_name"],
                                user = request.user)
                

                if request.POST.get("start_date") != '':
                    book.start_date = request.POST.get("start_date")
                if request.POST.get("end_date") != '':
                    book.end_date = request.POST.get("end_date")
                if request.POST.get("synopsis") != '':
                    book.synopsis = request.POST.get("synopsis")
                if request.POST.get("rating") != '':
                    book.rating = request.POST.get("rating")
                if request.POST.get("start_reading") != '':
                    book.start_reading = request.POST.get("start_reading")
                    

                book.save()
                form = BooksForm()
                return render(request, "library/index.html", {"user": request.user, "form":form, "books":books, "filter_form":field_form})
            else:
                return render(request, "library/index.html", {"user": request.user, "form":form, "books":books, "filter_form":field_form})
        else:
            return HttpResponseRedirect(reverse("login"))
    
class FilterBooksView(View):
    def post(self, request):
        field_form = BooksFilterForm(request.POST)
        form = BooksForm()
        if field_form.is_valid():
            books = BookModel.objects.all().filter(user=request.user)
            if request.POST.get('book_name') is not None and request.POST.get('book_name') != '':
                books = books.filter(book_name = request.POST['book_name'])
            if request.POST.get('rating_start') is not None and request.POST.get('rating_start') == 0:
                books = books.filter(rating__gte = request.POST['rating_start'])
            if request.POST.get('rating_end') is not None and request.POST.get('rating_end') == 0:
                books = books.filter(rating__lte = request.POST['rating_end'])
            if request.POST.get('start_date_init') is not None and request.POST.get('start_date_init') != '':
                books = books.filter(start_date__gte = request.POST['start_date_init'])
            if request.POST.get('start_date_end') is not None and request.POST.get('start_date_end') != '':
                books = books.filter(start_date__lte = request.POST['start_date_end'])
            if request.POST.get('end_date_init') is not None and request.POST.get('end_date_init') != '':
                books = books.filter(end_date__gte = request.POST['end_date_init'])
            if request.POST.get('end_date_end') is not None and request.POST.get('end_date_end') != '':
                books = books.filter(end_date__lte = request.POST['end_date_end'])
            if request.POST.get('start_reading') is not None and request.POST.get('start_reading') != '':
                books = books.filter(start_reading = request.POST.get('start_reading'))

            return render(request, "library/index.html", {"user": request.user, "form":form, "books":books, "filter_form":field_form})
        
class OpenBookFilter(View):
    def get(self, request, id):
        books = BookModel.objects.all().filter(user = request.user)
        book = BookModel.objects.get(pk=id)
        bookForm = BooksForm(initial={'book_name':book.book_name, 'rating':book.rating, 'synopsis':book.synopsis, 'start_date':book.start_date, 'end_date':book.end_date, 'start_reading':book.start_reading})
        form = BooksForm()
        field_form = BooksFilterForm
        return render(request, "library/index.html", {"user": request.user, "form":form, "books":books, "filter_form":field_form, "book" : bookForm, "book_id":book.id})
    
class EditBookView(View):
    def post(self, request, id):
        form = BooksForm(request.POST)

        if form.is_valid():
            book = BookModel.objects.get(pk = id)
            print(request.POST.get("synopsis"))
            if request.POST.get("book_name") != '' and request.POST.get("book_name") is not None:
                book.book_name = request.POST.get("book_name")
            if request.POST.get("start_date") != '':
                book.start_date = request.POST.get("start_date")
            if request.POST.get("end_date") != '':
                book.end_date = request.POST.get("end_date")
            if request.POST.get("synopsis") != '':
                book.synopsis = request.POST.get("synopsis")
            if request.POST.get("rating") != '':
                book.rating = request.POST.get("rating")
            if request.POST.get("start_reading") != '':
                book.start_reading = request.POST.get("start_reading")
            print(book.synopsis)
            book.save()

            return HttpResponseRedirect(reverse('open-book', args=[id]))

class DeleteBookView(View):
    def get(self, request, id):
        book = BookModel.objects.get(pk = id)
        book.delete()

        return HttpResponseRedirect(reverse("library-entry"))