import importlib
import filechanges
# import sample

# importlib.reload(sample)
# importlib.reload(sample)
# importlib.reload(sample)
# importlib.reload(sample)

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass
#doesn't execute without forloop
for i in range(5):
    changes()
    input("Hit enter to reload...")