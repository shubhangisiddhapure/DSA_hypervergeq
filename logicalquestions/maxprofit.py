# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def maxProfit(prices):
    maxprofit=0
    j=0
    i=0
    while(i<len(prices)):
        profit=prices[i]-prices[j]
        if(profit>maxprofit):
            maxprofit=profit
        elif(prices[i]<prices[j]):
            j=i
        i+=1
    return maxprofit
print(maxProfit([7,1,5,3,6,4]))
