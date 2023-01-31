# Adapt the shipping costs example to includes free shipping to Canada for 
# purchases over 100 dollars and shipping cost of 10 dollars for purchases 
# under 100 dollars.

total = 100
#country = "US"
country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
    elif total <= 100:
        print("Shipping Cost is $25")
    elif total <= 150:
	    print("Shipping Costs $5")
    else:
        print("Free shipping to the US for purchases over $150")
elif country == "AU": 
    if total <= 50:
        print("Shipping Cost is  $10")
    else:
        print("Free shipping to Austrailia for purchases over $50")