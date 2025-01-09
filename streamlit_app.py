import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# App structure
def main():
    # Set up the page layout
    st.set_page_config(page_title="Dashboard App", layout="wide")
    
    # Sidebar menu
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Select a page:", ["Home", "Visualization 1", "Visualization 2", "About"])
    
    # Render content based on menu selection
    if menu == "Home":
        home()
    elif menu == "Visualization 1":
        visualization_1()
    elif menu == "Visualization 2":
        visualization_2()
    elif menu == "About":
        about()

# Home page
def home():
    st.title("Welcome to the Dashboard")
    st.write("""
    This is a sample Streamlit app with a menu on the left side and dynamic dashboard content.
    Use the menu to navigate through the visualizations.
    """)

# Visualization 1
def visualization_1():
    st.title("Visualization 1: Random Data")
    
    # Generate some random data
    data = np.random.randn(100)
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color='skyblue', edgecolor='black')
    ax.set_title("Random Data Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    
    # Display the plot
    st.pyplot(fig)

# Visualization 2
def visualization_2():
    st.title("Visualization 2: Correlation Heatmap")
    
    # Generate a random DataFrame
    df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
    
    # Compute the correlation matrix
    corr = df.corr()
    
    # Plot the heatmap
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Correlation Heatmap")
    
    # Display the plot
    st.pyplot(fig)

# About page
def about():
    st.title("About This App")
    st.write("""
    This app demonstrates the structure of a Streamlit dashboard with:
    - A menu on the left side.
    - Dynamic visualizations in the center.
    - Simple navigation and interactivity.
    """)
    st.write("Built with Streamlit. 🖥️")

# Run the app
if __name__ == "__main__":
    main()
