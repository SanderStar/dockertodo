# Set nginx base image
FROM nginx

# Copy custom configuration file from the current directory
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static files to nginx www folder
COPY static /usr/share/nginx/html
