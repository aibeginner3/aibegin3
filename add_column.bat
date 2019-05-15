@echo off

:cut -d ',' -f 2 data1.csv
:@set dirs = cut -d ',' -f 2 data1.csv
:for /F gusebackq tokens=2 delims=,h %%a in (`cut -d ',' -f 2 data1.csv`) do @set dirs=%%a 
:echo %dirs%

:for /f %%i in (`cut -d ',' -f 2 data1.csv`) do (
:for /f "usebackq" %%i in (`cut -d ',' -f 2 data1.csv`) do (
:  @set dirs=%%i
:  echo %dirs%
:  @echo %%i
:}
:echo %dirs%

for /f %%a in (data1.csv) do (
:  echo %%a
  for /f "tokens=2 delims=," %%b in ("%%a") do (
:    echo %%b
    for /f "tokens=3-16 delims=\\" %%c in ("%%b") do (
      echo %%a,%%c,%%d,%%e,%%f,%%g,%%h >> test_out.csv
    )
  )
)

:for /F "delims=," %%i in (data1.csv) do echo %%i

:pause
