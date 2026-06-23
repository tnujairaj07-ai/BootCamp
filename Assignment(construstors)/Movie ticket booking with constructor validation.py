class Ticket:
    def __init__(self, movie, seats_available, seats_requested):
        self.movie = movie
        self.seats_available = seats_available
        self.seats_requested = seats_requested

        self.confirmed_seats = min(seats_available, seats_requested)

        if seats_requested <= seats_available:
            self.message = "Full request confirmed."
        else:
            self.message = f"Only {self.confirmed_seats} seat(s) could be confirmed."

    def show_details(self):
        print("Movie:", self.movie)
        print("Seats Available:", self.seats_available)
        print("Seats Requested:", self.seats_requested)
        print("Confirmed Seats:", self.confirmed_seats)
        print("Status:", self.message)
        print()

ticket1 = Ticket("Avengers", 50, 20)    
ticket2 = Ticket("Interstellar", 30, 30) 
ticket3 = Ticket("Batman", 10, 15)      

ticket1.show_details()
ticket2.show_details()
ticket3.show_details()

