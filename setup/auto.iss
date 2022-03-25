#define MyAppName "大连理工大学图书馆自动预约座位小程序"
#define MyAppVersion "1.1.1"
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

[Files]
Source: "J:\VSProjs\Library\exe\auto\dist\main\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\VSProjs\Library\exe\auto\dist\main\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "J:\VSProjs\Library\src\Chart.xlsx"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\VSProjs\Library\src\config.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\VSProjs\Library\src\seats.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\VSProjs\Library\driver\chromedriver.exe"; DestDir: "{app}/driver"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent unchecked
Filename: "{app}\config.txt"; Description: "修改配置文件（学号、密码等）"; Flags: nowait postinstall skipifsilent shellexec
Filename: "{app}\seats.txt"; Description: "修改期望座位"; Flags: nowait postinstall skipifsilent shellexec            

