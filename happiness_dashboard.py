import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache
def load_happiness_data ():
    return pd.read_csv( '2019.csv' )

happiness = load_happiness_data()

st.title("World Happiness Scores")
st.write(""" 
 """)

st.sidebar.markdown('''This data set from the World Happiness Report ranks countries by their happiness scores. This 
                    organization asked around 1000 people in each country to give them a score on these factors, such as 
                    freedom and generosity. Explore the data set to see which variables factor into the happiness score 
                    and see which countries were the happiest in 2019. Can you guess which variable mattered the most?''')

# User values
user_number = st.sidebar.slider("Choose how many countries you would like to view:", 1, 156, 10, 1)
user_column = st.sidebar.selectbox("Choose the variable you would like to view:", ('GDP per capita', 'Social support',
                        'Healthy life expectancy', 'Freedom to make life choices', 'Generosity',
                        'Perceptions of corruption'))
top_or_bottom = st.sidebar.selectbox("Choose if you want to look at the smallest or largest values for countries within that variable:",
                             ("Smallest", "Largest"))

# Getting top/bottom n values
if top_or_bottom == "Largest":
    countries = happiness.nlargest(user_number, user_column)
else:
    countries = happiness.nsmallest(user_number, user_column)

# Plotting
plt.figure(figsize=(10,8))
plt.scatter(countries[user_column], countries['Score'], c = 'red')
plt.xlabel(user_column, fontsize = 20)
plt.ylabel('Happiness Score', fontsize = 20)
title = 'Score vs. ' + user_column
plt.title(title, fontsize = 25)

# Plotting the name of the countries
def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'] + .002, point['y'], str(point['val']))

label_point(countries[user_column], countries['Score'], countries['Country or region'], plt.gca())

st.pyplot(plt.gcf())
