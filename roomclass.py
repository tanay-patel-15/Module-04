# create a class hotelroom with attributes room number, number of occupnats and rate

class hotelRoom:
  def __init__(self, roomNo, roomType, rate, smokingroom):
    self.__roomNo = roomNo
    self.__roomType = roomType
    self.__rate = rate
    self.__smokingroom = smokingroom



  def get_roomNo(self):
    return self.__roomNo
  
  def get_roomType(self):
    return self.__roomType
  
  def get_rate(self):
    return self.__rate
  
  def get_smokingroom(self):
    return self.__smokingroom
  
  def set_smoking(self, smokingroom):
    self.__smokingroom = smokingroom

  def set_rate(self, rate):
    self.__rate = rate

  def __eq__(self, other):
    return ((self.get_roomNo() == other.get_roomNo()) and (self.get_roomType() == other.get_roomType()))

  def __str__(self):
    smoking_status = "Smoking" if self.__smokingroom else "Non-Smoking"
    return f"{self.get_roomNo()} is a {self.get_roomType()} {smoking_status} room and the rate for that room is ${self.get_rate():.2f}/night"
  