class Booking:
    def __init__(self, name, seat_no, pickup, destination):
        self.name = name
        self.seat_no = seat_no
        self.pickup = pickup
        self.destination = destination


class BusBookingSystem:
    def __init__(self):
        self.bookings = []

    def book_seat(self):
        name = input("Enter your name: ")
        seat_no = int(input("Enter Your Seat Number: "))
        pickup = input("Enter Your Pickup Point: ")
        destination = input("Enter your Destination: ")

        new_booking = Booking(name, seat_no, pickup, destination)
        self.bookings.append(new_booking)
        print("Seat booked successfully.")

    def view_reservation(self):
        if not self.bookings:
            print("No reservations made yet.")
            return

        print("All reservations:")
        print("Seat No.   Name   Pickup    Destination")
        for booking in self.bookings:
            print(f"{booking.seat_no}   {booking.name}   {booking.pickup}   {booking.destination}")

    def edit_reservation(self):
        seat_to_edit = int(input("Enter seat number to edit: "))
        found = False
        for booking in self.bookings:
            if booking.seat_no == seat_to_edit:
                booking.name = input("Enter New Name: ")
                booking.pickup = input("Enter New Pickup: ")
                booking.destination = input("Enter your new Destination: ")

                print("Reservation edited successfully.")
                found = True
                break
        if not found:
            print("Reservation not found.")

    def print_ticket(self):
        seat_no = int(input("Enter seat number to print ticket: "))
        found = False
        for booking in self.bookings:
            if booking.seat_no == seat_no:
                print("\n--- Ticket ---")
                print(f"Name: {booking.name}")
                print(f"Seat No.: {booking.seat_no}")
                print(f"Pickup: {booking.pickup}")
                print(f"Destination: {booking.destination}")
                print("----------------\n")
                found = True
                break
        if not found:
            print("No ticket found for the given seat number.")


def main():
    system = BusBookingSystem()
    choice = 0

    while choice != 5:
        print("\nMini Bus Booking System")
        print("1. Book a Seat")
        print("2. View Reservation")
        print("3. Edit a Reservation")
        print("4. Print Ticket")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            system.book_seat()
        elif choice == 2:
            system.view_reservation()
        elif choice == 3:
            system.edit_reservation()
        elif choice == 4:
            system.print_ticket()
        elif choice == 5:
            print("Exiting...")
        else:
            print("Invalid choice. Please enter a valid choice.")


if __name__ == "__main__":
    main()
