#!/usr/bin/env python3

# sys - System-specific parameters and functions.
import sys
# gi - Provides bindings for GObject based libraries.
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject, GLib
# vte - Terminal emulator widget for GTK.
gi.require_version('Vte', '2.91')
from gi.repository import Vte
# io - Core tools for working with streams.
import io
# os - Miscellaneous operating system interfaces.
import os
# argparse - Parser for command-line options, arguments and sub-commands.
import argparse
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

# Extensible Markup Language file for GTK Builder.
MENU_XML = """
  <?xml version="1.0" encoding="UTF-8"?>
  <!-- Generated with glade 3.40.0 -->
  <interface>
    <requires lib="gtk+" version="3.24"/>
    <requires lib="vte-2.91" version="0.70"/>
    <object class="GtkImage" id="add-image">
      <property name="visible">True</property>
      <property name="can-focus">False</property>
      <property name="stock">gtk-add</property>
    </object>
    <object class="GtkImage" id="minus-image">
      <property name="visible">True</property>
      <property name="can-focus">False</property>
      <property name="stock">gtk-remove</property>
    </object>
    <object class="GtkWindow" id="main-window">
      <property name="can-focus">False</property>
      <signal name="destroy" handler="onDestroy" swapped="no"/>
      <child>
        <object class="GtkBox" id="main-box">
          <property name="visible">True</property>
          <property name="can-focus">False</property>
          <property name="orientation">vertical</property>
          <child>
            <object class="GtkBox">
              <property name="visible">True</property>
              <property name="can-focus">False</property>
              <child>
                <object class="GtkMenuBar">
                  <property name="visible">True</property>
                  <property name="can-focus">False</property>
                  <child>
                    <object class="GtkMenuItem">
                      <property name="visible">True</property>
                      <property name="can-focus">False</property>
                      <property name="label" translatable="yes">File</property>
                      <property name="use-underline">True</property>
                      <child type="submenu">
                        <object class="GtkMenu">
                          <property name="visible">True</property>
                          <property name="can-focus">False</property>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-new</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-open</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-save</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-save-as</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                          <child>
                            <object class="GtkSeparatorMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                            </object>
                          </child>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-quit</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                        </object>
                      </child>
                    </object>
                  </child>
                  <child>
                    <object class="GtkMenuItem">
                      <property name="visible">True</property>
                      <property name="can-focus">False</property>
                      <property name="label" translatable="yes">Edit</property>
                      <property name="use-underline">True</property>
                      <child type="submenu">
                        <object class="GtkMenu">
                          <property name="visible">True</property>
                          <property name="can-focus">False</property>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-cut</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-copy</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-paste</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-delete</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                        </object>
                      </child>
                    </object>
                  </child>
                  <child>
                    <object class="GtkMenuItem">
                      <property name="visible">True</property>
                      <property name="can-focus">False</property>
                      <property name="label" translatable="yes">View</property>
                      <property name="use-underline">True</property>
                    </object>
                  </child>
                  <child>
                    <object class="GtkMenuItem">
                      <property name="visible">True</property>
                      <property name="can-focus">False</property>
                      <property name="label" translatable="yes">Help</property>
                      <property name="use-underline">True</property>
                      <child type="submenu">
                        <object class="GtkMenu">
                          <property name="visible">True</property>
                          <property name="can-focus">False</property>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-about</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                        </object>
                      </child>
                    </object>
                  </child>
                  <child>
                    <object class="GtkMenuItem">
                      <property name="visible">True</property>
                      <property name="can-focus">False</property>
                      <property name="label" translatable="yes">Settings</property>
                      <child type="submenu">
                        <object class="GtkMenu">
                          <property name="visible">True</property>
                          <property name="can-focus">False</property>
                          <child>
                            <object class="GtkMenuItem">
                              <property name="visible">True</property>
                              <property name="can-focus">False</property>
                              <property name="label" translatable="yes">gtk-settings</property>
                              <property name="use-underline">True</property>
                            </object>
                          </child>
                        </object>
                      </child>
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
                <object class="GtkButton" id="add-button">
                  <property name="visible">True</property>
                  <property name="can-focus">True</property>
                  <property name="receives-default">True</property>
                  <property name="image">add-image</property>
                  <property name="always-show-image">True</property>
                  <signal name="clicked" handler="onAddButtonClicked" swapped="no"/>
                </object>
                <packing>
                  <property name="expand">False</property>
                  <property name="fill">True</property>
                  <property name="position">1</property>
                </packing>
              </child>
              <child>
                <object class="GtkButton" id="test-button">
                  <property name="visible">True</property>
                  <property name="can-focus">True</property>
                  <property name="receives-default">True</property>
                  <property name="image">minus-image</property>
                  <property name="always-show-image">True</property>
                  <signal name="clicked" handler="onMinusButtonClicked" swapped="no"/>
                </object>
                <packing>
                  <property name="expand">False</property>
                  <property name="fill">True</property>
                  <property name="position">2</property>
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
            <object class="GtkNotebook" id="main-notebook">
              <property name="visible">True</property>
              <property name="can-focus">True</property>
              <property name="tab-pos">bottom</property>
              <child>
                <object class="GtkBox">
                  <property name="visible">True</property>
                  <property name="can-focus">False</property>
                  <property name="orientation">vertical</property>
                  <child>
                    <object class="VteTerminal" id="terminal">
                      <property name="visible">True</property>
                      <property name="can-focus">True</property>
                      <property name="hscroll-policy">natural</property>
                      <property name="vscroll-policy">natural</property>
                      <property name="encoding">UTF-8</property>
                      <property name="scroll-on-keystroke">True</property>
                      <property name="scroll-on-output">False</property>
                    </object>
                    <packing>
                      <property name="expand">True</property>
                      <property name="fill">True</property>
                      <property name="position">0</property>
                    </packing>
                  </child>
                </object>
              </child>
              <child type="tab">
                <object class="GtkLabel">
                  <property name="visible">True</property>
                  <property name="can-focus">False</property>
                  <property name="label" translatable="yes">Terminal</property>
                </object>
                <packing>
                  <property name="tab-fill">False</property>
                </packing>
              </child>
              <child>
                <placeholder/>
              </child>
              <child type="tab">
                <placeholder/>
              </child>
              <child>
                <placeholder/>
              </child>
              <child type="tab">
                <placeholder/>
              </child>
            </object>
            <packing>
              <property name="expand">True</property>
              <property name="fill">True</property>
              <property name="position">1</property>
            </packing>
          </child>
          <child>
            <object class="GtkStatusbar" id="status-bar">
              <property name="visible">True</property>
              <property name="can-focus">False</property>
              <property name="margin-left">2</property>
              <property name="margin-right">2</property>
              <property name="margin-start">2</property>
              <property name="margin-end">2</property>
              <property name="orientation">vertical</property>
              <property name="spacing">1</property>
            </object>
            <packing>
              <property name="expand">True</property>
              <property name="fill">True</property>
              <property name="position">2</property>
            </packing>
          </child>
        </object>
      </child>
    </object>
  </interface>
"""

