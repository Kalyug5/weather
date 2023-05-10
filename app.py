from flask import Flask,request,render_template,flash,redirect
import requests
app=Flask(__name__)
app.secret_key="secret key"
@app.route("/",methods=['GET','POST'])
def main():
    if request.method=='POST':
        try:
        
            city_name=request.form['name']
            print(city_name)
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=UR API KEY'
            response=requests.get(url.format(city_name)).json()
            print(response)
            temp = response['main']['temp']
            weather = response['weather'][0]['description']
            min_temp = response['main']['temp_min']
            max_temp = response['main']['temp_max']
            icon = response['weather'][0]['icon']
            long=response['coord']['lon']
            lati=response['coord']['lat']
            feeling=response['main']['feels_like']
            return render_template('index.html',temp=temp,weather=weather,min_temp=min_temp,max_temp=max_temp,icon=icon, city_name = city_name,long=long,lati=lati,feeling=feeling)
        except Exception as e:
            flash(f'Error: {str(e)} enter the correct city name', 'error')
            return redirect("/")
    return render_template('index.html')

if (__name__=='__main__'):
    app.run(debug=True)
