# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
      self.channel = 1
      self.available_channels = []
      self.volume = 0
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
   def set_channel(self, new_channel_no):
      self.channel = new_channel_no
   def set_channels(self, channels_list):
      self.available_channels.append(channels_list)
   def show_channels(self):
      print(self.available_channels) 
   def volume_up(self):
      if self.volume < 10:
         self.volume += 1
   def volume_down(self):
      if self.volume  > 0:
         self.volume -= 1
   def show_status(self):
      if self.is_on == True:
        if len(self.available_channels)>0 and self.channel <= len(self.available_channels[0]): 
           print(f"The TV is ON, channel {self.channel} ", end = '')
           print(self.available_channels[0][self.channel-1])
        else:
           print(f"The TV is ON, channel {self.channel} ")
        print(f"Volume: {self.volume}")
      else:
        print("The TV is OFF.")