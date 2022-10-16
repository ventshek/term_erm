# Imports.
import sys
import gi
import io
from gi.repository import GObject
from gi.repository import GLib
gi.require_version('Vte', '2.91')
from gi.repository import Vte
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

if (sys.argv[1] == "--help"):
  print("help")
  quit()
elif (sys.argv[1] == "-h"):
  print("help")
  quit()

CSS_File = b"""
/* shrink headerbars */
headerbar {
    min-height: 0px;
    padding-left: 2px; /* same as childrens vertical margins for nicer proportions */
    padding-right: 2px;
    background-color: #2d2d2d;
    border:0;
}
textview text {
    color:#4fc3f7;
}
button {
    border-radius: 10px;
}
button:hover {
    border-color: pink;
    opacity: 50;
}
button:active {
  color: #FFF;
  background: #F00;
}
headerbar entry,
headerbar spinbutton,
headerbar button,
headerbar separator {
    margin-top: 0px; /* same as headerbar side padding for nicer proportions */
    margin-bottom: 0px;
}
/* shrink ssd titlebars */
.default-decoration {
    min-height: 0; /* let the entry and button drive the titlebar size */
    padding: 0px;
    background-color: #2d2d2d;
}
.default-decoration .titlebutton {
    min-height: 0px; /* tweak these two props to reduce button size */
    min-width: 0px;
}
window.ssd headerbar.titlebar {
    padding-top: 3px;
    padding-bottom: 3px;
    min-height: 0;
    background-color: #2d2d2d;
}
window.ssd headerbar.titlebar button.titlebutton {
    padding: 3px;
    min-height: 0;
    border-radius: 0;
    margin-right: 2px;
    background-color: #2d2d2d;
}
"""

# Gobject VTE entry.
GObject.type_register(Vte.Terminal)

# GTK Settings.
settings = Gtk.Settings.get_default()
settings.set_property("gtk-application-prefer-dark-theme", True)
screen = Gdk.Screen.get_default()
provider = Gtk.CssProvider()
provider.load_from_data(CSS_File)
Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class Handler:

    def onDestroy(self, *args):
        Gtk.main_quit()

        # p = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "t1.ps1"', stdout=sys.stdout)
        # p.communicate()

    def onRunClicked(self, button):
        text = textbuffer1.get_text(textbuffer1.get_start_iter(),
                        textbuffer1.get_end_iter(),
                        True)
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        print(text)
        output = new_stdout.getvalue()
        sys.stdout = old_stdout
        terminal.feed_child(output.encode("utf-8"))
        terminal.feed_child("\n".encode("utf-8"))

    def onSaveClicked(self, button):
        text = textbuffer1.get_text(textbuffer1.get_start_iter(),
                        textbuffer1.get_end_iter(),
                        True)
        title = entry1.get_text()
        writepath = ('%s.sh' % title)
        mode = 'w' if os.path.exists(writepath) else 'w'
        with open(writepath, mode) as f:
            f.write(text)

    def onOpenClicked(self, button):
        title = entry1.get_text()
        writepath = ('%s.sh' % title)
        with open(writepath, "r") as f:
            textbuffer1.set_text(f.read())

    def onRunScriptClicked(self, button):
        text = textbuffer1.get_text(textbuffer1.get_start_iter(),
                        textbuffer1.get_end_iter(),
                        True)
        title = "/tmp/eg"
        writepath = ('%s.sh' % title)
        mode = 'w' if os.path.exists(writepath) else 'w'
        with open(writepath, mode) as f:
            f.write(text)
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        print("sudo sh /tmp/eg.sh")
        output = new_stdout.getvalue()
        sys.stdout = old_stdout
        terminal.feed_child(output.encode("utf-8"))
        terminal.feed_child("\n".encode("utf-8"))


