#!/bin/bash
# Adds .desktop entry for termerm after installation.
post_install () {
cat > /usr/share/applications/term_erm.desktop <<'ENT'
[Desktop Entry]

# The type.
Type=Application

# The version of the desktop entry.
Version=0.0.1

# The name of the application.
Name=termerm

# A comment, used as a tooltip.
Comment=Terminal and editor.

# The path to the folder in which the executable is run.
Path=/usr/bin

# The executable of the application, possibly with arguments.
Exec=term_erm

# The name of the icon that will be used to display this entry.
Icon=sublime-text

# Describes whether this application needs to be run in a terminal or not.
Terminal=false
ENT
}
# Removes the desktop entry after uninstallation.
post_remove () {
    rm /usr/share/applications/term_erm.desktop
}