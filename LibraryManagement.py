from dask.bag.avro import read_file
from mypyc.build import write_file
from sphinx.testing.fixtures import status
from sympy.codegen.ast import continue_

from Book import Book


class Book_Service():


    def read_library_file(self):
        list = []
        class_list = []
        try:
            with open("C:\\Users\\omidd\\Desktop\\library.txt", "r", encoding="utf-8") as file:
                list = [line.strip().split("|") for line in file]
                if list != [['']] and list != []:
                    for item in list:
                        title = item[0]

                        author = item[1]

                        publication_year = item[2]

                        status = item[3]

                        book = Book(title, author, publication_year, status)
                        class_list.append(book)
                    return class_list
                else:
                    return 0
        except:
            print("*****There is no library.txt file in directory !!!*****")
            print("Make a new one?" + "   " + "Please go to add book menu" + "   " + "otherwise find backup file" + "\n")
            return 0

    def create_book(self):
        print("=== Add Book ===" + "\n")
        title = str(input("Pleas Write Here Book Title: "))

        author = str(input("Pleas Write Name of Book Author: "))

        publication_year = str(input("Pleas Write Publication year: "))

        status = "Returned"

        book = Book(title, author, publication_year, status)
        return book



    def list_book(self,all_books):
        print("=== List All Book ===" + "\n")
        count = 1
        try:
            for book in all_books:
                print(f"{count}.tilte:\033[1m{book.get_title()}\033[0m author:\033[1m{book.get_author()}\033[0m publication year:\033[1m{book.get_publication_year()}\033[0m status:\033[1m{book.get_status()}\033[0m")
                count += 1
        except:
            print("*****There is no book in library!*****"+"\n")
        return

    def search_book(self,all_books):
        print("=== Search Books ===" + "\n")
        count = 1
        list = []
        if all_books != 0 :

            name = str(input("Please write here the name of book or name of author:"))
            for book in all_books:
                if name in book.get_title()  or name in book.get_author():
                    list.append(book)
                else:
                    continue
            if list:
                for book in list:
                    print(f"{count}.tilte:\033[1m{book.get_title()}\033[0m author:\033[1m{book.get_author()}\033[0m publication year:\033[1m{book.get_publication_year()}\033[0m status:\033[1m{book.get_status()}\033[0m")
                    count += 1
                return book
            else:
                print(f"*****No {name} found as title or author!*****")
        else:
            print("*****There is no book in library!*****"+"\n")




    def mark_book(self,book,all_books):
        print("=== Borrow/Return ===" + "\n")
        if all_books != 0:
            value = str(input("--Do you want to change status of this book:-- " +"\n"+"if yes please enter 1 otherwise please enter 0: "))
            print(f"1.tilte:\033[1m{book.get_title()}\033[0m author:\033[1m{book.get_author()}\033[0m publication year:\033[1m{book.get_publication_year()}\033[0m status:\033[1m{book.get_status()}\033[0m")
            count = 0
            if value == "1":
                for item in all_books:
                    if item == book:
                        if item.status == "Returned":
                            item.status= "Borrowed"
                            print(f"1.tilte:\033[1m{book.get_title()}\033[0m author:\033[1m{book.get_author()}\033[0m publication year:\033[1m{book.get_publication_year()}\033[0m status:\033[1m{book.get_status()}\033[0m")
                            #print(all_books)
                        elif item.status == "Borrowed":
                            item.status = "Returned"
                            print(f"1.tilte:\033[1m{book.get_title()}\033[0m author:\033[1m{book.get_author()}\033[0m publication year:\033[1m{book.get_publication_year()}\033[0m status:\033[1m{book.get_status()}\033[0m")
            return all_books

        else:
            return 0


    def save_exit(self,all_books):
        #print(all_books)
        if all_books != 0:
            file = open("C:\\Users\\omidd\\Desktop\\library.txt", "w", encoding="utf-8")
            for book in all_books:
                #print(all_books)
                file.write(book.get_title() + "|" + book.get_author() + "|" + book.get_publication_year() + "|" + book.get_status() + "\n")

            file.close()

            return print("---Data saved---")
        else:
            print("*****There is no book in library!*****"+"\n")

    def back_to_menu(self):
        value = ""
        while (value != "0"):
            value = str(input("--Back to Menu? Please Enter 0-- : "))
            if value == "0":
                return "0"
            else:
                print(f" you pressed {value}")


def main_menu():
    print("=== Library Manager ===" +"\n"
    "1. Add Book"+"\n"
    "2. List All Books"+"\n"
    "3. Search Books"+"\n"
    "4. Borrow/Return Book"+"\n"
    "5. Save and Exit"+"\n")
    menu_input = str(input("Pleas select: "))
    return menu_input
k = 0
book_service = Book_Service()
all_books = book_service.read_library_file()
while (k < 1):
    menu_input = main_menu()

    #print(all_books)
    k += 1
    if menu_input == "1":
        book = book_service.create_book()
        if all_books == 0:
            all_books = []
        all_books.append(book)
        print(all_books)
        k = int(book_service.back_to_menu())


    elif menu_input == "2":
        book_service.list_book(all_books)
        k = int(book_service.back_to_menu())

    elif menu_input == "3":
        book_service.search_book(all_books)
        k = int(book_service.back_to_menu())

    elif menu_input == "4":
        book = book_service.search_book(all_books)
        all_books = book_service.mark_book(book,all_books)
        k = int(book_service.back_to_menu())


    elif menu_input == "5":
        book_service.save_exit(all_books)
        k = int(book_service.back_to_menu())








