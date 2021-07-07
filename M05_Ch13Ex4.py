import tkinter
import tkinter.messagebox

class Temperature_Converter:
    def __init__(self):
        # Windows
        self.main_window = tkinter.Tk()  # Makes main window
        self.main_window.title('Temperature Converter') # Names the window
        
        # Frames
        self.name_frame = tkinter.Frame(self.main_window)
        self.fahrenheit_frame = tkinter.Frame(self.main_window)
        self.celsius_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)


        # Name Row
        self.name_label = tkinter.Label(self.name_frame,text="Cameron Harter",relief='solid')

        # Pack Name Row
        self.name_label.pack()

        
        # Fahrenheit Row
        self.fahrenheit_label = tkinter.Label(self.fahrenheit_frame,text="Fahrenheit or Celcius:")
        self.Far_to_Cel = tkinter.Button(self.fahrenheit_frame,text='F° -> C°', command=self.F_to_C)


        # Pack Fahrenheit Row
        self.fahrenheit_label.pack(side='left')
        self.Far_to_Cel.pack(padx=(17,0),side='left')

        # Celsius Row
        self.number_input = tkinter.Entry(self.celsius_frame,width=15)
        self.Cel_to_Far = tkinter.Button(self.celsius_frame,text='C° -> F°', command=self.C_to_F)

        # Pack Celsius Row
        self.number_input.pack(padx=(40,29),side='left')
        self.Cel_to_Far.pack(padx=(0,25),side='left')

        
        # Buttons Row
        self.Quit = tkinter.Button(self.button_frame,text='Quit',command=self.main_window.destroy)

        # Pack Buttons Row
        self.Quit.pack(side='right')


        # Pack Frames
        self.name_frame.pack(padx=100,pady=(0,15))
        self.fahrenheit_frame.pack()
        self.celsius_frame.pack(pady=(0,15))
        self.button_frame.pack()

        tkinter.mainloop()  # Main loop

    def C_to_F(self):
        try:
            celsius = float(self.number_input.get())
            fahrenheit = ((celsius * 9) / 5) + 32
            fahrenheit = f'{fahrenheit:,.2f}'; celsius = f'{celsius:,.2f}'
            tkinter.messagebox.showinfo('Results',str(celsius)+
                                        ' C° --> '+str(fahrenheit)+' F°')
        except ValueError:
            self.Error_Message()

    def F_to_C(self):
        try:
            fahrenheit = float(self.number_input.get())
            celcius = ((fahrenheit - 32) / 9) * 5
            fahrenheit = f'{fahrenheit:,.2f}'; celcius = f'{celcius:,.2f}'
            tkinter.messagebox.showinfo('Results',str(fahrenheit)+
                                        ' F° --> '+str(celcius)+' C°')
        except ValueError:
            self.Error_Message()

    def Error_Message(self):
        tkinter.messagebox.showinfo('Error!','The values that you put in didn\'t work.\nPlease try again!')

if __name__ == '__main__':
    TC = Temperature_Converter()
