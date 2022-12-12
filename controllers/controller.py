from flask import render_template, request, redirect 
from app import app
from models.book_list import *
from models.Book import Book

@app.route('/library')
def index():
    return render_template('index.html', title='Home', books=book_list)

@app.route('/library', methods=['POST'])
def create():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title, author, genre)
    book_list.append(new_book)
    return redirect("/library")

@app.route('/library/delete/<index>', methods=['POST'])
def delete(index):
  delete_book_at_index(int(index))
  return redirect('/library')