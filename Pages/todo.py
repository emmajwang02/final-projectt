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

options = []

for i, l in enumerate(st.session_state["list_list"]):
     options.append(l)


st.sidebar.markdown("Current Lists:")
selected_list = st.sidebar.selectbox("", options)

#add task to a specific list

task_input = st.text_input("Add Task:")
if st.button("Add Task") and task_input:
    if task_input:
        st.session_state["task_list"].append(task_input)
        task_lists[selected_list] = task_input


st.markdown(f"{selected_list} Tasks:")

if "task_list" not in st.session_state:
    st.session_state["task_list"] = []


if selected_list in task_lists:
    tasks = task_lists[selected_list]
    for i, t in enumerate(st.session_state["task_list"]):
        st.checkbox(f"{i+1}: {t}")
            



