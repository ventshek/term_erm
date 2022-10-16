#!/bin/bash 
post_install () {
cat > /usr/share/applications/term_erm.desktop <<'ENT'
[Desktop Entry]

# The type as listed above
Type=Application

# The version of the desktop entry specification to which this file complies
Version=0.0.1

# The name of the application
Name=termerm

# A comment which can/will be used as a tooltip
Comment=Terminal stuff.

# The path to the folder in which the executable is run
Path=/usr/bin

# The executable of the application, possibly with arguments.
Exec=term_erm

# The name of the icon that will be used to display this entry
Icon=octopi

# Describes whether this application needs to be run in a terminal or not
Terminal=false
ENT
}

post_remove () {
    rm /usr/share/applications/term_erm.desktop
}