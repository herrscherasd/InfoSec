#!/bin/bash
current_time=$(date +%H:%M)
current_seconds=$(date +%s)

end_time=$(date -d "18:00" +%s)

remaining=$((end_time - current_seconds))

if [ $remaining -gt 0 ]; then
    hours=$((remaining / 3600))
    minutes=$(((remaining % 3600) / 60))

    echo "Current time: $current_time. Work day ends after $hours hours and $minutes minutes."
else
    echo "Current time: $current_time. Work day has ended."
fi
