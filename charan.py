#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#QUESTION - 1


# In[5]:


import pandas as pd
print(pd.__version__)


# In[ ]:


#QUESTION - 2


# In[4]:


import numpy as np
import pandas as pd
x=np.array([1,2,3,4,5,6,7,8,9])
print(x)
y=pd.Series(x)
print(y)


# In[ ]:


#QUESTION - 3


# In[3]:


import pandas as pd
df = pd.DataFrame({'RollNumber': ['ECE10', 'ECE25', 'ECE55', 'ECE89'], 
                   'Name': ['sai', 'charan', 'vinay', 'gautham'], 
                   'Marks In Percentage': [97, 90, 70, 82], 
                   'Grade': ['A', 'A', 'C', 'B'], 
                   'Subject': ['Physics', 'Physics', 'Physics', 'Physics']})
                               
x=df.index
print(df)


# In[ ]:


#QUESTION - 4


# In[2]:



import seaborn as sns
mpg=sns.load_dataset('mpg')
print(mpg)


# In[ ]:


#QUESTION - 5


# In[6]:


import seaborn as sns
import pandas as pd
mpg=sns.load_dataset('mpg')
df=pd.DataFrame(mpg)
df.origin


# In[ ]:


#QUESTION - 6


# In[7]:


import seaborn as sns
import pandas as pd
mpg=sns.load_dataset('mpg')
df=pd.DataFrame(mpg)
df[df['origin'].str.contains("usa")]


# In[ ]:




