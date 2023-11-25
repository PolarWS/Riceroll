import './assets/main.css';
import './assets/Markdown/markdown.css';
import './assets/Markdown/highlight.js/github.css'

import { createApp } from 'vue';
import { createPinia } from 'pinia'
import Markdown from 'vue3-markdown-it';
import App from './App.vue';
import router from './router';

const app = createApp(App);

app.use(Markdown);
app.use(router);
app.use(createPinia());
app.mount('#app');

