from collections import namedtuple
def can_take_order(driver,num_package):
    return driver.carcapacity>=num_package

def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    driver = namedtuple("driver",["name","cartype", "carcapacity"])
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    iris = driver("Iris", "Toyota Prius", 7)
    shahid = driver("Shahid", "Innova", 8)
    Semeena = driver("Semeena","BMW", 4)
    #check if they can take a certain order, given their car's capacity.
    print(can_take_order(shahid,5))
    return

if __name__ == "__main__":
    main()