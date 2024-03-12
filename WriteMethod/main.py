import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense
import graphviz
import plotly.graph_objects as go
from bokeh.plotting import figure
from sympy import symbols, Eq
st.title("This are some text Examples using write method")
# """ FUNCTION SIGNATURE """
# st.write(*args, unsafe_allow_html=False, **kwargs) #
# """  *args (any) 
#      One or many objects to print to the App.
#      Arguments are handled as follows:    """
# 1 write(string) : Prints the formatted Markdown string, with
# support for LaTeX expression, emoji shortcodes, and colored text
# "Example: Markdown Text"
st.write("This is *italic* and this is **bold**.")

# "Example: LaTex Text"
st.write("This is a LaTeX expression: $e^{i\pi} + 1 = 0$")

#"Example: Emoji short codes "
st.write("Here's an emoji: :smile:")

#"Example: Coloured Text"
st.write("This text is <span style='color:red;'>red</span>.")
st.header(" This a sample DataFrame using write method")
dt = pd.read_csv(r"WriteMethod/SampleCSVFile_11kb.csv", encoding='latin1')
st.write(dt)
st.header("Dictionary")
# Define a dictionary
my_dict = {
    'Name': 'John Doe',
    'Age': 30,
    'Location': 'New York',
    'Occupation': 'Engineer'
}

# Display the dictionary
st.write(my_dict)


# Error example
st.header("Error Example")
try:
    x = 1 / 0
except Exception as e:
    st.write(e)

# Function example
st.header("Function description-Doc String")
def greet(name):
    return f"Hello, {name}!"

st.write(greet)

# Module example
st.header("Module description-Doc String")
import math
st.write(math)

# Class example
st.header("Class description-Doc String")
class MyClass:
    def __init__(self, name):
        self.name = name

st.write(MyClass)

# Matplotlib figure example
st.header("Matplotlib figure example")
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.write(fig)


# Generator example
st.header("Generator example")
def my_generator():
    for i in range(5):
        yield i

st.write(my_generator())

# Altair chart example
st.header(" Altair chart example")
data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
chart = alt.Chart(data).mark_point().encode(x='x', y='y')
st.write(chart)

# PIL Image example
st.header(" PIL Image example")
image = Image.open(r"WriteMethod/narutoandjiraya.jpg")
st.write(image)

# Keras model example
st.header("Keras model example")
model = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),
    Dense(10, activation='softmax')
])
st.write(model)

# Graphviz graph example
st.header("Graphviz graph example")
dot = graphviz.Digraph()
dot.node('A')
dot.node('B')
dot.edges(['AB'])
st.write(dot)

# Plotly figure example
st.header("Plotly figure example")
fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 1, 2]))
st.write(fig)

# Bokeh figure example
from bokeh.plotting import figure
st.header("Bokeh figure example")
p = figure(width=400, height=400)
p.circle([1, 2, 3], [4, 5, 6], size=20)
st.bokeh_chart(p)

# SymPy expression example
st.header("SymPy expression example")
x, y = symbols('x y')
eq = Eq(x + y, 5)
st.write(eq)

# HTMLable example
st.header("HTML Code Rendering into streamlit")
class HTMLcode:
    def _repr_html_(self):
        # Construct a large HTML code
        html_code = """
        <html>
        <head>
            <h1>Large HTML Example</h1>
        </head>
        <body>
            <h1>This is a large HTML code</h1>
            <p>You can include any amount of HTML content here.</p>
            <!-- Include more HTML code as needed -->
        </body>
        </html>
        """
        # Return the HTML code
        return html_code

obj = HTMLcode()
st.write(obj)

# Variable(Object) example
st.header("Variable(Object) example")
obj = 42
st.write(obj)
