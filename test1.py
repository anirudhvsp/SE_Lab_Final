from flask import Flask, render_template, request
import requests, json 
app=Flask(__name__)

@app.route('/')
def student():
   return render_template('form1.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        api_key = "1b1ee5bc9d6bdb7769f87e25a8c7b380"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = result['cname']
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
        response = requests.get(complete_url)
        x = response.json() 
        if x["cod"] != "404":  
            y = x["main"] 
            current_temperature = y["temp"] 
            current_pressure = y["pressure"] 
            current_humidiy = y["humidity"]  
            z = x["weather"] 
            weather_description = z[0]["description"] 
            print(" Temperature (in kelvin unit) = " +
                            str(current_temperature) + 
                  "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                  "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                  "\n description = " +
                            str(weather_description)) 
          
        else: 
            print(" City Not Found ")
        z1={}
        for i in z[0]:
            z1[i]=z[0][i]
        print(z1)
        Table = []
        for key, value in z1.items():
            temp = []
            temp.extend([key,value])
            Table.append(temp)
        return render_template('form1.html',result=Table)
app.run()