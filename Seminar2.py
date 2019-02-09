class Myclass:
    x = 2
    c = 3
    d = 5
    def print_xcd(self):
        print("x=",self.x)
        print("y=",self.c)
        print("d=",self.d)
if __name__ =="__main__":
    p = Myclass()
    p.print_xcd()
    print(p.x,p.c,p.d)
