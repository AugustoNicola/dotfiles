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

import os
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.command import lazy as lazy_cmd
from libqtile.utils import guess_terminal

palette_colors = {
    "primary": [
        '#8A3B99',
        '#9F4AB0',
        '#A661B3',
        '#B58BBD',
        '#C59FCB',
        '#9130A5' #groups : [5]
    ],
    "secondary": [
        '#74D092'
    ],
    "background": "#252525"
}

mod = "mod4"
alt = "mod1"

terminal = "gnome-terminal"
web_browser = "firefox"
file_explorer = "xdg-open ."
music_player = "spotify"
spotify_cli = "bash /home/lambda/.config/qtile/sp.sh"
ide = "code -n"
text_editor = "subl -n"
discord = "discord"
screenshot = "scrot '%F_%H:%M.png' -zp -e 'mv $f ~/Pictures/Screenshots/'"
screenshot_and_edit = "scrot '%F_%H:%M.png' -zp -e 'mv $f ~/Pictures/Screenshots/ && gimp ~/Pictures/Screenshots/$f'"

# ============================================================================
# ===========================    KEYBINDINGS     =============================
# ============================================================================
keys = [
    # ========== Desplazarse entre ventanas ==========
    Key([mod], "Left", lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(),
        desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(),
        desc="Move window focus to next window"),

    # ========== Mover ventanas en un mismo grupo ==========
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),
        desc="Move window up"),

    # ========== Modificar el tamaño de ventanas ==========
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    
    # ========== Interactuar con ventanas ==========
    Key([mod], "w", lazy.window.kill(),
        desc="Kill focused window"),

    # ========== Desplazarse entre grupos ==========
    Key([mod], "Tab", lazy.screen.next_group(),
        desc="Go to next group"),
     Key([mod, "shift"], "Tab", lazy.screen.prev_group(),
        desc="Go to next group"),

    # ========== Alternar entre layout modes ==========
    Key([mod], "space", lazy.next_layout(),
        desc="Toggle between layouts"),

    # ========== Spawns ==========
    Key([mod], "r", lazy.spawn("rofi -show run"),
        desc="Spawn rofi to run applications"),
    Key([mod], "x", lazy.spawncmd(),
        desc="Run a command using a prompt widget"),

    Key([mod], "t", lazy.spawn(terminal),
        desc="Launch default terminal"),
    Key([mod], "e", lazy.spawn(web_browser),
        desc="Launch default web browser"),
    Key([mod], "f", lazy.spawn(file_explorer),
        desc="Launch default file explorer"),
    Key([mod], "m", lazy.spawn(music_player),
        desc="Launch default music player"),
    Key([mod], "c", lazy.spawn(ide),
        desc="Launch default IDE"),
    Key([mod], "s", lazy.spawn(text_editor),
        desc="Launch default text editor"),
    Key([mod], "d", lazy.spawn(discord),
        desc="Launch discord"),
    Key([], "Print", lazy.spawn(screenshot),
        desc="Take a screenshot of the current view, mouse included"),
    Key([mod], "Print", lazy.spawn(screenshot_and_edit),
        desc="Take a screenshot of the current view, mouse included, and then open it in GIMP"),

    # ========== Controles de Spotify ==========
    Key([alt], "F7", lazy.spawn(spotify_cli + " play"),
        desc="Play/pause spotify"),
    Key([alt], "F6", lazy.spawn(spotify_cli + " prev"),
        desc="Rewind spotify"),
    Key([alt], "F8", lazy.spawn(spotify_cli + " next"),
        desc="Foward spotify"),

    # ========== Alimentacion de Qtile ==========
    Key([mod, "control"], "r", lazy.restart(),
        desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),
]

# ============================================================================
# ===============================   GRUPOS   =================================
# ============================================================================
if __name__ in ["config", "__main__"]:

    group_props = [
    #   ("name", {"arg": "val"}),
        ("HOME", {'label':'ﬦ'}),
        ("WEB", {'label':'', 'matches': [Match(wm_class=["Firefox"])]}),
        ("DEV", {'label':'', 'matches': [Match(wm_class=["Code", "Sublime_text"])]}),
        ("TER", {'label':'', 'matches': [Match(wm_class=["Gnome-terminal"])]}),
        ("DIS", {'label':'', 'matches': [Match(wm_class=["Discord"])]}),
        ("MUS", {'label':'', 'matches': [Match(wm_class=["Spotify"])]}),
        ("CFG", {'label':'', 'matches': [Match(wm_class=["Pavucontrol"])]})
    ]
    groups = [Group(name, init=True, persist=True, **kwargs) for name, kwargs in group_props]

    for i, (name, kwargs) in enumerate(group_props, 1):
        keys.extend([
            # Cambiar a grupo
            Key([mod], str(i), lazy.group[name].toscreen(),
                desc="Switch to group {}".format(name)),

            # Mover ventana a grupo
            Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(name)),
        ])

# ============================================================================
# =============================      LAYOUTS     =============================
# ============================================================================
layouts = [
    layout.Columns(
        name = "columns",
        border_focus = palette_colors["secondary"][0],
        border_width = 3,
        border_on_single = True,
        grow_amount = 10,
        fair = False,
        num_columns = 2,
        margin = 3
    ),
    layout.Max(name = "fullscreen"),
    # layout.MonadTall(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
],
    border_focus = palette_colors["primary"][3],
    border_width = 3,
)
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# ============================================================================
# ========================    MOUSE CALLBACKS     ============================
# ============================================================================
def open_wifi_settings():
    qtile.cmd_spawn('nm-connection-editor')
    if qtile.current_group.name != "CFG":
        qtile.groups_map["CFG"].cmd_toscreen() #ver libqtile/core/manager.py -> metodo cmd_togroup()

