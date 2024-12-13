import csv
from tkinter import *
import formulas


class Gui:
    """
    This is the initialize method for the gui,
    it defines a gui that has a set of radiobuttons with four options,
    an entry to input numbers in a list format
    and a button to run the calculate function which outputs to the label at the end
    """
    def __init__(self,window:Tk):
        self.window = window

        #radiobutton operation selector
        self.operationFrame = Frame(self.window)
        self.operationLabel = Label(self.operationFrame, text="Operation")
        self.radioVar = IntVar()
        self.radioVar.set(0)
        self.radio_add = Radiobutton(self.operationFrame, text="Addition", variable=self.radioVar, value=1)
        self.radio_subtract = Radiobutton(self.operationFrame, text="Subtraction", variable=self.radioVar, value=2)
        self.radio_multiply = Radiobutton(self.operationFrame, text="Multiplication", variable=self.radioVar, value=3)
        self.radio_divide = Radiobutton(self.operationFrame, text="Division", variable=self.radioVar, value=4)

        self.operationLabel.pack(side="left", padx=3)
        self.radio_add.pack(side="left")
        self.radio_subtract.pack(side="left")
        self.radio_multiply.pack(side="left")
        self.radio_divide.pack(side="left")
        self.operationFrame.pack(pady=20,side="top")

        #Numbers
        self.numbersFrame = Frame(self.window)
        self.numbersLabel = Label(self.numbersFrame,text="List of Numbers")
        self.numbersEntry = Entry(self.numbersFrame,width=40)
        self.numbersLabel.pack(side="left")
        self.numbersEntry.pack(side="right")
        self.numbersFrame.pack(padx=10,side="top")

        #Calculate Button and notes
        self.calcFrame = Frame(self.window)
        self.calcButton = Button(self.calcFrame,text="Calculate",command=self.calculate)
        self.notesLabel = Label(self.calcFrame,text="Only numerical inputs will be read")
        self.calcButton.pack(side="top")
        self.notesLabel.pack(side="bottom")
        self.calcFrame.pack(pady = 20,side="bottom")
    
    """
    Calculate separates the value from numbersEntry and separates it into acceptable inputs.
    The function checks to make sure at least two acceptable values have been input
    If not, it tells the user to input two values. 
    Then it takes the value from the radio button and calls the function from formulas.py that corresponds to it
    If no operation has been selected it tells the user that one must be selected
    If every condition is met, it saves the operation to history.csv
    """
    def calculate(self):
        """
        This try separates the value from numbersEntry into a list of only the numbers,
        every other input is removed
        """
        newList = []
        try:
            numbersList = self.numbersEntry.get().split(',')
            for n in numbersList:
                try:
                    newList.append(float(n.strip()))
                except:pass
        except:
            raise ValueError
        if len(newList) < 2:
            self.notesLabel.config(text="Two values must be provided")
        else:
            operation = ""
            if self.radioVar.get() == 1:
                result = formulas.add(newList)
                operation = "add"
            elif self.radioVar.get() == 2:
                result = formulas.subtract(newList)
                operation = "subtract"
            elif self.radioVar.get() == 3:
                result = formulas.multiply(newList)
                operation = "multiply"
            elif self.radioVar.get() == 4:
                try: result = formulas.divide(newList)
                except ZeroDivisionError: result = "Cannot divide by zero"
                operation = "divide"
            else:
                result = "Must select an operation"
            self.notesLabel.config(text=result)
            if operation:
                with open("history.csv",'a',newline='') as csvfile:
                    csvWriter = csv.writer(csvfile)
                    csvWriter.writerow([newList,operation,result])
                self.radioVar.set(0)
                self.numbersEntry.delete(0,"end")

        
