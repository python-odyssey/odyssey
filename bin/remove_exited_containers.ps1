docker ps --all --filter status=exited --format "{{.ID}}" | ForEach-Object { docker rm $_ }
