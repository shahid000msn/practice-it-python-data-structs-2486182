from collections import Counter
def main():
    #suppose we have an invetory
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    #we meed to subtract/sell 5 starters, 3 salads, and 3 entrees
    sales_this_week = Counter(STA001=5, SAL002=3, ENT004=2)
    inventory = inventory- sales_this_week

    #we can also do update as below
    inventory_in = {"STA001":9, "SAL002": 1}
    inventory.update(inventory_in)
    print(inventory)

if __name__ == "__main__":
    main()