def open_audio_settings():
    qtile.cmd_spawn('pavucontrol')
    if qtile.current_group.name != "CFG":
        qtile.groups_map["CFG"].cmd_toscreen() #ver libqtile/core/manager.py -> metodo cmd_togroup()


# ============================================================================
# ============================    SCREENS     ================================
# ============================================================================
groupbox_defaults = dict(
    background = palette_colors["background"],

    this_current_screen_border = '#9130A5',
    highlight_method = 'block',

    active = '#FFFFFF',
    inactive = '#9b9b9b',
    urgent_alert_method = 'block',

    spacing = 5,
    padding = 12,
    margin_y = 2.5,
    rounded = False,
    use_mouse_wheel = False
)

widget_defaults = dict(
    font='JetBrains Mono Bold',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                # Barra de Grupos
                widget.GroupBox(
                    visible_groups = ["HOME"],
                    font = "FiraCode Nerd Font",
                    fontsize = 26,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["WEB"],
                    font = "Font Awesome 5 Free",
                    fontsize = 20,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["DEV", "TER"],
                    font = "Font Awesome 5 Free",
                    fontsize = 17,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["DIS", "MUS"],
                    font = "Font Awesome 5 Free",
                    fontsize = 20,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["CFG"],
                    font = "Font Awesome 5 Free",
                    fontsize = 18,
                    **groupbox_defaults
                ),
                # Prompt para correr comandos
                widget.Prompt(
                    background = palette_colors["background"],
                    prompt = 'Run: ',
                    name = 'prompt'
                ),
                # Espacio Dinamico
                widget.Spacer(background = palette_colors["background"]),
                # Nombre de Ventana
                widget.WindowName(
                    background = palette_colors["background"],
                    width = bar.CALCULATED,
                    max_chars = 100,
                    foreground = palette_colors["secondary"][0]
                ),
                # Espacio Dinamico
                widget.Spacer(background = palette_colors["background"]),
                # Flecha
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background = palette_colors["background"],
                    foreground = palette_colors["primary"][3]
                ),
                # Barra de Programas
                widget.Systray(
                    background = palette_colors["primary"][3],
                ),
                # Espaciado
                widget.Sep(linewidth = 0, padding = 5, background=palette_colors["primary"][3]),
                # Flecha
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background = palette_colors["primary"][3],
                    foreground = palette_colors["primary"][2]
                ),
                # Icono de internet
                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    text = '',
                    fontsize = 13.5,
                    background = palette_colors["primary"][2],
                    mouse_callbacks = {'Button1': open_wifi_settings}
                ),
                # Espaciado entre iconos
                widget.Sep(linewidth = 0, padding = 5, background = palette_colors["primary"][2]),
                # Icono de audio
                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    text = '',
                    fontsize = 13.5,
                    background = palette_colors["primary"][2],
                    mouse_callbacks = {'Button1': open_audio_settings}
                ),
                # Espaciado
                widget.Sep(linewidth = 0, padding = 5, background=palette_colors["primary"][2]),
                # Flecha
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background=palette_colors["primary"][2],
                    foreground=palette_colors["primary"][1]
                ),
                # Icono de calendario
                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    text = '',
                    fontsize = 14,
                    background = palette_colors["primary"][1]
                ),
                # Espaciado
                widget.Sep(linewidth = 0, padding = 3, background=palette_colors["primary"][1]),
                # Widget Fecha
                widget.Clock(
                    format='%Y/%m/%d %a',
                    background=palette_colors["primary"][1],
                ),
                # Espaciado
                widget.Sep(linewidth = 0, padding = 5, background=palette_colors["primary"][1]),
                # Flecha
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background=palette_colors["primary"][1],
                    foreground=palette_colors["primary"][0]
                ),
                # Icono de reloj
                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    text = '',
                    fontsize = 14,
                    background = palette_colors["primary"][0]
                ),
                # Espaciado
                widget.Sep(linewidth = 0, padding = 3, background=palette_colors["primary"][0]),
                # Widget Hora
                widget.Clock(
                    format='%I:%M %p',
                    background=palette_colors["primary"][0],
                ),
                # Espaciado borde derecho
                widget.Sep(linewidth = 0, padding = 10, background = palette_colors["primary"][0])
            ],
            32,
        ),
        wallpaper="/home/lambda/Pictures/Wallpapers/wallpaper.jpg",
        wallpaper_mode="fill"
    )
]

# ============================================================================
# =============================    SCRIPTS    ================================
# ============================================================================
#@hook.subscribe.startup_once
#def startup_once():
    # script = os.path.expanduser('~/.config/qtile/startup_once.sh')
    # subprocess.call([script])

@hook.subscribe.startup
def startup():
    script = os.path.expanduser('~/.config/qtile/startup.sh')
    subprocess.call([script])

# ============================================================================
# =============================    CONFIGS    ================================
# ============================================================================
auto_fullscreen = True
bring_front_click = False
cursor_warp = False
dgroups_app_rules = []  # type: List
dgroups_key_binder = None
focus_on_window_activation = "smart"
follow_mouse_focus = False
main = None  # WARNING: this is deprecated and will be removed soon
wmname = "qtile" # window manager name, e.g. used in neofetch // problema con JAVA?
