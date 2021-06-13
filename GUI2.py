import PySimpleGUI as sg
import EncriptDecript as encdec 
import os
import io
import tellme as tm
from PIL import ImageTk,Image
#lista con los diversos temas de pysimplegui
themes = ["Black", "BlueMono", "BluePurple", "BrightColors", "BrownBlue", "Dark", "Dark2", "DarkAmber", "DarkBlack", "DarkBlack1", "DarkBlue", "DarkBlue1", "DarkBlue10", "DarkBlue11", "DarkBlue12", "DarkBlue13", "DarkBlue14", "DarkBlue15", "DarkBlue16", "DarkBlue17", "DarkBlue2", "DarkBlue3", "DarkBlue4", "DarkBlue5", "DarkBlue6", "DarkBlue7", "DarkBlue8", "DarkBlue9", "DarkBrown", "DarkBrown1", "DarkBrown2", "DarkBrown3", "DarkBrown4", "DarkBrown5", "DarkBrown6", "DarkGreen", "DarkGreen1", "DarkGreen2", "DarkGreen3", "DarkGreen4", "DarkGreen5", "DarkGreen6", "DarkGrey", "DarkGrey1", "DarkGrey2", "DarkGrey3", "DarkGrey4", "DarkGrey5", "DarkGrey6", "DarkGrey7", "DarkPurple", "DarkPurple1", "DarkPurple2", "DarkPurple3", "DarkPurple4", "DarkPurple5", "DarkPurple6", "DarkRed", "DarkRed1", "DarkRed2", "DarkTanBlue", "DarkTeal", "DarkTeal1", "DarkTeal10", "DarkTeal11", "DarkTeal12", "DarkTeal2", "DarkTeal3", "DarkTeal4", "DarkTeal5", "DarkTeal6", "DarkTeal7", "DarkTeal8", "DarkTeal9", "Default", "Default1", "DefaultNoMoreNagging", "Green", "GreenMono", "GreenTan", "HotDogStand", "Kayak", "LightBlue", "LightBlue1", "LightBlue2", "LightBlue3", "LightBlue4", "LightBlue5", "LightBlue6", "LightBlue7", "LightBrown", "LightBrown1", "LightBrown10", "LightBrown11", "LightBrown12", "LightBrown13", "LightBrown2", "LightBrown3", "LightBrown4", "LightBrown5", "LightBrown6", "LightBrown7", "LightBrown8", "LightBrown9", "LightGray1", "LightGreen", "LightGreen1", "LightGreen10", "LightGreen2", "LightGreen3", "LightGreen4", "LightGreen5", "LightGreen6", "LightGreen7", "LightGreen8", "LightGreen9", "LightGrey", "LightGrey1", "LightGrey2", "LightGrey3", "LightGrey4", "LightGrey5", "LightGrey6", "LightPurple", "LightTeal", "LightYellow", "Material1", "Material2", "NeutralBlue", "Purple", "Reddit", "Reds", "SandyBeach", "SystemDefault", "SystemDefault1", "SystemDefaultForReal", "Tan", "TanBlue", "TealMono", "Topanga"]
#seleccion de tema pysimplegui
sg.theme(themes[2])    # Keep things interesting for your users
#carga imagenes
ruta = 'assets\images'
ruta_save = 'assets\imagesre'
file_list = os.listdir(ruta)

# for i in file_list:
#     img = Image.open(ruta + "\\" + i)
#     new_img = img.resize((50,100))
#     new_img.save(ruta_save + "\\" + i,'png')
list_lettername = ['1C','1P','1R','1T','10C','10P','10R','10T','2C','2P','2R','2T','9C','9P','9R','9T']
dic_identify = {}

list_data_img = []
for idx, file in enumerate(file_list):
    with open(ruta_save + "\\" + file, "rb") as image:
        f = image.read()
        b = bytes(f)
    dic_identify[list_lettername[idx]] = b
    list_data_img.append(b)
#print(dic_identify[list_lettername[7]])
     
    



