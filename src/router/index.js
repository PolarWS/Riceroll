import { createRouter, createWebHistory } from 'vue-router'
import config from '../config.json'

import navigationBar from '@/components/navigationBar.vue';
import informationBar from '@/components/informationBar.vue';
import articlePage from '@/components/body/articlePage.vue';
import filePage from '@/components/body/filePage.vue';
import aboutPage from '@/components/body/aboutPage.vue';
import friendLinkPage from '@/components/body/friendLinkPage.vue';
import musicPage from '@/components/body/musicPage.vue';
import searchPage from '@/components/body/searchPage.vue';
import bodyItem from '@/components/bodyItem.vue';


const componentMapping = {
    homePage: articlePage, // 这里使用实际的组件对象
    articlePage: articlePage, // 同样的，使用实际的组件对象
    // 其他页面的映射
};

const pages = [{ path: '/', component: componentMapping[config.navigationBarData.titleData[config.navigationBarData.defaultSelected - 1].id] }];

for (const allocation of config.navigationBarData.titleData) {
    pages.push({ path: '/' + allocation.id, component: componentMapping[allocation.id] });
}

console.log(pages);

const router = createRouter({
    history: createWebHistory(),
    routes: pages
})

export default router