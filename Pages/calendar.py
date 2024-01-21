import streamlit as st
import calendar
import datetime
from datetime import date


st.title("Calendar")

daily, weekly, monthly = st.tabs(["Daily", "Weekly", "Monthly"])


with daily:
       
       st.title("Daily Check-In")

       todayDay = date.today()
       
       selectedDate = st.date_input("Select a date:", todayDay)
       
       st.write("Today's date is:", selectedDate)

        #code logic from https://www.youtube.com/watch?v=frWARrEczb4

       userDailyEvent = st.text_input("Enter an event for today: ")
       if st.button("Add Daily Event") and userDailyEvent:
                st.session_state["events_list"].append(userDailyEvent)
                
       if "events_list" not in st.session_state:
                st.session_state["events_list"] = []

       displayEvents = []

       for i, e in enumerate(st.session_state["events_list"]):
                displayEvents.append(e)

       st.markdown("Today's Events:")
       for i, e in enumerate(displayEvents):
                st.checkbox(f"{i+1}. {e}")
                st.divider()

 
with weekly:
        def myWeeklyCalendar(start_day):
                daysWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                currentDayIndex = daysWeek.index(start_day)
                week_calendar = []

                for i in range(7):
                        week_calendar.append((daysWeek[currentDayIndex],))
                        currentDayIndex = (currentDayIndex + 1) % 7

                return week_calendar

        st.title("Weekly Calendar")


        selectedDay = st.selectbox("Select weekday:", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

        weekly_calendar = myWeeklyCalendar(selectedDay)

        st.write("Weekly Calendar for :")
        for day in weekly_calendar:
                st.write(f"{day[0]}")
                
with monthly:     
        def myMonthlyCalendar(year, month):
                cal = calendar.monthcalendar(year, month)
                header = calendar.month_name[month] + " " + str(year)

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

        event = st.sidebar.text_input("Enter Event:")

        todayMonth = date.today()

        
        date_input = st.sidebar.date_input("Enter a date: ", todayMonth)

        time_input = st.time_input("Enter a time: ", datetime.time(12, 00))



        if st.sidebar.button("Add Event") and event:
                 if event:
                         st.session_state["events"].append(event)


        if st.sidebar.button("Delete Event") and event:
                 if event:
                         st.session_state["list_list"].remove(event)

        if "events" not in st.session_state:
                st.session_state["events"] = []


        st.title("Monthly Calendar")
    
        year = st.number_input("Enter the year:", min_value=1900, max_value=2100, value=2022)
        month = st.slider("Select the month:", 1, 12, 1)



        calendar_html = myMonthlyCalendar(year, month)
        st.markdown(calendar_html, unsafe_allow_html=True)

 
        

    

    