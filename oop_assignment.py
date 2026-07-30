class LibraryBook:
    def __init__(self,Title,Author,Isbn,Year):

        self.Title=Title
        self.Author=Author
        self.Isbn=Isbn
        self.Year=Year
        self.available=True

    def borrow(self):
        if not self.available:
            
            print(f"The book {self.Title} has been borrowed")
        else:
            print(f"The book {self.Title} is already borrowed")

    def return_book(self):
        if not self.availlable:
           print(f"{self.Title} has been returned")
        else:
            print(f"{self.Title} is already returned")
        

    def introduce(self):
        print(f'The title is {self.Title}')
        print(f"The author is {self.Author}")
        print(f"The Isbn is {self.Isbn}")
        print(f"The year of publish is {self.Year}")

#Objects
Book1=LibraryBook("Thing fall apart","Chinua Achebe","7847692988","1960")
Book2=LibraryBook("The Alchemist","paulo coelho","6237843998","1990")
Book3=LibraryBook("Rich dad poor dad","robert kiyosaki","8598774576","1997")

Book1.introduce()
Book2.introduce()
Book3.introduce()
       


        