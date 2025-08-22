from pydantic import BaseModel, Field
from fastapi import FastAPI
from typing import List, Optional
import uvicorn


app = FastAPI()

# ================== SCHEMAS ===================

class GenresSchema(BaseModel):
    id: int
    title: str = Field(max_length=40)
    description: Optional[str] = Field(default=None, max_length=50)
    created_at: int


class AuthorsSchema(BaseModel):
    id: int
    first_name: str = Field(max_length=30)
    last_name: Optional[str] = Field(default=None, max_length=50)
    bio: Optional[str] = Field(default=None, max_length=100)


class BooksSchema(BaseModel):
    id: int
    name: str = Field(max_length=100)
    author: List[int] = []          # список ID авторов
    genres: List[int] = []          # список ID жанров
    description: str = Field(max_length=160)
    year: Optional[int]
    available: bool = True


class LibraryResponse(BaseModel):
    genre_schema: List[GenresSchema]
    author_schema: List[AuthorsSchema]
    book_schema: List[BooksSchema]


# ================== STORAGE ===================

genres: List[GenresSchema] = []
authors: List[AuthorsSchema] = []
books: List[BooksSchema] = []


# ================== ENDPOINTS ===================

@app.post("/genres")
def add_genre(genre: GenresSchema):
    genres.append(genre)
    return {"Success": True, "message": "Genre saved"}


@app.post("/authors")
def add_author(author: AuthorsSchema):
    authors.append(author)
    return {"Success": True, "message": "Author saved"}


@app.post("/books")
def add_book(book: BooksSchema):
    books.append(book)
    return {"Success": True, "message": "Book saved"}


# --------- GET endpoints ----------

@app.get("/library_schema/all", response_model=LibraryResponse)
def get_all():
    return LibraryResponse(
        genre_schema=genres,
        author_schema=authors,
        book_schema=books,
    )


@app.get("/library_schema/genres", response_model=List[GenresSchema])
def get_genres():
    return genres


@app.get("/library_schema/authors", response_model=List[AuthorsSchema])
def get_authors():
    return authors


@app.get("/library_schema/books", response_model=List[BooksSchema])
def get_books():
    return books


# ================== RUN ===================

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
