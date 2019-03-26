import unittest
from ..OOP import program_classes as prgm



class tests(unittest.TestCase):
    def test_author_maj(self):
        "test if the author name is changed in capital letters"
        name="Yohan Bornachot"
        name2="YOHAN BORNACHOT"
        self.assertEquals(name2,name.upper())
    
    def test_add_chapter_neg(self):
        "test if the book has a positive number of pages"
        Livre = prgm.Book('Les aventure de l IN','Y. Bornachot','23/03/2019',3,'comics')
        nb_page=42
        today_date='26/03/19'
        Livre.add_chapter(nb_page,today_date)
        self.assertTrue(Livre.nb_page>=0)

    def test_info_complete(self):
        "test if all the info are present in the description"
        pgrm.Book1=('Les aventure de l IN','Y. Bornachot','23/03/2019',3,'comics')
        pgrm.Book2=('20000 lieues sous les mers','Jules Vernes','03/06/1870',672,'roman')
        Known_Books=[Book1,Book2]

        for i in Known_Books:
            to_print=""'Name :',self.name,'\nAuthor :',self.author,
            '\nRelease date :',self.release_date,'\nNumber of pages :',
                self.nb_page,'\nGenre :',self.genre"
            self.assertEqual(to_print,i.print_info())



        
    def 

    
    if __name__ == '__main__':
        unittest.main()