"""
Replace the contents of this module docstring with your own details.
"""


def main():

    print("Songs To Learn 1.0 - by Caleb Forrest")
    menu_select = str(input("Menu: \nL - List Songs \nA - Add New Song \nC - Complete a Song \nQ - Quit\n>>>"))
    menu_select_upper = menu_select.upper()

    while menu_select_upper not in "Q":
        f = open("songs.csv", "r")
        song_list = f.readlines()
        menu(song_list, menu_select_upper)

        menu_select = str(input("Menu: \nL - List Songs \nA - Add New Song \nC - Complete a Song \nQ - Quit\n>>>"))
        menu_select_upper = menu_select.upper()

    print("b")


def menu(song_list, menu_select_upper):

    if menu_select_upper in "L":
        for row in song_list:
            make_list = row
            final_list = make_list.split(",")
        print (final_list[:-1])





    if menu_select_upper in "A":
        new_song = []
        song_name = str(input("Title: "))
        if not song_name:
            print("Input cannot be blank")
            song_name = str(input("Title: "))
        new_song.append(song_name)

        artist_name = str(input("Artist: "))
        if not artist_name:
            print("Input cannot be blank")
            artist_name = str(input("Artist: "))
        new_song.append(artist_name)

        valid_input = False
        while not valid_input:
            try:
                year = int(input("Year: "))
                if year < 0:
                    print("Must be >= 0")
                    year = int(input("Year: "))

                valid_input = True

            except ValueError:
                print("Invalid input; enter a valid number")
        output_year = str(year)
        new_song.append(output_year)

        new_song.append("n")
        output_list = ", ".join(new_song)
        return output_list











main()
