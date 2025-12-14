# calculates how many seats are available
# calculates how many seats are booked
# informs what the status of a seat is in a given row and given place (available or booked)

# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   rows = len(seats)
   columns = len(seats[0])
   return rows * columns

def seats_available(seats):
   avaliable = 0
   for row in seats:
      for seat in row:
         if seat == 'A':
            avaliable += 1
   return avaliable

def seats_booked(seats):
   booked = 0
   for row in seats:
      for seat in row:
         if seat == 'B':
            booked += 1
   return booked

def seat_status(seats, row, place):
   status = seats[row - 1][place - 1]

   if status == 'A':
      return 'Avaliable'
   else:
      return 'Booked'

print('CINEMA INFORMATION TABLE')
print(f'Total seats: {seats_total(cinema_seats)}')
print(f'Seats available: {seats_available(cinema_seats)}')
print(f'Seats booked: {seats_booked(cinema_seats)}')
print(f'Seat in row 1, place 1: {seat_status(cinema_seats, 1, 1)}')
print(f'Seat in row 5, place 5: {seat_status(cinema_seats, 5, 5)}')
print(f'Seat in row 3, place 5: {seat_status(cinema_seats, 3, 5)}')