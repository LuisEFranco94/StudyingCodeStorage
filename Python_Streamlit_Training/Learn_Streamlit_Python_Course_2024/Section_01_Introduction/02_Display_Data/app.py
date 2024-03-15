# Core Pkgs
import streamlit as st 

# Load EDA Pkgs
import pandas as pd 
import numpy as np



def main():
	st.title("Plotting In Streamlit")
	# Load Dataset
	df1 = pd.read_csv("data/iris.csv")
	df2 = pd.read_csv("data/lang_data.csv")
	st.dataframe(df1.head())
	st.divider()
	st.dataframe(df2.head())
	# Plotting with Plotly

	

	

if __name__ == '__main__':
	main()










































