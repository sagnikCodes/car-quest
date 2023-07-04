import streamlit as st
import joblib
import sklearn
import numpy as np

st.set_page_config(
    page_title="Car Seller",
    page_icon='🏎️'
)

car_data=joblib.load('data.pkl')
pipe=joblib.load('pipeline.pkl')
location_price=joblib.load('location_cost.pkl')

st.title('Know the Best Selling Price of Your Car')
st.write("Please Fill in the Valid details of your car :")
locations=list(location_price['Location'].values())+['Others']
company=st.selectbox('Company/Brand',set(car_data['Make'].values()))
model=st.text_input('Enter the Model of your Car')
year=int(st.number_input('When did you Buy the Car ?',value=2011))
kilometer=int(st.number_input('Kilometers Run',value=87000))
fuel_type=st.selectbox('Fuel Type',set(car_data['Fuel Type'].values()))
seating_capacity=st.selectbox('Seating Capacity',[2.0,4.0,5.0,6.0,7.0,8.0])
transmission=st.selectbox('Gear Type',['Manual','Automatic'])
location=st.selectbox('Location',locations)
color=st.selectbox('Color',set(car_data['Color'].values()))
owner=st.selectbox('Owner Status',set(car_data['Owner'].values()))
seller_type=st.selectbox('Seller Type',set(car_data['Seller Type'].values()))
drivetrain=st.selectbox('Drivetrain',['RWD','AWD','FWD'])
length=st.number_input('Length of Car(in mm)',value=4000)
width=st.number_input('Width of Car(in mm)',value=1680)
height=st.number_input('Height of Car(in mm)',value=1505)
fuel_tank_capacity=st.number_input('Fuel Tank Capacity',value=35)
bhp=st.number_input('Break HorsePower',value=87)
rpm=st.number_input('At what RPM does the above BHP occur ?',value=6000)
max_torque=st.number_input('Maximum Torque(in Nm)',value=109)
rpm_torque=st.number_input('At what RPM is the above Torque achieved',value=4500)

#Constructing Columns for Pipeline
def transformYear(year):
    if(year>2020):
        return 'Brand New'
    elif(year>2018):
        return 'New'
    elif(year>2014):
        return 'Medium Aged'
    elif(year>2010):
        return 'Old'
    else:
        return 'Very Old'
def fetchLocationPrice(text):
    if(text=='Others'):
        return 'Medium Aged'
    avg_cost=0
    for key,value in location_price['Location'].items():
        if value==text:
            avg_cost=location_price['Price'][key]
    if(avg_cost>3e6):
        return ('Extremely Costly')
    elif(avg_cost>1.5e6):
        return ('Costly')
    elif(avg_cost>1e6):
        return ('Medium Cost')
    elif(avg_cost>0.5e6):
        return ('Low Cost')
    else:
        return ('Very Low Cost')

year=transformYear(year)
location=fetchLocationPrice(location)
size=length*width*height
space=seating_capacity/size

if(st.button('Predict Price')):
    query=[[company,year,kilometer,fuel_type,transmission,location,color,owner,seller_type,drivetrain,length,width,fuel_tank_capacity,bhp,rpm,rpm_torque,size,space]]
    predictedPrice=int(np.exp(pipe.predict(query))[0])
    st.title("Consider selling your car at {:,} rupees to get the best value for your vehicle.".format(predictedPrice))