from libqtile.config import Screen
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile import bar
from Systray.Systray import Systray

from extras.color_bar import color_bar
colores = color_bar()

widget_defaults = dict(
    font="AgaveNerdFont",
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
                widget.TextBox("  ",fontsize=35,foreground=colores["gray"],padding=-6),
                widget.Prompt(),
                widget.WindowName(padding=5,foreground=colores["gray"]),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("  ",fontsize=35,foreground=colores["aqua"],padding=-0,**powerline2),
                widget.TextBox("󰍛",fontsize=16,background=colores["aqua"],padding=10),
                widget.Memory(background=[colores["aqua"]]),
                widget.TextBox("  ",fontsize=35,background=colores["aqua"],foreground=colores["yellow"],padding=-5,**powerline2),
                widget.TextBox("",fontsize=16,background=colores["yellow"],padding=13),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p",background=colores["yellow"]),
                widget.TextBox("  ",fontsize=30,background=colores["yellow"],foreground=colores["gray"],padding=-5, **powerline2),
                widget.QuickExit(background=colores["gray"], padding=0),
                widget.TextBox("  ",fontsize=30,background=colores["gray"],foreground=colores["bg-dark"],padding=-11, **powerline),
                Systray(),
            ],
            24,
            margin=[10,10,0,10],
            background="#00000000"
        ),
    ),
    Screen(
        top=bar.Bar(
            [
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
                widget.TextBox("  ",fontsize=35,foreground=colores["blue"],padding=-6.65),
                widget.Prompt(),
                widget.WindowName(padding=5,foreground=colores["gray"]),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(" ",fontsize=21,foreground=colores["aqua"],padding=0,**powerline2),
                widget.TextBox("󰍛",fontsize=16,background=colores["aqua"],padding=7),
                widget.Memory(background=[colores["aqua"]],padding=3),
                widget.TextBox(" ",fontsize=21,background=colores["aqua"],foreground=colores["yellow"],padding=1,**powerline2),
                widget.TextBox("",fontsize=16,background=colores["yellow"],padding=10),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p",background=colores["yellow"],padding=10),
            ],
            24,
            margin=[10,10,0,10],
            background="#00000000"
        ),
    ),
]
