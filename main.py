
import random
import matplotlib.pyplot as plt

random.seed(100)

casino_start_money = 0
roulette_zero_chance = 0.2
roulette_red_chance = 0.4
roulette_black_chance = 0.4
work_time = 1000
new_customer_probability = 0.01
max_money = 10000
max_attempts = 1000


class Gamer:

    def __init__(self, name, money, risk, attempts, start):
        self.name = name
        self.money = money
        self.risk = risk
        self.attempts = attempts
        self.start = start
        self.gamer_money_history = list()
        self.bet = ""
        self.bet_money = 0

    def make_bet(self):
        self.bet = "red" if random.random() < 0.5 else "black"
        self.bet_money = round(random.random() * self.risk * self.money)

    def tell_me_about(self):
        print("=== Gamer === ", self.name)
        print("money = ", self.money)
        print("risk = ", self.risk)
        print("attempts = ", self.attempts)
        print("bet = ", self.bet)
        print("bet_money = ", self.bet_money)


class Casino:

    def __init__(self, money):
        self.money = money
        self.casino_money_history = list()

    def roulette_spin(self):
        rand = random.random()
        if rand < roulette_zero_chance:
            return "zero"
        if rand < roulette_zero_chance + roulette_red_chance:
            return "red"
        return "black"


gamer_list = list()
casino = Casino(casino_start_money)
gamer_n = 0

for _ in range(0, work_time):
    # New gamer is coming
    if random.random() < new_customer_probability:
        gamer_n += 1
        gamer_list.append(
            Gamer(gamer_n, random.randint(1, max_money), random.random(), random.randint(1, max_attempts), _))
    # Bets
    for gamer in gamer_list:
        gamer.make_bet()
    # Bets are made, no more bets
    roulette_color = casino.roulette_spin()
    for gamer in gamer_list:
        if _ < gamer.attempts + gamer.start:
            gamer.money = gamer.money + gamer.bet_money if gamer.bet == roulette_color else gamer.money - gamer.bet_money
            gamer.gamer_money_history.append(gamer.money)
            casino.money = casino.money - gamer.bet_money if gamer.bet == roulette_color else casino.money + gamer.bet_money

    casino.casino_money_history.append(casino.money)

plt.figure(figsize=(9, 9))
plt.plot(range(0, work_time), casino.casino_money_history, label="Casino")
plt.xlabel('Spin')
plt.ylabel('Money')
plt.legend()
plt.suptitle("Casino Money. Chances: Zero = " + str(roulette_zero_chance) + "  Red = " + str(roulette_red_chance) + \
             "  Black =" + str(roulette_black_chance))
plt.show()

for gamer in gamer_list:
    last_attempt = gamer.start + gamer.attempts if gamer.start + gamer.attempts < work_time else work_time
    plt.plot(range(gamer.start, last_attempt), gamer.gamer_money_history)
plt.xlabel('Spin')
plt.ylabel('Money')
plt.suptitle("Gamers Money. Chances: Zero = " + str(roulette_zero_chance) + "  Red = " + str(roulette_red_chance) + \
             "  Black =" + str(roulette_black_chance))
plt.show()
