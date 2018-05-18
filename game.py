from battle import soldier
from battle import vehicle


if __name__ == "__main__":

    sold = soldier.Soldier(100, 55, 10)
    print("Health : " + str(sold.health))
    print("Attack : " + str(sold.attack()))
    print("Damage : " + str(sold.damage()))
    # print("Name : " + sold.__class__.__name__ + "_" + str(sold.get_id()))
    print(sold)
    print("Exp : " + str(sold.experience))
    sold.add_experience()
    print("Exp : " + str(sold.experience))
    print("Name : " + str(sold.get_id()))

    sold_1 = soldier.Soldier(100, 55, 10)

    print("Health : " + str(sold_1.health))
    print("Attack : " + str(sold_1.attack()))
    print("Damage : " + str(sold_1.damage()))
    print("Name : " + sold_1.__class__.__name__ + "_" + str(sold_1.get_id()))
    
    print( sold_1)

    print("Name : " + str(sold_1.get_id()))

    veh1 = vehicle.Vehicle(100, 1001, soldier.Soldier(100, 55, 10), soldier.Soldier(100, 55, 10))
    print("Operators count : " + str(len(veh1.operators)))
    print(veh1.operators[1])
    print(veh1.operators)
    print(veh1.name)
    
