#define MyAppName "大连理工大学图书馆自动预约座位小程序"
#define MyAppVersion "1.2.2"
#define MyAppPublisher "qhy040404"
#define MyAppURL "https://github.com/qhy040404/DLUT-library-auto-reservation"
#define MyAppExeName "main.exe"

[Setup]
AppId={{BBF7BDD6-FCB4-437C-B8CF-77B64214A325}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\DLUT-library-auto-reservation
DisableProgramGroupPage=yes
DisableWelcomePage=no
LicenseFile=J:\VSProjs\Library\LICENSE
OutputDir=J:\VSProjs\Library\setup\output
OutputBaseFilename=DLUT-library-auto-reservation-Installer
SetupIconFile=J:\VSProjs\Library\logo\logo.ico
SourceDir=J:\VSProjs\Library\setup\images
Compression=lzma
SolidCompression=yes
WizardStyle=modern
WizardImageFile=100.bmp,125.bmp,150.bmp,175.bmp
WizardSmallImageFile=100small.bmp,125small.bmp,150small.bmp,175small.bmp

[Languages]
Name: "chinesesimp"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; 
Name: "startfolder"; Description: "创建开始菜单文件夹(&P)"; GroupDescription: "{cm:AdditionalIcons}";

[Files]
Source: "J:\VSProjs\Library\exe\dist\main\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\VSProjs\Library\exe\dist\main\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "J:\VSProjs\Library\src\config.conf"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\VSProjs\Library\driver\chromedriver.exe"; DestDir: "{app}/driver"; Flags: ignoreversion
Source: "J:\VSProjs\Library-reservation-configGenerator\x64\Release\ConfigGenerator.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\{#MyAppName}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"; Tasks: startfolder
Name: "{autoprograms}\{#MyAppName}\配置生成器"; Filename: "{app}\ConfigGenerator.exe"; WorkingDir: "{app}"; Tasks: startfolder
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"; Tasks: desktopicon
Name: "{autodesktop}\配置生成器"; Filename: "{app}\ConfigGenerator.exe"; WorkingDir: "{app}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent unchecked
Filename: "{app}\ConfigGenerator.exe"; Description: "运行配置生成器"; Flags: nowait postinstall skipifsilent