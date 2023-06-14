import tkinter
from tkinter import colorchooser
import os

class RGBMatrixDemo:
    def __init__(self):
        self.colors = ['0xFF0000']
        self.runGUI()

    def getColors(self):
        colorString = ', '.join(self.colors)
        return f'{{{colorString}}}'

    def addColor(self):
        if (len(self.colors) == 5):
            self.addColorButton["state"] = tkinter.DISABLED
        elif (len(self.colors) == 1):
            self.removeColorButton["state"] = tkinter.NORMAL
        colorCode = colorchooser.askcolor(title ="Choose color")[1].upper().replace('#', '0x')
        self.colors.append(colorCode)
        self.setColorButtons()

    def removeColor(self):
        if (len(self.colors) == 6):
            self.addColorButton["state"] = tkinter.NORMAL
        elif (len(self.colors) == 2):
            self.removeColorButton["state"] = tkinter.DISABLED
        self.colors.pop()
        self.setColorButtons()

    def changeColor(self, index):
        colorCode = colorchooser.askcolor(title ="Choose color")[1].upper().replace('#', '0x')
        self.colors[index] = colorCode
        self.setColorButtons()

    def setColorButtons(self):
        self.clearColorButtons()
        for index, color in enumerate(self.colors):
            color = color.replace('0x', '#')
            button = tkinter.Button(self.colorFrame, text="Change Color", bg=color, fg=color, command=lambda: self.changeColor(index))
            button.pack(pady=20, side=tkinter.TOP)

    def clearColorButtons(self):
        for widgets in self.colorFrame.winfo_children():
            widgets.destroy()

    def updateText(self):
        self.text.delete('1.0', tkinter.END)
        with open("rgb-matrix.ino", "r") as file:
            lines = file.readlines()
            for line in lines:
                self.text.insert(tkinter.END, line)

    def submit(self):
        colors = f'{{{", ".join(self.colors)}}}'
        shape = self.shape.get()
        os.system(f'rgb-matrix.sh "{shape}" "{colors}"')
        self.updateText()

    def runGUI(self):
        window = tkinter.Tk()
        window.title("RGB Matrix Demo")
        window.state('zoomed')

        leftFrame = tkinter.Frame(window)
        leftFrame.pack(expand=True, fill=tkinter.BOTH, side=tkinter.LEFT)
        scroll=tkinter.Scrollbar(leftFrame, orient='vertical')
        scroll.pack(side=tkinter.RIGHT, fill='y')
        text=tkinter.Text(leftFrame, font=("Terminal, 18"), yscrollcommand=scroll.set, wrap=tkinter.WORD)
        self.text = text
        self.updateText()
        scroll.config(command=text.yview)
        text.pack(expand=True, fill=tkinter.BOTH)

        rightFrame = tkinter.Frame(window)
        rightFrame.pack(expand=True, fill=tkinter.BOTH, side=tkinter.LEFT)
        colorGroupFrame = tkinter.Frame(rightFrame)
        colorGroupFrame.pack(expand=True, fill=tkinter.BOTH, side=tkinter.TOP, pady=20)
        self.colorFrame = tkinter.Frame(colorGroupFrame)
        self.colorFrame.pack(expand=True, fill=tkinter.X, side=tkinter.TOP)
        self.setColorButtons()
        addColorFrame = tkinter.Frame(colorGroupFrame)
        addColorFrame.pack(expand=True, fill=tkinter.X, side=tkinter.LEFT, padx=10)
        removeColorFrame = tkinter.Frame(colorGroupFrame)
        removeColorFrame.pack(expand=True, fill=tkinter.X, side=tkinter.LEFT, padx=10)
        self.addColorButton = tkinter.Button(addColorFrame, text = "Add Color", command = self.addColor)
        self.removeColorButton = tkinter.Button(removeColorFrame, text = "Remove Color", command = self.removeColor)
        self.addColorButton.pack(side=tkinter.RIGHT)
        self.removeColorButton.pack(side=tkinter.LEFT)
        self.removeColorButton["state"] = tkinter.DISABLED
        shapeFrame = tkinter.Frame(rightFrame)
        shapeFrame.pack(expand=True, fill=tkinter.BOTH, side=tkinter.TOP, pady=20)
        self.shape = tkinter.StringVar()
        horizontalRadioButton = tkinter.Radiobutton(shapeFrame, text='Horizontal', variable=self.shape, value='horizontal')
        horizontalRadioButton.pack(pady=20)
        verticalRadioButton = tkinter.Radiobutton(shapeFrame, text='Vertical', variable=self.shape, value='vertical')
        verticalRadioButton.pack(pady=20)
        diagonalRadioButton = tkinter.Radiobutton(shapeFrame, text='Diagonal', variable=self.shape, value='diagonal')
        diagonalRadioButton.pack(pady=20)
        self.shape.set('horizontal')
        submitFrame = tkinter.Frame(rightFrame)
        submitFrame.pack(expand=True, fill=tkinter.BOTH, side=tkinter.BOTTOM, pady=20)
        submitButton = tkinter.Button(submitFrame, text="Submit", command=self.submit)
        submitButton.pack()

        window.mainloop()

if __name__=='__main__':
    RGBMatrixDemo()