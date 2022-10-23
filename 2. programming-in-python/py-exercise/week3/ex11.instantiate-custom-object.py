class MyFirstClass():
    print("Who wrote this?")
    index = "Author Book"
    
    def hand_list(self, philosopher, book, year):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book " + book + " where " + philosopher + \
            " is the philosopher and " + book + " is the book. In the year " + str(year))


whodunnit = MyFirstClass()
whodunnit.hand_list("Plato", "Republic", 45)
whodunnit.hand_list("Sun Tzu", "The Art Of War", "5th century BC")
