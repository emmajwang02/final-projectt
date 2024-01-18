import streamlit as st
import pandas as pd
import calendar
import numpy as np

    
# Create a table to display the calendar
def generate_monthly_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    header = calendar.month_name[month] + " " + str(year)
    
    # Create a table to display the calendar
    table = "<table style='width:100%'>"
    table = "<table style='neight:200%'>"
    table += "<tr><th colspan='7'>" + header + "</th></tr>"
    table += "<tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr>"
    
    for week in cal:
        table += "<tr>"
        for day in week:
            if day == 0:
                table += "<td></td>"
            else:
                table += "<td>" + str(day) + "</td>"
        table += "</tr>"
    
    table += "</table>"
    
    return table

st.title("Monthly Calendar Generator")
    
# Get user input for the year and month
year = st.number_input("Enter the year:", min_value=1900, max_value=2100, value=2022)
month = st.slider("Select the month:", 1, 12, 1)

# Generate and display the monthly calendar
calendar_html = generate_monthly_calendar(year, month)
st.markdown(calendar_html, unsafe_allow_html=True)

    

    