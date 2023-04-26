# /bin/bash

# Start the first process
# With uvicorn worker:
# uvicorn fileName:application -h hostAddress -p port
# If there are any testing (pytest)
pytest tests/
uvicorn app:app --host $HOST --port $PORT