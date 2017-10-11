# Node image
FROM node:7

# Create app directory
RUN mkdir -p /app
WORKDIR /app

COPY package.json /app

# Install app dependencies
RUN npm install

# Copy the current directory contents into the container at /app
ADD . /app

EXPOSE 3000

CMD [ "node", "index.js" ]

