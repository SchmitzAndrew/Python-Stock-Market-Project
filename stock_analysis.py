# pulls the data from the csv
# lines= horizontal rows
# output= vertical rows
def get_adjusted_close(stock):
    lines = [line.split(',') for line in stock.readlines()]
    lines.pop(0)
    output = []
    for line in lines:
        output.append(float(line[5]))
    return output

def get_max(stock):
    values = get_adjusted_close(stock)
    out_max = values[0]
    for value in values:
        if value > out_max:
            out_max = value
    return out_max

def get_min(stock):
    values = get_adjusted_close(stock)
    out_min = values[0]
    for value in values:
        if value < out_min:
            out_min = value
    return out_min

def get_avg(stock):
    values = get_adjusted_close(stock)
    out_avg = sum(values) / len(values)
    return out_avg


