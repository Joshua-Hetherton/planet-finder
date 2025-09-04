from skyfield.api import *
from skyfield import *
from skyfield import almanac
from skyfield.magnitudelib import planetary_magnitude
from skyfield.data import mpc, hipparcos

from datetime import timedelta

def get_coordinates():
    
    """
    Attempts to get the user's current latitude and longitude. 
    Falls back to defaults if unavailable.
    """
    
    try:
        return NotImplementedError("Not Yet Implemented")
    
    except:
        return NotImplementedError("Not Yet Implemented")
    

def get_planet_position(planet_name, ts, lat, lon, eph):
    """
    Calculates the current altitude, azimuth, and distance of a planet
    as observed from a specific location on Earth at the current time.

    (altitude_degrees, azimuth_degrees, distance_km).
    """
    # Gets the users current time
    time=ts.now()

    #Set the observers location as earth
    #Give their lat and lon position
    observer=eph["earth"]+ wgs84.latlon(latitude_degrees = lat, longitude_degrees = lon)

    #Sets the selected planet
    planet = eph[planet_name.lower()]

    #Calculates the position of the planet
    astrometric = observer.at(time).observe(planet)

    # Corrects for lights travel time
    apparent = astrometric.apparent()

    # Convert apparent position to altitude, azimuth, and distance
    alt, az, distance = apparent.altaz()

    return alt.degrees, az.degrees, distance.km

def get_visible_planets(lat, lon, ts, eph):
    """
    Returns a list of planets currently above the horizon 
    from the user's location.
    """
    try:

        planets_visible={}

        #Change in the future to allow the user to select a range of planets to show.
        #E.g Viewing Asteroids, Star clusters, etc.
        for planet in ["mercury", "venus", "moon", "mars", "jupiter", "saturn", "uranus", "neptune"]:
            alt, az, distance = get_planet_position(planet, ts, lat, lon, eph)

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


def view_planet(planet_name, ts, eph, lat, lon):
    """
    Returns key astronomical info for the given planet 
    It returns:
        Planet Rising and Setting times
        Visible Magnitude (How visible it is from where you are)
        Altitude
        Azimuth
        Distance

    """
    observer=eph["earth"]+ wgs84.latlon(latitude_degrees = lat, longitude_degrees = lon)
    
    #Rising and Setting
    time = ts.now()
    time1 = ts.utc(time.utc_datetime() + timedelta(days=1))

    planet_rise_set=almanac.risings_and_settings(observer, eph[f'{planet_name.lower()}'], time, time1)

    #Apparent Magnitude (How visible it is from where you are)

    astrometric = eph['earth'].at(time).observe(eph[f'{planet_name.lower()}'])

    magnitude=planetary_magnitude(astrometric)

    #Azimuth, Altitude and Distance
    alt, az, distance = get_planet_position(planet_name, ts, lat, lon, eph)

    return planet_rise_set,magnitude, alt, az, distance

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
    ts = load.timescale()        # Load timescale for time calculations
    
    return eph, ts

def load_minor_bodies():
    """
    Loads a selection of minor boides from the Minor Planet Center

    Contains all orbital elements of the minor planets
    """
    with load.open(mpc.MINOR_PLANET_URL) as f:
        minor_bodies= mpc.load_mpcorb_dataframe(f)
    
    return minor_bodies

def load_stars_data():
    """
    Loads the Hipparcos Catalog of stars

    Returns the:
    DataFrame(Position, magnitude, and other properties of the stars)
    """
    with load.open(hipparcos.URL) as f:
        stars = hipparcos.load_dataframe(f)
    
    return stars

def load_artifical_data():
    """
    Loads all data from Celestrak

    Returns a dictionary of names
    """

    url = 'https://celestrak.com/NORAD/elements/active.txt'

    satellites = load.tle_file(url)

    return {sat.name: sat for sat in satellites}


