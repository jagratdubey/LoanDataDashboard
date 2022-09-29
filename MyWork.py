import streamlit as st
import pandas as pd
import plotly.express as px
st.write("""# Loan Data Dashboard - Jagrat Dubey""")
df = pd.read_csv("datapo.csv")

# Tenure in Years
st.subheader('Branch v/s Tenure Type of Loan :')
newframe=df[['Loan ID','Branch','Term','Loan Process Date',]]
newframe['Loan Process Date']=(pd.DatetimeIndex(newframe['Loan Process Date']).year).map('{:,.0f}'.format)
#newframe
fig = px.bar(newframe, y="Branch",
                color="Term", barmode="group", color_discrete_map={
                    'Short Term':'darkblue',
                    'Long Term':'red'
                },labels={'count':'Number of Loans'})
st.plotly_chart(fig)


# Yearwise distribution of types of loans sanctioned pie chart
st.subheader('Distribution of Type of Loans Sanctioned based on Loan Amount:')

newframe=df[['Loan ID','Purpose','Loan Process Date','Current Loan Amount','Loan Sanctioned (Yes/No)']]
newframe['Loan Process Date']=(pd.DatetimeIndex(newframe['Loan Process Date']).year).map('{:,.0f}'.format)
nf=newframe[newframe['Loan Process Date']=='2,017']
fig = px.pie(nf, values='Current Loan Amount', names='Purpose', title='Year 2017')
st.plotly_chart(fig)

newframe=df[['Loan ID','Purpose','Loan Process Date','Current Loan Amount']]
newframe['Loan Process Date']=(pd.DatetimeIndex(newframe['Loan Process Date']).year).map('{:,.0f}'.format)
nf=newframe[newframe['Loan Process Date']=='2,018']
fig = px.pie(nf, values='Current Loan Amount', names='Purpose', title='Year 2018')
st.plotly_chart(fig)

newframe=df[['Loan ID','Purpose','Loan Process Date','Current Loan Amount']]
newframe['Loan Process Date']=(pd.DatetimeIndex(newframe['Loan Process Date']).year).map('{:,.0f}'.format)
nf=newframe[newframe['Loan Process Date']=='2,019']
fig = px.pie(nf, values='Current Loan Amount', names='Purpose', title='Year 2019')
st.plotly_chart(fig)

newframe=df[['Loan ID','Purpose','Loan Process Date','Current Loan Amount']]
newframe['Loan Process Date']=(pd.DatetimeIndex(newframe['Loan Process Date']).year).map('{:,.0f}'.format)
nf=newframe[newframe['Loan Process Date']=='2,020']
fig = px.pie(nf, values='Current Loan Amount', names='Purpose', title='Year 2020')
st.plotly_chart(fig)

newframe=df[['Loan ID','Purpose','Loan Process Date','Current Loan Amount']]
newframe['Loan Process Date']=(pd.DatetimeIndex(newframe['Loan Process Date']).year).map('{:,.0f}'.format)
nf=newframe[newframe['Loan Process Date']=='2,021']
fig = px.pie(nf, values='Current Loan Amount', names='Purpose', title='Year 2021')
st.plotly_chart(fig)

newframe=df[['Loan ID','Purpose','Loan Process Date','Current Loan Amount']]
newframe['Loan Process Date']=(pd.DatetimeIndex(newframe['Loan Process Date']).year).map('{:,.0f}'.format)
nf=newframe[newframe['Loan Process Date']=='2,022']
fig = px.pie(nf, values='Current Loan Amount', names='Purpose', title='Year 2022')
st.plotly_chart(fig)




# Scatter plot
st.subheader('Rejected Loans'' Data based on Credit Score:')
newframe=df[['Credit Score','Current Loan Amount','Purpose','Loan Process Date','Loan Sanctioned (Yes/No)']]
newframe['Loan Process Date']=(pd.DatetimeIndex(newframe['Loan Process Date']).year).map('{:,.0f}'.format)
nf=newframe[newframe['Loan Sanctioned (Yes/No)']=='No']
fig = px.scatter(nf, y="Loan Process Date", x="Credit Score", color="Purpose",
                  hover_data=['Credit Score'])
st.plotly_chart(fig)




# Branchwise loan insurance figures
st.subheader('Branch-wise Loan Insurance Data:')
newframe=df[['Loan ID','Branch','Loan Process Date','Loan Insurance Enrolled (Yes/No)']]
newframe['Loan Process Date']=(pd.DatetimeIndex(newframe['Loan Process Date']).year).map('{:,.0f}'.format)
nf=newframe[newframe['Loan Insurance Enrolled (Yes/No)']=='Yes']
fig = px.bar(nf, x="Branch",
                color="Loan Process Date", barmode="group",labels={'count':'Number of Loans Enrolled for Insurance'})
st.plotly_chart(fig)




# Insurance enrolled vs claimed
st.subheader('Year-wise Insurance Enrolled v/s Claimed:')
newframe=df[['Loan ID','Loan Insurance Enrolled (Yes/No)','Loan Amount Sanctioned by Bank on Insurance (Yes/No)','Loan Process Date',]]
newframe['Loan Process Date']=(pd.DatetimeIndex(newframe['Loan Process Date']).year).map('{:,.0f}'.format)
#newframe
fig = px.bar(newframe, x="Loan Process Date",
                color="Loan Amount Sanctioned by Bank on Insurance (Yes/No)", color_discrete_map={
                    'Yes':'brown',
                    'No':'darkgrey'
                },labels={'count':'Number of Loans Enrolled for Insurance'})
st.plotly_chart(fig)

