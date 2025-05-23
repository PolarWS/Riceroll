import { createRouter, createWebHistory } from 'vue-router';
import bodyItem from '@/components/body/bodyItem.vue';
import pageMD from '@/components/body/pageMD.vue';
import NotFound from '@/components/body/notFound.vue';

export function createVueRouter(config) {
    const navigationBarData = config.navigationBarData;

    let defaultVue = ["articlePage", "searchPage", "musicPage", "filePage", "friendLinkPage", "aboutPage"];
    let pages = [];

    if (navigationBarData.titleData[navigationBarData.defaultSelected - 1].url === undefined && defaultVue.includes(navigationBarData.titleData[navigationBarData.defaultSelected - 1].id)) {
        pages = [{
            path: '/',
            props: { itemData: navigationBarData.titleData[navigationBarData.defaultSelected - 1].data },
            component: () => import(`@/components/body/${navigationBarData.titleData[navigationBarData.defaultSelected - 1].id}.vue`)
        }];
    } else {
        pages = [{
            path: '/',
            props: { itemData: navigationBarData.titleData[navigationBarData.defaultSelected - 1].data },
            component: bodyItem
        }];
    }

    for (const allocation of navigationBarData.titleData) {
        if (allocation.url === undefined && defaultVue.includes(allocation.id)) {
            pages.push({
                path: '/' + allocation.id,
                props: { itemData: allocation.data },
                component: () => import(`@/components/body/${allocation.id}.vue`)
            });
        } else {
            pages.push({
                path: '/' + allocation.id,
                props: { itemData: allocation.data },
                component: bodyItem
            });
        }
    }

    pages.push({
        path: '/articlePage/:id',
        component: pageMD
    }, {
        path: '/:pathMatch(.*)*',
        component: NotFound
    });

    const router = createRouter({
        history: createWebHistory(),
        routes: pages,
    })

    return router
}