with open("read_write_file\\stocks.csv", "r") as f, open("read_write_file\\output.csv","w") as c:
    c.write("Company Name,PE Ratio, PB Ratio\n")
    next(f) # next header
    for line in f:
        token = line.split(",")
        stocks = token[0]
        price = float(token[1])
        EPS = float(token[2])
        BV = float(token[3])
        pe_ratio = round(price / EPS, 2)
        pb_ratio = round(price / BV, 2)
        c.write(f"{stocks},{pe_ratio},{pb_ratio}\n")
        
        
        