class Book():

    def __init__(self,title, author, publication_year, status):

        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.status = status

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publication_year(self):
        return self.__publication_year

    def get_status(self):
        return self.status

    #def set_status_returned(self):
     #   self.__status = "Returned"
      #  return

    #def set_status_borrowed(self):
     #   self.__status ="Borrowed"
      #  return

