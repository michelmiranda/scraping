from book import Book
from controller import scrapeBook, getDownload

if __name__ == "__main__":

    owner = 'http://'
    links = ['http://']
    for link in links:
        Book = scrapeBook(link)
        getDownload(Book, owner)




