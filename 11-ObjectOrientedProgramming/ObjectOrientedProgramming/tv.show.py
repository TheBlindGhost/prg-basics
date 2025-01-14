# tv_show.py file
# main program
import tv

def main():
   # object creation
    tel = tv.TV()
    channels = ["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"]




   # object usage
    tel.show_status()
    tel.turn_on()
    tel.show_status()
    tel.show_channels()
    tel.set_channels(channels)
    tel.show_channels()
    tel.show_status()
    tel.set_channel(2)
    tel.volume_up()
    tel.show_status()
    tel.set_channel(10)
    tel.volume_down()
    tel.volume_down()
    tel.volume_down()
    tel.show_status()
    tel.turn_off()
    tel.show_status()

if __name__ == "__main__":
   main() 