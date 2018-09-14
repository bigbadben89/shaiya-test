echo "Applying all..."

.\batch_scripts\install-python-dependencies.bat

echo "Backing up database..."
python python_scripts\sqlHandler.py backup

echo "Cleaning ActionLog & ChatLog..."
python python_scripts\sqlHandler.py execute ..\sql\truncate_log.sql
