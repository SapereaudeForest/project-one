from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title' : 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'category': 'Fiction'},
    {'title' : 'To Kill a Mockingbird', 'author': 'Harper Lee', 'category': 'Fiction'},
    {'title' : '1984', 'author': 'George Orwell', 'category': 'Dystopian'},
    {'title' : 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'category': 'Fiction'},
    {'title' : 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'category': 'Fantasy'},
    {'title' : 'Pride and Prejudice', 'author': 'Jane Austen', 'category': 'Romance'},
    {'title' : 'The Hobbit', 'author': 'J.R.R. Tolkien', 'category': 'Fantasy'}
]

@app.get("/mybook")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book['title'].lower() == book_title.lower():
            return book
    return {"error": "Book not found"}

@app.get("/books/category/{book_category}")
async def read_book_by_category(book_category: str):
    matching_books = [book for book in BOOKS if book['category'].lower() == book_category.lower()]
    if matching_books:
        return matching_books
    return {"error": "Category book not found"}

@app.get("/books/{book_author}/")
async def read_author_books_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').lower() == book_author.lower() and book.get('category').lower() == category.lower():
            books_to_return.append(book)
    if books_to_return:
        return books_to_return
    return {"error": "Author or category book not found"}

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "Book created successfully", "book": new_book}

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for index in range(len(BOOKS)):
        if BOOKS[index]['title'].lower() == updated_book.get('title').lower():
            BOOKS[index] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for index in range(len(BOOKS)):
        if BOOKS[index].get('title').lower() == book_title.lower():
            deleted_book = BOOKS.pop(index)
            return {"message": "Book deleted successfully", "book": deleted_book}
    return {"error": "Book not found"}

          