# CSS configuration file loaded by Gtk.CssProvider.
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

# Command line options.
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-f",
                    "--file", 
                    default="", 
                    help="File chosen to open with.")
args = vars(parser.parse_args())
file = args["file"]

# GTK Settings.
settings = Gtk.Settings.get_default()
settings.set_property("gtk-application-prefer-dark-theme", True)
screen = Gdk.Screen.get_default()
provider = Gtk.CssProvider()
provider.load_from_data(CSS_File)
Gtk.StyleContext.add_provider_for_screen(screen,
                                         provider, 
                                         Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

# GTK Handeler class.
class Handler:
    # Closes program when window is exited.
    def onDestroy(self,*args):
      Gtk.main_quit()

    def onMinusButtonClicked(self,button):
      #statusbar.remove_all(context)
      if (mainnotebook.get_n_pages() >= 2):
        mainnotebook.remove_page(-1)
      mainnotebook.set_current_page(-1)
      context = statusbar.get_context_id("statusbar")
      text = 'Terminal removed'
      statusbar.push(context, text)
    
    def onAddButtonClicked(self,button):
      mainnotebook.page = Gtk.Box()
      mainnotebook.page.set_border_width(0)
      terminal1 = Vte.Terminal()
      terminal1.spawn_sync(Vte.PtyFlags.DEFAULT,
                           os.environ['HOME'],
                           ["/bin/sh"],
                           [],
                           GLib.SpawnFlags.DO_NOT_REAP_CHILD,
                           None,
                           None,
                           )
      mainnotebook.page.add(terminal1)
      mainnotebook.page.set_child_packing(terminal1, True, True, 0, 0)
      mainnotebook.append_page(mainnotebook.page, Gtk.Label(label="Terminal"))
      window.show_all()
      mainnotebook.set_current_page(-1)
      context = statusbar.get_context_id("statusbar")
      text = 'Terminal added'
      statusbar.push(context, text)

# Builder definitions.
builder = Gtk.Builder.new_from_string(MENU_XML, -1)
builder.connect_signals(Handler())
window = builder.get_object("main-window")
terminal = builder.get_object("terminal")
statusbar = builder.get_object("status-bar")
mainnotebook = builder.get_object("main-notebook")

# Terminal spawn settings.
terminal.spawn_sync(
    Vte.PtyFlags.DEFAULT,
    os.environ['HOME'],
    ["/bin/bash"],
    [],
    GLib.SpawnFlags.DO_NOT_REAP_CHILD,
    None,
    None,
    )

# Initial window and terminal configs. 
window.set_default_size(700, 400)
terminal.set_font_scale(1.05)

# Opends the file specified in -f command line option if provided.
if (file != ""):
  pass

# Recursively shows the 'window' widget, and any child widgets.
window.show_all()

# Runs the main loop until gtk_main_quit() is called.
Gtk.main()