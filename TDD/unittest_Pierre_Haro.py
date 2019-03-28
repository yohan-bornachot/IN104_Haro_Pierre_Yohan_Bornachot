import program_classes
import unittest
import os
os.chdir("C:/IN104_Haro_Pierre_Yohan_Bornachot/TDD")

class KnownMedia(unittest.TestCase):

	Movie_list = [Movie('Les aventures de l\'in104','P.Haro','22/03/2019','800',['Thibaut','Théo']),Movie('TOP GUN','Jean-Luc','22/03/1996','121',['Jules','Bruno'])]


	def test_Order_Duration(self):
		"""Order_Duration shoul give movies in descending order"""
		result = program_classes.Order_Duration(self.Movie_list)
		nb_movies = len(result)
		for i in nb_movies:
			self.assertEqual(result[i], ordered_movies[i])

	def test_create_from_file(self):
		"""verify if create_from_file actually generate movies from a file"""

		file1 = open("test_file_from.txt","r")
		content = file1.readlines()
		file1.close()

		New_movie_list = []
		for movie in content:
			movie_description = movie.split(';')
			Film=Movie(movie_description[0],movie_description[1],movie_description[2],movie_description[3],movie_description[4])
			New_movie_list.append(Film)
		self.assertEqual(New_movie_list[0],Movie_list[0])
		self.assertEqual(New_movie_list[1],Movie_list[1])


	def test_export_to_file(self):
		file1 = open("test_file_to.txt","w")
		for movie in Movie_list:
			file1.write(movie.name+';'movie.author+';'movie.release_date+';'movie.duration+';'movie.actors+'\n')
		file1.close()

		file1 = open("test_file_to.txt","r")
		content = file1.readlines()
		file1.close()

		New_movie_list = []
		for movie in content:
			movie_description = movie.split(';')
			Film=Movie(movie_description[0],movie_description[1],movie_description[2],movie_description[3],movie_description[4])
			New_movie_list.append(Film)
		self.assertEqual(New_movie_list[0],Movie_list[0])
		self.assertEqual(New_movie_list[1],Movie_list[1])


	def test_get_duration_converted(self):
		Film = Movie('Les aventures de l\'in104','P.Haro','22/03/2019','121',['Thibaut','Théo'])
		Duration = int(Film.duration)
		minutes = Duration%60
		Hours = Duration//60
		Days = Hours//24
		Hours = Hours%24
		self.assertEqual(str(Days)+' days ' + str(Hours) + ' Hours ' + str(minutes) +' minutes', '0 days 2 Hours 1 minutes')


if __name__ = '__main__':
	unittest.main()