# Set nginx base image
FROM nginx

# Copy custom configuration file from the current directory
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static files to nginx static folder
COPY index.html /usr/share/nginx/html
COPY links.png /usr/share/nginx/html
