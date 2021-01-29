class Metric:
    # geri dönüş değeri emu cinsinden
    def cmToEmu(cmLenght):
        return cmLenght*360000

    # ggeri dönüş değeri cm cinsinden

    def emuToCm(emuLenght):
        return emuLenght/360000

    # geri dönüş değeri emu cinsinden

    def inchToEmu(inchLenght):
        return inchLenght*914400

    # ggeri dönüş değeri inch cinsinden

    def emuToIcnh(emuLenght):
        return emuLenght/914400
    #  https://developers.google.com/slides/reference/rest/v1/Unit


class CheckTrue:
    def checkMargin(existingValue, desiredValue):
        if(existingValue == desiredValue):
            return True
        else:
            return False
