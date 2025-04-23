<template>
    <div>
        <div class="bodyItemTopImg" :style="`background-image: url(${itemData.title.img})`">
            <div class="brightnessAdjustment">
                <h1>「{{ itemData.title.content }}」</h1>
            </div>
        </div>
        <markDown :markDownUrl="itemData.markdown" />
        <slot></slot>
        <commentList v-if="this.itemData.comment" />
    </div>
</template>
<script>
import markDown from '@/components/markDown.vue';
import commentList from '@/components/component/commentList.vue';
export default {
    props: {
        itemData: Object,
    }, components: {
        markDown,
        commentList,
    },
    mounted() {
        const routeName = this.$route.fullPath.split('/').pop();
        if (routeName.split('#').length > 1) {
            const anchor = routeName.split('#')[1];
            setTimeout(() => {
                const anchorElement = document.getElementById(anchor);
                if (anchorElement) {
                    anchorElement.scrollIntoView({ behavior: 'smooth' });
                }
            }, 1000);
        }
    },

}
</script>
<style scoped>
.bodyItemTopImg {
    width: 100%;
    height: 15rem;
    background-size: 100%;
    background-position: center;
    background-repeat: no-repeat;
    transition: background-size 0.5s;
    background-color: var(--color-theme-grayscale1);
}

.brightnessAdjustment {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--color-theme-white);
    background-color: var(--color-theme-black0);
}

.bodyItemTopImg:hover {
    background-size: 110%;
}

@media screen and (max-width: 600px) {
    .bodyItemTopImg {
        background-size: cover;
    }

    .bodyItemTopImg:hover {
        background-size: cover;
    }
}
</style>