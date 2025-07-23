from skyfield.api import *

def get_coordinates():
    """
    Attempts to get the user's current latitude and longitude. 
    Falls back to defaults if unavailable.
    """

    try:
        return NotImplementedError("Not Yet Implemented")
    
    except:
        return NotImplementedError("Not Yet Implemented")
    

def get_planet_position(planet_name, ts, lat, lon, planets):
    """
    Calculates the current altitude, azimuth, and distance of a planet
    as observed from a specific location on Earth at the current time.

    (altitude_degrees, azimuth_degrees, distance_km).
    """
    # Gets the users current time
    time=ts.now()

    #Set the observers location as earth
    #Give their lat and lon position
    observer=planets["earth"]+ wgs84.latlon(latitude_degrees = lat, longitude_degrees = lon)

    #Sets the selected planet
    planet = planets[planet_name.lower()]

    #Calculates the position of the planet
    astrometric = observer.at(time).observe(planet)

    # Corrects for lights travel time
    apparent = astrometric.apparent()

    # Convert apparent position to altitude, azimuth, and distance
    alt, az, distance = apparent.altaz()

    return alt.degrees, az.degrees, distance.km

def get_visible_planets(lat, lon, ts, planets):
    """
    Returns a list of planets currently above the horizon 
    from the user's location.
    """
    try:

        planets_visible={}
        for planet in ["mercury", "venus", "moon", "mars", "jupiter", "saturn", "uranus", "neptune"]:
            alt, az, distance = get_planet_position(planet, ts, lat, lon, planets)

            if az>0:
                
                #Stores all visible planets information

                planets_visible[planet] = {
                        "altitude": alt.degrees,
                        "azimuth": az,
                        "distance_km": distance.km
                    }
        return planets_visible
    
    except KeyError:
        return Exception("A problem occured while finding visible planets above your horizon")


def view_planet(planet_name):
    """
    Returns key astronomical info for the given planet 
    (distance, azimuth, visibility, etc.).
    """
    

    return NotImplementedError("Not Yet Implemented")

def get_apo_peri_apsis():
    """
    Estimates the closest and farthest points (periapsis and apoapsis)
    in a planet's orbit by sampling its distance from the Sun over time.
    """
    return NotImplementedError("Not Yet Implemented")

def load_planetary_data():
    """
    Loads and returns planetary data from Skyfield:
    ephemeris (positions), planetary objects, and timescale (time handling).
    """

    #de421.bsp is used by NASA's JPL to calculate where any planet is at any given time

    eph = load('de421.bsp')      # Load planetary ephemeris data
    planets = eph                # Planets accessed directly from eph
    ts = load.timescale()        # Load timescale for time calculations
    return eph, planets, ts


