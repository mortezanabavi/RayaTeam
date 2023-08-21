
class circle:
    def __init__(self, Shoa):
        self.Shoa = Shoa
    def Mohit(self):
        return self.Shoa * self.Shoa * 3.14
    def Masahat(self):
        return (self.Shoa + self.Shoa) * 3.14


Shoa = circle(int(input("Enter Shoa : ")))
print("Masahat :", Shoa.Masahat(),", Mohit :", Shoa.Mohit())