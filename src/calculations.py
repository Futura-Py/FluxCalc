calculation = ""

def _btnClick(key):
    global calculation
    calculation = calculation + str(key)
    return calculation

def _btnEqualsInput():
    try:
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
        return ["development", "feature still in"]