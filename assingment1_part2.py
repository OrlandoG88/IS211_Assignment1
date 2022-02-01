class Book:

  author = ""
  title = ""


  def __init__(self, titleName, authorName):
   self.title = titleName
   self.author = authorName

  def display(self):
   print self.title, "written by", self.author


obj1 = Book("Of Mice and Men", "John Steinbeck")
obj2 = Book("To kill a Mockingbird", "Harper Lee")

obj1.display()
obj2.display()



