import random
import time
import tkinter
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


class SortingAlgorithmVisualizer:
    def __init__(self, length=100):
        self.barFrame = None
        self.algorithm = None
        self.canvas = None
        self._changeLength(length)
        self._initGUI()

    def insertionSort(self):
        self._updateAlgorithm('insertionSort')
        numberList = self.list.copy()
        for i in range(len(numberList)):
            minimum = min(numberList[i:])
            minimumIndex = numberList.index(minimum)
            while minimumIndex > i:
                numberList[minimumIndex], numberList[minimumIndex-1] = numberList[minimumIndex-1], numberList[minimumIndex]
                self._drawChart([(minimumIndex, numberList[minimumIndex]), (minimumIndex-1, numberList[minimumIndex-1])])
                minimumIndex -= 1
        self._drawChart()

    def selectionSort(self):
        self._updateAlgorithm('selectionSort')
        numberList = self.list.copy()
        index = 0
        while index < len(numberList):
            numberToSwap = min(numberList[index:])
            indexToSwap = index + numberList[index:].index(numberToSwap)
            numberList[index], numberList[indexToSwap] = numberList[indexToSwap], numberList[index]
            self._drawChart([(index, numberList[index]), (indexToSwap, numberList[indexToSwap])])
            index += 1
        self._drawChart()

    def mergeSort(self):
        self._updateAlgorithm('mergeSort')
        numberList = self.list.copy()
        groupSize = 1
        while groupSize < len(numberList):
            iteration = 1
            lastGroup = False
            while not lastGroup:
                minimumIndex = 2*(iteration-1) * groupSize
                iteration += 1
                maximumIndex1 = min(minimumIndex + groupSize, len(numberList))
                maximumIndex2 = min(maximumIndex1 + groupSize, len(numberList))
                lastGroup = maximumIndex2==len(numberList)
                tempSlice = []
                slice1 = numberList[minimumIndex:maximumIndex1]
                slice2 = numberList[maximumIndex1:maximumIndex2]
                while len(slice1) and len(slice2):
                    if slice1[0] < slice2[0]:
                        num = slice1.pop(0)
                        tempSlice.append(num)
                        indicesToDraw = list(range(minimumIndex+len(tempSlice)-1, minimumIndex+len(tempSlice)+len(slice1)))
                        valuesToDraw = [tempSlice[-1]] + slice1 
                        self._drawChart(zip(indicesToDraw, valuesToDraw))
                    else:
                        num = slice2.pop(0)
                        tempSlice.append(num)
                        indicesToDraw = list(range(minimumIndex+len(tempSlice)-1, minimumIndex+len(tempSlice)+len(slice1)+len(slice2)))
                        valuesToDraw = [tempSlice[-1]] + slice1 + slice2
                        self._drawChart(zip(indicesToDraw, valuesToDraw))
                while len(slice1):
                    num = slice1.pop(0)
                    tempSlice.append(num)
                    indicesToDraw = list(range(minimumIndex+len(tempSlice)-1, minimumIndex+len(tempSlice)+len(slice1)))
                    valuesToDraw = [tempSlice[-1]] + slice1 
                    self._drawChart(zip(indicesToDraw, valuesToDraw))
                while len(slice2):
                    num = slice2.pop(0)
                    tempSlice.append(num)
                    indicesToDraw = list(range(minimumIndex+len(tempSlice)-1, minimumIndex+len(tempSlice)+len(slice2)))
                    valuesToDraw = [tempSlice[-1]] + slice2
                    self._drawChart(zip(indicesToDraw, valuesToDraw))
                numberList[minimumIndex:maximumIndex2] = tempSlice
            groupSize *= 2
        self._drawChart()

    def bubbleSort(self):
        self._updateAlgorithm('bubbleSort')
        numberList = self.list.copy()
        swapsMade = True
        while swapsMade:
            swapsMade = False
            index = 0
            while index < len(numberList)-1:
                if numberList[index+1] < numberList[index]:
                    numberList[index+1], numberList[index] = numberList[index], numberList[index+1]
                    swapsMade = True
                    self._drawChart([(index, numberList[index]), (index+1, numberList[index+1])])
                index += 1
        self._drawChart()

    def shellSort(self):
        self._updateAlgorithm('shellSort')
        gaps = [701, 301, 132, 57, 23, 10, 4, 1]
        numberList = self.list.copy()
        for gap in gaps:
            if gap > len(numberList):
                continue
            swapsMade = True
            while swapsMade:
                index = 0
                swapsMade = False
                while index+gap < len(numberList):
                    if numberList[index+gap] < numberList[index]:
                        numberList[index], numberList[index+gap] = numberList[index+gap], numberList[index]
                        self._drawChart([(index, numberList[index]), (index+gap, numberList[index+gap])])
                        swapsMade = True
                    index += 1
        self._drawChart()

    def exchangeSort(self):
        self._updateAlgorithm('shellSort')
        numberList = self.list.copy()
        index = 0
        while index < len(numberList)-1:
            compareIndex = index+1
            while compareIndex < len(numberList):
                if numberList[compareIndex] < numberList[index]:
                    numberList[index], numberList[compareIndex] = numberList[compareIndex], numberList[index]
                    self._drawChart([(index, numberList[index]), (compareIndex, numberList[compareIndex])])
                compareIndex += 1 
            index += 1
        self._drawChart()

    def _changeLength(self, length):
        self.length = length
        self.list = list(range(1, length+1))
        random.shuffle(self.list)
        self._restartAnimation(self.algorithm)

    def _initGUI(self):
        window = tkinter.Tk()
        window.title("Sorting Algorithm Demo")
        window.state('zoomed')
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=2)
        window.columnconfigure(1, weight=3)

        leftFrame = tkinter.Frame(window)
        leftFrame.grid(row=0, column=0, sticky="nsew")
        leftFrame.pack_propagate(False)
        scroll = tkinter.Scrollbar(leftFrame, orient='vertical')
        scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.text = tkinter.Text(leftFrame, font=("Terminal, 18"), yscrollcommand=scroll.set, wrap=tkinter.WORD)
        scroll.config(command=self.text.yview)
        self.text.pack(expand=True, fill=tkinter.BOTH)

        rightFrame = tkinter.Frame(window)
        rightFrame.grid(row=0, column=1, sticky="nsew")
        rightFrame.grid_propagate(False)
        rightFrame.rowconfigure(0, weight=1)
        rightFrame.rowconfigure(1, weight=9)
        rightFrame.columnconfigure(0, weight=1)
        optionsFrame = tkinter.Frame(rightFrame)
        optionsFrame.grid(row=0, column=0, sticky="nsew")
        optionsFrame.pack_propagate(False)
        sizeFrame = tkinter.Frame(optionsFrame)
        sizeFrame.pack(expand=True, fill=tkinter.BOTH, side=tkinter.LEFT, padx=20, pady=10)
        sizeFrame.grid_propagate(False)
        sizeFrame.columnconfigure(0, weight=100)
        sizeFrame.columnconfigure(1, weight=1)
        sizeFrame.columnconfigure(2, weight=1)
        sizeFrame.rowconfigure(0, weight=1)
        sizeFrame.rowconfigure(1, weight=1)
        size = tkinter.IntVar(window, self.length)
        tenRadio = tkinter.Radiobutton(sizeFrame, text='10', variable=size, value=10, command=lambda: self._changeLength(size.get()))
        tenRadio.grid(row=0, column=1)
        twentyFiveRadio = tkinter.Radiobutton(sizeFrame, text='25', variable=size, value=25, command=lambda: self._changeLength(size.get()))
        twentyFiveRadio.grid(row=0, column=2)
        fiftyRadio = tkinter.Radiobutton(sizeFrame, text='50', variable=size, value=50, command=lambda: self._changeLength(size.get()))
        fiftyRadio.grid(row=1, column=1)
        oneHundredRadio = tkinter.Radiobutton(sizeFrame, text='100', variable=size, value=100, command=lambda: self._changeLength(size.get()))
        oneHundredRadio.grid(row=1, column=2)
        algorithmFrame = tkinter.Frame(optionsFrame)
        algorithmFrame.pack(expand=True, fill=tkinter.BOTH, side=tkinter.LEFT, padx=20, pady=10)
        algorithmFrame.grid_propagate(False)
        algorithmFrame.columnconfigure(0, weight=1)
        algorithmFrame.columnconfigure(1, weight=1)
        algorithmFrame.columnconfigure(2, weight=1)
        algorithmFrame.columnconfigure(3, weight=100)
        algorithmFrame.rowconfigure(0, weight=1)
        algorithmFrame.rowconfigure(1, weight=1)
        algorithm = tkinter.StringVar(window, 'Empty')
        insertionRadio = tkinter.Radiobutton(algorithmFrame, text='Insertion Sort', variable=algorithm, value='insertionSort', command=lambda: self.insertionSort())
        insertionRadio.grid(row=0, column=0)
        selectionRadio = tkinter.Radiobutton(algorithmFrame, text='Selection Sort', variable=algorithm, value='selectionSort', command=lambda: self.selectionSort())
        selectionRadio.grid(row=0, column=1)
        mergeRadio = tkinter.Radiobutton(algorithmFrame, text='Merge Sort', variable=algorithm, value='mergeSort', command=lambda: self.mergeSort())
        mergeRadio.grid(row=0, column=2)
        bubbleRadio = tkinter.Radiobutton(algorithmFrame, text='Bubble Sort', variable=algorithm, value='bubbleSort', command=lambda: self.bubbleSort())
        bubbleRadio.grid(row=1, column=0)
        shellRadio = tkinter.Radiobutton(algorithmFrame, text='Shell Sort', variable=algorithm, value='shellSort', command=lambda: self.shellSort())
        shellRadio.grid(row=1, column=1)
        exchangeRadio = tkinter.Radiobutton(algorithmFrame, text='Exchange Sort', variable=algorithm, value='exchangeSort', command=lambda: self.exchangeSort())
        exchangeRadio.grid(row=1, column=2)
        self.barFrame = tkinter.Frame(rightFrame)
        self.barFrame.grid(row=1, column=0, sticky="nsew")
        self._restartAnimation()

        window.mainloop()

    def _drawChart(self, bars=[]):
        for bar in self.bars:
            bar.set_color('b')
        for bar in bars:
            index = bar[0]
            value = bar[1]
            self._updateBar(index, value)
        self.canvas.draw()
        self.barFrame.update()
        sleepTime = 20 / self.length**2
        time.sleep(sleepTime)

    def _updateBar(self, index, value):
        self.bars[index].set_height(value)
        self.bars[index].set_color('r')

    def _restartAnimation(self, algorithm = None):
        if self.barFrame is not None:
            for widgets in self.barFrame.winfo_children():
                widgets.destroy()
            self.figure = Figure()
            self.canvas = FigureCanvasTkAgg(self.figure, self.barFrame)
            axes = self.figure.add_subplot()
            self.bars = axes.bar(list(range(len(self.list))), self.list)
            self._drawChart()
            axes.set_xticks([])
            axes.set_yticks([])
            self.canvas.get_tk_widget().pack(expand=True, fill=tkinter.BOTH)

        if algorithm == 'insertionSort':
            self.insertionSort()
        elif algorithm == 'selectionSort':
            self.selectionSort()
        elif algorithm == 'mergeSort':
            self.mergeSort()
        elif algorithm == 'bubbleSort':
            self.bubbleSort()
        elif algorithm == 'shellSort':
            self.shellSort()
        elif algorithm == 'exchangeSort':
            self.exchangeSort()

    def _updateAlgorithm(self, algorithm):
        self.algorithm = algorithm
        self._updateAlgorithmCode()
        self._restartAnimation()

    def _updateAlgorithmCode(self):
        if self.algorithm=='insertionSort':
            algorithmCode = '''
def insertionSort(self):
    self._updateAlgorithm('insertionSort')
    numberList = self.list.copy()
    for i in range(len(numberList)):
        minimum = min(numberList[i:])
        minimumIndex = numberList.index(minimum)
        while minimumIndex > i:
            numberList[minimumIndex], numberList[minimumIndex-1] = numberList[minimumIndex-1], numberList[minimumIndex]
            minimumIndex -= 1
            '''
        elif self.algorithm == 'selectionSort':
            algorithmCode = '''
def selectionSort(self):
    numberList = self.list.copy()
    index = 0
    while index < len(numberList):
        numberToSwap = min(numberList[index:])
        indexToSwap = index + numberList[index:].index(numberToSwap)
        numberList[index], numberList[indexToSwap] = numberList[indexToSwap], numberList[index]
        index += 1
            '''
        elif self.algorithm == 'mergeSort':
            algorithmCode = '''
def mergeSort(self):
    self._updateAlgorithm('mergeSort')
    numberList = self.list.copy()
    groupSize = 1
    while groupSize < len(numberList):
        iteration = 1
        lastGroup = False
        while not lastGroup:
            minimumIndex = 2*(iteration-1) * groupSize
            iteration += 1
            maximumIndex1 = min(minimumIndex + groupSize, len(numberList))
            maximumIndex2 = min(maximumIndex1 + groupSize, len(numberList))
            lastGroup = maximumIndex2==len(numberList)
            tempSlice = []
            slice1 = numberList[minimumIndex:maximumIndex1]
            slice2 = numberList[maximumIndex1:maximumIndex2]
            while len(slice1) and len(slice2):
                if slice1[0] < slice2[0]:
                    num = slice1.pop(0)
                    tempSlice.append(num)
                else:
                    num = slice2.pop(0)
                    tempSlice.append(num)
            while len(slice1):
                num = slice1.pop(0)
                tempSlice.append(num)
            while len(slice2):
                num = slice2.pop(0)
                tempSlice.append(num)
            numberList[minimumIndex:maximumIndex2] = tempSlice
        groupSize *= 2
            '''
        elif self.algorithm == 'bubbleSort':
            algorithmCode = '''
def bubbleSort(self):
    numberList = self.list.copy()
    swapsMade = True
    while swapsMade:
        swapsMade = False
        index = 0
        while index < len(numberList)-1:
            if numberList[index+1] < numberList[index]:
                numberList[index+1], numberList[index] = numberList[index], numberList[index+1]
                swapsMade = True
            index += 1
            '''
        elif self.algorithm == 'shellSort':
            algorithmCode = '''
def shellSort(self):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    numberList = self.list.copy()
    for gap in gaps:
        if gap > len(numberList):
            continue
        swapsMade = True
        while swapsMade:
            index = 0
            swapsMade = False
            while index+gap < len(numberList):
                if numberList[index+gap] < numberList[index]:
                    numberList[index], numberList[index+gap] = numberList[index+gap], numberList[index]
                    swapsMade = True
                index += 1
            '''
        elif self.algorithm == 'exchangeSort':
            algorithmCode = '''
def exchangeSort(self):
    numberList = self.list.copy()
    index = 0
    while index < len(numberList)-1:
        compareIndex = index+1
        while compareIndex < len(numberList):
            if numberList[compareIndex] < numberList[index]:
                numberList[index], numberList[compareIndex] = numberList[compareIndex], numberList[index]
            compareIndex += 1 
        index += 1
            '''
        self.text.delete('1.0', tkinter.END)
        self.text.insert(tkinter.END, algorithmCode)

if __name__=='__main__':
    SortingAlgorithmVisualizer()