class Metric:
    # geri dönüş değeri emu cinsinden
    def cmToEmu(cmLenght):
        if cmLenght is None:
            return 0
        else:
            return cmLenght*360000

    # ggeri dönüş değeri cm cinsinden

    def emuToCm(emuLenght):
        if emuLenght is None:
            return 0
        else:
            return int(emuLenght)/360000

    # geri dönüş değeri emu cinsinden

    def inchToEmu(inchLenght):
        if inchLenght is None:
            return 0
        else:
            return inchLenght*914400

    # ggeri dönüş değeri inch cinsinden

    def emuToIcnh(emuLenght):
        if emuLenght is None:
            return 0
        else:
            return emuLenght/914400
    #  https://developers.google.com/slides/reference/rest/v1/Unit


class CheckTrue:
    def checkMargin(existingValue, desiredValue):
        if(existingValue == desiredValue):
            return True
        else:
            return False
