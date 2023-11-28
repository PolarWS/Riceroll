<!-- 公告组件 -->
<template>
    <sideTemplate>
        <template #title>
            <div class="title">导航栏</div>
        </template>
        <template #content>
            <div ref="scrollContainer" v-html="markDownToc" class="markDownToc" @click="interruptEvent()"></div>
        </template>
    </sideTemplate>
</template>
<script>
import sideTemplate from '../sideTemplate.vue';
export default {
    data() {
        return {
            interruptEventbool: false,
        }
    },
    components: {
        sideTemplate,
    },
    props: {
        markDownToc: String,
        markdownTocIndex: Number,
        markdownTocDisplay: Boolean,
    },
    methods: {
        scrollToAnchor(newVal) {
            if (this.interruptEventbool) return;
            const anchor = "markdownTocID" + newVal;
            this.$nextTick(() => {
                const element = this.$refs.scrollContainer.querySelector(`#${anchor}`);
                if (!element) return;
                const containerHeight = this.$refs.scrollContainer.offsetHeight;
                const elementHeight = element.offsetHeight;
                const containerTop = this.$refs.scrollContainer.offsetTop;
                this.$refs.scrollContainer.scrollTop = element.offsetTop - containerTop - containerHeight / 2 + elementHeight / 2;

                const oldElement = this.$refs.scrollContainer.querySelector(`.markDownTocSelected`);
                oldElement?.classList.remove('markDownTocSelected');

                element.classList.add('markDownTocSelected');
            });
        },
        interruptEvent() {
            this.interruptEventbool = true;
            setTimeout(() => {
                this.interruptEventbool = false;
                this.scrollToAnchor(this.markdownTocIndex);
            }, 800);
        },
    },
    watch: {
        markdownTocDisplay(newVal) {
            if (newVal) {
                this.$nextTick(() => {
                    this.$refs.scrollContainer.scrollTop = 0;
                });
            }
        },
        markdownTocIndex(newVal) {
            this.scrollToAnchor(newVal);
        },
        '$route.hash': function (newVal) {
            this.interruptEvent();
        },
    }
}
</script>
<style>
.markDownToc {
    width: 14rem;
    padding: 0rem;
    max-height: 26rem;
    overflow: auto;
    scrollbar-width: none;
    /* Firefox */
    -ms-overflow-style: none;
    /* IE and Edge */
    background-color: var(--color-theme-grayscale1);
    scroll-behavior: smooth;
}

.markDownToc::-webkit-scrollbar {
    display: none;
    /* Chrome, Safari and Opera */
}

@media screen and (max-width: 1280px) {
    .markDownToc {
        width: 13rem;
    }
}

.markDownTocSelected a {
    font-weight: 600;
    color: var(--color-theme-blue-1);
}
</style>