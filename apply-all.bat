echo "If you change MSSQL user Shaiya password, please update your password in shaiya-test\config\db.conf"

timeout /T 5

echo "Applying all..."
.\batch_scripts\install-python-dependencies.bat
.\batch_scripts\backup-databases.bat
.\batch_scripts\clean-logs.bat

exit 
