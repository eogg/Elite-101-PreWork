#class imports
import random
isActive = True;
orderNum = 0;
class personsOrder:
  tableNum = 0;
  order = [];
  
  def __init__(self, orderTableNum):
    self.tableNum = orderTableNum;

  def addToOrder(self, thing):
    self.order.append(thing);

  def __str__(self):
    for item in self.order:
      return (', '.join(self.order));

  def getOrder(self, index):
    return self.order[index];

class reservationMaker:
  guestName = "";
  guestNum = 0;
  hour = 0;
  amOrPm = "A.M."
  date = ""

  def __init__(self, hourAv, amtGuests, name, dateAv):
    self.guestName = name;
    if hourAv > 12:
      self.hour = (hourAv - 12);
      self.amOrPm = "P.M.";
    self.guestNum = amtGuests;
    self.date = dateAv;

  

    
def continue_loop():
  global isActive;
  while True:
    yesOrNo = input("\nWill that be all? (y/n) ");
    if yesOrNo == "y":
      isActive = False;
      break;
    elif yesOrNo == "n":
      isActive = True;
      start_menu();
      break;
    else:
      print("That option isn't valid, please try again.")

def order_cont_loop():
  global isActive;
  while isActive:
    yesOrNo = input("\nWill that be all? (y/n) ");
    if yesOrNo == "y":
      print("\nAlright, we have " + str(guest) + " all for table number " + str(guest.tableNum) + ", it'll be right out for you. Thank you!");
      isActive = False;
    elif yesOrNo == "n":
      isActive = True;
      display_menu_options();
      break;
    else:
      print("That option isn't valid, please try again.");
def display_menu_options():
  global guest;
  print("\n---------------------------CHILI'S MENU---------------------------")
  print("\nFind everything from our Texas-Size Baby Back Ribs, \nour Big Mouth Burgers and our always sizzling, Full-on Fajitas."
    )
  tabNum = int(input("\nWhat's your table number?: "));
  guest = personsOrder(tabNum);
  print("\n1. Appetizers")
  print("2. Big Mouth Burgers")
  print("3. Ribs & Steaks")
  print("4. Lunch Specials")
  print("5. Desserts")

def display_appetizer_menu():
    print(
      "\n----------------------------APPETIZERS----------------------------")
    print(
      "\nStart your meal with one of our famous fresh-to-order appetizers \nyou know and love. Whether you're in the mood for Southwestern \nEggrolls, Skillet Queso or multiple finger foods with our \nTriple Dipper, you're sure to find something everyone will enjoy!"
    )
    print("\n1. Triple Dipper")
    print("2. Fried Mozzarella")
    print("3. Dip Trio")
    print("4. Southwestern Eggrolls")
    print("5. Skillet Queso")
    print("6. Texas Cheese Fries")

def display_Big_Mouth_Burgers_menu():
    print(
      "\n-------------------------BIG MOUTH BURGERS------------------------")
    print(
      "\nChoose a hand-crafted, made-to-order Big Mouth Burger from our \nmenu. We handsmash all our burgers to lock in flavor, then serve \nthem up on a delicious, toasted brioche bun. Served with fries \n(add 420 cal)."
    )
    print("\n1. Bacon Rancher")
    print("2. BBQ Brisket Burger")
    print("3. Chili’s Secret Sauce Burger")
    print("4. Queso Burger")
    print("5. Just Bacon Burger")
    print("6. Oldtimer® w/Cheese")

def display_Ribs_and_Steaks():
    print(
      "\n---------------------------RIBS & STEAKS--------------------------")
    print(
      "\nOur Texas-Size Baby Back Ribs are smoked in-house over pecan wood \nand slow-cooked. Our steaks are hand-trimmed, 100% USDA ribeye \n& choice sirloin. All grain-fed & optimally aged."
    )
    print("\n1. House BBQ Full Order Ribs")
    print("2. Texas Dry Rub Full Order Ribs")
    print("3. Honey-Chipotle Full Order Ribs")
    print("4. Classic Ribeye")
    print("5. 10 oz. Classic Sirloin with Avocado")

def display_Lunch_Specials():
    print(
      "\n--------------------------LUNCH SPECIALS--------------------------");
    print(
      "\nWe've got great lunch specials starting at just $9! Start off \nfresh with a salad or soup, then pick your favorite entree. \nAvailable Monday through Friday from 11 a.m. to 4 p.m. at \nparticipating locations. All lunch portions. No substitutions."
    );
    print("\n1. Lunch Combo - Double Burger");
    print("2. Lunch Combo - Spicy Shrimp Tacos");
    print("3. Lunch Combo - Half Order Bacon Ranch Chicken Quesadillas");
    print("4. Lunch Combo - Boneless Wings");
    print("5. Lunch Combo - Bacon Avocado Grilled Chicken Sandwich");
