from book import Book
from controller import scrapeBooks, getDownload

if __name__ == "__main__":

    owner = 'http://link.springer.com'
    links = ['http://link.springer.com/openurl?genre=book&isbn=978-0-387-93837-0']
    for link in links:
        Book = scrapeBooks(link)
        getDownload(Book, owner)




