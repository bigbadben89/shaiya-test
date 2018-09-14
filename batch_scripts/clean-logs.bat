echo "Cleaning ActionLog & ChatLog..."
python ..\python_scripts\sqlHandler.py executeFile ..\sql\truncate_log.sql

timeout /T 30
exit