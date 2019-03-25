class Media :
    def __init__(self,name,author,release_date):
        self.name=name
        self.author=author
        self.release_date=release_date

class Book(Media):
    def __init__(self,name,author,release_date,nb_page,genre):
        Media.__init__(self,name,author,release_date)
        self.nb_page=nb_page
        self.genre=genre
    
    def get_info(self):
        print('Name :',self.name,'\nAuthor :',self.author,
            '\nRelease date :',self.release_date,'\nNumber of pages :',
                self.nb_page,'\nGenre :',self.genre)
    
    def add_chapter(self,new_chapter_page,today_date):
        self.nb_page+=new_chapter_page
        self.release_date=today_date
        print('the number of pages of',self.name,'is now :',self.nb_page)

class Movie(Media):
    def __init__(self,name,author,release_date,duration):
        Media.__init__(self,name,author,release_date)
        self.actors=[]
        self.duration=duration
    
    def add_actor(self,new_actor):
        self.actors.append(new_actor)
    
    def print_casting(self):
        print('The casting is :')
        for i in self.actors:
            print(i)

# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    Livre = Book('Les aventure de l IN','Y. Bornachot','23/03/2019',3,'comics')
    Livre.get_info()

    Film=Movie('Les aventures de l\'in104','P.Haro','22/03/2019','15h01')
    Film.add_actor('Yohan Bornachot')
    Film.add_actor('Megan Perez')
    print('\n')
    Film.print_casting()