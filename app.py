#!/usr/bin/env python
# coding: utf-8

# In[42]:


from flask import Flask, render_template, request


# In[43]:


import joblib


# In[44]:


app = Flask(__name__)


# In[45]:


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model = joblib.load("regression")
        pred = model.predict([[rates]])
        return (render_template("index.html",result = pred))
    else :
        return (render_template("index.html",result = "WAITING"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




