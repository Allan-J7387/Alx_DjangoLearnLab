[Unit]
Description=gunicorn daemon for social_media_api
After=network.target

[Service]
User=deploy
Group=www-data
WorkingDirectory=/home/deploy/social_media_api
EnvironmentFile=/home/deploy/social_media_api/.env
ExecStart=/home/deploy/social_media_api/venv/bin/gunicorn \
  --access-logfile - \
  --workers 3 \
  --bind unix:/run/gunicorn.sock \
  social_media_api.wsgi:application

[Install]
WantedBy=multi-user.target
