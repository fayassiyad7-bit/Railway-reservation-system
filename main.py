# Railway Reservation System

TOTAL_SEATS = 50
available_seats = list(range(1, TOTAL_SEATS + 1))
bookings = {}
booking_counter = 100


def check_availability():
    print("\nAvailable Seats:", len(available_seats))
    print(available_seats)


def book_ticket():
    global booking_counter

    if len(available_seats) == 0:
        print("\nNo seats available!")
        return

    name = input("Enter passenger name: ")
    age = input("Enter passenger age: ")

    seat = available_seats.pop(0)

    booking_id = f"B{booking_counter}"
    booking_counter += 1

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat
    }

    print("\nTicket Booked Successfully!")
    print("Booking ID:", booking_id)
    print("Seat Number:", seat)


def view_ticket():
    booking_id = input("Enter Booking ID: ")

    if booking_id in bookings:
        data = bookings[booking_id]

        print("\nReservation Details")
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Seat Number:", data["seat"])
    else:
        print("Booking not found!")


def cancel_ticket():
    booking_id = input("Enter Booking ID to cancel: ")

    if booking_id in bookings:
        seat = bookings[booking_id]["seat"]

        available_seats.append(seat)
        available_seats.sort()

        del bookings[booking_id]

        print("Ticket cancelled successfully!")
    else:
        print("Booking ID not found!")


def menu():
    while True:
        print("\n===== Railway Reservation System =====")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            check_availability()

        elif choice == '2':
            book_ticket()

        elif choice == '3':
            view_ticket()

        elif choice == '4':
            cancel_ticket()

        elif choice == '5':
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


menu()
