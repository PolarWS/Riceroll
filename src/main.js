import './assets/main.css';
import './assets/Markdown/markdown.css';
import './assets/Markdown/highlight.js/github.css'
import axios from 'axios';
import { createApp } from 'vue';
import { createPinia } from 'pinia'
import Markdown from 'vue3-markdown-it';
import App from './App.vue';
import { createVueRouter } from './router';
import { axiosStore } from './store/axiosStore.js';

const APICONFIG = {
    "url": "http://127.0.0.1:8080/",
    "config": "config",
    "friendLinkPage": "friendLinkPage",
    "articlePage": "articlePage",
    "filePage": "filePage",
    "markdown": "md",
    "markdownFile": "markdownPage",
    "labelBar": "tagHots",
    "announcementBoard": "blogTotal",
    "replyBar": "commentNew",
    "searchPage": "search",
    "cover": "image",
    "comment": {
        "commentList": "comment",
        "commentAdd": "commentAdd",
        "meme": "memeImage",
        "memeList": "memeList"
    },
    "captcha": {
        "captchaCreate": "captchaCreate",
        "captchaImage": "captchaImg",
        "captchaCheck": "captchaCheck"
    }
};

let config = (await axios.get(APICONFIG.url + APICONFIG.config)).data.data;
const router = createVueRouter(config);
const app = createApp(App, {
    configData: config,
});

app.use(createPinia());
app.use(Markdown);
app.use(router);
axiosStore().api = APICONFIG
app.mount('#app');