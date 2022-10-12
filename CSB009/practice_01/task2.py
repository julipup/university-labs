# Write a program for selling tickets to IT-events.
# Each ticket has a unique number and a price. There
# are four types of tickets: regular ticket,
# advance ticket (purchased 60 or more days before the event),
# late ticket (purchased fewer than 10 days before the
# event) and student ticket.
#
# Additional information:
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
#
# All tickets must have the following properties:
# -the ability to construct a ticket by number;
# -the ability to ask for a ticket’s price;
# -the ability to print a ticket as a String.

# Ticket types:
# 1 - Regular ticket
# 2 - Advance ticket
# 3 - Late ticket
# 4 - Student ticket

class Ticket:
    # Class variables
    last_id = 0
    issued_tickets = []

    # Regular ticket price
    base_price = 100

    # format: Tuple[ticket type, discount (+/- int%)]
    discounts = [
        (2, -40),
        (3, +10),
        (4, -50),
    ]

    def __init__(self, ticket_type: int):
        if not 1 <= ticket_type <= 4:
            raise ValueError("Unknown ticket type:", ticket_type)

        # Updating class variables
        Ticket.last_id += 1
        Ticket.issued_tickets.append(self)

        # Saving this ticket's information
        self.__id = Ticket.last_id
        self.__type = ticket_type
        self.__base_price = Ticket.base_price

        # Applied discounts
        self.__applied_discounts: list[int] = list(
            map(
                lambda d: d[1],
                filter(lambda d: d[0] == self.__type, Ticket.discounts)
            )
        )

    # Properties
    @property
    def id(self):
        return self.__id

    @property
    def type(self):
        return self.__type

    @property
    def price(self):
        price = self.__base_price

        # Applying discounts
        for discount in self.__applied_discounts:
            if discount < 0:
                price *= -discount / 100
            else:
                price += price * (discount / 100)

        return price if price > 0 else 0

    def __str__(self):
        return f'Ticket ( id: { self.__id }, type: { self.__type }, applied_discounts: { self.__applied_discounts }, ' \
               f'price: { self.price } ) '


# Tests
regular_ticket = Ticket(1)
advance_ticket = Ticket(2)
late_ticket = Ticket(3)
student_ticket = Ticket(4)

print("Regular ticket:", regular_ticket)
print("Advance ticket:", advance_ticket)
print("Late ticket:", late_ticket)
print("Student ticket:", student_ticket)