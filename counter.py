import PySimpleGUI as sg

f = open("number.txt", "r")
counter = f.read()

sg.change_look_and_feel('DarkGrey3') 
layout = [[sg.Image("<imagenamehere68pxby99px>.png",size=(68,88)),sg.Text(counter, font=("Arial",40), key="upb"), sg.Button(" ",image_filename="Up.png", enable_events=True)]]

# Create the window
window = sg.Window("Counter", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    if event == " ":
        f = open("number.txt", "r")
        test = f.read()
        counter = int(test)
        
        counter += 1
        w = open("number.txt", "w")
        w.write(str(counter))
        w.close()
        window["upb"].update(counter)
        
    
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break

window.close()
