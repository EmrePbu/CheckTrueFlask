class Metric:
    """
    ENGLISH:
        There are methods that convert the English Metric Unit(EMU) value used in the Word file to centimeters and inches.
    As Source: https://developers.google.com/slides/reference/rest/v1/Unit
    TÜRKÇE:
        Word dosyasında kullanılan İngiliz Metrik Birim (EMU) değerini santimetre ve inç'e dönüştüren yöntemler vardır.
    Kaynak Olarak: https://developers.google.com/slides/reference/rest/v1/Unit
    """
    def cmToEmu(cmLenght):
        """
        ENGLISH:\n
            This method converts the cm value given as a parameter to the British Metric Unit (EMU) value.\n
        TÜRKÇE:\n
            Bu metot parametre olarak verilen cm değerini English Metric Unit(EMU) değerine çevirme işlemini yapar.\n

        Args:\n
            cmLenght (NoneType):
                ENGLISH:\n
                    The parameter type is NoneType if there is no value, and int if there is.\n
                TÜRKÇE:\n
                    Değer yoksa parametre türü NoneType ve varsa int şeklindedir.\n

        Returns:
            int:\n
                ENGLISH:\n
                If the given parameter is None, it returns the value of English Metric Unit (EMU) if it is not 0.\n
                TÜRKÇE:\n
                    Eğer verilen parametre None ise 0 değerini değil ise English Metric Unit(EMU) değerini döndürür.\n
        """
        if cmLenght is None:
            return 0
        else:
            return cmLenght*360000

    def emuToCm(emuLenght):
        """
        ENGLISH:\n
            This method converts the English Metric Unit (EMU) value given as a parameter to cm.\n
        TÜRKÇE:\n
            Bu metot parametre olarak verilen English Metric Unit(EMU) değerini cm değerine çevirme işlemini yapar.\n

        Args:\n
            emuLenght (NoneType):
                ENGLISH:\n
                    The parameter type is NoneType if there is no value, and int if there is.\n
                TÜRKÇE:\n
                    Değer yoksa parametre türü NoneType ve varsa int şeklindedir.\n

        Returns:
            int:\n
                ENGLISH:\n
                    If the given parameter is None, it returns cm value if not 0.\n
                TÜRKÇE:\n
                    Eğer verilen parametre None ise 0 değerini değil ise cm değerini döndürür.\n
        """
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


class CheckTrue:
    def checkMargin(existingValue, desiredValue):
        if(existingValue == desiredValue):
            return True
        else:
            return False
