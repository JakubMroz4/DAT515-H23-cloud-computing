FROM node:18-alpine
WORKDIR /frontend
ENV NODE_ENV=development
COPY .env /frontend/
COPY package*.json ./
RUN npm install
RUN npm install react-router-dom
COPY public/ /frontend/public
COPY src/ /frontend/src
CMD ["npm", "start"]
