class Human:
  def __init__(self,name,occupation):#__init__ going to initialise the properties of that class(Constructor)
    self.name=name#self.name(property of that class)
    self.occupation=occupation
#whenever we do any method the first argument is self
  def do_work(self):
    if self.occupation == "tennis player":
      print(self.name,"plays tennis")
    elif self.occupation == "actor":
      print(self.name,"shoots film")
  def speaks(self):
    print(self.name,"Says how are you?")

#creating object
tom = Human("tom cruise","actor")
tom.do_work()
tom.speaks()
sindhu= Human("Pv Sindhu","tennis player")
sindhu.do_work()
  