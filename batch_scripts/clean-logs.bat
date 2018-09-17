echo "Cleaning ActionLog & ChatLog..."
python ..\python_scripts\sqlHandler.py executeFile ..\sql\truncate_log.sql
exit