def display_desserts():
    print("\n-----------------------------DESSERTS-----------------------------");
    print("\nClassic desserts big enough to share, but too good to actually \ndo it.");
    print("\n1. Molten Chocolate Cake");
    print("2. Skillet Chocolate Chip Cookie");
    print("3. Cheesecake");

def user_selection_menu():
  print("\n--------------------------USER SELECTION--------------------------");
  print("\nWould you like to:");
  print("1. Order");
  print("2. Make a reservation");

def startOrder():
  global isActive;
  global guest;
  print("Hello, welcome to Chili's!");
  start_menu();
    
        
  
  

def menu_selection():
  global isActive;
  global orderNum;
  while isActive:
    user_choice = int(input("\nEnter the number next to your choice (1-5): "));
    if user_choice == 1:
      display_appetizer_menu();
      appetizer_selection();
      break;
    elif user_choice == 2:
      display_Big_Mouth_Burgers_menu();
      big_mouth_burgers_selection();
      break;
    elif user_choice == 3:
      display_Ribs_and_Steaks();
      ribs_n_steaks_selection();
      break;
    elif user_choice == 4:
      display_Lunch_Specials();
      lunch_specials_selection()
      break;
    elif user_choice == 5:
      display_desserts();
      desserts_selection()
      break;
    else:
      print("That's not a valid choice, please try again.");
  orderNum += 1;













