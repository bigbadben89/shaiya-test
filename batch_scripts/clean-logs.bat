echo "Cleaning ActionLog & ChatLog..."
timeout /T 10
python ..\python_scripts\sqlHandler.py executeFile ..\sql\truncate_log.sql
exit
