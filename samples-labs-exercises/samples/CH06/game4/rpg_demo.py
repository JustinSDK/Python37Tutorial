from rpg import Role, SwordsMan, Magician

def draw_fight(role: Role):
    print(role, end = '')
    role.fight()

swordsman = SwordsMan('Justin', 1, 200)
draw_fight(swordsman)

magician = Magician('Monica', 1, 100)
draw_fight(magician)
