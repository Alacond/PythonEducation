class Programmer:
    
    wage = {
        'Junior': 10,
        'Middle': 15,
        'Senior': 20,
    }

    ranks = [key for key in wage.keys()]

    def __init__(self, name, position, bonus=0, work_time=0, salary=0):
        self.name = name
        self.position = position
        self.bonus = bonus
        self.work_time = work_time
        self.salary = salary

    def work(self, time):
        self.work_time += time
        self.salary += (self.wage[self.position] + self.bonus) * time
    
    def rise(self):
        if self.position != self.ranks[-1]:
            index = self.ranks.index(self.position)
            self.position = self.ranks[index + 1]
        else:
            self.bonus += 1

    def info(self):
        return f"{self.name} {self.work_time}ч. {self.salary}тгр."


if __name__ == "__main__":
    programmer = Programmer('Васильев Иван', 'Junior')
    programmer.work(750)
    print(programmer.info())
    programmer.rise()
    programmer.work(500)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())