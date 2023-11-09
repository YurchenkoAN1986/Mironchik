import dataclasses



    #инкапсуляция полиморфизм наследование
@dataclasses.dataclass
class Person:
    """"""
    fn:str
    ln:str
    age:int

if __name__ == '__main__':
    p:Person=Person(fn="Ivan", ln= "Ivanov", age=33)
    print(p, p.fn, p. ln)

