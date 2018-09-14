echo "Cleaning ActionLog & ChatLog..."
python ..\python_scripts\sqlHandler.py execute ..\sql\truncate_log.sql

exit
