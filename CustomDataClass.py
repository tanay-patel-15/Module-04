# Importing necessary modules
from colorama import Fore
from roomclass import hotelRoom  # Assuming roomclass module contains the definition of hotelRoom class

# Main function
if __name__ == "__main__":
    
    # Creating instances of hotelRoom class

    Room129 = hotelRoom(129, "BNK", 109.00, True)  # Creating Room129 object
    Room325 = hotelRoom(325, "SNK", 159.00, True)  # Creating Room325 object

    # Printing cyan text for visual separation
    print(Fore.CYAN + "\n")
    

    # Printing information of Room129 and Room325

    print(Room129)  # Printing Room129 object
    print(Room325, "\n\n", Fore.RESET)  # Printing Room325 object


    # Modifying attributes of Room325

    Room325.set_rate(149.99)  # Setting new rate for Room325
    Room129.set_smoking(False)  # Setting smoking status for Room129 as False


    # Printing yellow text for visual separation
    print(Fore.YELLOW)
    

    # Printing updated information of Room129 and Room325
    
    print(Room129)  # Printing updated Room129 object
    print(Room325, "\n\n", Fore.RESET)  # Printing updated Room325 object
