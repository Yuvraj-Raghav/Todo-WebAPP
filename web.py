import streamlit as st

import functions as func


todos = func.get_todos()

def add_todo():

    todo = st.session_state['new_todo']
    if todo.strip():
        todos.append(todo + "\n")
        func.write_todos(todos)
    st.session_state['new_todo'] = ""


st.title("My Todo App")
st.subheader("This is my Todo App.")
st.write("This app is to increase productivity")

for index,todo in enumerate(todos):
    key = f"{todo}_{index}"
    checkbox = st.checkbox(todo,key=key)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[key]
        st.rerun()
st.text_input(label="Add a new Todo",label_visibility="collapsed",placeholder="Add new todo....",
              on_change=add_todo,key='new_todo')


