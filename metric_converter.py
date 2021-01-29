class Metric:
    """
    ENGLISH:
        There are methods that convert the English Metric Unit(EMU) value used in the Word file to centimeters and inches.
        As Source: https://developers.google.com/slides/reference/rest/v1/Unit \n
    TÜRKÇE:
        Word dosyasında kullanılan İngiliz Metrik Birim (EMU) değerini santimetre ve inç'e dönüştüren yöntemler vardır.
        Kaynak Olarak: https://developers.google.com/slides/reference/rest/v1/Unit \n
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
        Returns:\n
            int:
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

        Returns:\n
            int:
                ENGLISH:\n
                    If the given parameter is None, it returns cm value if not 0.\n
                TÜRKÇE:\n
                    Eğer verilen parametre None ise 0 değerini değil ise cm değerini döndürür.\n
        """
        if emuLenght is None:
            return 0
        else:
            return int(emuLenght)/360000

    def inchToEmu(inchLenght):
        """
        ENGLISH:\n
            This method converts inch value given as parameter to English Metric Unit (EMU) value.\n
        TÜRKÇE:\n
            Bu metot parametre olarak verilen inç değerini English Metric Unit(EMU) değerine çevirme işlemini yapar.\n
        Args:\n
            inchLenght (NoneType):
                ENGLISH:\n
                    The parameter type is NoneType if there is no value, and int if there is.\n
                TÜRKÇE:\n
                    Değer yoksa parametre türü NoneType ve varsa int şeklindedir.\n
        Returns:\n
            int:
                ENGLISH:\n
                If the given parameter is None, it returns the value of English Metric Unit (EMU) if it is not 0.\n
                TÜRKÇE:\n
                    Eğer verilen parametre None ise 0 değerini değil ise English Metric Unit(EMU) değerini döndürür.\n
        """
        if inchLenght is None:
            return 0
        else:
            return inchLenght*914400

    def emuToIcnh(emuLenght):
        """
        ENGLISH:\n
            This method converts the English Metric Unit (EMU) value given as a parameter to inch.\n
        TÜRKÇE:\n
            Bu metot parametre olarak verilen English Metric Unit(EMU) değerini inç değerine çevirme işlemini yapar.\n
        Args:\n
            emuLenght (NoneType):
                ENGLISH:\n
                    The parameter type is NoneType if there is no value, and int if there is.\n
                TÜRKÇE:\n
                    Değer yoksa parametre türü NoneType ve varsa int şeklindedir.\n
        Returns:\n
            int:
                ENGLISH:\n
                    If the given parameter is None, it returns inch value if not 0.\n
                TÜRKÇE:\n
                    Eğer verilen parametre None ise 0 değerini değil ise inç değerini döndürür.\n
        """
        if emuLenght is None:
            return 0
        else:
            return emuLenght/914400


class CheckTrue:
    """
    ENGLISH:
        It is the class that contains the methods used in verification and checking.\n
    TÜRKÇE:
        Doğrulama ve kontrol etme işlemlerinde kullanılan metotların bulunduğu sınıftır.\n
    """

    def checkMargin(existingValue, desiredValue):
        """
        ENGLISH:
            It allows to check whether two variables are equal to each other.\n
        TÜRKÇE:
            İki değişkenin birbirine eşit olup olmadığını kontrol etmeyi sağlar.\n
        Args:
            existingValue (NoneType):\n
                ENGLISH:
                    It is the current value we want to compare.\n
                TÜRKÇE:
                    Karşılaştırmak istediğimiz mevcut değerdir.\n
            desiredValue (NoneType):\n
                ENGLISH:
                    It is the value we want to compare.\n
                TÜRKÇE:
                    Karşılaştırmak istediğimiz değerdir.\n
        Returns:
            bool:\n
                ENGLISH:
                    Returns True or False.\n
                TÜRKÇE:
                    Doğru yada Yanlış değerini döndürür.\n
        """
        if(existingValue == desiredValue):
            return True
        else:
            return False
