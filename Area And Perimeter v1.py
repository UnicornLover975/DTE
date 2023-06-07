import math
import tkinter
from tkinter import *

# Creates the window to put all labels and buttons onto
main_window = Tk()
main_window.title("Area/Perimeter Tool")

# Choosing my font and size of the words
my_font = ("Pacifico", 9)
my_font_2 = ("Pacifico", 10)
my_font_3 = ("Pacifico", 12)

# A list to save the calculations into
saved_calcs = []

def choosetab():
    # Below runs when button to choose rectangle is clicked
    def rectangletab():
        # Predefined functions to remove unnecessary buttons and labels
        def remove_rec():
            shape_name1.destroy()
            spacer2.destroy()
            width_value.destroy()
            height_value.destroy()
            width_label.destroy()
            height_label.destroy()
            calculate_button1.destroy()
            spacer1.destroy()
        def back1():
            remove_rec()
            choosetab()
            back_button1.destroy()
        remove1()
        close_button.destroy()
        # Below places labels and entry widgets to enter the known values
        shape_name1 = Label(main_window, text="Rectangle", font=my_font, width=62)
        shape_name1.grid(row=0, columnspan=2)
        spacer2 = Label(main_window, text="       ")
        spacer2.grid(row=1, column=0, columnspan=2)
        width_value = Entry(main_window, width=35, borderwidth=1)
        width_value.grid(row=2, column=1)
        height_value = Entry(main_window, width=35, borderwidth=1)
        height_value.grid(row=3, column=1)
        width_label = Label(main_window, text="     Enter the width:", width=15, font=my_font)
        height_label = Label(main_window, text="     Enter the height:", width=15, font=my_font)
        width_label.grid(row=2, column=0)
        height_label.grid(row=3, column=0)
        # Below calculates using the entered values from above to find the area and perimeter
        def calc_rec():
            try:
                width1 = float(width_value.get())
                height1 = float(height_value.get())
                rec_area = (height1 * width1)
                rec_perimeter = (height1 * 2) + (width1 * 2)
            except ValueError:
                back1()
            remove_rec()
            back_button1.destroy()
            # Below shows the values that the user entered and the area and perimeter that was calculated
            values = Label(main_window, text="Entered Values: ", font=my_font_3)
            width_show = Label(main_window, text=width1, font=my_font_2)
            width_show2 = Label(main_window, text="Width - ", font=my_font_2)
            height_show = Label(main_window, text=height1, font=my_font_2)
            height_show2 = Label(main_window, text="Height - ", font=my_font_2)
            rec_area_show = Label(main_window, text=rec_area, font=my_font_2)
            rec_area_show2 = Label(main_window, text="Rectangle Area - ", font=my_font_2)
            rec_perimeter_show = Label(main_window, text=rec_perimeter, font=my_font_2)
            rec_perimeter_show2 = Label(main_window, text="Rectangle Perimeter - ", font=my_font_2)
            spacer12 = Label(main_window, text="       ")
            spacer13 = Label(main_window, text="       ")
            values.grid(row=1, column=0, columnspan=2)
            width_show.grid(row=2, column=1)
            width_show2.grid(row=2, column=0)
            height_show.grid(row=3, column=1)
            height_show2.grid(row=3, column=0)
            rec_area_show.grid(row=4, column=1)
            rec_area_show2.grid(row=4, column=0)
            rec_perimeter_show.grid(row=5, column=1)
            rec_perimeter_show2.grid(row=5, column=0)
            spacer12.grid(row=0, column=0, columnspan=2)
            spacer13.grid(row=6, column=0, columnspan=2)
            # Clear1() removes the labels from above when the user continues
            def clear1():
                values.destroy()
                width_show2.destroy()
                width_show.destroy()
                height_show.destroy()
                height_show2.destroy()
                rec_area_show.destroy()
                rec_area_show2.destroy()
                rec_perimeter_show.destroy()
                rec_perimeter_show2.destroy()
                spacer12.destroy()
                spacer13.destroy()
                save_rec_button.destroy()
                back_button5.destroy()
            def back5():
                remove_rec()
                choosetab()
                back_button5.destroy()
                save_rec_button.destroy()
                clear1()
            # Saves the values into the list at the top to show when the user chooses to end the program
            def save_rec():
                saved_calcs.append("Rectangle:")
                saved_calcs.append("      Width: ")
                saved_calcs.append("      " + str(width1))
                saved_calcs.append("      Height: ")
                saved_calcs.append("      " + str(height1))
                saved_calcs.append("      Area: ")
                saved_calcs.append("      " + str(rec_area))
                saved_calcs.append("      Perimeter: ")
                saved_calcs.append("      " + str(rec_perimeter))
                clear1()
                back1()
            # Puts the save button and back button for the user to choose to save the values or not
            save_rec_button = Button(main_window, text="Save", font=my_font, width=30, command=save_rec)
            back_button5 = Button(main_window, text="Back", font=my_font, width=30, command=back5)
            save_rec_button.grid(row=7, column=1)
            back_button5.grid(row=7, column=0)
        # Adds the calculate button for when the user has entered the known values, so it runs the code that does the
        # calculations, also the back button incase the user chose the wrong shape
        calculate_button1 = Button(main_window, text="Calculate", width=30, font=my_font, command=calc_rec)
        calculate_button1.grid(row=6, column=1)
        spacer1 = Label(main_window, text="       ")
        spacer1.grid(row=5, column=0, columnspan=2)
        back_button1 = Button(main_window, text="Back", width=30, font=my_font, command=back1)
        back_button1.grid(row=6, column=0)

        # Below runs when user chooses shape so the buttons get removed, so they are not interrupting the next screen

    def remove1():
        shape_label.destroy()
        spacer3.destroy()
        spacer4.destroy()
        rectangle_button.destroy()
        circle_button.destroy()
        triangle_button.destroy()
        parallelogram_button.destroy()
        finish_button.destroy()
    # Puts all the labels and buttons onto the window for the user to choose what shape they want to calculate for
    # and the buttons to end the program and show the calculated values.
    shape_label = Label(main_window, text="What shape do you want to calculate for?", font=my_font_2)
    shape_label.grid(row=1, column=0, columnspan=2)
    spacer3 = Label(main_window, text="       ")
    spacer3.grid(row=2, column=0, columnspan=2)
    spacer4 = Label(main_window, text="       ")
    spacer4.grid(row=0, column=0, columnspan=2)
    rectangle_button = Button(main_window, text="Rectangle", padx=42, pady=20, command=rectangletab, font=my_font)
    circle_button = Button(main_window, text="Circle", padx=59, pady=20, command=circletab, font=my_font)
    triangle_button = Button(main_window, text="Right Angle Triangle", padx=14, pady=20, command=triangletab, font=my_font)
    parallelogram_button = Button(main_window, text="Parallelogram", padx=36, pady=20, command=parallelogramtab, font=my_font)
    rectangle_button.grid(row=3, column=0, columnspan=1)
    circle_button.grid(row=3, column=1, columnspan=1)
    triangle_button.grid(row=4, column=0, columnspan=1)
    parallelogram_button.grid(row=4, column=1, columnspan=1)
    close_button = Button(main_window, text="Close", padx=54, pady=4, command=close, font=my_font)
    close_button.grid(row=5, column=0)
    finish_button = Button(main_window, text="See Values", padx=44, pady=4, command=finish, font=my_font)
    finish_button.grid(row=5, column=1)

# Runs the whole code
choosetab()
main_window.mainloop()