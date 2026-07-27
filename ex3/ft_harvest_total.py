def ft_harvest_total():
    days_amt = 3
    days = [""] * days_amt
    i = 0
    while (i < days_amt):
        days[i] = input(f"Day {i+1} harvest: ")
        i += 1
    i = 0
    summ = 0
    while (i < days_amt):
        summ += int(days[i])
        i += 1
    print("Total harvest:", summ)
