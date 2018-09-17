REM echo "Cleaning ActionLog & ChatLog..."
start /W /B "python ..\python_scripts\sqlHandler.py executeFile ..\sql\truncate_log.sql"
