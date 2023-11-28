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
            }, 550);
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
    background-color: var(--color-theme-grayscale1);
    scroll-behavior: smooth;

    scrollbar-width: none; /* Firefox */
    scrollbar-color: transparent transparent; /* Firefox */
}

.markDownToc::-webkit-scrollbar {
    width: 0; /* Chrome, Safari, Edge */
}

.markDownToc::-webkit-scrollbar-thumb {
    background-color: transparent; /* Chrome, Safari, Edge */
}

.markDownToc:hover {
    scrollbar-width: 0.35rem; /* Firefox */
    scrollbar-color: var(--color-theme-grayscale5) transparent; /* Firefox */
}

.markDownToc:hover::-webkit-scrollbar {
    width: 0.35rem; /* Chrome, Safari, Edge */
}

.markDownToc:hover::-webkit-scrollbar-thumb {
    background-color: var(--color-theme-grayscale5); /* Chrome, Safari, Edge */
}

@media screen and (max-width: 1280px) {
    .markDownToc {
        width: 13rem;
    }
}

body .markDownTocSelected a {
    font-weight: 600;
    color: var(--color-theme-blue-1);
}
.announcementBoard a:hover {
    font-weight: 600;
    color: var(--color-theme-grayscale6);
}

body .markDownTocSelected a::before {
    content: '# ';
}

body .markdownTocClass1,
body .markdownTocClass2 {
    font-weight: 600;
    color: var(--color-theme-grayscale65);
}

body .markdownTocClass5,
body .markdownTocClass6 {
    padding-left: 0.75rem;
}
</style>