#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pdfrw')


# In[ ]:


import PyPDF2
import re
import xlsxwriter

from pdfrw import PdfReader


# #### Open a pdf file

# In[ ]:


pdfFileObj = open('C:/Users/SurajC/Downloads/desktop/ML/demo1.pdf', 'rb')


# In[ ]:


pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


# In[ ]:


print(pdfReader.numPages)


# In[ ]:


pageObj = pdfReader.getPage(0)


# #### Extract the content from pdf

# In[ ]:


print(pageObj.extractText())


# #### Export to text file

# In[7]:


String = "Maharashtra Sales Tax"
NumPages=pdfReader.numPages

with open("C:/Users/SurajC/Downloads/Desktop/out.txt", "w") as f:
    for i in range(0, NumPages):
        pageObj = pdfReader.getPage(0)
        Text = pageObj.extractText() 
        # print(Text)
        ResSearch = re.search(String, Text)
        print("this is page " + str(i),"&",ResSearch)
        f.write("this is page " + str(i) + str(ResSearch))


# #### Export to excel file

# In[47]:


String = "Maharashtra Sales Tax"
NumPages = pdfReader.numPages
workbook = xlsxwriter.Workbook('C:/Users/SurajC/Downloads/Desktop/ML/out.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0
sum = 0
count = 0

for i in range(0, NumPages):
    pageObj = PyPDF2.PdfFileReader.getPage(i)
    Text = pageObj.extractText() 
    ResSearch = re.search(String, Text)
    if ResSearch is not None :
        count = String.count(String)
        sum = count + sum
        content1 = sum
        content2 = "The word occurs {} times in given pdf".format(sum)
        
worksheet.write(row, column, content1)
worksheet.write(row, column + 1, content2)
row += 1
              
print("The word occurs {} times in {} pdf" .format(sum,object))
workbook.close()


# In[48]:


import PyPDF2
import re

String = "Maharashtra Sales Tax"
NumPages = PyPDF2.PdfFileReader.numPages
workbook = xlsxwriter.Workbook('C:/Users/SurajC/Downloads/Desktop/ML/out.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 0
    

for k in range(1,3):
    # open the pdf file
    object = PdfReader("C:/Users/SurajC/Downloads/Desktop/ML/demo%s.pdf"%(k))
    print(object.Info.Title)
    NumPages = object.getNumPages()

    sum = 0
    count = 0
    content1 = ''
    content2 = ''
    
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText() 
        ResSearch = re.search(String, Text)
        if ResSearch is not None :
            count = String.count(String)
            sum = count + sum
            content1 = sum
            content2 = "The word occurs {} times in {} pdf".format(sum+1,object)
            
    worksheet.write(row, column, content1+1)
    worksheet.write(row, column + 1, content2)
    row += 1
    print("The word occurs {} times in {} pdf" .format(sum+1,object))
    
workbook.close()


# In[ ]:





# In[ ]:




