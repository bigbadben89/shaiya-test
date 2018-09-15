echo "STOPPING SHAIYA SERVICES..."
net stop ps_login
net stop ps_game
net stop ps_gameLog
net stop ps_dbAgent
net stop ps_session
net stop ps_userLog

timeout /T 5
exit