def appetizer_selection():
  global isActive;
  global guest;
  global orderNum;
  while isActive:
    user_selection = int(input("\nEnter the number next to your choice (1-6): "));
    if user_selection == 1:
      print("\n---------------------------Triple Dipper--------------------------")
      print("\nWhy choose one when you can choose three? Select three appetizers \nand enjoy! Served with dipping sauces.");
      print("\n1. Crispy Chicken Crispers");
      print("2. Boneless Buffalo Wings");
      print("3. Fried Mozzarella");
      print("4. Boneless Honey-Chipotle Wings");
      print("5. Boneless House BBQ Wings");
      print("6. Buffalo Wings");
      print("7. Honey-Chipotle Wings");
      print("8. House BBQ Wings");
      print("9. Crispy Honey-Chipotle Chicken Crispers");
      print("10. Southwestern Eggrolls");
      print("11. Fried Pickles");
      print("12. Big Mouth Bites");
    
      choice = [];
      count = 1;
      while count != 4:
        uss_select = int(input("\nChoose appetizer #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Crispy Chicken Crispers");
          count+=1;
        elif uss_select == 2:
          choice.append("Boneless Buffalo Wings");
          count+=1;
        elif uss_select == 3:
          choice.append("Fried Mozzarella");
          count+=1;
        elif uss_select == 4:
          choice.append("Boneless Honey-Chipotle Wings");
          count+=1;
        elif uss_select == 5:
          choice.append("Boneless House BBQ Wings");
          count+=1;
        elif uss_select == 6:
          choice.append("Buffalo Wings");
          count+=1;
        elif uss_select == 7:
          choice.append("Honey-Chipotle Wings");
          count+=1;
        elif uss_select == 8:
          choice.append("House BBQ Wings");
          count+=1;
        elif uss_select == 9:
          choice.append("Crispy Honey-Chipotle Chicken Crispers");
          count+=1;
        elif uss_select == 10:
          choice.append("Southwestern Eggrolls");
          count+=1;
        elif uss_select == 11:
          choice.append("Fried Pickles");
          count+=1;
        elif uss_select == 12:
          choice.append("Big Mouth Bites");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Triple Dipper with " + choice[0] + ", " + choice[1] + ", and " + choice[2]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      
      break;
    elif user_selection == 2:
      print("\n-------------------------FRIED MOZZARELLA-------------------------");
      print("\nServed with Marinara sauce.");
      choice = [guest.addToOrder("Fried Mozzarella")];
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 3:
      print("\n---------------------------Dip Trio---------------------------");
      print("\nChoose any three. Skillet queso, white queso, fresh salsa, fresh guacamole or house-made ranch. Served with warm corn tostada chips.")
      print("\n1. Ranch");
      print("2. Fresh Guacamole");
      print("3. Skillet Queso");
      print("4. White Queso");
      print("5. Fresh Salsa");
      choice = [];
      count = 1;
      while count != 4:
        uss_select = int(input("\nChoose appetizer #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Ranch");
          count+=1;
        elif uss_select == 2:
          choice.append("Fresh Guacamole");
          count+=1;
        elif uss_select == 3:
          choice.append("Skillet Queso");
          count+=1;
        elif uss_select == 4:
          choice.append("White Queso");
          count+=1;
        elif uss_select == 5:
          choice.append("Fresh Salsa");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Dip Trio with " + choice[0] + " dip, " + choice[1] + " dip, and " + choice[2] + " dip");
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;

    elif user_selection == 4:
      print("\n-----------------------SOUTHWESTERN EGGROLLS----------------------");
      print("\nThese aren’t your ordinary eggrolls. Crispy flour tortillas, \nchicken, black beans, corn, jalapeño Jack cheese, red peppers, \nspinach. Served with avocado-ranch.");
      choice = [guest.addToOrder("Southwestern Eggrolls")];
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 5: 
      print("\n---------------------------SKILLET QUESO--------------------------");
      print("\nYour chip’s favorite dip for over 25 years. Original with beef. \nServed with chips & salsa.");
      choice = [guest.addToOrder("Skillet Queso")];
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 6:
      print("\n------------------------Texas Cheese Fries------------------------");
      print("\nShredded cheese, bacon, jalapeños, green onions. Served with \nhouse-made ranch.");
      print("\nYou've chosen the Texas Cheese Fries")
      break;

    
  order_cont_loop();
def big_mouth_burgers_selection():
  global isActive;
  global guest;
  global orderNum;
  while isActive:
    user_selection = int(input("\nEnter the number next to your choice (1-6): "));
    if user_selection == 1:
      print("\n---------------------------Bacon Rancher--------------------------")
      print("\nTwo beef patties, six slices of bacon, house-made ranch,\n American cheese, sauteed onions, pickles.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Bacon Rancher with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 2:
      print("\n-------------------------BBQ Brisket Burger-----------------------")
      print("\nBrisket, house BBQ, cheddar, pickles, coleslaw.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("BBQ Brisket Burger with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 3:
      print("\n---------------------Chili’s Secret Sauce Burger------------------")
      print("\nSecret sauce, American cheese, lettuce and sauteed onions.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Chili’s Secret Sauce Burger with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 4:
      print("\n-------------------------Queso Burger----------------------")
      print("\nWhite queso, crunchy tortilla strips, pico.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Queso Burger with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 5: 
      print("\n--------------------------Just Bacon Burger-----------------------")
      print("\nDon’t let the name fool you. This classic is layered with slices \nof bacon, cheddar, pickles, lettuce, red onion, tomato & mayo.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Just Bacon Burger with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 6:
      print("\n--------------------------Oldtimer® w/Cheese----------------------")
      print("The original burger. Pickles, lettuce, tomato, red onion, mustard,\ncheese.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Oldtimer® w/Cheese with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;

  order_cont_loop();
def ribs_n_steaks_selection():
  global isActive;
  global guest;
  global orderNum;
  while isActive:
    user_selection = int(input("\nEnter the number next to your choice (1-5): "));
    if user_selection == 1:
      print("\n---------------------HOUSE BBQ FULL ORDER RIBS--------------------")
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 3:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("House BBQ Full Order Ribs with sides of " + choice[0] + " and " + choice[1]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 2:
      print("\n-------------------TEXAS DRY RUB FULL ORDER RIBS------------------")
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 3:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Texas Dry Rub Full Order Ribs with sides of " + choice[0] + " and " + choice[1]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 3:
      print("\n-------------------HONEY-CHIPOTLE FULL ORDER RIBS-----------------")
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 3:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Honey-Chipotle Full Order Ribs with sides of " + choice[0] + " and " + choice[1]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 4:
      print("\n-------------------------Classic Ribeye----------------------")
      print("\nMarbled, thick-cut steak topped with garlic butter. \nServed with loaded mashed potatoes (add 350 cal), and steamed\nbroccoli (add 40 cal).")
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 3:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Classic Ribeye with sides of " + choice[0] + " and " + choice[1]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 5: 
      print("\n-----------------10 OZ. CLASSIC SIRLOIN WITH AVOCADO--------------")
      print("\nSeasoned and topped with cilantro pesto, avocado slices, \ncilantro & pico. Served with roasted asparagus.")
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 3:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("10 oz. Classic Sirloin with Avocado with sides of " + choice[0] + " and " + choice[1]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
  order_cont_loop();
def lunch_specials_selection():
  global isActive;
  global guest;
  global orderNum;
  while isActive:
    user_selection = int(input("\nEnter the number next to your choice (1-5): "));
    if user_selection == 1:
      print("\n--------------------LUNCH COMBO - DOUBLE BURGER-------------------")
      print("\nTwo grilled patties, American cheese, lettuce, tomato & mustard. \nServed with fries.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Double Burger with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 2:
      print("\n------------------LUNCH COMBO - SPICY SHRIMP TACOS----------------")
      print("\nTwo spicy chile-lime shrimp tacos in flour tortillas with pico, \ncilantro, avocado, coleslaw, queso fresco. Served with \nchips & salsa.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Spicy Shrimp Tacos with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 3:
      print("\n------LUNCH COMBO - HALF ORDER BACON RANCH CHICKEN QUESADILLAS----")
      print("\nTwo spicy chile-lime shrimp tacos in flour tortillas with pico, \ncilantro, avocado, coleslaw, queso fresco. Served with \nchips & salsa.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Half Order Bacon Ranch Chicken Quesadillas with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 4:
      print("\n--------------------LUNCH COMBO - BONELESS WINGS------------------")
      print("Hand-tossed in House BBQ Served with fries and a choice of side.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Boneless Wings with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 5: 
      print("\n--------LUNCH COMBO - BACON AVOCADO GRILLED CHICKEN SANDWICH------")
      print("\nHalf sandwich with grilled chicken, bacon, swiss, avocado, \nsauteed onions, lettuce, tomato, mayo on a toasted buttery roll. \nServed with fries.");
      print("\n1. Fries");
      print("2. Black Beans");
      print("3. Steamed Broccoli");
      print("4. Coleslaw");
      print("5. Corn On The Cob");
      print("6. Loaded Mashed Potatoes");
      print("7. Mexican Rice");
      print("8. Caesar Salad");
      print("9. Roasted Asparagus");
      print("10. House Salad");
      print("11. Roasted Street Corn");
      print("12. Texas Cheese Fries");
    
      choice = [];
      count = 1;
      while count != 2:
        uss_select = int(input("\nChoose side #" + str(count) + ": "));
        if uss_select == 1:
          choice.append("Fries");
          count+=1;
        elif uss_select == 2:
          choice.append("Black Beans");
          count+=1;
        elif uss_select == 3:
          choice.append("Steamed Broccoli");
          count+=1;
        elif uss_select == 4:
          choice.append("Coleslaw");
          count+=1;
        elif uss_select == 5:
          choice.append("Corn On The Cob");
          count+=1;
        elif uss_select == 6:
          choice.append("Loaded Mashed Potatoes");
          count+=1;
        elif uss_select == 7:
          choice.append("Mexican Rice");
          count+=1;
        elif uss_select == 8:
          choice.append("Caesar Salad");
          count+=1;
        elif uss_select == 9:
          choice.append("Roasted Asparagus");
          count+=1;
        elif uss_select == 10:
          choice.append("House Salad");
          count+=1;
        elif uss_select == 11:
          choice.append("Roasted Street Corn");
          count+=1;
        elif uss_select == 12:
          choice.append("Texas Cheese Fries");
          count+=1;
        else: 
          print("That choice is not valid, try again.");
      guest.addToOrder("Bacon Avocado Grilled Chicken Sandwich with a side of " + choice[0]);
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
  order_cont_loop();
def desserts_selection():
  global isActive;
  global guest;
  global orderNum;
  while isActive:
    user_selection = int(input("\nEnter the number next to your choice (1-3): "));
    if user_selection == 1:
      print("\n-----------------------MOLTEN CHOCOLATE CAKE----------------------");
      print("\nChocolate cake with a molten chocolate center, topped with vanilla\nice cream in a chocolate shell. Big enough to share, too good to \nactually do it.");
      choice = [guest.addToOrder("Molten Chocolate Cake")];
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 2:
      print("\n-------------------SKILLET CHOCOLATE CHIP COOKIE------------------");
      print("\nTopped with vanilla ice cream, hot fudge. YOU DESERVE DESSERT! BUY\nONE SKILLET COOKIE, GET ONE FOR $2. ");
      choice = [guest.addToOrder("Skillet Chocolate Chip Cookie")];
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;
    elif user_selection == 3:
      print("\n-------------------------CHEESECAKE-------------------------");
      print("\nServed over strawberry puree.");
      choice = [guest.addToOrder("Cheesecake")];
      print("\nYou've chosen the " + guest.getOrder(orderNum) + ".");
      break;

  order_cont_loop();
def start_menu():
  while isActive:
    user_selection_menu();
    user_selection = int(input("\nChoose what you'd like to do (1-2): "));
    if user_selection == 1:
      display_menu_options();
      menu_selection();
      break;
    elif user_selection == 2:
      reservation_making();
      break;
    else:
      print("That selection is not valid, please try again.");
def reservation_making():
  print("\n---------------RESERVATION---------------");
  input("\nHello, How are you?\n");
  print("\nGreat! Let's get started with your reservation!");
  name = input("\nWhat name will the reservation be under?: ");
  date = input("\nGreat! When is the reservation for? (mm/dd/yyyy): ");
  time = int(input("\nAwesome! What time of day will the reservation be for? (24HR Format): "));
  guests = int(input("\nAnd how many guests for the reservation? (including you): "));
  reservation = reservationMaker(time, guests, name, date);
  print("\nAlright, you're all set. We have the reservation for a party of " + str(reservation.guestNum) + " under the name " + reservation.guestName + ", at " + str(reservation.hour) + ":00" + reservation.amOrPm + " on " + reservation.date + ". Thank you!");
  continue_loop();
startOrder();