list_questions = []
#declaracion de layout y sus componetes
layout = [
        #declaracion del texto del titulo
        [sg.Text('Bienvenido al Juego de Cartas ',font=('Any 20'), justification='center')],
        [sg.Text("Piensa en una carta de las siguientes, yo te la adivinaré", justification='center')],
        [sg.Image(data = list_data_img[0]),sg.Image(data = list_data_img[1]),sg.Image(data = list_data_img[2]),sg.Image(data = list_data_img[3]),
        sg.Image(data = list_data_img[8]),sg.Image(data = list_data_img[9]),sg.Image(data = list_data_img[10]),sg.Image(data = list_data_img[11]),],
        [sg.Image(data = list_data_img[12]),sg.Image(data = list_data_img[13]),sg.Image(data = list_data_img[14]),sg.Image(data = list_data_img[15]),
        sg.Image(data = list_data_img[4]),sg.Image(data = list_data_img[5]),sg.Image(data = list_data_img[6]),sg.Image(data = dic_identify[list_lettername[7]]),],
        
        
        

        # #declaracion de un input-text
        # [sg.Input(key='-IN-')],  
        #declaracion de el button mostrar carta    
        [sg.Button('Estoy listo', key = "READY")],
        [sg.Text("", key = "QUESTIONS", size=(50,2),  visible=False, justification='center')],

        #preguntas
        [sg.Text("", key = "ONE", size=(50,1),  visible=False, justification='center')],        
        [sg.pin(sg.Button('', key = "SI1",  visible=False)),sg.pin(sg.Button('', key = "NO1",  visible=False))],

        [sg.Text("", size=(50,1), key = "TWO", justification='center')],
        [sg.pin(sg.Button('', key = "SI2",  visible=False)),sg.pin(sg.Button('', key = "NO2",  visible=False))],

        [sg.Text("", size=(50,1), key = "THREE", justification='center',  visible=False)],
        [sg.pin(sg.Button('', key = "SI3",  visible=False)),sg.pin(sg.Button('', key = "NO3",  visible=False))],

        [sg.Text("", size=(50,1), key = "FOUR", justification='center',  visible=False)],
        [sg.pin(sg.Button('', key = "SI4",  visible=False)),sg.pin(sg.Button('', key = "NO4",  visible=False))],

        [sg.Text("", size=(50,1), key = "FIVE", justification='center',  visible=False)],
        [sg.Text("", key="QUESTION1", size=(100,1), justification='center',  visible=False)],
        [sg.pin(sg.Button('', key = "SI5",  visible=False)),sg.pin(sg.Button('', key = "NO5",  visible=False))],

        [sg.Text("", size=(50,1), key = "SIX", justification='center',  visible=False)],
        [sg.Text("", key="QUESTION2", size=(100,1), justification='center',  visible=False)],
        [sg.pin(sg.Button('', key = "SI6",  visible=False)),sg.pin(sg.Button('', key = "NO6",  visible=False))],

        [sg.Text("", size=(50,1), key = "SEVEN", justification='center',  visible=False)],
        [sg.Text("", key="QUESTION3", size=(100,1), justification='center',  visible=False)],
        [sg.pin(sg.Button('', key = "SI7",  visible=False)),sg.pin(sg.Button('', key = "NO7",  visible=False))],
        [sg.Text("", size=(50,1), key = "ANSWER", justification='center',  visible=False)],
        [sg.Image(key="IMGFINAL",  visible=False)],
        [sg.Text("", size=(50,1), key = "LIE", justification='center',  visible=False)],

        # [sg.Text("Tu carta es: ", size=(50,1), key = "SEVEN", justification='center')],
        # [sg.Text("Tienes una mentira y es en la pregunta: ", size=(50,1), key = "SEVEN", justification='center')],
          
          ]      


#establecimiento de la ventana con el parametro layout y su dimension 
window = sg.Window('Proyecto Final TDC', layout, size=(1500,1000), element_justification='c')      

