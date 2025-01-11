# Stage 1: Build Stage
FROM node:18-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy package files for dependency installation
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install --frozen-lockfile

# Copy the rest of the application code
COPY . .

# Build the Next.js application
RUN npm run build

# Stage 2: Production Stage
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/next.config.mjs ./next.config.mjs
COPY --from=builder /app/node_modules ./node_modules

# Expose the port Next.js will run on
EXPOSE 3000

# Start the Next.js application
CMD ["npm", "start"]
