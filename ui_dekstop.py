import customtkinter as ctk
from planet_api import *
import tkinter.messagebox
from loading_json import *
from PIL import Image, ImageDraw




def configure_grid_layout(widget, rows, columns):	
    for row in range(rows):
      widget.rowconfigure(row,weight=1)
    for col in range(columns):
        widget.columnconfigure(col,weight=1)


def show_frame(frame):
    frame.tkraise()

def layout_picture(frame, row, col, img, pixelw, pixelh):

    object_picture=ctk.CTkImage(light_image=Image.open(img),
                            dark_image=Image.open(img),
                            size=(pixelw, pixelh))
    image_label = ctk.CTkLabel(frame, image=object_picture, text="") 
    image_label.grid(row=row, column=col)


def show_menu_frame(container):

    #Setting Up Frame
    main_frame = ctk.CTkScrollableFrame(container, width=800, height=600)
    main_frame.grid(row=0,column=0, sticky="nsew")

    configure_grid_layout(main_frame, 10, 10)
    show_frame(main_frame)

    #Settings button
    show_settings=ctk.CTkButton(main_frame, text="Show Settings",command=lambda: show_settings_frame(container))
    show_settings.grid(row=10,column=0,stick="w")


    ##Loading the ephemeris (positions), ts
    eph, ts = load_planetary_data()

    #Buttons to allow the user to pick between different types of objects
    
    """
    Layout_picture takes arguements:
    frame:      What frame it is to appear in
    row:        Row to position the picture
    col:        Column to position the picture
    img path:   Path of the Image Needed
    pixelw:     Desired Pixel Width
    pixelh:     Desired Pixel Height
    """
    #Planets
    layout_picture(main_frame, 2, 3, r"Images\saturn-farewell-pia21345.jpg", 800, 400)
    view_planets=ctk.CTkButton(main_frame,text="Planets", command=lambda: planets_ui(container))
    view_planets.grid(row=3, column=3)

    #Dwarf Planets
    layout_picture(main_frame, 5, 3, r"Images\pluto_enhanced.png", 400, 400)
    view_dwarf_planets=ctk.CTkButton(main_frame,text="Dwarf Planets", command=lambda: dwarf_planets_ui(container))
    view_dwarf_planets.grid(row=6, column=3)

    #Natural Satellites (Moons)
    layout_picture(main_frame, 8, 3, r"Images\Moon.jpg", 400, 400)
    view_natural_sats=ctk.CTkButton(main_frame,text="Natural Satellites", command=lambda: natural_sats_ui(container))
    view_natural_sats.grid(row=9, column=3)

    #Minor Bodies
    layout_picture(main_frame, 11, 3, r"Images\asteroid_Psyche.jpg", 600, 400)
    view_natural_sats=ctk.CTkButton(main_frame,text="Minor Bodies", command=lambda: minor_bodies_ui(container))
    view_natural_sats.grid(row=12, column=3)
    #Deep Sky Objects
    layout_picture(main_frame, 14, 3, r"Images\Crab_Nebula.jpg", 400, 400)
    view_natural_sats=ctk.CTkButton(main_frame,text="Deep Sky Objects", command=lambda: deep_sky_objects_ui(container))
    view_natural_sats.grid(row=15, column=3)

    #Artifical Objects
    layout_picture(main_frame, 17, 3, r"Images\Hubble.jpg", 600, 400)
    view_natural_sats=ctk.CTkButton(main_frame,text="Artifical Objects", command=lambda: artifical_obj_ui(container))
    view_natural_sats.grid(row=18, column=3)
    # All planet_api Buttons

def save_settings():

    return NotImplementedError

def show_settings_frame(container):
    """
    Shows All current settings in the config.json.
    The Frame is setup to have a grid size of 50x20
    """
    #Setting Up Frame
    settings_frame=ctk.CTkFrame(container, width=400, fg_color="grey")
    settings_frame.grid(row=0, column=0, sticky="nsw")
    settings_frame.grid_propagate(False)

    configure_grid_layout(settings_frame, 50, 20)
    show_frame(settings_frame)

    #Returns User to the Main Menu
    return_to_menu=ctk.CTkButton(settings_frame, text="Show Settings",command=lambda: show_menu_frame(container))
    return_to_menu.grid(row=50,column=0,sticky="w")

    #Gets all settings
    config=load_json("config.json")
    """Currently Returns:
    1. Mode, {mode_type}
    2. LATITUDE, {latitude number}
    3. LONGITUDE, {longitude number}
    """

    #Displaying Settings
    entries= {}
    for i,(key, value) in enumerate(config.items()):
        label=ctk.CTkLabel(settings_frame, text=f"{key}")
        label.grid(row=i,column=0, sticky="w")

        entry=ctk.CTkEntry(settings_frame,placeholder_text=f"{value}")
        entry.grid(row=i, column=1)

        if key=="MODE":
            entry.configure(state="readonly")

        entries[key]= entry
    
    #Save Settings
    try:
        save_settings_button=ctk.CTkButton(settings_frame, text="Save Settings", command=lambda: save_settings(entries,config))
        save_settings_button.grid(row=50,column=1,sticky="w")
    except:
        tkinter.messagebox.showerror("Error", "Probelm Saving JSON config")


    def save_settings(entries, original_config):
        new_config={}
        for key, entry in entries.items():
            if key == "MODE":
                new_config[key]=original_config[key]
            else:
                new_config[key]=entry.get()
        save_json("config.json",new_config)

def create_ui():
         
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Planet Finder")
    root.geometry("800x600")

    configure_grid_layout(root, 10, 10)

    # Create a container frame for the switching frames
    container = ctk.CTkFrame(root)
    container.grid(row=0, column=0, columnspan=10, rowspan=10, sticky="nsew", padx=10, pady=10)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    show_menu_frame(container)

    root.mainloop()

"""
With the Planet API, I could split it all up:

"""

#Planet Section
def planets_ui(container):
    """
Planets:
    Mecury
    Venus
    Earth
    Mars
    Juipter
    Saturn
    Uranus
    Neptune
    """
    return NotImplementedError

#Dwarf Planets
def dwarf_planets_ui(container):
    """
Dwarf Planets:
    Pluto
    Ceres
    Haumea
    Eris
    """
    return NotImplementedError

#Natural Satellites
def natural_sats_ui(container):
    """
Natural Satellites:
    Moon (Earth)
    Europa, Ganymede, Io, Callisto (Jupiter)
    Titan, Enceladus (Saturn)
    Triton (Neptune)
    """
    return NotImplementedError

#Deep Sky Objects
def minor_bodies_ui(container):
    """
Minor Bodies:
    Asteroids
    Comets
    Meteoroids    
    """
    return NotImplementedError

#Deep Sky Objects
def deep_sky_objects_ui(container):
    """
Deep Sky Objects:
    Stars
    Star Clusters
    Nebulae
    Galaxies
    """
    return NotImplementedError

#Artifical Objects
def artifical_obj_ui(container):
    """
Artifical Objects(Satellites)
    ISS
    Prominent Satellites
    Search By Name
    """
    return NotImplementedError