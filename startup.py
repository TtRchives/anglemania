print("Welcome to Anglemania!")
print()
def load():
   guicli = input("Would you like a graphical interface or a text interface? (gui/cli, case-sensitive)")
   if guicli == "gui":
      print("Loading...")
      os.system('python gui.py')
   elif guicli == "cli":
      print("Okay, loading...")
      os.system('python cli.py')
   else:
      print("Please type either gui or cli, case-sensitive (gui is graphical, cli is text")
      load()
print("Something's wrong...")
load()