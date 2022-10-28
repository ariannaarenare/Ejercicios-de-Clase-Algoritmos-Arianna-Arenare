from caballo import Horse
from valida import Valid
from race import Race

def main():
    print ("WELCOME TO DERBY OF KENTUCKY")
    valids = int(input ("Please enter how many valids will we have: "))
    races = int(input ("How many races will we have in each valid: "))
    
    horse1 = Horse("El Rayo Veloz", 1)
    horse2 = Horse("Gustavo", 2)
    horse3 = Horse("El Caballo Maravilla", 3)
    horse4 = Horse("Superman", 4)
    horse5 = Horse("Caballo Random", 5)
    horse6 = Horse("El más crack", 6)
    
    for valid in range (valids):
        race_list = []
        horse_list = [horse1, horse2, horse3, horse4, horse5, horse6]
        for  race in range (races):
            race_list.append(Race (race, horse_list))
        for race in race_list:
            race.start_race()
            race.choose_winner()



main()