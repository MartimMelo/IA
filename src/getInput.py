class getInput:
    def getFloat(text):
        numero = input(text)
        try:
            numero = float(numero)
        except ValueError:
            print("Invalid number!")
            return getInput.getFloat(text)
        return numero
        
    def getInt(text):
        numero = input(text)
        try:
            numero = int(numero)
        except ValueError:
            print("Invalid number!")
            return getInput.getInt(text)
        return numero