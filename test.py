variable_1 = "HELLO"
variable_2 = "ADIOS"
varlist = [variable_1,variable_2]
var_string = ', '.join('?' * len(varlist))
print(var_string)