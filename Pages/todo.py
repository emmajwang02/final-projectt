import streamlit as st

st.title("To-Do List App")

task_lists = {}

#code logic from Source: https://www.youtube.com/watch?v=frWARrEczb4
#list addition and removal

list_name = st.sidebar.text_input("Enter List Name:")
if st.sidebar.button("Create List") and list_name:
     if list_name:
        st.session_state["list_list"].append(list_name)

if st.sidebar.button("Delete List") and list_name:
    if list_name:
            st.session_state["list_list"].remove(list_name)

if "list_list" not in st.session_state:
     st.session_state["list_list"] = []

#idk this just helped print the checkbox

options = []

for i, l in enumerate(st.session_state["list_list"]):
     options.append(l)


st.sidebar.markdown("Current Lists:")
selected_list = st.sidebar.selectbox("", options)

#add task to a specific list when the button is pressed, logic is when button = true, task_input added to list and added to dicitonary as a value (the selected list is a key)

task_input = st.text_input("Add Task:")
if st.button("Add Task") and task_input:
    if task_input:
        st.session_state["task_list"].append(task_input)
        task_lists[selected_list] = task_input


st.markdown(f"{selected_list} Tasks:")

if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

#if the selectedlist is in the dict, task_lists, loop begins and the tasks in the list start printing
if selected_list in task_lists:
    for i, t in enumerate(st.session_state["task_list"]):
        st.checkbox(f"{i+1}: {t}")
            