MENU_XML = """
<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.40.0 -->
<interface>
  <requires lib="gtk+" version="3.24"/>
  <requires lib="vte-2.91" version="0.69"/>
  <object class="GtkTextBuffer" id="textbuffer1"/>
  <object class="GtkWindow" id="window1">
    <property name="can-focus">False</property>
    <signal name="destroy" handler="onDestroy" swapped="no"/>
    <child>
      <object class="GtkBox">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkBox">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="margin-left">2</property>
            <property name="margin-right">2</property>
            <property name="margin-top">2</property>
            <property name="margin-bottom">2</property>
            <child>
              <object class="GtkButton">
                <property name="label" translatable="yes">Run</property>
                <property name="visible">True</property>
                <property name="can-focus">True</property>
                <property name="receives-default">True</property>
                <signal name="clicked" handler="onRunScriptClicked" swapped="no"/>
                <accelerator key="Return" signal="clicked" modifiers="GDK_SHIFT_MASK"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton">
                <property name="label" translatable="yes">Run Script</property>
                <property name="visible">True</property>
                <property name="can-focus">True</property>
                <property name="receives-default">True</property>
                <signal name="clicked" handler="onRunScriptClicked" swapped="no"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <object class="GtkButton">
                <property name="label" translatable="yes">Save</property>
                <property name="name">Save</property>
                <property name="visible">True</property>
                <property name="can-focus">True</property>
                <property name="receives-default">True</property>
                <signal name="clicked" handler="onSaveClicked" swapped="no"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="pack-type">end</property>
                <property name="position">17</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton">
                <property name="label" translatable="yes">Open</property>
                <property name="name">Save</property>
                <property name="visible">True</property>
                <property name="can-focus">True</property>
                <property name="receives-default">True</property>
                <signal name="clicked" handler="onOpenClicked" swapped="no"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="pack-type">end</property>
                <property name="position">18</property>
              </packing>
            </child>
            <child>
              <object class="GtkEntry" id="entry1">
                <property name="visible">True</property>
                <property name="can-focus">True</property>
                <property name="placeholder-text" translatable="yes">Name of Script</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="pack-type">end</property>
                <property name="position">19</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkBox">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="orientation">vertical</property>
            <child>
              <object class="GtkScrolledWindow">
                <property name="visible">True</property>
                <property name="can-focus">True</property>
                <property name="shadow-type">in</property>
                <child>
                  <object class="GtkTextView" id="terminal_text">
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="hexpand">True</property>
                    <property name="vexpand">True</property>
                    <property name="wrap-mode">word</property>
                    <property name="left-margin">2</property>
                    <property name="right-margin">2</property>
                    <property name="top-margin">2</property>
                    <property name="bottom-margin">2</property>
                    <property name="buffer">textbuffer1</property>
                    <property name="input-purpose">terminal</property>
                    <property name="monospace">True</property>
                  </object>
                </child>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkScrolledWindow">
                <property name="visible">True</property>
                <property name="can-focus">True</property>
                <property name="shadow-type">in</property>
                <child>
                  <object class="VteTerminal" id="terminal">
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="margin-left">2</property>
                    <property name="margin-right">2</property>
                    <property name="margin-top">2</property>
                    <property name="margin-bottom">2</property>
                    <property name="hscroll-policy">natural</property>
                    <property name="vscroll-policy">natural</property>
                    <property name="allow-hyperlink">True</property>
                    <property name="audible-bell">False</property>
                    <property name="bold-is-bright">True</property>
                    <property name="cursor-shape">underline</property>
                    <property name="encoding">UTF-8</property>
                    <property name="scrollback-lines">10000</property>
                    <property name="scroll-on-keystroke">True</property>
                    <property name="scroll-on-output">False</property>
                    <accelerator key="v" signal="paste-clipboard" modifiers="GDK_CONTROL_MASK"/>
                  </object>
                </child>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">True</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
"""

# Builder definitions.

builder = Gtk.Builder.new_from_string(MENU_XML, -1)
builder.connect_signals(Handler())
window = builder.get_object("window1")

terminal = builder.get_object("terminal")
terminal_text = builder.get_object("terminal_text")
textbuffer1 = builder.get_object("textbuffer1")
entry1 = builder.get_object("entry1")

terminal.spawn_sync(
    Vte.PtyFlags.DEFAULT,
    os.environ['HOME'],
    ["/bin/bash"],
    [],
    GLib.SpawnFlags.DO_NOT_REAP_CHILD,
    None,
    None,
    )

terminal.set_font_scale(1.1)

textbuffer1.set_text("#!/bin/bash")

# GTK window start.

window.show_all()

Gtk.main()
