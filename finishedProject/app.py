# DearPyGUI Imports
from dearpygui.dearpygui import *

# functions.py Imports
from functions import pre_process, predict


# button callbak function
# runs each time when the "Check" button is clicked
def check_spam():
    # collect input
    input_value = get_value("_Input")
    print(f"input value:\n\t{input_value}")

    # input pre-process and get prediction
    input_value = pre_process(input_value)
    pred_text, text_color = predict(input_value)

    # delete last prediction displayed
    delete_item("del")
    # display prediction to user
    add_text(default_value=pred_text, color=text_color, tag="del", parent="win1", before="text pred before this")

# DearPyGUI
create_context()
set_global_font_scale(1.25)  # global font scale

# loading logo_spamFilter.png
width, height, channels, data = load_image("logo_spamFilter.png")
with texture_registry(show=False):
    add_static_texture(width=width, height=height, default_value=data, tag="logo")

with window("Simple SMS Spam Filter", width=520, height=677, tag="win1"):
    print("GUI is running...")
    with group(pos=[30, 70]):
        # inserting logo_spamFilter.png
        add_image(texture_tag="logo")
    # height of image + position from image group
    with group(pos=[30, height+70]):add_separator()
        add_spacer(height=12)
        # text instructions
        add_text("Please Enter an SMS message of your choice to check if it's spam or not.",
                 color=[232, 163, 33], wrap=460)
        add_spacer(height=12)
        # collect input
        add_input_text(label="Input", tag="_Input", width=415, default_value="type message here!")
        add_spacer(height=12)
        # action button
        add_button(label="Check", callback=check_spam)
        add_spacer(height=12)
        add_separator()
        add_spacer(height=12)
        add_spacer(tag="text pred before this")

create_viewport(width=540, height=720, x_pos=600, y_pos=256)
setup_dearpygui()
show_viewport()
start_dearpygui()
print("Bye Bye, GUI")
destroy_context()
