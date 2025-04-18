<!-- 导航栏Mob -->
<template>
    <div class="navigationBarMob">
        <div class="sideItems">
            <sideItem :iconSvg="closeSwitchSvg" @click="navigationBarMobClosed">
                <template #title>
                    关闭
                </template>
            </sideItem>
            <sideItem v-for="(item, index) in navigationBarData.titleData" :key="index"
                @click.prevent="handleClick(item.id, item.url)" :iconSvg="item.icon">
                <template #title>
                    {{ item.title }}
                </template>
            </sideItem>
        </div>
    </div>
</template>
<script>
import sideItem from '@/components/sideItem.vue';
export default {
    data() {
        return {
            closeSwitchSvg: "<svg t=\"1700272935751\" class=\"icon\" viewBox=\"0 0 1024 1024\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" p-id=\"3992\" width=\"35\" height=\"35\"><path d=\"M576 512l277.333333 277.333333-64 64-277.333333-277.333333L234.666667 853.333333 170.666667 789.333333l277.333333-277.333333L170.666667 234.666667 234.666667 170.666667l277.333333 277.333333L789.333333 170.666667 853.333333 234.666667 576 512z\" fill=\"#2c2c2c\" p-id=\"3993\"></path></svg>",
        }
    },
    components: {
        sideItem,
    },
    methods: {
        handleClick(id, url) {
            if (url === undefined) {
                this.$router.push('/' + id);
                this.navigationBarMobClosed();
            } else {
                location.replace(url)
            }
        },
        navigationBarMobClosed() {
            this.$emit('navigationBarMobSwitch', false);
        },
    },
    props: ['navigationBarData']
}
</script>
<style scoped>
.navigationBarMob {
    width: 100%;
    margin: 0;
    padding: 1rem 0;
    display: flex;
    flex-direction: column;
    position: fixed;
    top: 0;
    max-height: 100vh;
    background-color: var(--color-theme-white-3);
    z-index: 4;
    height: 100%;
    transition: right 0.35s;
}
</style>