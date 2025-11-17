from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "Server is running"

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print("received data", data)

    # Extract form values
    planet_name = data.get("planet_name")
    mass = data.get("mass")
    temperature = data.get("temperature")
    pressure = data.get("pressure")
    elements = data.get("elements", [])  
    water = data.get("water")
    star = data.get("star")
    distance = data.get("distance")
    moons = data.get("moons")
    magnet = data.get("magnet")
    radiation = data.get("rads")

    class hycean_planets:
        def __init__(self, planet_name, mass, temperature, pressure, elements, water, star, distance, moons, magnet, radiation):
            self.planet_name = planet_name
            self.mass = mass
            self.temperature = temperature
            self.pressure = pressure
            self.elements = list(elements)
            self.water = water
            self.star = star
            self.distance = distance
            self.moons = moons
            self.magnet = magnet
            self.radiation = radiation

        def Mass(self):
            x = 0
            if 1 <= self.mass <= 1.2:
                mass_output = "The mass of the planet is ideal for life to sustain"
                x = 3
            elif 1.2 < self.mass <= 1.5:
                mass_output = "The mass of planet is a little heavy"
                x = 1
            elif 0.8 <= self.mass < 1:
                mass_output = "The mass of the planet is a little light"
                x = 1
            elif self.mass > 1.5:
                mass_output = "The mass of the planet is too heavy for life to sustain"
                x = 0
            elif self.mass < 0.8:
                mass_output = "The mass of planet is too light for life to sustain"
                x = 0
            print(mass_output)
            return x, mass_output

        def Temperature(self):
            x = 0
            if -25 <= self.temperature <= 25:
                temperature_output = "The temperature of planet is ideal for life to sustain"
                x = 3
            elif 25 < self.temperature <= 50:
                temperature_output = "The temperature is more on the tropical and hot side"
                x = 1
            elif -50 <= self.temperature < -25:
                temperature_output = "The temperature is more on the polar and cold side"
                x = 1
            elif self.temperature > 50:
                temperature_output = "The temperature is too hot for life to sustain"
                x = 0
            elif self.temperature < -50:
                temperature_output = "The temperature is too cold for life to sustain"
                x = 0
            print(temperature_output)
            return x, temperature_output

        def Pressure(self):
            x = 0
            if 100 <= self.pressure <= 150:
                pressure_output = "The pressure is ideal for life to sustain"
                x = 3
            elif 150 < self.pressure <= 200:
                pressure_output = "The pressure is high making the atmosphere dense"
                x = 1
            elif 50 <= self.pressure < 100:
                pressure_output = "The pressure is low making the atmosphere thin"
                x = 1
            elif self.pressure < 50:
                pressure_output = "The pressure is too low for life to sustain"
                x = 0
            elif self.pressure > 200:
                pressure_output = "The pressure is too high for life to sustain"
                x = 0
            print(pressure_output)
            return x, pressure_output

        def Composition(self):
            x = 0
            composition_output = ""
            h = 0
            c = 0
            n = 0
            o = 0
            if 'H' in self.elements:
                h = 1
            if 'C' in self.elements:
                c = 1
            if 'N' in self.elements:
                n = 1
            if 'O' in self.elements:
                o = 1
            
            x = h + c + n + o
            if x==4:
                composition_output="The planet has all essential elements for life"
            elif x==3:
                composition_output="The planet has most essential elements for life"
            elif x==2:
                composition_output="The planet has some essential elements for life"
            elif x==1:
                composition_output="The planet has few essential elements for life"
            else:
                composition_output="The planet lacks essential elements for life"

            
            return x, composition_output

        def Presence_of_water(self):
            x = 0
            if self.water == "Yes":
                presence_of_water_output = "There are chances of pre-existing life"
                x = 1
            else:
                presence_of_water_output = "There are no chances of pre-existing life"
                x = 0
            print(presence_of_water_output)
            return x, presence_of_water_output

        def Distance_from_star(self):
            x = 0
            distance_output = ""
            
            if self.star == "Sun":
                if 0.95 <= self.distance <= 1.37:
                    distance_output = "The planet is in the goldilock zone"
                    x = 3
                elif self.distance > 1.37:
                    distance_output = "The planet is too far from the star"
                    x = 0
                elif self.distance < 0.95:
                    distance_output = "The planet is too close to the star"
                    x = 0

            elif self.star == "Red Dwarfs":
                if 0.01 <= self.distance <= 0.1:
                    distance_output = "The planet is in the goldilock zone"
                    x = 3
                elif self.distance > 0.1:
                    distance_output = "The planet is too far from the star"
                    x = 0
                elif self.distance < 0.01:
                    distance_output = "The planet is too close to the star"
                    x = 0

            elif self.star == "Blue Giants":
                if 2 <= self.distance <= 3:
                    distance_output = "The planet is in the goldilock zone"
                    x = 3
                elif self.distance > 3:
                    distance_output = "The planet is too far from the star"
                    x = 0
                elif self.distance < 2:
                    distance_output = "The planet is too close to the star"
                    x = 0
                    
            print(distance_output)
            return x, distance_output

        def Moons(self):
            x = 0
            if self.moons >= 1:
                moons_output = "The sky would look nice with so many moons"
                x = 1
            else:
                moons_output = "The sky is boring"
                x = 0
            print(moons_output)
            return x, moons_output

        def Magnetic_field(self):
            x = 0
            if self.magnet == "Yes":
                magnetic_field_output = "The planet will have protection from 'UV' light"
                x = 1
            else:
                magnetic_field_output = "The planet won't have protection from 'UV' light"
                x = 0
            print(magnetic_field_output)
            return x, magnetic_field_output

        def Radiation_level(self):
            x = 0
            radiation_level_output = ""
            
            if self.radiation == "Medium":
                radiation_level_output = "There will be geothermal heat"
                x = 1
            elif self.radiation == "High":
                radiation_level_output = "There will be risk of cancer"
                x = 0
            elif self.radiation == "Low":
                radiation_level_output = "There won't be much resources"
                x = 0
                
            print(radiation_level_output)
            return x, radiation_level_output

    # Create an instance of hycean_planets
    try:
        hycean = hycean_planets(planet_name, float(mass), float(temperature), float(pressure), 
                               elements, water, star, float(distance), int(moons), magnet, radiation)

        # Get ratings and messages
        ym, mass_msg = hycean.Mass()
        yt, temp_msg = hycean.Temperature()
        yp, pressure_msg = hycean.Pressure()
        yc, comp_msg = hycean.Composition()
        ypw, water_msg = hycean.Presence_of_water()
        yd, distance_msg = hycean.Distance_from_star()
        ymn, moons_msg = hycean.Moons()
        ymf, magnet_msg = hycean.Magnetic_field()
        yr, radiation_msg = hycean.Radiation_level()

        # Store ratings in list
        rate = [ym, yt, yp, yc, ypw, yd, ymn, ymf, yr]
        print(rate)

        # Calculate total rating
        rating = sum(rate)
        average = rating / 9

        # Determine habitability rate
        if 0 <= average < 0.5:
            habitability = "Your planet has a 0% habitability rate"
        elif 0.5 <= average < 1:
            habitability = "Your planet has a 20% habitability rate"
        elif 1 <= average < 1.5:
            habitability = "Your planet has a 40% habitability rate"
        elif 1.5 <= average < 2:
            habitability = "Your planet has a 60% habitability rate"
        elif 2 <= average < 2.5:
            habitability = "Your planet has a 80% habitability rate"
        elif 2.5 <= average <= 3:
            habitability = "Your planet has a 100% habitability rate"
        else:
            habitability = "Unable to calculate habitability rate"

        # Prepare result
        result = {
            "planet_name": planet_name,
            "habitability": habitability,
            "habitability_percentage": round(average * 100 / 3, 1),
            "analysis": {
                "mass": mass_msg,
                "temperature": temp_msg,
                "pressure": pressure_msg,
                "composition": comp_msg,
                "water": water_msg,
                "distance": distance_msg,
                "moons": moons_msg,
                "magnetic_field": magnet_msg,
                "radiation": radiation_msg
            }
        }
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)