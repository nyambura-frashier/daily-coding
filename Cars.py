class Cars:
  car_name="The menace"
  
  def __init__(self,name,plate):
    self.name=name
    self.plate=plate

  def introduce(self):
      print(f"Name of car is {self.name}")
      print(f"The plate number is {self.plate}")

  
car1=Cars("BMW","KDE")
car2=Cars("Toyotta","KCD")

car1.introduce()
car2.introduce()