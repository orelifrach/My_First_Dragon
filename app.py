from pet import Pet

class app():
    def __init__(self):
        type = input(f"""Enter the pet type from the list
{Pet.get_pet_type_list()}: """)
        while not Pet.verify_type(type):
            type = input(f"""The requested type is not found in the list,
Enter the pet type from the list
{Pet.get_pet_type_list()}: """)
    
        name = input("Enter the pet's name: ")
        while not Pet.verify_name(name):
            name = input("""The name must be 2-9 chars long and contain only letters,
Enter the pet's name: """)
        
        self.pet = Pet(name, type)
        self.play()
        
    def play(self):
        actions_list = Pet.get_actions_list()
        actions_str = ""
        for i in range(len(actions_list)):
            actions_str += f"{i+1} - {actions_list[i-1]}\n"
        request_str = "Enter the number of the requested action:\n" + actions_str
        requested_action = int(input(request_str))
        while not isdigit(requested_action):
            
        while not 0 < requested_action <= len(actions_list):
            requested_action = int(input(f"The number of the requested action was out of range\n{request_str}"))
        
        # while True:
        #     if requested_action == 1:
        #     elif requested_action == 2:
        #     elif requested_action == 3:
##להמשיך מפה לממש את ממשק המשחק למשתמש

app()