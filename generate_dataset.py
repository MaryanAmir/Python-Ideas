import pandas as pd
import numpy as np
import random
import os 

output_folder = r"D:\POWER BI_M_Analysis\PROJ2 Excel"

products = ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard",
            "Mouse", "Headset", "Printer", "Webcam", "External Hard Drive"
            ]

distributors = ["Cairo Distributor","Alexandria Distributor","Delta Distributor",
    "Canal Distributor","Upper Egypt Distributor"
]

prices = {"Laptop": 25000, "Smartphone": 15000, "Tablet": 9000, 
          "Monitor": 6000, "Keyboard": 1200, "Mouse": 500,
          "Headset": 1500, "Printer": 7000, "Webcam": 2000, "External Hard Drive": 3500
}

dates = pd.date_range(
    start="2025-01-01",
    end="2025-12-31",
    freq="D"
)

n = 5000

df= pd.DataFrame({
    'Date':np.random.choice(dates,n),
    'Distributor':np.random.choice(distributors,n),
    'Products':np.random.choice(products,n),
    'Quantity':np.random.randint(1,50,n),

})


df["Unit Price"] = df["Products"].map(prices)
df['sales_amount'] = df['Quantity'] * df["Unit Price"]

#Changes in products helps us in cleaning stage
#df.loc[df.sample(frac=0.02).index, "Products"] = "laptop"
#1

laptop_rows = df[df["Products"] == "Laptop"].sample(frac=0.1).index
df.loc[laptop_rows, "Products"] = "laptop"

#2
cairo_rows = df[df["Distributor"] == "Cairo Distributor"].sample(frac=0.1).index
df.loc[cairo_rows, "Distributor"] = "cairo distributor"

#3
#df["Date"] = df["Date"].dt.strftime("%d/%m/%Y")


#5 disttibutions
for distributor in distributors:
    #file_name = distributor.replace(" ", "_") + ".xlsx"
    file_name = os.path.join(output_folder,distributor.replace(" ", "_") + ".xlsx")
    df[df["Distributor"] == distributor].to_excel(file_name, index=False)
print("Files created successfully!")


print(df.head())



#df.to_excel('new.xlsx',index=False)