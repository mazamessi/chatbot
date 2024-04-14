class NPS:
    def __init__(self, n, h, hp, w, c):
        self.name = n
        self.hight = h
        self.hp = hp
        self.work = w
        self.product=c
    def privetstvije(self):
        print("Здравствуйте, меня зовут",self.name,', я',self.hight,'роста')
        print('У  меня ',self.hp,"здоровья",'моя работа:',self.work,"купите у меня",self.product,"за недорого")
    def proshanja(self):
        print("До свидания от всех нас")
    def servis(self):
        print("купите у меня ",self.product)
q=NPS('Анатолий',170,'Сибирское','продавец,',"хлеб")
q.privetstvije()
q2=NPS('Игорь',150,'Таджикское','мясник,',"говядину")
q2.privetstvije()
q3=NPS('Кирилл',190,'Русское','булочник,',"булочку")
q3.privetstvije()
q.proshanja()
