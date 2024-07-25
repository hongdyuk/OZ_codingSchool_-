from flask_smorest import Blueprint, abort
from schemas import BookSchema
from flask.views import MethodView

blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

books = []

@blp.route('/')
class BookList(MethodView):
    @blp.response(200)
    def get(self):
        return books

    @blp.arguments(BookSchema)
    @blp.response(200, description='Book added')
    def post(self, new_book):
        books.append(new_book)
        return new_book

@blp.route('/<int:book_id>')
class Book(MethodView):
    @blp.response(200)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message='Book not found')
        return book

    @blp.arguments(BookSchema)
    @blp.response(200, description='Book updated')
    def put(self, new_book, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message='Book not found')
        book.update(new_book)
        return book

    @blp.response(204)
    def delete(self, book_id):
        global books
        if not any(book for book in books if book['id'] == book_id):
            abort(404, message='Book not found')
        books = [book for book in books if book['id'] != book_id]
        return ''