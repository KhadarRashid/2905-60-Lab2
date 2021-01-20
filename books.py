
class Author:
    #Initializing the variables need
    def __init__(self, name):
	    self.name = name
        #turning the list into a set to avoid the possibilities of duplicates
	    self.books = set([])
        
    def publish(self, title):
        #If statement to notify the user whether a duplicate can be added
        if title in self.books:
            print('Can\'t add that, sorry. It already exists')
        else:
            self.books.add(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books' #or function which is baslically the else in this case
        return f'Name {self.name}, Books: {titles}'

def main():

    jkr = Author('J.K Rowling')
    #calling the publish function to add the books
    jkr.publish('Fantastic Beasts')
    jkr.publish('Chamber of secrets')
    jkr.publish('Fantastic Beasts')

    print(jkr)

    dan = Author('Dan Brown')
    print(dan)

main()
