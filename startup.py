print("Welcome to Anglemania!")
import os
print()
def load():
   guicli = raw_input("Would you like a graphical interface or a text interface? (gui/cli, case-sensitive)")
   if guicli == "gui":
      print("Loading...")
      os.system('python gui.py')
   elif guicli == "cli":
      #print("Okay, loading...")
      #os.system('python cli.py')
	  print("Unfortunatley the text-based version hasn't been programmed yet :(")
	  exit()
   else:
      print("Please type either gui or cli, case-sensitive (gui is graphical, cli is text")
      load()
load()
print("Either something's wrong, or you exited the program.")
print("NOTE: if it said gui not found, cd to the directory BEFORE running the script")