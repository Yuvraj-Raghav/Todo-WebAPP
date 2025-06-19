import streamlit as st

import functions as func

user = st.query_params.get("user", [None])[0]

if not user:
    user = st.text_input("Enter your name to get your personal todo list:")
    if not user:
        st.stop()
filename = f"{user}_todos.txt"

todos = func.get_todos(filename)

def add_todo():

    todo = st.session_state.get('new_todo','').strip()
    if todo:
        todos.append(todo + "\n")
        func.write_todos(todos,filename)
    st.session_state['new_todo'] = ""





st.title(f"{user.capitalize()}'s Todo App")
st.subheader("This is my Todo App.")
st.write("This app is to increase productivity")

for index,todo in enumerate(todos):
    key = f"{todo}_{index}"
    checkbox = st.checkbox(todo,key=key)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos,filename)
        del st.session_state[key]
        st.rerun()
st.text_input(label="Add a new Todo",label_visibility="collapsed",placeholder="Add new todo....",
              on_change=add_todo,key='new_todo')


