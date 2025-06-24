# ⚡️ 1. Use official Node image
FROM node:18-alpine as build

# 📂 2. Set working directory inside container
WORKDIR /app

# 📦 3. Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# 🚀 4. Copy the rest of your app and build it
COPY . .
RUN npm run build

# 🗂️ 5. Use Nginx to serve the built static files
FROM nginx:stable-alpine as production

# 📂 6. Copy built files from the previous stage to Nginx's public folder
COPY --from=build /app/dist /usr/share/nginx/html

# 📄 7. Copy a custom Nginx config if needed (optional)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# 🔑 8. Expose port 80
EXPOSE 80

# ⚡️ 9. Start Nginx
CMD ["nginx", "-g", "daemon off;"]

