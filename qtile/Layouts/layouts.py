from libqtile import layout
from libqtile.config import Match
from  extras import color_bar
colores = color_bar.color_bar()
layouts = [
        layout.MonadTall(border_focus=[colores["purple"],colores["purple"]],margin=8,single_margin=8,border_width=3,border_on_single=colores["purple"]),
]
floating_layout = layout.Floating(
        float_rules=[
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
        ],
        border_focus = colores["purple"]
)
