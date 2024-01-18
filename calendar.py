import streamlit as st
import calendar
import pandas as pd
import numpy as np

st.title('Calendar')

daily, weekly, biweekly, monthly,  = st.tabs(["Daily", "Weekly", "Biweekly", "Monthly"])

with monthly: 

        monthList = {"January": 1, "Febuary": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July":7, "August": 8, "September": 9, "October": 10, "November":11, "December":12}

        # Input for month and year
        monthInput = st.selectbox("Select month:", monthList.keys())
        year = st.slider("Select Year:", 1900, 2100, 2022)


        
         # Display the calendar
        st.write(f"Calendar for {monthInput} {year}")

        col_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        monthCal = pd.DataFrame(np.random.randn(5, 7), columns=(col_names))

        st.table(monthCal)

    

    