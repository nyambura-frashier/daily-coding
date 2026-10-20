class Library:
  library_name="The manace"

  def __init__(self,author,title,year):
    self.author=author
    self.title=title
    self.year=year
    
  def introduce(self):
    print (f"The author is{self.author}")
    print (f"The title is {self.title}")
    print (f"The year is {self.year}")
    

book1=Library("brian","The look",1930)
book2=Library("Jesus","the bible",1938)

book1.introduce()
book2.introduce()

    