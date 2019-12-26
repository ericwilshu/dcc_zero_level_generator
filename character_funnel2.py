"""
This module is a command line application that outputs a 11'x8.5' .pdf with 4
randomly generated Dungeon Crawl Classic RPG 0-level characters on it.

Functions:
    get_characters()

Dependencies:
    Modules:
        argparse
        datetime
        webbrowser
        cairosvg
        import_data
        char_sheet_assembler2
        char_sheet_creator2
        character_generator2
    Files:
        2x2_template_blank.svg
        char_sheet_blank.svg
        Table1_1_Ability_Score_Modifiers.csv
        Table1_2_Luck_Score.txt
        Human_Occupations.csv
        Dwarf_Occupations.csv
        Elf_Occupations.csv
        Halfling_Occupations.csv
        Table1_3a_Farmer_Type.txt
        Table1_3b_Animal_Type.txt
        Table1_3c_Whats_In_The_Cart.txt
        Table3_4_Equipment.txt
        AppendixL.csv
"""
import argparse
from datetime import datetime
import webbrowser
from cairosvg import svg2pdf as s2p
from import_data import getDataFiles
from char_sheet_assembler2 import assemble_sheets



def getCharacters():
    """Output a .pdf file with 4 zero level Dungeon Crawl Classics RPG characters on it."""
    #Parse the command line arguments.
    parser = argparse.ArgumentParser(description='Create a 11"x8.5" pdf with 4 Dungeon Crawl Classics 0-level characters on it.')
    parser.add_argument(    "-t",
                            "--testSuitability",
                            help="Only use characters with a attribute bonus total of 0 or greater.",
                            action="store_true")
    parser.add_argument(    "-X",
                            "--noHuman",
                            help="Disallow human characters in your funnel.",
                            action="store_true")
    parser.add_argument(    "-d",
                            "--noDwarf",
                            help="Disallow dwarf characters in your funnel.",
                            action="store_true")
    parser.add_argument(    "-e",
                            "--noElf",
                            help="Disallow elf characters in your funnel.",
                            action="store_true")
    parser.add_argument(    "-x",
                            "--noHalfling",
                            help="Disallow halfling characters in your funnel.",
                            action="store_true")
    args = parser.parse_args()
    #Get the current date and time to label the .pdf file.
    now = datetime.today().strftime("%Y-%m-%d_%H:%M:%S")
    NEW_SHEET_PDF = "static/new_sheets/" + now + ".pdf"

    #Get the rulebook data!
    dataDict = getDataFiles("data_files/")
    #Assemble the sheet by running char_sheet_assembler2.
    new_sheet = assemble_sheets(dataDict, args.testSuitability, args.noHuman, args.noDwarf, args.noElf, args.noHalfling)
    #Convert from .svg to .pdf with cairosvg module.
    s2p(url=new_sheet, write_to=NEW_SHEET_PDF)
    #Open the .pdf in whatever app the user's os has set to look at .pdfs!
    webbrowser.open(NEW_SHEET_PDF, new=2)



if __name__ == "__main__":
    getCharacters()
