@echo off
for /r ./ %%f in (*.csv) do (
echo %%f
  find /c /v "" %%f
)

pause
