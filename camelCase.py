
def camelcase():

    # Getting the input and capitalizing first letter of every word
    txt = input(" please enter something to be turned into camelCase").title() 
    # Splitting it into a list
    txtList = txt.split( )
    #Joining the list to get rid of whitespace
    txtList2 = ("".join(txtList)) 
    # Isolating the first letter to make it lowercase and extracting the rest of the 
    # letters and adding it to the camelCase variable
    camelCase = txt[0:1].lower() + txtList2[1:]
    print(camelCase)
    return camelCase

def banner():
    """Display welcome banner"""
    message = "CAMELCASE PROGRAM!!!"
    stars = '*' * len(message)
    print(f'{stars}\n{message}\n{stars}\n')


banner()
camelcase()