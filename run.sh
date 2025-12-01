#!/bin/bash

docker build -t butterfly-dashboard .

docker run --rm -p 5000:5000 butterfly-dashboard