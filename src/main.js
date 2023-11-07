import './assets/main.css';

import { createApp } from 'vue';
import Markdown from 'vue3-markdown-it';
import App from './App.vue';
import router from './router';

const app = createApp(App);

app.use(Markdown);
app.use(router);

app.mount('#app');

