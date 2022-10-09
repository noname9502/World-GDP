import matplotlib.pyplot as plt
import pandas as pd
   
Data = {'Country': ['USA','China','Japan','Germany','India'],
        'World GDP': [24.08,15.12,6.02,4.56,3.28]
       }
df = pd.DataFrame(Data,columns=['Country','World GDP'])

New_Colors = ['green','blue','purple','brown','teal']
plt.bar(df['Country'], df['World GDP'], color=New_Colors)
plt.title('Country and World GDP', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('World GDP', fontsize=14)
plt.grid(True)
plt.show()
