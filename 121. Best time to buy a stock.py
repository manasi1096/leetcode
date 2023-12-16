def sliding_window(input):
  l,r = 0,1
  max_profit = 0
  while r < len(input):

    if input[r]>input[l]:

      profit = input[r] - input[l]
      if profit > max_profit:
        max_profit = profit
    else:
      l = r
    r = r+1
  return max_profit
