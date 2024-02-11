from colorama import Fore
from roomclass import hotelRoom

if  __name__ == "__main__":
  Room129 = hotelRoom(129, "BNK", 109.00, True)
  Room325 = hotelRoom(325, "SNK", 159.00, True)  
  
  print(Fore.CYAN + "\n")
  print(Room129)
  print(Room325, "\n\n", Fore.RESET)

  Room325.set_rate(149.99)
  Room129.set_smoking(False)

  print(Fore.YELLOW)
  print(Room129)
  print(Room325, "\n\n", Fore.RESET)








