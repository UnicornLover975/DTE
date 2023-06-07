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

    # Below runs when the user chooses to calculate for circle
    def circletab():
        def remove_circ():
            shape_name2.destroy()
            spacer14.destroy()
            spacer15.destroy()
            radius_value.destroy()
            radius_label.destroy()
            calculate_button2.destroy()
        def back2():
            remove_circ()
            choosetab()
            back_button2.destroy()
        remove1()
        close_button.destroy()
        shape_name2 = Label(main_window, text="Circle", font=my_font, width=62)
        shape_name2.grid(row=0, columnspan=2)
        radius_value = Entry(main_window, width=35, borderwidth=1)
        radius_value.grid(row=2, column=1)
        radius_label = Label(main_window, text="Enter the radius:", width=15)
        radius_label.grid(row=2, column=0)
        spacer14 = Label(main_window, text="       ")
        spacer14.grid(row=3,   column=0, columnspan=2)
        spacer15 = Label(main_window, text="       ")
        spacer15.grid(row=1, column=0, columnspan=2)
        def calc_circ():
            try:
                radius = float(radius_value.get())
                circ_area = ((radius * radius) * 3.14159)
                circ_circum = (2 * 3.14159 * radius)
            except ValueError:
                back2()
            remove_circ()
            back_button2.destroy()
            values2 = Label(main_window, text="Entered Values: ", font=my_font_3)
            radius_show = Label(main_window, text="Radius - ", font=my_font_2)
            radius_show2 = Label(main_window, text=radius, font=my_font_2)
            circ_area_show = Label(main_window, text="Area - ", font=my_font_2)
            circ_area_show2 = Label(main_window, text=circ_area, font=my_font_2)
            circ_circum_show = Label(main_window, text="Circumference - ", font=my_font_2)
            circ_circum_show2 = Label(main_window, text=circ_circum, font=my_font_2)
            spacer16 = Label(main_window, text="       ")
            spacer17 = Label(main_window, text="       ")
            values2.grid(row=1, column=0, columnspan=2)
            radius_show.grid(row=2, column=0)
            radius_show2.grid(row=2, column=1)
            circ_area_show.grid(row=3, column=0)
            circ_area_show2.grid(row=3, column=1)
            circ_circum_show.grid(row=4, column=0)
            circ_circum_show2.grid(row=4, column=1)
            spacer16.grid(row=0, column=0, columnspan=2)
            spacer17.grid(row=5, column=0, columnspan=2)
            def clear2():
                values2.destroy()
                radius_show.destroy()
                radius_show2.destroy()
                circ_area_show.destroy()
                circ_area_show2.destroy()
                circ_circum_show.destroy()
                circ_circum_show2.destroy()
                spacer16.destroy()
                spacer17.destroy()
                save_circ_button.destroy()
                back_button6.destroy()
            def back6():
                remove_circ()
                choosetab()
                back_button6.destroy()
                clear2()
            def save_circ():
                saved_calcs.append("Circle:")
                saved_calcs.append("      Radius: ")
                saved_calcs.append("      " + str(radius))
                saved_calcs.append("      Area: ")
                saved_calcs.append("      " + str(circ_area))
                saved_calcs.append("      Circumference: ")
                saved_calcs.append("      " + str(circ_circum))
                clear2()
                back2()
            save_circ_button = Button(main_window, text="Save", font=my_font_2, command=save_circ, padx=40)
            back_button6 = Button(main_window, text="Back", font=my_font_2, command=back6, padx=40)
            save_circ_button.grid(row=6, column=1)
            back_button6.grid(row=6, column=0)
        calculate_button2 = Button(main_window, text="Calculate", width=30, font=my_font, command=calc_circ)
        calculate_button2.grid(row=6, column=1)
        spacer18 = Label(main_window, text="       ")
        spacer18.grid(row=5, column=0, columnspan=2)
        back_button2 = Button(main_window, text="Back", width=30, font=my_font, command=back2)
        back_button2.grid(row=6, column=0)

    # Below runs when the user chooses to calculate for triangle
    def triangletab():
        def remove_tri():
            shape_name3.destroy()
            only.destroy()
            spacer9.destroy()
            base_label.destroy()
            base_value.destroy()
            height_label2.destroy()
            height_value2.destroy()
            calculate_button3.destroy()

        def back3():
            remove_tri()
            choosetab()
            back_button3.destroy()

        remove1()
        close_button.destroy()
        shape_name3 = Label(main_window, text="Triangle", font=my_font, width=62)
        shape_name3.grid(row=0, columnspan=2)
        only = Label(main_window, text="Right Angle Only", font=my_font)
        only.grid(row=1, column=0, columnspan=2)
        base_value = Entry(main_window, width=35, borderwidth=1)
        base_value.grid(row=2, column=1)
        height_value2 = Entry(main_window, width=35, borderwidth=1)
        height_value2.grid(row=3, column=1)
        base_label = Label(main_window, text="     Enter the base:", width=15, font=my_font)
        height_label2 = Label(main_window, text="     Enter the height:", width=15, font=my_font)
        base_label.grid(row=2, column=0)
        height_label2.grid(row=3, column=0)
        spacer9 = Label(main_window, text="       ")
        spacer9.grid(row=5, column=0, columnspan=2)

        def calc_tri():
            try:
                tri_base = float(base_value.get())
                tri_height = float(height_value2.get())
                tri_area = ((tri_height * tri_base) / 2)
                tri_perimeter = tri_height + tri_base + (math.sqrt((tri_base * tri_base) + (tri_height * tri_height)))
            except ValueError:
                back3()
            remove_tri()
            back_button3.destroy()

            tri_values = Label(main_window, text="Entered Values: ", font=my_font_3)
            tri_base_show = Label(main_window, text=tri_base, font=my_font_2)
            tri_base_show2 = Label(main_window, text="Base - ", font=my_font_2)
            tri_height_show = Label(main_window, text=tri_height, font=my_font_2)
            tri_height_show2 = Label(main_window, text="Height - ", font=my_font_2)
            tri_area_show = Label(main_window, text=tri_area, font=my_font_2)
            tri_area_show2 = Label(main_window, text="Area - ", font=my_font_2)
            tri_perimeter_show = Label(main_window, text= tri_perimeter, font=my_font_2)
            tri_perimeter_show2 = Label(main_window, text="Perimeter - ", font=my_font_2)
            spacer25 = Label(main_window, text="       ")
            spacer26 = Label(main_window, text="       ")
            tri_values.grid(row=1, column=0, columnspan=2)
            tri_base_show.grid(row=2, column=1)
            tri_base_show2.grid(row=2, column=0)
            tri_height_show.grid(row=3, column=1)
            tri_height_show2.grid(row=3, column=0)
            tri_area_show.grid(row=4, column=1)
            tri_area_show2.grid(row=4, column=0)
            tri_perimeter_show.grid(row=5, column=1)
            tri_perimeter_show2.grid(row=5, column=0)
            spacer25.grid(row=0, column=0, columnspan=2)
            spacer26.grid(row=6, column=0, columnspan=2)

            def clear3():
                tri_values.destroy()
                tri_base_show.destroy()
                tri_base_show2.destroy()
                tri_height_show.destroy()
                tri_height_show2.destroy()
                tri_area_show.destroy()
                tri_area_show2.destroy()
                tri_perimeter_show.destroy()
                tri_perimeter_show2.destroy()
                spacer25.destroy()
                spacer26.destroy()
                save_tri_button.destroy()
                back_button7.destroy()

            def back7():
                remove_tri()
                choosetab()
                back_button7.destroy()
                save_tri_button.destroy()
                clear3()

            def save_tri():
                saved_calcs.append("Triangle:")
                saved_calcs.append("      Base: ")
                saved_calcs.append("      " + str(tri_base))
                saved_calcs.append("      Height: ")
                saved_calcs.append("      " + str(tri_height))
                saved_calcs.append("      Area: ")
                saved_calcs.append("      " + str(tri_area))
                saved_calcs.append("      Perimeter: ")
                saved_calcs.append("      " + str(tri_perimeter))
                clear3()
                back3()

            save_tri_button = Button(main_window, text="Save", font=my_font, width=30, command=save_tri)
            back_button7 = Button(main_window, text="Back", font=my_font, width=30, command=back7)
            save_tri_button.grid(row=7, column=1)
            back_button7.grid(row=7, column=0)

        calculate_button3 = Button(main_window, text="Calculate", width=30, font=my_font, command=calc_tri)
        calculate_button3.grid(row=6, column=1)
        back_button3 = Button(main_window, text="Back", width=30, font=my_font, command=back3)
        back_button3.grid(row=6, column=0)
        spacer27 = Label(main_window, text="       ")
        spacer27.grid(row=5, column=0, columnspan=2)

    # Below runs when the user chooses to calculate for parallelogram
    def parallelogramtab():
        def remove_para():
            shape_name4.destroy()
            spacer21.destroy()
            height_value3.destroy()
            base_value2.destroy()
            side_value.destroy()
            height_label3.destroy()
            base_label2.destroy()
            side_label.destroy()
            calculate_button4.destroy()
        def back9():
            remove_para()
            choosetab()
            back_button4.destroy()
        remove1()
        close_button.destroy()
        shape_name4 = Label(main_window, text="Parallelogram", font=my_font_2, width=62)
        shape_name4.grid(row=0, columnspan=2)
        spacer21 = Label(main_window, text="       ")
        spacer21.grid(row=1, columnspan=2)
        height_value3 = Entry(main_window, width=35, borderwidth=1)
        height_value3.grid(row=2, column=1)
        height_label3 = Label(main_window, text="     Enter the height:", width=15, font=my_font)
        height_label3.grid(row=2, column=0)
        base_value2 = Entry(main_window, width=35, borderwidth=1)
        base_value2.grid(row=3, column=1)
        base_label2 = Label(main_window, text="     Enter the base:", width=15, font=my_font)
        base_label2.grid(row=3, column=0)
        side_value = Entry(main_window, width=35, borderwidth=1)
        side_value.grid(row=4, column=1)
        side_label = Label(main_window, text="     Enter the side length:", width=18, font=my_font)
        side_label.grid(row=4, column=0)
        def calc_para():
            try:
                height3 = float(height_value3.get())
                base2 = float(base_value2.get())
                side = float(side_value.get())
                para_area = (height3 * base2)
                para_perimeter = (side + side + base2 + base2)
            except ValueError:
                back9()
            remove_para()
            back_button4.destroy()
            values4 = Label(main_window, text="Entered Values: ", font=my_font_3)
            height_show = Label(main_window, text=height3, font=my_font_2)
            height_show2 = Label(main_window, text="Height - ", font=my_font_2)
            base_show = Label(main_window, text=base2, font=my_font_2)
            base_show2 = Label(main_window, text="Base - ", font=my_font_2)
            side_show = Label(main_window, text=side, font=my_font_2)
            side_show2 = Label(main_window, text="Side - ", font=my_font_2)
            para_area_show = Label(main_window, text=para_area, font=my_font_2)
            para_area_show2 = Label(main_window, text="Area - ", font=my_font_2)
            para_perimeter_show = Label(main_window, text=para_perimeter, font=my_font_2)
            para_perimeter_show2 = Label(main_window, text="Perimeter - ", font=my_font_2)
            spacer22 = Label(main_window, text="       ")
            spacer23 = Label(main_window, text="       ")
            values4.grid(row=1, column=0, columnspan=2)
            height_show.grid(row=2, column=1)
            height_show2.grid(row=2, column=0)
            base_show.grid(row=3, column=1)
            base_show2.grid(row=3, column=0)
            side_show.grid(row=4, column=1)
            side_show2.grid(row=4, column=0)
            spacer22.grid(row=0, columnspan=2)
            spacer23.grid(row=7, columnspan=2)
            para_area_show.grid(row=5, column=1)
            para_area_show2.grid(row=5, column=0)
            para_perimeter_show.grid(row=6, column=1)
            para_perimeter_show2.grid(row=6, column=0)
            def clear4():
                values4.destroy()
                height_show.destroy()
                height_show2.destroy()
                base_show.destroy()
                base_show2.destroy()
                side_show.destroy()
                side_show2.destroy()
                spacer22.destroy()
                spacer23.destroy()
                save_para_button.destroy()
                back_button8.destroy()
                para_area_show.destroy()
                para_perimeter_show.destroy()
                para_area_show2.destroy()
                para_perimeter_show2.destroy()
            def back8():
                remove_para()
                choosetab()
                back_button8.destroy()
                save_para_button.destroy()
                clear4()
            def save_para():
                saved_calcs.append("Parallelogram:")
                saved_calcs.append("     Height: ")
                saved_calcs.append("     " + str(height3))
                saved_calcs.append("     Base: ")
                saved_calcs.append("     " + str(base2))
                saved_calcs.append("     Side: ")
                saved_calcs.append("     " + str(side))
                saved_calcs.append("     Area: ")
                saved_calcs.append("     " + str(para_area))
                saved_calcs.append("     Perimeter: ")
                saved_calcs.append("     " + str(para_perimeter))
                clear4()
                back8()

            save_para_button = Button(main_window, text="Save", font=my_font, width=30, command=save_para)
            back_button8 = Button(main_window, text="Back", font=my_font, width=30, command=back8)
            save_para_button.grid(row=8, column=1)
            back_button8.grid(row=8, column=0)

        spacer23 = Label(main_window, text="     ")
        spacer23.grid(row=5, columnspan=2)
        calculate_button4 = Button(main_window, text="Calculate", width=40, font=my_font, command=calc_para)
        calculate_button4.grid(row=6, column=1)
        back_button4 = Button(main_window, text="Back", width=40, font=my_font, command=back9)
        back_button4.grid(row=6, column=0)

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

    # When the close button gets clicked uses this to close the program
    def close():
        main_window.destroy()

    # When the 'show values' button is clicked, it runs this predefined function to show the saved_calcs list at the top
    def finish():
        remove1()
        list_display = Text(font=my_font)
        list_display.grid(row=0, column=0)
        for value in saved_calcs:
            list_display.insert(tkinter.END, str(value) + '\n')
        close_button.grid(row=1, column=0)

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