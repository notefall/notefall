import thorpy
import pygame

application = thorpy.Application((800, 600), "notefall")

title = thorpy.make_text("notefall", 42, (255,0,0))

playbutton = thorpy.make_button("Play")
playbutton.set_size((80, 40))
thorpy.makeup.add_basic_help(playbutton,"Play the game.")

optionsbutton = thorpy.make_button("Options")
optionsbutton.set_size((80, 40))
thorpy.makeup.add_basic_help(optionsbutton, "Open settings.")

exitbutton = thorpy.make_button("Exit")
exitbutton.set_size((80, 40))
thorpy.makeup.add_basic_help(exitbutton, "Exit the game.")

elements = [title, playbutton, optionsbutton, exitbutton]

background = thorpy.Background(image="default_theme/homescreen_bg.jpg", elements=[title, playbutton, optionsbutton, exitbutton])

thorpy.store(background)

menu = thorpy.Menu(background)
menu.play()

application.quit()