#!/bin/bash

# Create images directory if it doesn't exist
mkdir -p public/images

# Download sample images (replace with your preferred images)
curl -o public/images/bg1.jpg "https://source.unsplash.com/1920x1080/?nature"
curl -o public/images/bg2.jpg "https://source.unsplash.com/1920x1080/?city"
curl -o public/images/bg3.jpg "https://source.unsplash.com/1920x1080/?technology"
curl -o public/images/bg4.jpg "https://source.unsplash.com/1920x1080/?architecture"

echo "Background images downloaded successfully!"
