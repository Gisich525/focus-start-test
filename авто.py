class Car:
    def __init__(self, brand = None, model = None, body_type = None, year = None, from_line = None):
        if from_line is None:
            self.brand = brand
            self.model = model
            self.body_type = body_type
            self.year = year
        else:
            self.brand, self.model, self.body_type, self.year = str(from_line).split(" ")

    def __str__(self):
        return '\nАвтомобиль {} {} {} {} года выпуска\n'.format(self.brand, self.model, self.body_type, self.year)

class Storage:
    def get_default_cars(self):
        list = []
        list.append(Car('Honda', 'Civic', 'hatchback', '2005'))
        list.append(Car('Toyota', 'Camry', 'sedan', '2001'))
        list.append(Car('Honda', 'Accord', 'sedan', '2010'))
        return(list)
       
    def chek_storage(self):
        try:
            f = open('data.txt', 'r')
            print('Cars from file')
        except:
            print('Default cars')
            f = open('data.txt', 'w')
            for car in self.get_default_cars():
                self.add_car(car)
                
    def __init__(self):
        self.chek_storage()                    
                
    def find_inf_about_car(self, inf_car):
        f = open('data.txt', 'r')
        for line in f.readlines():
            car = Car(from_line = line.rstrip('\n'))
            if (car.brand, car.model) == (inf_car.brand, inf_car.model):
                return(car)
            
    def find_certain_car(self, car):
        f = open('data.txt', 'r')
        lines = f.readlines()
        for line in f.readlines():
            found_car = Car(from_line = line.rstrip('\n'))
            if (car.brand, car.model, car.body_type, car.year) == (found_car.brand, found_car.model, found_car.body_type, found_car.year):
                return(car)       

    def add_car(self, car):
        if self.find_certain_car(car) is None:
            f = open('data.txt', 'a')
            f.write('{brand} {model} {body_type} {year}\n'.format(brand = car.brand, model= car.model, body_type= car.body_type, year= car.year))
            print('\nАвтомобиль {brand} {model} {body_type} {year} успешно добавлен\n'.format(brand = car.brand, model= car.model, body_type= car.body_type, year= car.year)) 
            f.close()
        else:
            print('Данный автомобиль уже есть')
         
    def delete_car(self, del_car):
        list = []
        f = open('data.txt', 'r')
        for line in f.readlines():
            car = Car(from_line = line.rstrip('\n'))  
            if (car.brand, car.model, car.body_type, car.year) != (del_car.brand, del_car.model, del_car.body_type, del_car.year):
                list.append(line)
            else:    
                print('\nАвтомобиль {brand} {model} {body_type} {year} успешно удален\n'.format(brand = del_car.brand, model =del_car.model, body_type = del_car.body_type, year = del_car.year ))
        f = open('data.txt', 'w')
        f.write(''.join(list))
        f.close()

    def show_all_cars(self):
        f = open('data.txt', 'r')
        for line in f.readlines():
            car = Car(from_line = line.rstrip('\n'))
            print(car)
            
    def edit(self, inf_car, edit_car):
        f = open('data.txt', 'r')
        for line in f.readlines():
            car = Car(from_line = line.rstrip('\n'))
            if (car.brand, car.model) == (inf_car.brand, inf_car.model):
                car.body_type = edit_car.body_type
                car.year = edit_car.year
                return(car)

def choice():
    selector = None
    try:
        selector = int(input('Введите "1" если хотите посмотреть сведения об автомобиле\n' + \
                             'Введите "2" если хотите добавить новый автомобиль\n' + \
                             'Введите "3" если хотите удалить автомобиль\n' + \
                             'Введите "4" если хотите просмотреть весь перечень автомобилей\n' + \
                             'Введите "5" если хотите редактировать сведения об автомобиле\n' + \
                             
                             'Ввести здесь ------->:'))
    except ValueError:
        print('\n\nНе корректный ввод!!!\n')
        print('Необходимо ввести целое число!!!\n\n')
    return selector

c = Storage()
while True:
    selector = choice()
    if selector == 1:
        inf_car = Car(brand = input('Для поиска автомобиля введите производителя: '),
                      model = input('Для поиска автомобиля введите модель: '))
        print(c.find_inf_about_car(inf_car))        
    elif selector == 2:
        new_car = Car(brand = input('Для добавления автомобиля введите производителя: '),
                      model = input('Для добавления автомобиля введите модель: '),
                      body_type = input('Для добавления автомобиля введите тип кузова: '),
                      year = input('Для добавления автомобиля введите год выпуска: '))
        c.add_car(new_car)                   
    elif selector == 3:
        del_car = Car(brand = input('Для удаления автомобиля введите производителя: '),
                      model = input('Для удаления автомобиля введите модель: '),
                      body_type = input('Для удаления автомобиля введите тип кузова: '),
                      year = input('Для удаления автомобиля введите год выпуска: '))       
        c.delete_car(del_car)        
    elif selector == 4:
        c.show_all_cars()       
    elif selector == 5:
        inf_car = Car(brand = input('Для поиска автомобиля введите производителя: '),
                      model = input('Для поиска автомобиля введите модель: '))       
        edit_car = Car(body_type = input('Изменить тип кузова на: '),
                      year = input('Изменить год выпуска на: '))
        new_car = c.edit(inf_car, edit_car)
        c.delete_car(c.find_inf_about_car(inf_car))
        c.add_car(new_car)
