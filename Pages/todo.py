import streamlit as st

st.title("To-Do List App")

 # Create a dictionary to store tasks for each list
task_lists = {}

# Sidebar for creating new lists
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

    # Add Tasks
        
    

    # Display current lists
st.sidebar.markdown("Current Lists:")
selected_list = st.sidebar.selectbox("", options)

    # Add tasks to selected list, code used from video
task_input = st.text_input("Add Task:")
if st.button("Add Task"):
    if task_input:
        st.session_state["task_list"].append(task_input)

if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

for i, t in enumerate(st.session_state["task_list"]):
    st.checkbox(f"{i+1}: {t}")

## get a way to remove checkboxes
## get them in list!
# then youre done




