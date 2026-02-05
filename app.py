import pandas as pd
import plotly.express as px
import streamlit as st

def top_n_emitters(df, start_year=2008, end_year=2011, nb_displayed=10):
    
    selected_years = df[(df["Year"] >= start_year) & (df["Year"] <= end_year)]
    mean_df = pd.DataFrame(selected_years.groupby("Country Name")["CO2 Per Capita (metric tons)"].mean().sort_values(ascending=False)).reset_index()[:nb_displayed]   
    fig1 = px.histogram(mean_df, x="Country Name", y="CO2 Per Capita (metric tons)")
    return fig1

def fig_world(df):
    fig = px.scatter_geo(df, locations="Country Code", projection= 'winkel tripel',hover_data="CO2 Per Capita (metric tons)", size="CO2 Per Capita (metric tons)", animation_frame="Year")
    return fig



st.title("Welcome to this first application to visualize the CO2 production per country and for specific year")

filepath = "CO2_continent.csv"


co2_df = pd.read_csv(filepath, sep=";")


co2_df.dropna(inplace=True)
min = co2_df["Year"].min()
max = co2_df["Year"].max()
min_year = st.slider("Select the minimum boundary", min_value=min, max_value=max, step=1, value=min)
nbr_years = st.slider("Select the number of years to display", min_value=1, max_value=15, step=1, value=1)
nbr_countries = st.selectbox(label='Number of countries to display:',
                options=[3, 5, 10, 20, 30],
                index=0,
                )
fig1 = top_n_emitters(co2_df, min_year, min_year+nbr_years, nbr_countries)
st.plotly_chart(fig1)


fig2 = px.scatter_geo(co2_df, locations="Country Code", 
                     projection= 'mollweide',
                     hover_data="CO2 Per Capita (metric tons)", 
                     size="CO2 Per Capita (metric tons)", 
                     animation_frame="Year",
                     color="Continent_Name")
st.plotly_chart(fig2)

    