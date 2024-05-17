
#Mina importer
import PySimpleGUI as sg
import time

# Bubblesort koden, tar en lista och sorterar den och sparar varje steg
# n = len(arr) - hämtar längden på listan
def bubble_sort_step(arr):
    n = len(arr)
    steps = []
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(list(arr))
    return steps

# Selection Sort koden, tar en lista och sorterar den och sparar varje steg
# De två looparna används för att hitta det minsta värdet på elementerna i den osorterade listan
def selection_sort_step(arr):
    n = len(arr)
    steps = []
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(list(arr))
    return steps

# GUI layout, Här kan man mata in sina siffror och välja vilken sorteringsalgoritm man vill använda, visar också resultaten i Listbox
layout = [
    [sg.Text('Välj heltal och separera dem me kommatecken:')],
    [sg.InputText(key='-NUMBERS-')],
    [sg.Text('Välj sorteringsalgoritm:')],
    [sg.Button('Bubble Sort'), sg.Button('Selection Sort')],
    [sg.Text('Sorting steps:', size=(40, 1), key='-STEPS-')],
    [sg.Listbox(values=[], size=(40, 10), key='-LISTBOX-')]
]

# skapae ett fönster
window = sg.Window('Sorting Visualizer', layout)

#Loopen för fönstret
#Skapar en loop för att hålla fönstret öppet
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    #Konverterar talen till en lista med heltal
    if event in ('Bubble Sort', 'Selection Sort'):
        try:
            numbers = list(map(int, values['-NUMBERS-'].split(',')))
        except ValueError:
            sg.popup_error('Ange ett giltigt tal.')
            continue
        
        steps = []
        if event == 'Bubble Sort':
            steps = bubble_sort_step(numbers)
        elif event == 'Selection Sort':
            steps = selection_sort_step(numbers)
        
        # Använder time.sleep för att man ska kunna se alla steg.
        for step in steps:
            window['-LISTBOX-'].update(step)
            window.refresh()
            time.sleep(0.5)     

window.close()
