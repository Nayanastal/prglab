class ElectricityBill:
    
    slab1_rate = 3.50  
    slab2_rate = 4.50 
    slab3_rate = 6.00  
    
    def __init__(self, units_consumed):
       
        self.units_consumed = units_consumed
    
    def calculate_bill(self):
        
        bill_amount = 0
        
        if self.units_consumed <= 100:
           
            bill_amount = self.units_consumed * self.slab1_rate
        elif self.units_consumed <= 200:
           
            bill_amount = (100 * self.slab1_rate) + ((self.units_consumed - 100) * self.slab2_rate)
        else:
           
            bill_amount = (100 * self.slab1_rate) + (100 * self.slab2_rate) + ((self.units_consumed - 200) * self.slab3_rate)
        
        return bill_amount


try:
    units = int(input("Enter the number of units consumed: "))
    
   
    bill = ElectricityBill(units)
    
    
    print(f"Total electricity bill for {units} units is: ${bill.calculate_bill():.2f}")
except ValueError:
    print("Invalid input! Please enter a valid integer for units consumed.")
