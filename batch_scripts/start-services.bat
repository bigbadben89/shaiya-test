echo "STARTING SHAIYA SERVICES..."
net start ps_userLog
net start ps_session
net start ps_gameLog
net start ps_dbAgent
net start ps_game
net start ps_login

timeout /T 5
cd ..\python_scripts
python serviceHandler.py vchkoff
python serviceHandler.py nprotectoff

timeout /T 5
exit