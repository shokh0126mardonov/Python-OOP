class Movie:
    def __init__(self,title: str , genre: str , duration: float , rating: float):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

kino1 = Movie("Sehrgar","Fantastika",65,9.5)

print(kino1.title)
print(kino1.genre)
print(kino1.duration)
print(kino1.rating)