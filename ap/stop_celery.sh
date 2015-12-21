ps aux | grep celery | awk '{system("sudo kill -9 " $2)}' &

rabbitmqctl stop &

ps aux | grep rabbit | awk '{system("sudo kill -9 " $2)}' &