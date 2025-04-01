FROM node:latest

# Set working directory to match your project structure
WORKDIR /docker-spy

# Copy necessary files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy spyware script
COPY spyware.js . 

CMD ["node", "spyware.js"]
