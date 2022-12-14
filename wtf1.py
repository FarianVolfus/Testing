from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as message
import matplotlib
import matplotlib.pyplot as plt
import urllib.request
import xml.dom.minidom
import xml.etree.ElementTree as ET
import datetime
from datetime import timedelta

class Parser:
    @staticmethod
    def getNames():
        today = datetime.datetime.today()
        d = str(today.strftime("%d/%m/%Y"))
        response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + d)
        Name = []
        dom1 = xml.dom.minidom.parse(response)
        dom1.normalize()
        nodeArray = dom1.getElementsByTagName("Valute")
        for node in nodeArray:
            childlist = node.childNodes
            for child in childlist:
                if child.nodeName == "Name":
                    Name.append(child.childNodes[0].nodeValue)
        return Name

    @staticmethod
    def getValues():
        today = datetime.datetime.today()
        d = str(today.strftime("%d/%m/%Y"))
        response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + d)
        Value = []
        dom1 = xml.dom.minidom.parse(response)
        dom1.normalize()
        nodeArray = dom1.getElementsByTagName("Valute")
        for node in nodeArray:
            childlist = node.childNodes
            for child in childlist:
                if child.nodeName == "Value":
                    Value.append(child.childNodes[0].nodeValue)
        return Value

    @staticmethod
    def getNominal():
        today = datetime.datetime.today()
        d = str(today.strftime("%d/%m/%Y"))
        response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + d)
        Nominal = []
        dom1 = xml.dom.minidom.parse(response)
        dom1.normalize()
        nodeArray = dom1.getElementsByTagName("Valute")
        for node in nodeArray:
            childlist = node.childNodes
            for child in childlist:
                if child.nodeName == "Nominal":
                    Nominal.append(child.childNodes[0].nodeValue)
        Nominal.append('1')
        return Nominal

    def getDates(period):
        today = datetime.datetime.today()
        a = []
        if period == 1:
            for i in range(4):
                s = ''
                per = today - timedelta(6)
                d1 = str(per.strftime("%d/%m/%y"))
                d2 = str(today.strftime("%d/%m/%y"))
                today = per
                s = d1 + '-' + d2
                a.append(s)
        elif period == 2:
            mes = 0
            for i in range(4):
                s = ''
                per = today - timedelta(30)
                if i == 0:
                    d1 = str(today.strftime("%m/%Y"))
                else:
                    d1 = str(per.strftime("%m/%Y"))
                stl = d1.split('/')
                if stl[0] == '01':
                    mes = 1
                    s += '????????????'
                elif stl[0] == '02':
                    s += '??????????????'
                    mes = 2
                elif stl[0] == '03':
                    s += '????????'
                    mes = 3
                elif stl[0] == '04':
                    s += '????????????'
                    mes = 4
                elif stl[0] == '05':
                    s += '??????'
                    mes = 5
                elif stl[0] == '06':
                    s += '????????'
                    mes = 6
                elif stl[0] == '07':
                    s += '????????'
                    mes = 7
                elif stl[0] == '08':
                    s += '????????????'
                    mes = 8
                elif stl[0] == '09':
                    s += '??????????????????'
                    mes = 9
                elif stl[0] == '10':
                    s += '??????????????'
                    mes = 10
                elif stl[0] == '11':
                    s += '????????????'
                    mes = 11
                elif stl[0] == '12':
                    s += '??????????????'
                    mes = 12
                s += ' ' + stl[1]
                if i != 0:
                    today = per
                a.append(s)
        elif period == 3:
            a.append('1  ??????????????')
            a.append('2  ??????????????')
            a.append('3  ??????????????')
            a.append('4  ??????????????')
        elif period == 4:
            for i in range(4):
                per = today - timedelta(365)
                if i == 0:
                    d1 = str(today.strftime("%Y"))
                else:
                    d1 = str(per.strftime("%Y"))
                if i != 0:
                    today = per
                a.append(d1)
        return a

    def getValuesForDate(period, dates, name):
        if period == 1:
            ssp = dates.split('-')
            ssp = ssp[0].split('/')
            ssp[2] = '20'+ssp[2]
            dateAgo = datetime.date(int(ssp[2]), int(ssp[1]), int(ssp[0]))
            dateAgo1 = dateAgo
            Value = []
            for i in range(7):
                dateAgo = dateAgo1 + timedelta(i)
                d = str(dateAgo.strftime("%d/%m/%Y"))
                response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + d)
                b = False
                dom1 = xml.dom.minidom.parse(response)
                dom1.normalize()
                nodeArray = dom1.getElementsByTagName("Valute")
                for node in nodeArray:
                    childlist = node.childNodes
                    for child in childlist:
                        if child.nodeName == "Name":
                            if child.childNodes[0].nodeValue == name:
                                b = True
                        if child.nodeName == "Value":
                            if b:
                                Value.append(child.childNodes[0].nodeValue)
                                b = False
            return Value
        elif period == 2:
            j = 0
            mes = 0
            stl = dates.split(' ')
            if stl[0] == '????????????':
                mes = 1
            elif stl[0] == '??????????????':
                mes = 2
            elif stl[0] == '????????':
                mes = 3
            elif stl[0] == '????????????':
                mes = 4
            elif stl[0] == '??????':
                mes = 5
            elif stl[0] == '????????':
                mes = 6
            elif stl[0] == '????????':
                mes = 7
            elif stl[0] == '????????????':
                mes = 8
            elif stl[0] == '????????????????':
                mes = 9
            elif stl[0] == '??????????????':
                mes = 10
            elif stl[0] == '????????????':
                mes = 11
            elif stl[0] == '??????????????':
                mes = 12
            mes = str(mes)
            if len(mes) != 2:
                mes = '0' + str(mes)
            Value = []
            k = ''
            for i in range(1,31,2):
                if len(str(i)) != 2:
                    k = '0' + str(i)
                else:
                    k = str(i)
                d = k + '/' + mes + '/' + stl[1]
                print(d)
                response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + d)
                b = False
                dom1 = xml.dom.minidom.parse(response)
                dom1.normalize()
                nodeArray = dom1.getElementsByTagName("Valute")
                for node in nodeArray:
                    childlist = node.childNodes
                    for child in childlist:
                        if child.nodeName == "Name":
                            if child.childNodes[0].nodeValue == name:
                                b = True
                        if child.nodeName == "Value":
                            if b:
                                Value.append(child.childNodes[0].nodeValue)
                                j+=1
                                b = False
            print(j)
            return Value
        elif period == 3:
            stl = dates.split(' ')
            if stl[0] == '1':
                st = 1
                end = 92
            elif stl[0] == '2':
                st = 92
                end = 182
            elif stl[0] == '3':
                st = 182
                end = 272
            elif stl[0] == '4':
                st = 272
                end = 365
            today = datetime.datetime.today()
            d1 = int(today.strftime("%Y"))
            dateAgo1 = datetime.date(d1,1,1)
            dateAgo = dateAgo1
            print(dateAgo)
            Value = []
            for i in range(st,end,10):
                dateAgo = dateAgo1 + timedelta(i)
                d = str(dateAgo.strftime("%d/%m/%Y"))
                print(d)
                response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + d)
                b = False
                dom1 = xml.dom.minidom.parse(response)
                dom1.normalize()
                nodeArray = dom1.getElementsByTagName("Valute")
                for node in nodeArray:
                    childlist = node.childNodes
                    for child in childlist:
                        if child.nodeName == "Name":
                            if child.childNodes[0].nodeValue == name:
                                b = True
                        if child.nodeName == "Value":
                            if b:
                                Value.append(child.childNodes[0].nodeValue)
                                b = False
            return Value
        elif period == 4:
            d1 = int(dates)
            print(d1)
            dateAgo1 = datetime.date(d1, 1, 1)
            dateAgo = dateAgo1
            Value = []
            for i in range(0,366,20):
                dateAgo = dateAgo1 + timedelta(i)
                d = str(dateAgo.strftime("%d/%m/%Y"))
                print(d)
                response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + d)
                b = False
                dom1 = xml.dom.minidom.parse(response)
                dom1.normalize()
                nodeArray = dom1.getElementsByTagName("Valute")
                for node in nodeArray:
                    childlist = node.childNodes
                    for child in childlist:
                        if child.nodeName == "Name":
                            if child.childNodes[0].nodeValue == name:
                                b = True
                        if child.nodeName == "Value":
                            if b:
                                Value.append(child.childNodes[0].nodeValue)
                                b = False
            return Value


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def konverter():
    v1 = combo1.get()
    v2 = combo2.get()
    try:
        number = int(txt.get())
    except ValueError:
        message.showwarning("????????????", "?????????? ???????????? ?????????? ?? ?????????????????? ????????????")
        return
    names = Parser.getNames()
    try:
        index1 = names.index(v1)
        index2 = names.index(v2)
    except Exception:
        message.showwarning("????????????", "?????????? ?????????????? ???????????? ???? ????????????")
        return
    values = Parser.getValues()
    nom = Parser.getNominal()
    nom1 = nom[index1]
    nom2 = nom[index2]
    value1 = values[index1]
    value2 = values[index2]
    value1 = value1.replace(',', '.')
    value2 = value2.replace(',', '.')
    res = (float(value1) * number) / float(nom1) / (float(value2) * float(nom2))
    lbl['text'] = str(res)

