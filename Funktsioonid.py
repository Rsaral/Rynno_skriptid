def welcome():
    """"" Väljastab staatilise tervitusteksti """""
    print('Tere, kuidas läheb?')

def welcome_name(name):
    """"Tagastab tervitussõnumi koos nimega."""
    return f'Tere, {name}!'

def division(number1, number2):
    """
    Teostab kahe arvu jagamist.

    Args:
        number1 (float): Jagatav arv
        number2 (float): Jagaja (ei tohi olla null)

    Returns:
        float: jJagatise väärtus
    """
    if number2 !=0:
        return number1 / number2
    return -1

def introduce(name, age=35):
    """
    Loob lihtsa tutvustava lause.
    
    :param name: Isiku nimi
    :type name: str
    :param age: Isiku vanus (vaikimisi 25)
    :type age: int, valikuline
    :return: Tekstilise tutvustusvormis
             'Tema on <nimi> ja ta on <vanus> aastane!
    :rtype: str
    """
    return f'Tema on {name} ja ta on {age} aastane!'

welcome()

print(welcome_name('Rünno'))

kukimuki = welcome_name('Kukimuki')
print(kukimuki)

a = 10
b = 5 
print(division(a, b))
print(division(b, 0))
print(division(b, a))
print(division(0, b))

print(introduce('Rünno'))
print(introduce('Juhan', 34))
print(introduce(1234, 5432))

"""
Ülesanne: loo list viie nimega. Väljasta tervitus viie nime kohta. 
"""
names = ["Mari", "Jüri", "Kalle", "Madis", "Liisa"]

for name in names:
    print(welcome_name(name))
