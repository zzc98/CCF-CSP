class Person:
    def __init__(self, position, attack_value, health_value):
        self.position = position
        self.attack = attack_value
        self.health = health_value


def main():
    First = [Person(0, 0, 30)]
    Second = [Person(0, 0, 30)]
    flag = 0
    n = int(input())
    for _ in range(n):
        string = input().split()
        if string[0] == 'end':  # 交换
            if flag == 0:
                flag = 1
            else:
                flag = 0
        elif string[0] == 'summon':  # 召唤
            po = int(string[1])
            p = Person(po, int(string[2]), int(string[3]))
            if flag == 0:
                First.insert(po, p)
            else:
                Second.insert(po, p)
        else:  # 攻击
            i, j = int(string[1]), int(string[2])
            if flag == 0:
                attacker, defender = First[i], Second[j]
                attacker.health -= defender.attack
                defender.health -= attacker.attack
                if attacker.health <= 0:
                    First.remove(attacker)
                if defender.health <= 0 and j != 0:
                    Second.remove(defender)
            else:
                attacker, defender = Second[i], First[j]
                attacker.health -= defender.attack
                defender.health -= attacker.attack
                if attacker.health <= 0:
                    Second.remove(attacker)
                if defender.health <= 0 and j != 0:
                    First.remove(defender)

    # 输出
    win = 0
    first_hero = First.pop(0)
    if first_hero.health <= 0:
        win = -1
    second_hero = Second.pop(0)
    if second_hero.health <= 0:
        win = 1
    print(win)
    print(first_hero.health)
    print(len(First), end=' ')
    for h in First:
        print(h.health, end=' ')
    print()
    print(second_hero.health)
    print(len(Second), end=' ')
    for h in Second:
        print(h.health, end=' ')
    print()


if __name__ == "__main__":
    main()
