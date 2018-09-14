echo "Backing database..."
python ..\python_scripts\sqlHandler.py backup

timeout /T 15
exit