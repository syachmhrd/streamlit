import streamlit as st
import pandas as pd
import altair as alt
from numerize import numerize

st.set_page_config(layout='wide')

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQMqC_6fkaH6oZweJDIIYFDdE9o3P3G1hB0OKLzkGGf0pB-FjWJoAMoYca2iXV2ID5dE7hoklCSx6hE/pub?gid=0&single=true&output=csv')

df['order_date']= pd.to_datetime(df['order_date'])
df['ship_date']= pd.to_datetime(df['ship_date'])

df['order_year']= df['order_date'].dt.year

CURR_YEAR = max(df['order_date'].dt.year)
PREV_YEAR = CURR_YEAR-1

st.title("Tokopaedi Dashboard")

st.metric("Sales",1000,-10) #cara buat metric di streamlit

#1. periksa tahun terakhir dari data
# Hitung sales, banyaknya order, banyaknya konsumen, profit%
# ditahun tersebut

data = pd.pivot_table(
    data= df,
    #data= df[df['order_year']==CURR_YEAR],
    index= 'order_year',
    aggfunc={
        'sales':'sum',
        'profit':'sum',
        'order_id':pd.Series.nunique,
        'customer_id':pd.Series.nunique
    }
).reset_index()

data['gpm']= 100.0 * data['profit']/data['sales']

mx_sales, mx_order, mx_customer, mx_gpm = st.columns(4)

with mx_sales:
    curr_sales = data.loc[data['order_year']==CURR_YEAR, 'sales'].values[0]
    prev_sales = data.loc[data['order_year']==PREV_YEAR, 'sales'].values[0]
    sales_diff_pct = 100.0 * (curr_sales-prev_sales)/prev_sales
    st.metric("Sales", value= numerize.numerize(curr_sales),delta=f'{sales_diff_pct:.2f}%')

with mx_order:
    st.metric("Number of order",value =100,delta=10)

freq =st.selectbox("Freq",['Harian','Bulanan'])

timeUnit = {
    'Harian' :'yearmonthdate',
    'Bulanan':'yearmonth'
}

Agr =st.selectbox("Aggregate",['Jumlah','Rata-rata'])

Agfunc = {
    'Jumlah':'sum',
    'Rata-rata' :'mean'
}

st.header("Sales trend")
#altair membuat objek berupa chart dengan data di dalam parameter
sales_line = alt.Chart(df[df['order_year']== CURR_YEAR]).mark_line().encode(
    alt.X('order_date',title='Order Date',timeUnit=timeUnit[freq]),
    alt.Y('sales',title='Revenue', aggregate=Agfunc[Agr])
)

st.altair_chart(sales_line,use_container_width=True)

sales_bar = alt.Chart(df[df['order_year']== CURR_YEAR]).mark_bar().encode(
    alt.X('order_date',title='Order Date',timeUnit=timeUnit[freq]),
    alt.Y('sales',title='Revenue', aggregate=Agfunc[Agr])
)

st.altair_chart(sales_bar,use_container_width=True)

#Buat 4 kolom berisi sales dari tiap kategori
#Setiap kolom mewakili region berbeda

st.dataframe(data,use_container_width=True)