cd %~dp0
call "S:\Compiler\Setting.bat"
set PATH=%CMAKE%;%DOTNET%;%GCC%\bin;%GCC%\x86_64-w64-mingw32\bin;C:\Program Files\Git\usr\bin;%RUST%;%PATH%
start S:\VSCode\Code.exe .
