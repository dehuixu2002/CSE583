#!/bin/bash

mkdir -p pronto
echo "Pronto bike-sharing data for Seattle, including trips, stations, system status, and weather." > pronto/README.txt
mkdir -p pronto/data
cd pronto/data || exit 1
curl -L -o open_data_year_one.zip "https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"
unzip -o open_data_year_one.zip
head -n 5 2015_trip_data.csv
