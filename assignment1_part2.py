
#create book class with the two attributes
class Book:
  def __init__(self, author, title):

    self.author = author
    self.title = title

#create function to display written by book and title format
  def display(self):

    print (self.title + ", written by " + self.author)

#creating objects
book1 = Book("John Steinbeck", "Of Mice and Men")
book2 = Book("Robert Lee", "To Kill A Mockingbird")


book1.display()
book2.display()

