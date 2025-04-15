#!/bin/bash

SESSION_NAME="minecraft-server"

# Ensure tmux server is running
if ! tmux info &>/dev/null; then
  echo "Starting tmux server..."
  tmux start-server
fi

# Check if the tmux session already exists
if tmux has-session -t $SESSION_NAME 2>/dev/null; then
  echo "Session $SESSION_NAME already exists. Attaching..."
  tmux attach-session -t $SESSION_NAME
else
  echo "Creating new tmux session: $SESSION_NAME"
  # Create a new tmux session and run docker-compose up
  tmux new-session -d -s $SESSION_NAME "docker-compose up"
  # Split the tmux window horizontally and run htop
  tmux split-window -h -t $SESSION_NAME "htop"
  echo "Tmux session $SESSION_NAME created with a window for htop. Use 'tmux attach-session -t $SESSION_NAME' to view."
fi