def makeGraf():
    matplotlib.use('TkAgg')
    fig = plt.figure()
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=tab2)
    plot_w = canvas.get_tk_widget()
    fig.clear()
    mesa = Parser.getDates(radio_state.get())
   # mesa = mesa[-1]
    print(mesa)
    v = Parser.getValuesForDate(radio_state.get(), combo4.get(), combo3.get())
    for i in range(len(v)):
        v[i] = v[i].replace(',', '.')
        v[i] = float(v[i])
    print(v)
    gg = []
    for i in range(1,len(v)+1):
        gg.append(i)

    plt.plot(gg, v)
    plt.grid()
    plot_w.grid(column=3, row=6)
    pass
def fixCombo():
    if radio_state.get() == 2:
        mass = Parser.getDates(radio_state.get())
        mass = mass[:len(mass)]
        combo4['values'] = mass
    else:
        combo4['values'] = Parser.getDates(radio_state.get())
#?????????????????????? ?????????????????? ?? ??????????
window = Tk()
window.title("??????????????????????????????????")
window.geometry("1200x800")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='?????????????????????? ??????????')
tab_control.add(tab2, text='???????????????? ??????????')
#?????????????????? ?????? ???????????????????? ??????????????????
combo1 = ttk.Combobox(tab1)
combo1['values'] = Parser.getNames()
combo1.grid(column=1, row=1, padx=15, pady=15)
combo2 = ttk.Combobox(tab1)
combo2['values'] = Parser.getNames()
combo2.grid(column=1, row=2, padx=15, pady=15)
txt = Entry(tab1)
txt.grid(column=2, row=1, padx=15)
lbl = Label(tab1, text="")
lbl.grid(column=2, row=2, padx=15)
btnKonv = Button(tab1, text='????????????????????????????', command=konverter)
btnKonv.grid(column=3, row=1, padx=15)
#?????? ???????????? ???????? ?????????????????? ?????? ??????????????
lblVal = Label(tab2, text='????????????')
lblVal.grid(column=1, row=1, padx=55)
lblPer = Label(tab2, text='????????????')
lblPer.grid(column=2, row=1, padx=55)
lblCh = Label(tab2, text='?????????? ??????????????')
lblCh.grid(column=3, row=1, padx=55)
radio_state = IntVar()
radio_state.set(4)
rb1 = Radiobutton(tab2, text='????????????', value=1, variable=radio_state, command=fixCombo)
rb1.grid(column=2, row=2)
rb2 = Radiobutton(tab2, text='??????????', value=2, variable=radio_state, command=fixCombo)
rb2.grid(column=2, row=3)
rb3 = Radiobutton(tab2, text='??????????????', value=3, variable=radio_state, command=fixCombo)
rb3.grid(column=2, row=4)
rb4 = Radiobutton(tab2, text='??????', value=4, variable=radio_state, command=fixCombo)
rb4.grid(column=2, row=5)
combo3 = ttk.Combobox(tab2)
combo3['values'] = Parser.getNames()
combo3.grid(column=1, row=2, padx=15, pady=15)
btnGraf = Button(tab2, text='?????????????????? ????????????', command=makeGraf)
btnGraf.grid(column=1, row=4, padx=15)
combo4 = ttk.Combobox(tab2)
if radio_state.get() == 2:
    mass = Parser.getDates(radio_state.get())
    mass = mass[:len(mass)-1]
    combo4['values'] = mass
else:
    combo4['values'] = Parser.getDates(radio_state.get())
combo4.grid(column=3, row=2, padx=15, pady=15)
tab_control.pack(expand=0, fill='both')


window.mainloop()
