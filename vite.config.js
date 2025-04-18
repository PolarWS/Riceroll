import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import viteCompression from 'vite-plugin-compression'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    viteCompression({
      filter: /.(js|css|html|json|mjs|png|jpg|jpeg|svg)$/i,
      threshold: 5240,
      algorithm: 'gzip',
    }),
  ],
  build: {
    target: ["chrome89", "edge89", "firefox89", "safari15"]
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: '0.0.0.0',
    port: 4173,
  }
})
