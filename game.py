from battle import soldier
from battle import vehicle


if __name__ == "__main__":

    sold = soldier.Soldier("Ivan",100, 55, 10)
    print("Health : " + str(sold.health))
    print("Attack : " + str(sold.attack()))
    print("Damage : " + str(sold.damage()))
    # print("Name : " + sold.__class__.__name__ + "_" + str(sold.get_id()))
    print(sold)
    print("Exp : " + str(sold.experience))
    sold.add_experience()
    print("Exp : " + str(sold.experience))

    sold_1 = soldier.Soldier("Roman", 100, 55, 10)

    print("Health : " + str(sold_1.health))
    print("Attack : " + str(sold_1.attack()))
    print("Damage : " + str(sold_1.damage()))

    print( sold_1)

    veh1 = vehicle.Vehicle("Tank", 100, 1001, soldier.Soldier("Ivan_1", 100, 55, 10),
                           soldier.Soldier("Petya_2", 100, 55, 10),
                           soldier.Soldier("Petya_3", 80, 44, 15))
    print("Operators count : " + str(len(veh1.operators)))
    print(veh1.operators[1])
    print(str(veh1.operators[1].attack()))
    print(veh1.operators)
    print("Attack : " + str(veh1.attack()))
    print(veh1)
    
