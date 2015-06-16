__author__ = 'Carlos'


class Calculator:
    def __init__(self, statusVariables, inputData):
        self.dataScreen = statusVariables["DATASCREEN"]
        self.operator = statusVariables["OPERATOR"]
        self.dataBack = statusVariables["DATABACKSCREEN"]
        self.lastClick = statusVariables["LASTCLICK"]
        self.memory = statusVariables["MEMORY"]
        self.button = inputData

        if (self.lastClick is "isError") or (self.dataScreen is "inf"):
            if self.button == "CLEAN":  #elimina calculo actual
                self.buttonClear()
        else:
            if self.button in "0123456789.":
                self.addNumber()
            elif self.button in ("ADD", "SUBT", "MULTIP", "DIVIS" ):
                self.setOperator()
            elif self.button == "EQUAL":
                self.setEqual()
            elif self.button == "CLEARENTRY": #elimina ultimo numero
                self.buttonCE()
            elif self.button == "CLEAN":  #elimina calculo actual
                self.buttonClear()
            elif self.button == "MCLEAN": #clear memory
                self.buttonMC()
            elif self.button == "MRECOV": #recupera memory
                self.buttonMR()
            elif self.button == "MSAVE": #save numero
                self.buttonMS()
            elif self.button == "MPLUS": #almacena numero
                self.buttonMPlus()

            else:
                # DO NOTHING, WRONG INPUT
                print "nada hago 32"
                pass



    def getData(self):
        while (self.dataScreen[0] is "0"):  #Delete zeros on the right
            try:
                if (len(self.dataScreen) > 0) and (self.dataScreen[1] != "."):
                    self.dataScreen = self.dataScreen[1:]
                else: break
            except: break

        if self.dataScreen.endswith(".0") and self.lastClick is not "isNumber":
            self.dataScreen = self.dataScreen[:-2]

        return {"DATASCREEN": self.dataScreen,
                "DATABACKSCREEN": self.dataBack,
                "OPERATOR": self.operator,
                "LASTCLICK": self.lastClick,
                "MEMORY": self.memory }

    def addNumber(self):
        if '.' in self.dataScreen and self.button == ".":
            pass  # DO NOTHING NOT POSSIBLE TO ADD SECOND "."
        elif self.lastClick is None:
            self.dataScreen = self.button
        elif self.lastClick in ("isEqual", "isOperat"):
            self.dataBack = self.dataScreen
            self.dataScreen = self.button
        elif self.lastClick is "isNumber":
            self.dataScreen = self.dataScreen + self.button
        self.lastClick = "isNumber"

    def setOperator(self):

        if (self.operator is None) or (self.lastClick is "isOperat" or "isEqual"):
            #ASSIGN OPERATOR #UPDATE OPERATOR
            self.operator = self.button
        elif self.lastClick is "isNumber":
            self.operator = self.button
            self.makeCalculation()

        self.lastClick = "isOperat"

    def setEqual(self):
        if self.operator is None:
            pass  # DO NOTHING NOT OPERATOR NOT OPERATION
        elif self.lastClick is not "isEqual":
            temp = self.dataScreen
            self.makeCalculation()
            self.dataBack = temp
        elif self.lastClick is "isEqual":
            self.makeCalculation()

        if self.lastClick is not "isError": #Only is there is not error adjust to equal
            self.lastClick = "isEqual"

    def makeCalculation(self):
        y = float(self.dataScreen)
        if self.dataBack is None: x = y
        else: x = float(self.dataBack)

        if self.operator == "ADD":
            y = x + y
        elif self.operator == "SUBT":
            y = x - y
        elif self.operator == "MULTIP":
            y = x * y
        elif self.operator == "DIVIS":
            try:
                y = x / y
            except ZeroDivisionError:
                y = "Error, Division by zero."
                self.lastClick = "isError"

        self.dataScreen = str(y)

    def buttonCE(self):
        self.dataScreen = "0"

    def buttonClear(self):
        self.buttonCE()
        self.dataBack = None
        self.operator = None
        self.lastClick = None
        self.buttonMC()

    def buttonMS(self):
        self.memory = self.dataScreen

    def buttonMR(self):
        self.dataScreen = self.memory

    def buttonMPlus(self):
        self.memory = str(float(self.memory) + float(self.dataScreen))

    def buttonMC(self):
        self.memory = "0"


