echo "Cleaning ActionLog & ChatLog..."
start /W "python ..\python_scripts\sqlHandler.py executeFile ..\sql\truncate_log.sql"
