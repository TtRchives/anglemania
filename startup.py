print("Welcome to Anglemania!")
print()
def load():
   print("Would you like a graphical interface or a text interface? gui/cli, case-sensitive")
   guicli = input("Type: ")
   if guicli == "gui":
      print("Loading...")
      os.system('python gui.py')
   elif guicli == "cli":
      print("Okay, loading...")
      os.system('python cli.py')
   else:
      print("Please type either gui or cli, case-sensitive (gui is graphical, cli is text")
      load()
load()
print("Something's wrong...")
