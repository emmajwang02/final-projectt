import streamlit as st


def main():
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

    # Display current lists
    st.sidebar.markdown("Current Lists:")
    selected_list = st.sidebar.selectbox("", options)

    # Add tasks to selected list
    task_input = st.text_input("Add Task:")
    if st.button("Add Task") and task_input:
        task_lists[selected_list] = task_input    

 
            

if __name__ == "__main__":
    main()

