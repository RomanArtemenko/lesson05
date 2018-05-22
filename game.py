from battle import unit
from battle import soldier
from battle import vehicle
from battle import clock
from battle import squad


if __name__ == "__main__":

    sold = soldier.Soldier("Ivan", clock.Clock(1), 100, 55, 10)
    print("Health : " + str(sold.health))
    print("Attack : " + str(sold.attack))
    print("Damage : " + str(sold.damage))
    # print("Name : " + sold.__class__.__name__ + "_" + str(sold.get_id()))
    print(sold)
    print("Exp : " + str(sold.experience))
    # sold.add_experience()
  
    sold_1 = soldier.Soldier("Roman", clock.Clock(1), 100, 55, 10)

    print("Health : " + str(sold_1.health))
    sold_1.take_damage(5)
    print("Health : " + str(sold_1.health))
    sold_1.health = 66
    print("Health : " + str(sold_1.health))
    print("Attack : " + str(sold_1.attack))
    print("Damage : " + str(sold_1.damage))

    print( sold_1)

    veh1 = vehicle.Vehicle("Tank", clock.Clock(1), 100, 1001, 
    [soldier.Soldier("Ivan_1", clock.Clock(1), 0, 55, 10),
                           soldier.Soldier("Petya_2", clock.Clock(1), 10, 55, 10)])
    print("Operators count : " + str(len(veh1.operators)))
    # print(veh1.operators[1])
    # print(str(veh1.operators[1].attack))
    print(veh1.operators)
    print("Attack : " + str(veh1.attack))

    for op in veh1.operators:
        if op.active:
            print("%s is active" % op)
        else:
            print("%s is dead" % op)
    
    if veh1.operators_active:
        print("Operaotrs is ative")
    else:
        print("Operaotrs is dead")

    if veh1.active:
        print("Vahl is active")
    else:
        print("Vehl is dead")
    print("%s active is : %s" % (veh1, veh1.active))
    # print("Is active + " + str(veh1.active)) 
    print(veh1)

    squad1 = squad.Squad([vehicle.Vehicle("Tank", clock.Clock(1), 100, 1001, 
    [soldier.Soldier("Ivan_1", clock.Clock(1), 0, 55, 10),
                           soldier.Soldier("Petya_2", clock.Clock(1), 10, 55, 10)]),
                           soldier.Soldier("Roman", clock.Clock(1), 100, 55, 10)])
    
    print("Attack : " + str(squad1.attack))
    print("Damage : " + str(squad1.damage))