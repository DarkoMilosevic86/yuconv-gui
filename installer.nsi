; Copyright (C) 2024-2025  Darko Milosevic

; This program is free software: you can redistribute it and/or modify
; it under the terms of the GNU General Public License as published by
; the Free Software Foundation, either version 3 of the License, or
    ; (at your option) any later version.

; This program is distributed in the hope that it will be useful,
; but WITHOUT ANY WARRANTY; without even the implied warranty of
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
; GNU General Public License for more details.

    
!include "mui2.nsh"
Name "YuConv GUI 0.2"
OutFile "YuConv_GUI_V0.2_Install.exe"
Unicode True
InstallDir "$PROGRAMFILES64\YuConv GUI"
RequestExecutionLevel admin
Icon "res/icon.ico"

!define MUI_ABORTWARNING
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "license"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "Serbian"

VIAddVersionKey /LANG=${LANG_SERBIAN} "ProductName" "YuConv GUI Installer"
VIAddVersionKey /LANG=${LANG_SERBIAN} "Comments" "YuConv GUI Installer"
VIAddVersionKey /LANG=${LANG_SERBIAN} "CompanyName" "Darko Milosevic"
VIAddVersionKey /LANG=${LANG_SERBIAN} "LegalTrademarks" "YuConv GUI Installer is a trademark of Darko Milosevic"
VIAddVersionKey /LANG=${LANG_SERBIAN} "LegalCopyright" "© Darko Milosevic"
VIAddVersionKey /LANG=${LANG_SERBIAN} "FileDescription" "YuConv GUI installing application"
VIAddVersionKey /LANG=${LANG_SERBIAN} "FileVersion" "0.2.0"
VIProductVersion "0.2.0.0"

Section "Install"
SetOutPath "$INSTDIR"
File "dist\gui\gui.exe"
File "LICENSE"
File "README.md"
File "res\icon.ico"
SetOutPath "$INSTDIR\_internal"
File /r "dist\gui\_internal\*"
WriteUninstaller "$INSTDIR\Uninstall.exe"
WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\YuConv GUI" \
"DisplayName" "YuConv GUI Application"
WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\YuConv GUI" \
"UninstallString" "$\"$INSTDIR\Uninstall.exe$\""
SectionEnd

Section "CreateShortcuts"
CreateDirectory "$SMPROGRAMS\YuConv GUI"
CreateShortcut "$SMPROGRAMS\YuConv GUI\YuConv GUI.lnk" "$INSTDIR\gui.exe" "" "$INSTDIR\icon.ico" 0
CreateShortcut "$SMPROGRAMS\YuConv GUI\View License.lnk" "$INSTDIR\LICENSE"
CreateShortcut "$SMPROGRAMS\YuConv GUI\View Readme.lnk" "$INSTDIR\README.md"
CreateShortcut "$SMPROGRAMS\YuConv GUI\Uninstall YuConv GUI.lnk" "$INSTDIR\Uninstall.exe"
CreateShortcut "$DESKTOP\YuConv GUI.lnk" "$INSTDIR\gui.exe" "" "$INSTDIR\icon.ico" 0
SectionEnd

Section "Uninstall"
DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\YuConv GUI"
Delete "$INSTDIR\*.*"
Delete "$INSTDIR\_internal\*.*"
RMDir /r "$INSTDIR\_internal"
Delete "$SMPROGRAMS\YuConv GUI\*.*"
RMDir /r "$SMPROGRAMS\YuConv GUI"
Delete "$DESKTOP\YuConv GUI.lnk"
RMDir /r "$INSTDIR"
SectionEnd
