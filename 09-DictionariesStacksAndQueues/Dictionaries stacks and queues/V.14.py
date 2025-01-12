import queue

order = queue.Queue()

while True:
   print('1. Add ticket')
   print('2. Serve custoner')
   print('0. Quit')
   menu = input('Select an option: ')
   
   
   if menu == '1':
        name = input('Enter name: ')
        order.put(name)
   

   elif menu == "2":
      if order.empty() == False:
         serve = order.get()
         print(f'File {serve} is currently being served. Please wait!')
      else:
         print("No customer in the queue")

   elif menu == '0':
      break