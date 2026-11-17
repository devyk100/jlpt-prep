import { defineConfig } from '@playwright/test';
export default defineConfig({ testDir: './tests', workers: 1, use: { baseURL: 'http://127.0.0.1:5175', headless: true }, webServer: { command: 'npm.cmd run dev -- --port 5175', url: 'http://127.0.0.1:5175', reuseExistingServer: false }, reporter: 'list' });
