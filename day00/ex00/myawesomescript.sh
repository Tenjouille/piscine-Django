
curl -Is $1 | grep 'Location' | cut -d ' ' -f 2