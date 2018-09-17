echo "Backing database..."
timeout /T 10
python ..\python_scripts\sqlHandler.py backup

exit
