import streamlit as st
import joblib

location_price=joblib.load('location_cost.pkl')
fuel=joblib.load('fuel.pkl')
gear=joblib.load('gear.pkl')
owner=joblib.load('owner.pkl')
seating=joblib.load('seating.pkl')
seller=joblib.load('seller.pkl')

st.set_page_config(
    page_title="AutoInsights",
    page_icon='📈'
)

st.title('Auto Insights')
st.write("Discover the power of data analysis for selling your Car, unlocking valuable insights to optimize your selling strategy.")
location=st.selectbox('Select Your Location',list(location_price['Location'].values())+['Others'])
def fetchAveragePrice(text,dataframe,columnName):
    if(text=='Others'):
        return 'Medium Aged'
    avg_cost=0
    for key,value in dataframe[columnName].items():
        if value==text:
            avg_cost=dataframe['Price'][key]
            if(columnName!='Location'):
                return "{:,}".format(int(avg_cost))
    if(avg_cost>3e6):
        return ('Extremely Costly')
    elif(avg_cost>1.5e6):
        return ('Pricey')
    elif(avg_cost>1e6):
        return ('Moderately priced')
    elif(avg_cost>0.5e6):
        return ('Affordable')
    else:
        return ('Budget Friendly')
if(st.button('Enter Location')):
    st.write("Cars in Your Location are "+str(fetchAveragePrice(location,location_price,'Location')))

gears=st.selectbox('Gear Manual/Automatic',['Manual','Automatic'])
if(st.button('Enter Gear')):
    cost=fetchAveragePrice(gears,gear,'Transmission')
    st.write(f'{gears} Geared Vehicles Cost : '+cost+' on an average')

owners=st.selectbox('Owner Type',list(owner['Owner'].values()))
if(st.button('Enter Owner')):
    cost=fetchAveragePrice(owners,owner,'Owner')
    st.write(f'If Owner Type is {owners} Car costs : '+cost+' on an average')

seatings=st.selectbox('Seating Capacity of Car',list(seating['Seating Capacity'].values()))
if(st.button('Enter Seating Capacity')):
    cost=fetchAveragePrice(seatings,seating,'Seating Capacity')
    st.write(f'If Seating Capacity is {seatings} Car costs : '+cost+' on an average')

fuels=st.selectbox('Select Fuel Type in Car',list(fuel['Fuel Type'].values()))
if(st.button('Enter Fuel Type')):
    cost=fetchAveragePrice(fuels,fuel,'Fuel Type')
    st.write(f'If Fuel Type is {fuels} Car costs : '+cost+' on an average')

sellers=st.selectbox('Select Seller Type',list(seller['Seller Type'].values()))
if(st.button('Enter Seller Type')):
    cost=fetchAveragePrice(sellers,seller,'Seller Type')
    st.write(f'If Seller Type is {sellers} Car costs : '+cost+' on an average')