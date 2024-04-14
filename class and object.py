class slime:
    def __init__(self, n, s, w, c):
        self.name = n
        self.size = s
        self.weight = w
        self.color = c
    def privetstvije(self):
        print("Здравствуйте, меня зовут",self.name,', я',self.color,'цвета')
        print('мой вес',self.weight,',мой размер',self.size)
    def ispugatsya(self,size_vs):
        if size_vs > self.size:
            print(self.name,'испугался!!!!')
q=slime('анатолий',10,'120 грамм','rainbow')
q.privetstvije()
q2=slime('Игорь',20,'200 грамм','фиолетового')
q2.privetstvije()
q.ispugatsya(q2.size)
q2.ispugatsya(q.size)
