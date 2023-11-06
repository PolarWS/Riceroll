import { createRouter, createWebHistory } from 'vue-router'
import config from '../config.json'

// import navigationBar from '@/components/navigationBar.vue';
// import informationBar from '@/components/informationBar.vue';
// import articlePage from '@/components/body/articlePage.vue';
// import filePage from '@/components/body/filePage.vue';
// import aboutPage from '@/components/body/aboutPage.vue';
// import friendLinkPage from '@/components/body/friendLinkPage.vue';
// import musicPage from '@/components/body/musicPage.vue';
// import searchPage from '@/components/body/searchPage.vue';
import bodyItem from '@/components/bodyItem.vue';

const navigationBarData = config.navigationBarData;

let defaultVue = ["articlePage", "searchPage", "musicPage", "filePage", "friendLinkPage", "aboutPage"];
let pages = [];

if (defaultVue.includes(navigationBarData.titleData[navigationBarData.defaultSelected - 1].id)) {
    pages = [{ path: '/', component: () => import(`@/components/body/${navigationBarData.titleData[navigationBarData.defaultSelected - 1].id}.vue`) }];
} else {
    pages = [{ path: '/', component: bodyItem }];
}

// 在此处可以使用 `pages`


// 接下来可以在路由配置中使用`pages`


// for (const allocation of navigationBarData.titleData) {
//     if (defaultVue.includes(allocation.id)) {
//         pages.push({ path: '/' + allocation.id, component: allocation.id });
//     } else {
//         pages.push({ path: '/' + allocation.id, component: bodyItem });
//     }
// }

for (const allocation of navigationBarData.titleData) {
    if (defaultVue.includes(allocation.id)) {
        pages.push({ path: '/' + allocation.id, component: () => import(`@/components/body/${allocation.id}.vue`) });
    } else {
        pages.push({ path: '/' + allocation.id, component: bodyItem });
    }
}

console.log(pages);

const router = createRouter({
    history: createWebHistory(),
    routes: pages
})

export default router