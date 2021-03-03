helloIntent = ["hi","hey","hello","hi there"]
dateIntent = ["date","tell me date","what's the date"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print("Hello User")
    elif msg in dateIntent:
        pass
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
