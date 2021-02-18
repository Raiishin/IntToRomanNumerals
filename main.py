def IntToRomanNumerals(number, answer):
    digitValue = [
        1000, 900, 600, 500, 400, 100, 90, 60, 50, 40, 10, 9, 6, 5, 4, 1
    ]

    romanDict = {
        1000: "M",
        900: "CM",
        600: "DC",
        500: "C",
        400: "CD",
        100: "C",
        90: "XC",
        60: "LX",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        6: "VI",
        5: "V",
        4: "IV",
        1: "I"
    }

    resultStr = ""
    diffNum = number

    while (diffNum >= 0):
        count = 0
        while count < (len(digitValue)):
            if diffNum - digitValue[count] < 0:
                count += 1
            else:
                diffNum = diffNum - digitValue[count]
                resultStr = resultStr + str(romanDict[digitValue[count]])

        print("Case #" + str(number) + " = " + resultStr)
        if (resultStr == answer):
            print("Correct")
        else:
            print("Wrong")
        return resultStr

#Test Cases
IntToRomanNumerals(125, "CXXV")
IntToRomanNumerals(298, "CCXCVIII")
IntToRomanNumerals(159, "CLIX")
IntToRomanNumerals(943, "CMXLIII")
IntToRomanNumerals(225, "CCXXV")
IntToRomanNumerals(5, "V")
IntToRomanNumerals(15, "XV")
IntToRomanNumerals(29, "XXIX")
IntToRomanNumerals(789, "DCCLXXXIX")
IntToRomanNumerals(956, "CMLVI")
IntToRomanNumerals(716, "DCCXVI")
IntToRomanNumerals(348, "CCCXLVIII")
IntToRomanNumerals(2214, "MMCCXIV")
IntToRomanNumerals(1243, "MCCXLIII")
