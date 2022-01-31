t_var =0
var = 0
for i in range(1, 100001):
        var = (-1) ** (i+1) /((2 * i)-1)
        t_var = t_var + var
        print(t_var * 4)