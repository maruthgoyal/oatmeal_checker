#!/bin/bash
screen -S oatmeal_screen -t oatmeal_runner -dm
screen -S oatmeal_screen -p oatmeal_runner -X stuff 'source venv/bin/activate && python main.py
'
