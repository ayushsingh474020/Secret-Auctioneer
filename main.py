from art import logo
print(logo)
bidders={}
choice="y"
while choice=="y":
  user=input("Enter your name: ")
  bid=int(input("Enter your bid: "))
  bidders[user]=bid
  choice=input("Are there other bidders: (y/n)")
  
max=0
max_bidder=""
for items in bidders:
  if(max<bidders[items]):
    max=bidders[items]
    max_bidder=items

print(f"Highest bidder is {max_bidder} and his bid is {max}")