from book import Book
from controller import scrapeBook, getDownload

if __name__ == "__main__":

    owner = 'http://link.domain.com'
    links = ['http://link.domain.com/openurl?genre=book&isbn=978-0-387-93837-0']
    for link in links:
        Book = scrapeBook(link)
        getDownload(Book, owner)




