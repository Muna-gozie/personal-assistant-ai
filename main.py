from core.router import route_command

# route command is responsible for receiveing user prompt

while True:
    try:
        command = input("You: ")
        response = route_command(command)
        print("Assistant: ",response)
    except KeyboardInterrupt:
        print("Exiting....")
        break
    
# print("Welcome to python")