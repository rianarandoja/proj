import xml.etree.ElementTree as ET
import webbrowser
from tkinter import *
from tkinter import messagebox
from urllib.request import urlopen


def WeatherInformation(location):
    # Aken:
    # Fotod eeldavad toplevelit.
    weather_window = Toplevel()
    weather_window.geometry("400x260")
    weather_window.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(weather_window, width=400, height=260)

    try:
        # Avab veebilehelt xml:
        base_url = urlopen("http://www.ilmateenistus.ee/ilma_andmed/xml/observations.php")
        # Parsib sisu:
        weather_data = ET.parse(base_url)
        # Hangib failipuu:
        root = weather_data.getroot()
        base_url.close()
    except:
        messagebox.showinfo(message='Ühendamine Riigi Ilmateenistusega ebaõnnestus. Proovi hiljem uuesti või '
                                    'kontakteeru oma kohaliku IT osakonnaga! :)', title='Rawr! Feeling angry I am.')
        print("No internet connection or wrong URL")
        return

    # Teeb kasutaja sisendi xml-iga vastavaks.
    location = location[0]
    location = location.capitalize()
    if location == "Tartu":
        location = "Tartu-Tõravere"
    elif location == "Tallinn":
        location = "Tallinn-Harku"
    elif location == "Pärnu":
        location = "Pärnu-Sauga"
    elif location == "Narva":
        location = "Narva-Jõesuu"
    elif location == "Türi":
        location = "Türi-Alliku"
    elif location == "Rannu":
        location = "Rannu-Jõesuu"

    # Käib kõik märksõnad "station" läbi.
    # Kui leidub otsitud koht, kuvatakse vajalik ekraanile (ka fotod) ja katkestatakse tsükkel.
    station_name_exists = False

    for weather in root.findall('station'):
        station_name = weather.find("name").text
        if station_name == location:
            station_name_exists = True
            # Määrab dünaamilise akna tausta:
            weather_window_background = str(weather.find("phenomenon").text)
            try:
                background_img = PhotoImage(file=".\\Photos_for_weather\\" + str(weather_window_background) + ".gif")
            except:
                background_img = PhotoImage(file=".\\Photos_for_weather\\Clear.gif")
                print("Background image not found.")
            # Teksti taust:
            canvas.create_image(0, 0, image=background_img, anchor="nw")
            text_background = PhotoImage(file=".\\Photos_for_weather\\text_background.png")
            canvas.create_image(0, 0, image=text_background, anchor="nw")

            font_ = "Calibri 9"
            canvas.create_text(29, 28, text="Temperatuur: " + str(weather.find("airtemperature").text) + " °C", font=font_ , anchor="w")
            canvas.create_text(29, 56, text="Sademed: " + str(weather.find("precipitations").text) + " mm", font=font_, anchor="w")
            canvas.create_text(29, 84, text="Tuule kiirus: " + str(weather.find("windspeed").text) + " m/s", font=font_, anchor="w")
            canvas.create_text(29, 112, text="Tuule suund: " + str(weather.find("winddirection").text) + " °", font=font_, anchor="w")
            canvas.create_text(29, 140, text="Nähtavus: " + str(weather.find("visibility").text) + " km", font=font_, anchor="w")
            canvas.create_text(29, 168, text="Õhurõhk: " + str(weather.find("airpressure").text) + " hPa", font=font_, anchor="w")
            canvas.create_text(29, 196, text="Õhuniiskus: " + str(weather.find("relativehumidity").text) + " %", font=font_, anchor="w")
            canvas.create_text(28, 224 , text=" Andmed: Riigi Ilmateenistus \n http://www.ilmateenistus.ee/", font=font_,anchor="w")

            weather_window.title(station_name)
            canvas.pack()
            weather_window.mainloop()
            break

    # Kui sisendit ei leita, avatakse brauser:
    if not station_name_exists:
        webbrowser.open('http://www.ilmateenistus.ee/')
        print("station name was not found")
        return
