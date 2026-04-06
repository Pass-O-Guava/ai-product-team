import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Fix: use default Vite naming (hashed) instead of custom index-index naming
// which some platforms/CDNs may not handle correctly
export default defineConfig({
  plugins: [react()],
  base: '/',
})
