class Yty:
    def __init__(self, list_: list) -> None:
        self.list_ = list_
        self.lst_end = []

    def decomp(self, lst) -> None:
        if isinstance(lst, list):
            for i in lst:
                if not isinstance(i, list):
                    self.lst_end.append(i)
                else:
                    Yty.decomp(self, i)

    def process(self):
        for i in self.list_:
            if isinstance(i, list):
                Yty.decomp(self, i)
            else:
                self.lst_end.append(i)
        return self.lst_end
            
    def display(self) -> None:
        print('lst-end: ' + str(self.lst_end))


'''
Exemple        
x = [1, [2, 3], 4, [5, 6, [7, 8, [9, 10]]]]

lst = Yty(x)  

for i in lst.process():
    print(i)

>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
>>> 6
>>> 7
>>> 8
>>> 9
>>> 10

'''




