""" 
COMP 593 - Lab 8

Description: 
  Displays a graphical user interface to request a pokemon name, and then show its 
  basic information and stats.

Usage:
  python Pokemon_Info_Viewer.py

Parameters:
  None.

History:
  Date        Author      Description
  2022-04-15  A.Asturias  Initial creation
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pokeinfo import retrieve_pokemon_data

def main():

    #function that gets called when the button is clicked
    def get_pokemon_info():

        #get name from textbox
        pokemon_name = name_textbox.get()

        #get pokemon info as a dictionary
        pokemon_info = retrieve_pokemon_data(pokemon_name)

        if pokemon_info:

            #change labels' text
            value_height_label['text'] = str(pokemon_info['height']) + ' dm'
            value_weight_label['text'] = str(pokemon_info['weight']) + ' hg'

            #get all the types and change label's text
            pokemon_types = []
            for type in pokemon_info['types']:
                pokemon_types.append(type['type']['name'])
            value_type_label['text'] = ', '.join(pokemon_types)

            #get pokemon stats and change values from progress bars
            hp_progress['value'] = pokemon_info['stats'][0]['base_stat']
            attack_progress['value'] = pokemon_info['stats'][1]['base_stat']
            defense_progress['value'] = pokemon_info['stats'][2]['base_stat']
            spe_attack_progress['value'] = pokemon_info['stats'][3]['base_stat']
            spe_defense_progress['value'] = pokemon_info['stats'][4]['base_stat']
            speed_progress['value'] = pokemon_info['stats'][5]['base_stat']

        #for every possible scenario where data was not retrieved
        else:
            #change labels' text
            value_height_label['text'] = ''
            value_weight_label['text'] = ''
            value_type_label['text'] = ''

            #change values from progress bars
            hp_progress['value'] = 0
            attack_progress['value'] = 0
            defense_progress['value'] = 0
            spe_attack_progress['value'] = 0
            spe_defense_progress['value'] = 0
            speed_progress['value'] = 0

            #display messagebox
            messagebox.showerror('Catastrophic Error!', 'Unable to get pokemon info, try again.')


    #instantiate script window
    main_window = Tk()

    #change title, icon, and disable resize
    main_window.title('Pokemon Info Viewer')
    main_window.iconbitmap('blue_pokeball.ico')
    main_window.resizable(False, False)

    #instantiate frames and their position in the script window grid
    input_frame = ttk.Frame(main_window)
    input_frame.grid(row=0, column=0, columnspan=2, pady=(20,0))

    info_frame = ttk.LabelFrame(main_window, text='Pokemon Info', width=200)
    info_frame.grid(row=1, column=0, padx=(20,10), pady=20, sticky=N)

    stats_frame = ttk.LabelFrame(main_window, text='Pokemon Stats')
    stats_frame.grid(row=1, column=1, padx=(10,20), pady=20)

    #instantiate all elements inside input frame
    name_label = ttk.Label(input_frame, text='Pokemon Name:')
    name_label.grid(row=0, column=0)

    name_textbox = ttk.Entry(input_frame)
    name_textbox.grid(row=0, column=1, padx=(5,10))

    name_button = ttk.Button(input_frame, text='Get Info', command=get_pokemon_info)
    name_button.grid(row=0, column=2)

    #instantiate all labels inside info frame
    #height info
    height_label = ttk.Label(info_frame, text='Height:')
    height_label.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)

    value_height_label = ttk.Label(info_frame, width=15)
    value_height_label.grid(row=0, column=1, pady=(10,5), sticky=W)

    #weight info
    weight_label = ttk.Label(info_frame, text='Weight:')
    weight_label.grid(row=1, column=0, padx=(10,5), pady=5, sticky=E)

    value_weight_label = ttk.Label(info_frame, width=15)
    value_weight_label.grid(row=1, column=1, pady=5, sticky=W)

    #type info
    type_label = ttk.Label(info_frame, text='Type:')
    type_label.grid(row=3, column=0, padx=(10,5), pady=(5,10), sticky=E)

    value_type_label = ttk.Label(info_frame, width=15)
    value_type_label.grid(row=3, column=1, pady=(5,10), sticky=W)

    #instantiate all labels and progress bars for the stats frame
    #hp stats
    hp_label = ttk.Label(stats_frame, text='HP:')
    hp_label.grid(row=0, column=0, padx=(10,5), sticky=E)

    hp_progress = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    hp_progress.grid(row=0, column=1, padx=(0, 10), pady=(10,5))

    #attack stats
    attack_label = ttk.Label(stats_frame, text='Attack:')
    attack_label.grid(row=1, column=0, padx=(10,5), sticky=E)

    attack_progress = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    attack_progress.grid(row=1, column=1, padx=(0, 10), pady=5)

    #defense stats
    defense_label = ttk.Label(stats_frame, text='Defense:')
    defense_label.grid(row=2, column=0, padx=(10,5), sticky=E)

    defense_progress = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    defense_progress.grid(row=2, column=1, padx=(0, 10), pady=5)

    #special attack stats
    spe_attack_label = ttk.Label(stats_frame, text='Special Attack:')
    spe_attack_label.grid(row=3, column=0, padx=(10,5), sticky=E)

    spe_attack_progress = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    spe_attack_progress.grid(row=3, column=1, padx=(0, 10), pady=5)

    #special defense stats
    spe_defense_label = ttk.Label(stats_frame, text='Special Defense:')
    spe_defense_label.grid(row=4, column=0, padx=(10,5), sticky=E)

    spe_defense_progress = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    spe_defense_progress.grid(row=4, column=1, padx=(0, 10), pady=5)

    #speed stats
    speed_label = ttk.Label(stats_frame, text='Speed:')
    speed_label.grid(row=5, column=0, padx=(10,5), sticky=E)

    speed_progress = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    speed_progress.grid(row=5, column=1, padx=(0, 10), pady=(5,10))
    
    #infinite loop to look for events and keep window open
    main_window.mainloop()

main()