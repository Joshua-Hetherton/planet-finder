import customtkinter as ctk
import planet_position



#Stuff Needed for the UI


def show_frame(frame):
        frame.tkraise()

def create_ui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Planet Finder")
    root.geometry("800x600")

    # Create frames
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(fill="both", expand=True)

    # Add content to the main frame
    label = ctk.CTkLabel(main_frame, text="Welcome to Planet Finder!")
    label.pack(pady=20)

    # Add a button to show planet positions
    button = ctk.CTkButton(main_frame, text="Show Planet Positions")
    button.pack(pady=10)

    # Show the main frame
    show_frame(main_frame)

    root.mainloop()



