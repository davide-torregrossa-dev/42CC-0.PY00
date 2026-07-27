def ft_count_harvest_recursive():
    days_amt = input("Days until harvest: ")
    def ft_countdown():
        if ft_countdown.val == ft_countdown.stopat:
            print("Harvest time!")
        else:
            print(f"Day {ft_countdown.val+1}")
            ft_countdown.val += 1
            ft_countdown()
    ft_countdown.stopat = int(days_amt)
    ft_countdown.val = 0
    ft_countdown()