if "%~x1"==".ui" (
    pyuic5 -x %1 -o %2
) else (
    echo Not a ui file! & pause
)