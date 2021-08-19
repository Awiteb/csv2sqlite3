<center>
<h1>
csv2sqlite3
</h1>
<b>
csv2sqlite3 It is a command line tool that helps you to add one or more csv tables to a sqlite3 database.
</b>
</center>

<br>
<p align="center">
  <a href="#Features">Features</a>
  •
  <a href="#Requirements">Requirements</a>
  •
  <a href="#Install">Install</a>
  •
  <a href="#Uses">Uses</a>
  •
  <a href="#Example">Example</a>
  <br>
  <a href="#License">License</a>
</p>

> Note: Please check that the file encoding is UTF-8

## Features
* Change the name of output database
* Add one or more csv files to the database
* Information about file flow (see [examples](#Example))

## Requirements
* **[python3.8](https://www.python.org/downloads/) +**
* **[git](https://git-scm.com/)**
* **[pip](https://pip.pypa.io/en/stable/installation/)**

## Install
use [GitHub](https://github.com/) to clone the tool
```bash
git clone https://github.com/Awiteb/csv2sqlite3
cd csv2sqlite3
pip3 install -r requirements.txt
```

## Uses
```text
Usage: csv2sqlite3.py [OPTIONS] CSV_FILENAMES...

Arguments:
  CSV_FILENAMES...  [required]

Options:
  --output-filename TEXT  [default: output.sqlite3]
  --help                  Show this message and exit.

```

## Example

```bash
$ python3 csv2sqlite3.py books.csv
N: Output file is output.sqlite3
N: Done connect with output.sqlite3
N: Working with books.csv
N: Table name: book
N: Columns: ['bookID', 'title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code', 'num_pages', 'ratings_count', 'text_reviews_count', 'publication_date', 'publisher']
N: Done insert into book 11127 rows in 0.27s
```

```bash
$ python3 csv2sqlite3.py --output-filename test.db Book\ reviews/Book\ reviews/*
N: Output file is test.db
N: Done connect with test.db
N: Working with BX-Book-Ratings.csv
N: Table name: BX-Book-Rating
N: Columns: ['User-ID', 'ISBN', 'Book-Rating']
N: Done insert into BX-Book-Rating 1048575 rows in 20.00s
N: Working with BX_Books.csv
N: Table name: BX_Book
N: Columns: ['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-S', 'Image-URL-M', 'Image-URL-L', '']
N: Done insert into BX_Book 271379 rows in 12.03s
N: Working with BX-Users.csv
N: Table name: BX-User
N: Columns: ['User-ID', 'Location', 'Age', '']
N: Done insert into BX-User 278851 rows in 8.49s
```

## License
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)