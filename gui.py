# Copyright (C) 2024-2025  Darko Milosevic

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

    
from yuconv import YuConverter
import wx

class TransliterationApp(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 400))

        notebook = wx.Notebook(self, style=wx.TAB_TRAVERSAL)

        notebook.AddPage(self.create_text_transliteration_panel(notebook), "Preslovljavanje teksta")
        notebook.AddPage(self.create_file_transliteration_panel(notebook), "Preslovljavanje Datoteke")
        notebook.AddPage(self.create_word_transliteration_panel(notebook), "Preslovljavanje Word Dokumenta")

        self.Centre()
        self.Show()

    def create_text_transliteration_panel(self, parent):
        panel = wx.Panel(parent, style=wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text_input = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(-1, 200))
        sizer.Add(self.text_input, 1, wx.EXPAND | wx.ALL, 10)

        self.text_mode = wx.Choice(panel, choices=["Latinica u Ćirilicu", "Ćirilica u Latinicu"])
        self.text_mode.SetSelection(0)
        sizer.Add(self.text_mode, 0, wx.EXPAND | wx.ALL, 10)

        text_transliterate_btn = wx.Button(panel, label="Preslovi")
        text_transliterate_btn.Bind(wx.EVT_BUTTON, self.on_text_transliterate)
        sizer.Add(text_transliterate_btn, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)
        return panel

    def create_file_transliteration_panel(self, parent):
        panel = wx.Panel(parent, style=wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.VERTICAL)

        input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.input_file = wx.TextCtrl(panel)
        input_sizer.Add(self.input_file, 1, wx.EXPAND | wx.ALL, 5)
        input_browse_btn = wx.Button(panel, label="Traži...")
        input_browse_btn.Bind(wx.EVT_BUTTON, self.on_browse_input_file)
        input_sizer.Add(input_browse_btn, 0, wx.ALL, 5)
        sizer.Add(input_sizer, 0, wx.EXPAND)

        # Output File
        output_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.output_file = wx.TextCtrl(panel)
        output_sizer.Add(self.output_file, 1, wx.EXPAND | wx.ALL, 5)
        output_browse_btn = wx.Button(panel, label="Traži...")
        output_browse_btn.Bind(wx.EVT_BUTTON, self.on_browse_output_file)
        output_sizer.Add(output_browse_btn, 0, wx.ALL, 5)
        sizer.Add(output_sizer, 0, wx.EXPAND)

        self.file_mode = wx.Choice(panel, choices=["Latinica u Ćirilicu", "Ćirilica u Latinicu"])
        self.file_mode.SetSelection(0)
        sizer.Add(self.file_mode, 0, wx.EXPAND | wx.ALL, 10)

        file_transliterate_btn = wx.Button(panel, label="Preslovi")
        file_transliterate_btn.Bind(wx.EVT_BUTTON, self.on_file_transliterate)
        sizer.Add(file_transliterate_btn, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)
        return panel

    def create_word_transliteration_panel(self, parent):
        panel = wx.Panel(parent, style=wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.VERTICAL)

        input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.word_input_file = wx.TextCtrl(panel)
        input_sizer.Add(self.word_input_file, 1, wx.EXPAND | wx.ALL, 5)
        word_input_browse_btn = wx.Button(panel, label="Traži...")
        word_input_browse_btn.Bind(wx.EVT_BUTTON, self.on_browse_word_input_file)
        input_sizer.Add(word_input_browse_btn, 0, wx.ALL, 5)
        sizer.Add(input_sizer, 0, wx.EXPAND)

        output_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.word_output_file = wx.TextCtrl(panel)
        output_sizer.Add(self.word_output_file, 1, wx.EXPAND | wx.ALL, 5)
        word_output_browse_btn = wx.Button(panel, label="Traži...")
        word_output_browse_btn.Bind(wx.EVT_BUTTON, self.on_browse_word_output_file)
        output_sizer.Add(word_output_browse_btn, 0, wx.ALL, 5)
        sizer.Add(output_sizer, 0, wx.EXPAND)

        self.word_mode = wx.Choice(panel, choices=["Latinica u Ćirilicu", "Ćirilica u Latinicu"])
        self.word_mode.SetSelection(0)
        sizer.Add(self.word_mode, 0, wx.EXPAND | wx.ALL, 10)

        word_transliterate_btn = wx.Button(panel, label="Preslovi")
        word_transliterate_btn.Bind(wx.EVT_BUTTON, self.on_word_transliterate)
        sizer.Add(word_transliterate_btn, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)
        return panel

    def on_text_transliterate(self, event):
        mode = self.text_mode.GetStringSelection()
        text = self.text_input.GetValue()
        yu_converter = YuConverter()
        if mode == 'Latinica u Ćirilicu':
            self.text_input.SetValue(yu_converter.transliterate_text(text, 'lat-to-cyr'))
        else:
            self.text_input.SetValue(yu_converter.transliterate_text(text, 'cyr-to-lat'))

    def on_browse_input_file(self, event):
        with wx.FileDialog(self, "Odaberite ulaznu datoteku", wildcard="All files (*.*)|*.*") as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                self.input_file.SetValue(dlg.GetPath())

    def on_browse_output_file(self, event):
        with wx.FileDialog(self, "Odaberite izlaznu datoteku", wildcard="All files (*.*)|*.*", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                self.output_file.SetValue(dlg.GetPath())

    def on_file_transliterate(self, event):
        yu_converter = YuConverter()
        mode = self.file_mode.GetStringSelection()
        input_path = self.input_file.GetValue()
        output_path = self.output_file.GetValue()
        try:
            if mode == 'Latinica u Ćirilicu':
                yu_converter.transliterate_text_file(input_path, output_path, 'lat-to-cyr')
            else:
                yu_converter.transliterate_text_file(input_path, output_path, 'cyr-to-lat')
            wx.MessageBox('Preslovljavanje je završeno.', 'Gotovo', style=wx.OK)
        except Exception as e:
            wx.MessageBox(str(e), 'Error', style=wx.OK | wx.ICON_ERROR)

    def on_browse_word_input_file(self, event):
        with wx.FileDialog(self, "Odaberite ulazni Word dokument", wildcard="Word files (*.docx)|*.docx") as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                self.word_input_file.SetValue(dlg.GetPath())

    def on_browse_word_output_file(self, event):
        with wx.FileDialog(self, "Odaberite izlazni Word dokument", wildcard="Word files (*.docx)|*.docx", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                self.word_output_file.SetValue(dlg.GetPath())

    def on_word_transliterate(self, event):
        mode = self.word_mode.GetStringSelection()
        input_path = self.word_input_file.GetValue()
        output_path = self.word_output_file.GetValue()
        yu_converter = YuConverter()
        try:
            if mode == 'Latinica u Ćirilicu':
                yu_converter.transliterate_word_document(input_path, output_path, 'lat-to-cyr')
            else:
                yu_converter.transliterate_word_document(input_path, output_path, 'cyr-to-lat')
            wx.MessageBox('Preslovljavanje je završeno.', 'Gotovo', style=wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            wx.MessageBox(str(e), 'Error', style=wx.OK | wx.ICON_ERROR)


if __name__ == "__main__":
    app = wx.App()
    TransliterationApp(None, title="YuConv GUI Aplikacija")
    app.MainLoop()
    