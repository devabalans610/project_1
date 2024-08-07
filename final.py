import psycopg2
import pandas as pd
import streamlit as st
import pandas as pd
import streamlit_pandas as sp
#import matplotlib.pyplot as plt 
conn = psycopg2.connect(

    host="localhost",

    user="postgres",

    port="5432",

    password="deva0610",

    database="redbus"

)

table_name='redbus'
database="redbus"
cursor = conn.cursor()

writer = cursor 

query = "SELECT * FROM redbus"

#query2 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND TABLE_SCHEMA = '{database}' ORDER BY ORDINAL_POSITION"

writer.execute(query)

view = cursor.fetchall()

data=pd.DataFrame(view)

#writer.execute(query2)
#s=cursor.fetchall() 
data=pd.DataFrame(view)
#flat_list = [item[0] for item in s]
flat_list_1=['s_no','route-collected','name','type','arrival_time','departure_time','duration','price','seats_available','rating']
data.columns=flat_list_1
#data=data.set_index('s_no')
#data['price'] = pd.to_numeric(data['price'], errors='coerce')
#data['price']=data['price'].fillna(0)
#data['price']=data['price'].astype('int64')




st.set_page_config(
    page_title="Red-Bus Details",
    page_icon="png-transparent-redbus-in-india-ticket-discounts-and-allowances-bus-text-logo-india.png",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)
col1,col2=st.columns([1,4])
with col2:
    st.title("Bar chart for seats_Available")
st._arrow_bar_chart(data['seats_available'])
create_data = {
                "name": "text",
                "route": "multiselect",
                "Date":"text"}

all_widgets = sp.create_widgets(data, create_data, ignore_columns=["s_no","route-collected","departure_time","arrival_time","duration","seats_available"])
res = sp.filter_df(data, all_widgets)
col1, col2, col3 = st.columns([1,2,1])


with col2:
    st.title("Red-Bus Details:bus:")
try:
    st.header("All-Bus")
    st.write(data)
    st.header("Filter-Bus")
    st.write(res)
except:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("NO BUS FOUND!!!") 

#price_min=int(data['price'].min())
#price_max=int(data['price'].max())
#price=st.slider('price',price_min,price_max,(price_min, price_max))
#filtered_df = data[(data['price'] >= price[0]) & (data['price'] <= price[1])]
#st.write('filterdf',filtered_df) 
#x=data['route'].drop_duplicates()
#route_collected=st.selectbox('route',x)
#filter1=data[data['route']==route_collected]
#st.write(filter1)
#data2=data.drop(columns=['route-collected','name','type','arrival_time','departure_time','duration','rating'])
#data2=data2.groupby(data2['route']).sum()
#plt.bar(data2['route'],data2['seats_available'])
#st.pyplot(plt)
