# Define a class named 'hotelRoom'
class hotelRoom:
    # Define the constructor method for the 'hotelRoom' class
    def __init__(self,roomNo, roomType, rate, smokingroom):
        # Initialize the instance variables
        self.__roomNo = roomNo
        self.__roomType = roomType
        self.__rate = rate
        self.__smokingroom = smokingroom

    # Define the getter method for the 'roomNo' instance variable
    def get_roomNo(self):
        return self.__roomNo

    # Define the getter method for the 'roomType' instance variable
    def get_roomType(self):
        return self.__roomType

    # Define the getter method for the 'rate' instance variable
    def get_rate(self):
        return self.__rate

    # Define the getter method for the 'smokingroom' instance variable
    def get_smokingroom(self):
        return self.__smokingroom

    # Define the setter method for the 'smokingroom' instance variable
    def set_smoking(self, smokingroom):
        self.__smokingroom = smokingroom

    # Define the setter method for the 'rate' instance variable
    def set_rate(self, rate):
        self.__rate = rate

    # Define the magic method for comparing two 'hotelRoom' objects
    def __eq__(self, other):
        # Compare the 'roomNo' and 'roomType' instance variables of the current object and the 'other' object
        return ((self.get_roomNo() == other.get_roomNo()) and (self.get_roomType() == other.get_roomType()))

    # Define the magic method for converting a 'hotelRoom' object to a string
    def __str__(self):
        # Determine the smoking status of the room
        smoking_status = "Smoking" if self.__smokingroom else "Non-Smoking"
        # Return a string representation of the 'hotelRoom' object
        return f"{self.get_roomNo()} is a {self.get_roomType()} {smoking_status} room and the rate for that room is ${self.get_rate():.2f}/night"