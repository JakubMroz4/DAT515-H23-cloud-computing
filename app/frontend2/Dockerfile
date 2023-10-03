FROM node:18-alpine
WORKDIR /frontend2
ENV NODE_ENV=development
COPY . .
RUN npm install
RUN npm install react-router-dom
CMD ["npm", "start"]
