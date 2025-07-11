class Movie:
    def __init__(self,title: str,genre: str,duration: float,rating: float):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating
        
    def show_summary(self):
        print(f"{self.title} - {self.genre} janridagi film.Reyting: {self.rating}/10")
        return
    
kino01 = Movie("Inception","fantastika",2,8.8)
kino01.show_summary()