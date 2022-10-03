# audo_ml_server



curl -X 'POST' \
  'http://localhost:4002/audio' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@country.0.wav;type=application/json'


curl -X 'POST' 'localhost:4002/audio' -F 'file=@country.0.wav