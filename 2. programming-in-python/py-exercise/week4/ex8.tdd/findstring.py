def ispresent(pc):
    pc_names = ["dell", "hp", "mac"]
    if pc in pc_names:
        return True
    else:
        return False

def nodeigit():
    if pc.isalpha(): #for trst case pc isn't defined
        return True
    else:
        return False