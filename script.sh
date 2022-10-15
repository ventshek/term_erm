#!/bin/bash 
post_install () {
cat > /usr/share/applications/term_erm.desktop <<'ENT'
[Desktop Entry]

# The type as listed above
Type=Application

# The version of the desktop entry specification to which this file complies
Version=0.0.1

# The name of the application
Name=term_erm

# A comment which can/will be used as a tooltip
Comment=Terminal stuff.

# The path to the folder in which the executable is run
Path=/usr/lib/python3.10/site-packages/term_erm

# The executable of the application, possibly with arguments.
Exec=python main.py

# The name of the icon that will be used to display this entry
Icon=jmemorize

# Describes whether this application needs to be run in a terminal or not
Terminal=false
ENT
}