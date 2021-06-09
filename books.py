class Books:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):

        return f"Title: {self.title} Author: {self.author}"

mybook = Books("Python basics", "Orland", '250')
print(mybook)
