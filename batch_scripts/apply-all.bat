echo "If you change MSSQL user Shaiya password, please update your password in shaiya-test\config\db.conf"

echo "Applying all..."
cd batch_scripts
start /W install-python-dependencies.bat
start /W backup-databases.bat
start /W clean-logs.bat

exit
