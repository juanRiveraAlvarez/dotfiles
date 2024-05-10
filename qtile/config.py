# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from PIL import Image
import os
import psutil

import subprocess

def rgbTohex(tupla):
    return "#{:02x}{:02x}{:02x}".format(tupla[0],tupla[1],tupla[2])

background_image = "/home/juan/Pictures/wallpaper2.png"
img = Image.open(background_image)
bg_dark = img.getpixel((5,5))

colores = {"bg-dark":rgbTohex(bg_dark),"bg":"#e1d6a9","red":"#cc241d","green":"#98971a","yellow":"#d79921","blue":"#458588","purple":"#b16286","aqua":"#689d6a","gray":"#928374"}


mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.shrink(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_down(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.shrink(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "c", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([mod], "e", lazy.spawn("alacritty -e ranger"), desc="Spawn a command using a prompt widget"),

    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]



__groups = { 1:Group(" 󰣇 "),2:Group("  "),3:Group(" 󰈙 "),4:Group("  "),5:Group("  "),6:Group("  "),7:Group("  "),8:Group("  "),9:Group("  ")}


groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    #layout.Max(),
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_focus=[colores["purple"],colores["purple"]],margin=8,single_margin=8,border_width=3,border_on_single=colores["purple"]),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="HackNerdFont",
    fontsize=12,
    padding=0,
)
extension_defaults = widget_defaults.copy()

powerline = {
        "decorations":[
            PowerLineDecoration(path="rounded_left", padding_y=0)   
        ]        
}
powerline2 = {
        "decorations":[
            PowerLineDecoration(path="rounded_right", padding_y=0)   
        ]        
    }

screens = [
    Screen(
        top=bar.Bar(
            [
   #             widget.CurrentLayout(),
                widget.GroupBox(
                    background=colores["blue"],
                    highlight_color=colores["purple"],
                    highlight_method="line",
                    spacing=0,
                    active=colores["gray"],
                    block_highlight_text_color="#ffffff",
                    borderwidth=0,
                    padding=10,
                    **powerline 
                    ),
                widget.TextBox("  ",fontsize=35,background=colores["bg-dark"],foreground=colores["blue"],padding=-6.65),
                widget.Prompt(),
                widget.WindowName(background=colores["bg-dark"],padding=5),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.TextBox("  ",fontsize=35,background=colores["bg-dark"],foreground=colores["aqua"],padding=0,**powerline2),
                widget.TextBox(" 󰍛",fontsize=16,background=colores["aqua"],padding=2),
                widget.Memory(background=[colores["aqua"]]),
                widget.TextBox("  ",fontsize=35,background=colores["aqua"],foreground=colores["yellow"],padding=0,**powerline2),
                widget.TextBox("",fontsize=16,background=colores["yellow"],padding=10),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p",background=colores["yellow"]),
                widget.TextBox("  ",fontsize=30,background=colores["yellow"],foreground=colores["gray"],padding=0, **powerline2),
                widget.QuickExit(background=colores["gray"], padding=7),
                widget.Systray(background=colores["gray"]),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
    Screen(
        top=bar.Bar(
            [
   #             widget.CurrentLayout(),
                widget.GroupBox(
                    background=colores["blue"],
                    highlight_color=colores["purple"],
                    highlight_method="line",
                    spacing=0,
                    active=colores["gray"],
                    block_highlight_text_color="#ffffff",
                    borderwidth=0,
                    padding=10,
                    **powerline
                    ),
                widget.TextBox("  ",fontsize=35,background=colores["bg-dark"],foreground=colores["blue"],padding=-6.65),
                widget.Prompt(),
                widget.WindowName(background=colores["bg-dark"],padding=5),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.TextBox(" ",fontsize=21,background=colores["bg-dark"],foreground=colores["aqua"],padding=0,**powerline2),
                widget.TextBox(" 󰍛",fontsize=16,background=colores["aqua"],padding=1),
                widget.Memory(background=[colores["aqua"]],padding=3),
                widget.TextBox("  ",fontsize=21,background=colores["aqua"],foreground=colores["yellow"],padding=0,**powerline2),
                widget.TextBox(" ",fontsize=16,background=colores["yellow"],padding=1),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p",background=colores["yellow"],padding=10),
            ],
            25,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None



# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

#start =  ["feh --bg-fill /home/juan/Images/wallpaper.png &","xset b off &"]

#for i in start:
#    os.system(i)

autostart = [
        f'feh --bg-fill {background_image} &',
        "xset b off",
        "setxkbmap us",
        "udiskie &",
        "nm-applet &",
        "cbatticon &",
        "picom &",
        "volumeicon &",
]

def check(name):
    name = name[:-2]
    for i in psutil.process_iter(['pid','name']):
        if name == i.info['name']:
            return True
    return False

for x in autostart:
    if check(x) is False:
        os.system(x)

    




wmname = "LG3D"

