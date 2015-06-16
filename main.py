__author__ = 'Carlos'

import logicCalc

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class CalculatorRoot(BoxLayout):
    screen_output = StringProperty()

    statusVariables = {
        "DATASCREEN" : "0",
        "DATABACKSCREEN" : None,
        "OPERATOR" : None,
        "LASTCLICK" : None,
        "MEMORY" : "0" } ;

    def __init__(self):
        super(CalculatorRoot, self).__init__()
        #self.screen_output = self.statusVariables["DATASCREEN"]


    def pressAnyButton(self, inputData):
        self.statusVariables = logicCalc.Calculator(self.statusVariables, inputData).getData()
        self.screen_output = self.statusVariables["DATASCREEN"]
        print self.statusVariables


class CalculatorApp(App):
    pass

if __name__ == '__main__':
    CalculatorApp().run()