#while para leer los eventos de los botones
while True:                             # The Event Loop
    event, values = window.read()
    #if si el evento es mostrar carta
    if event == 'READY':        
        window.FindElement("READY").Update(visible=False)
        window.FindElement("ONE").Update('¿Tu carta es de CORAZÓN o de PICAS?',  visible=True)
        window.FindElement("SI1").Update('SÍ',  visible=True)
        window.FindElement("NO1").Update('NO',  visible=True)
        window.FindElement("QUESTIONS").Update('Contesta las siguientes preguntas \n Puedes mentirme en una sola pregunta si quieres)',  visible=True)


    if event == 'SI1' or event == 'NO1':
        window.FindElement("ONE").Update(visible=False)
        window.FindElement("TWO").Update('¿Es roja?',  visible=True)
        window.FindElement("SI1").Update(visible=False)
        window.FindElement("NO1").Update(visible=False)
        window.FindElement("SI2").Update('SÍ',  visible=True)
        window.FindElement("NO2").Update('NO',  visible=True)
        if event == 'SI1':
            list_questions.append(0)

        else:
            list_questions.append(1)


    if event == 'SI2' or event == 'NO2':
        window.FindElement("TWO").Update(visible=False)
        window.FindElement("THREE").Update('¿Es de valor alto?',  visible=True)
        window.FindElement("SI2").Update(visible=False)
        window.FindElement("NO2").Update(visible=False)
        window.FindElement("SI3").Update('SÍ',  visible=True)
        window.FindElement("NO3").Update('NO',  visible=True)
        if event == 'SI2':
            list_questions.append(0)

        else:
            list_questions.append(1)
        

    if event == 'SI3' or event == 'NO3':
        window.FindElement("THREE").Update(visible=False)
        window.FindElement("FOUR").Update('¿Es par?',  visible=True)
        window.FindElement("SI3").Update(visible=False)
        window.FindElement("NO3").Update(visible=False)
        window.FindElement("SI4").Update('SÍ',  visible=True)
        window.FindElement("NO4").Update('NO',  visible=True)
        if event == 'SI3':
            list_questions.append(0)

        else:
            list_questions.append(1)
        

    if event == 'SI4' or event == 'NO4':
        window.FindElement("FOUR").Update(visible=False)
        window.FindElement("FIVE").Update('¿Es alguna de éstas?')
        window.FindElement("QUESTION1").Update('2 de Corazones, 10 de Corazones, 1 de Picas, 9 de Picas, 1 de Rombos, 9 de Rombos, 2 de Trebol, 10 de Trebol',  visible=True)
        window.FindElement("SI4").Update(visible=False)
        window.FindElement("NO4").Update(visible=False)
        window.FindElement("SI5").Update('SÍ',  visible=True)
        window.FindElement("NO5").Update('NO',  visible=True)
        if event == 'SI4':
            list_questions.append(0)

        else:
            list_questions.append(1)
        

    if event == 'SI5' or event == 'NO5':
        window.FindElement("FIVE").Update(visible=False)
        window.FindElement("SIX").Update('¿Es alguna de éstas?',  visible=True)
        window.FindElement("QUESTION1").Update(visible=False)       
        window.FindElement("QUESTION2").Update('9 de Corazones, 10 de Corazones, 1 de Picas, 2 de Picas, 1 de Rombos, 2 de Rombos, 9 de Trebol, 10 de Trebol',  visible=True)
        window.FindElement("SI5").Update(visible=False)
        window.FindElement("NO5").Update(visible=False)
        window.FindElement("SI6").Update('SÍ',  visible=True)
        window.FindElement("NO6").Update('NO',  visible=True)
        if event == 'SI5':
            list_questions.append(0)

        else:
            list_questions.append(1)
        

    if event == 'SI6' or event == 'NO6':
        window.FindElement("SIX").Update(visible=False)
        window.FindElement("SEVEN").Update('¿Es alguna de éstas?',  visible=True)
        window.FindElement("QUESTION2").Update(visible=False)
        window.FindElement("QUESTION3").Update('1 de Corazones, 10 de Corazones, 1 de Picas, 10 de Picas, 2 de Rombos, 9 de Rombos, 2 de Trebol, 9 de Trebol',  visible=True)
        window.FindElement("SI6").Update(visible=False)
        window.FindElement("NO6").Update(visible=False)
        window.FindElement("SI7").Update('SÍ',  visible=True)
        window.FindElement("NO7").Update('NO',  visible=True)
        if event == 'SI6':
            list_questions.append(0)

        else:
            list_questions.append(1)
        
    
    if event == 'SI7' or event == 'NO7':
        window.FindElement("QUESTION3").Update(visible=False)
        window.FindElement("SIX").Update(visible=False)
        window.FindElement("SI7").Update(visible=False)
        window.FindElement("NO7").Update(visible=False)
        if event == 'SI7':
            list_questions.append(0)

        else:
            list_questions.append(1)
        print(list_questions)
        my_letter,lie_number =tm.tell_me_my_letter(list_questions)
        window.FindElement("ANSWER").Update("TU CARTA ES LA SIGUIENTE",  visible=True)
        window.FindElement("IMGFINAL").Update(data = dic_identify[my_letter],  visible=True)
        if lie_number == 0:
            window.FindElement("LIE").Update("No me mentiste en ninguna pregunta, !ERES MUY HONESTO!",  visible=True)
        else: 
            window.FindElement("LIE").Update("Me mentiste en la pregunta " + str(lie_number) + " MENTIRS@!!",  visible=True)

        


    #if si el evento es salir o si se cierra la ventana
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
#cierra la ventana al terminar el while
window.close()