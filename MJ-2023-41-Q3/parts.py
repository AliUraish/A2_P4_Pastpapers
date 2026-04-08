Animal=[]
Colour=[]
AnimalTopPointer=0
ColourTopPointer=0


def PushAnimal(data):
    if AnimalTopPointer==20:
        return False
    else:
        Animal[AnimalTopPointer]=data
        AnimalTopPointer=AnimalTopPointer+1
        return True

        

