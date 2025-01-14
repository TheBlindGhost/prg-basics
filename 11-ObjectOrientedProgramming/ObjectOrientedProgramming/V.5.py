import termometer
import random

def main():
    temp = termometer.termometer()
    t = random.randint(30,48)

    temp.turn_on()
    temp.measure(t)
    temp.show_resault()
    temp.turn_off()


if __name__ == "__main__":
    main()