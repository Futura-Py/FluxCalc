import strsplit

calculation = ""

def bracketcheck():
    global calculation
    if "(" in calculation:
        for i in range(10):
            if strsplit.before(calculation, "(").endswith(str(i)):
                calculation = strsplit.before(calculation, "(") + "*" + str(eval(strsplit.inbetween(calculation, "(", ")"))) + strsplit.after(calculation, ")")
        if "(" in calculation and strsplit.before(calculation, "(") == "":
            calculation = strsplit.after(calculation, "(")
            calculation = str(eval(strsplit.before(calculation, ")"))) + strsplit.after(calculation, ")")
        bracketcheck()
    else: pass


def _btnClick(key):
    global calculation
    calculation = calculation + str(key)
    return calculation

def _btnEqualsInput():
    global calculation
    try:
        bracketcheck()
        return [eval(calculation), calculation]
    except:
        return ["Error", ""]

def _backspace():
    global calculation
    calculation = calculation[:-1]

def _square():
    global calculation
    try:
        int(calculation)
        squared = eval("{}*{}".format(calculation, calculation))        
        if str(squared).endswith(".0"): squared = str(squared).rstrip(".0")
        return [squared, calculation + '²']
    except ValueError:
        if not calculation == "":
            return ["development", "feature still in"]
        else:
            return ["0", ""]