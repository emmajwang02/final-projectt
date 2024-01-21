import streamlit as st 
from datetime import datetime

st.title('Reminders')

if 'reminders' not in st.session_state:
    st.session_state.reminders = []

def addReminder():
    task = st.text_input("Task:")
    dueDate = st.date_input("Due Date:", min_value=datetime.today())
    
    if st.button("Add Reminder"):
        st.session_state.reminders.append({'Task': task, 'Due Date': dueDate, 'Completed': False})
        st.success(f"Reminder '{task}' added successfully!")

def displayReminders():
    st.header("Current Reminders")
    if not st.session_state.reminders:
        st.info("No reminders available.")
    else:
        remindersTable = []
        for reminder in st.session_state.reminders:
            remindersTable.append([reminder['Task'], reminder['Due Date'], reminder['Completed']])
        st.table(remindersTable)
        
        completed_tasks = [task['Task'] for task in st.session_state.reminders if task['Completed']]
        if completed_tasks:
            st.success("Task(s) completed:")
            for task in completed_tasks:
                st.write(f"- {task}")

def removeReminders():
    st.session_state.reminders = [task for task in st.session_state.reminders if not task['Completed']]
    st.success("Completed reminders removed.")

def completeTask(taskDone):
    st.session_state.reminders[taskDone]['Completed'] = True
    st.success(f"Task '{st.session_state.reminders[taskDone]['Task']}' marked as completed!")

page = st.sidebar.selectbox("Select Page", ["Add Reminder", "View Reminders", "Remove Completed Reminders"])

if page == "Add Reminder":
    addReminder()
elif page == "View Reminders":
    displayReminders()
    if st.session_state.reminders:
        taskToDo = st.selectbox("Mark Task as Completed:", [task['Task'] for task in st.session_state.reminders])
        taskEnum = [i for i, task in enumerate(st.session_state.reminders) if task['Task'] == taskToDo][0]
        if st.button("Mark as Completed"):
            completeTask(taskEnum)
elif page == "Remove Completed Reminders":
    removeReminders()


