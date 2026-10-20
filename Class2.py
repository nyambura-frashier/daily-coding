class  Students:
  school_name="Kenyataa University"

  def __init__(self,name,reg_no):
    self.name=name
    self.reg_no=reg_no

  def introduce (self):
    return f"hey,, I am {self.name} {self.reg_no}"

brian=Students("brian","sct211")
print (brian.introduce())




