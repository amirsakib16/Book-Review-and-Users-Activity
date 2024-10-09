class Book:
    def __init__(self,*info):
        self.info = info
class BookDirectory:
    def __init__(self):
        self.bookName, self.reviewValue, self.result, self.sortedInfo, self.output = [], [], [], [], []
    def add_book(self,memoryLocationBook):
        self.bookName.append(f"{memoryLocationBook.info[0]}$@${memoryLocationBook.info[1]}$@${memoryLocationBook.info[2]}")
        self.bookName.append(0)
        self.bookName.append("")
    def add_reader(self,memoryLocationReader):
        counter = 1
        for i in range(0,len(self.bookName)-1,3):
            for j in range(0,len(memoryLocationReader.review)-1,3):
                if self.bookName[i] == memoryLocationReader.review[j]:
                    counter+=1
                    self.bookName[i+1] += memoryLocationReader.review[j+1]
                    self.bookName[i+2] += f"   COMMENT->  {memoryLocationReader.review[j+2]}\n"
            self.bookName[i+1] /= counter
            counter = 1
    def get_highest_rated_books(self,rank):
        self.result = []
        for i in range(0,len(self.bookName)-1,3):
            self.result.append(f"{self.bookName[i]}@$@{self.bookName[i+1]}@$@{self.bookName[i+2]}")
        for i in range(len(self.result)-1,0,-1):
            for j in range(i):
                if float(self.result[j].split('@$@')[1])<float(self.result[j+1].split('@$@')[1]):
                    self.result[j],self.result[j+1] = self.result[j+1],self.result[j]
        for i in self.result:
            self.sortedInfo.append(i.split("@$@")[0])
            self.sortedInfo.append(i.split("@$@")[2])
        for i in range(0,len(self.sortedInfo),2):
            self.output.append(f"{self.sortedInfo[i].split('$@$')[0]} ({self.sortedInfo[i].split('$@$')[1]}) by {self.sortedInfo[i].split('$@$')[2]}")
            self.output.append(self.sortedInfo[i+1])
        return self.output[0:rank*2]
class Reader:
    def __init__(self,name):
        self.name = name
        self.review = []
    def add_review(self,*review):
        self.review.append(f"{review[0].info[0]}$@${review[0].info[1]}$@${review[0].info[2]}")
        self.review.append(review[1])
        self.review.append(review[2])



Book1 = Book("Harry Potter and the Goblet of Fire", 2000, "J. K. Rowling")
Book2 = Book("If Tomorrow Comes", 1985, "Sidney Sheldon")
Book3 = Book("Diary of a Wimpy Kid", 2007, "Jeff Kinney")
Book4 = Book("Sapiens: A Brief History of Humankind", 2011, "Yuval Noah Harari")



directory = BookDirectory()
directory.add_book(Book1)
directory.add_book(Book2)
directory.add_book(Book3)
directory.add_book(Book4)


Reader1 = Reader("Bob")
Reader1.add_review(Book1, 5, "The best book I ever read!")
Reader1.add_review(Book2, 4, "One of the best thrillers")
Reader2 = Reader("Carol")
Reader2.add_review(Book1, 4, "Love a good magical story!")
Reader2.add_review(Book3, 3, "I somewhat liked the book but the genre is not my type.")
Reader2.add_review(Book4, 5, "Beautifully written.")
Reader3 = Reader("Harry")
Reader3.add_review(Book4, 5, "What a fantastic book!")


directory.add_reader(Reader1)
directory.add_reader(Reader2)
directory.add_reader(Reader3)

highest_rated_books = directory.get_highest_rated_books(2)


print('-------------------------------')
print("Highest rated books:")
for book in highest_rated_books:
    print(book)
print('-------------------------------')


highest_rated_books = directory.get_highest_rated_books(3)


print('-------------------------------')
print("Highest rated books:")
for book in highest_rated_books:
    print(book)
print('-------------------------------')