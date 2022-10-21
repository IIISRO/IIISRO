from operator import le
from time import sleep


class rectangle:

    def __init__(self,len,wid):
        self.len=len
        self.wid=wid


    def perimeter(self):
        l=self.len
        w=self.wid
        p=(l+w)*2
        return p

    def area(self):
        l=self.len
        w=self.wid
        a=l*w
        return a
    def display(self):
        return(f'{"="*40}\nRectangle length: {self.len}\nRectangle width: {self.wid}\nRectangle perimeter: { self.perimeter()}\nRectangle area: {self.area()}\n{"="*40}')


class prlpd(rectangle):

    def __init__(self, len, wid, hei):
        self.hei=hei
        super(self, rectangle).__init__(len,wid)

    def volume(self):
        l=self.len
        w=self.wid
        h=self.hei
        v=l*w*h
        return v


rect=rectangle(5,10)
parelpd=prlpd(5,10,4)
print(rect.display())
print(f'Parallelepipede volume: {parelpd.volume()}\n{"="*40}')
