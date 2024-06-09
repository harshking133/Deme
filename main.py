import streamlit as st

st.title("Welcome to my first website")

st.header("Python")

st.subheader("Starting Python:")

st.text("""Open Python IDE or any other text editor of your preferred choice. Let's
understand Python code execution with the simplest print statement.
Type the following in the IDE: """)

st.code("""print("Hello World !!!")""")

st.text("""Now save the file with a .py extension and Run it. You will get the following 
output: """)

st.code("""Hello World !!!""")

st.subheader("Installing Packages:")

st.text("""To install packages in Python, we use the pip command. 
e.g. pip install "Package Name"

Following command installs pandas package in Python""")

st.code("""pip install pandas""")

st.subheader("What is Syntax?")

st.text("""In simplest words, Syntax is the 
arrangement of words 
and phrases to create well-formed 
sentences in a language. In the case of a 
computer language, 
the syntax is the structural arrangement 
of comments, 
variables, numbers, operators, statements, 
loops, functions, 
classes, objects, etc. which helps us 
understand the meaning 
or semantics of a computer language.

For E.g. a 'comment' is used to explain the 
functioning of a block of code. It starts with 
a '#'.

More on comments in the comments 
chapter.

For E.g. a block of code is identified 
by an 'indentation'.
Have a look at the following 
code, here print(i) 
is said to be indented with respect 
to the link 
above it. In simple words,
indentation is the addition 
of spaces before the line "print(i)""")

st.code("""for i in range(5):
    print(i)""")