import pandas as pd

IDG = pd.DataFrame([
        {"I":"i0", "D": "d0", "G": "g1", "Prob": 0.126},
        {"I":"i0", "D": "d0", "G": "g2", "Prob": 0.168},
        {"I":"i0", "D": "d0", "G": "g3", "Prob": 0.126},
        {"I":"i0", "D": "d1", "G": "g1", "Prob": 0.009},
        {"I":"i0", "D": "d1", "G": "g2", "Prob": 0.045},
        {"I":"i0", "D": "d1", "G": "g3", "Prob": 0.126},
        {"I":"i1", "D": "d0", "G": "g1", "Prob": 0.252},
        {"I":"i1", "D": "d0", "G": "g2", "Prob": 0.0224},
        {"I":"i1", "D": "d0", "G": "g3", "Prob": 0.0056},
        {"I":"i1", "D": "d1", "G": "g1", "Prob": 0.06},
        {"I":"i1", "D": "d1", "G": "g2", "Prob": 0.036},
        {"I":"i1", "D": "d1", "G": "g3", "Prob": 0.024},
    ])
# display(HTML(IDG.to_html(index=False)))


# In[16]:

ID = IDG.groupby(['D', 'I']).sum()
ID


# In[21]:

pd.DataFrame(ID)


# In[ ]:



