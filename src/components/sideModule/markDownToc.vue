<!-- 公告组件 -->
<template>
    <sideTemplate>
        <template #title>
            <div class="title">导航栏</div>
        </template>
        <template #content>
            <div ref="scrollContainer" class="markDownToc">
                <div v-for="(item, index) in markDownToc.data" :id="'markdownTocID' + index"
                    :class="[item.class, { 'markdownTocSelected': index === 0 }]">
                    <a :href="item.href" @click="interruptEvent()">{{ item.title }}</a>
                </div>
            </div>
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
        markDownToc: Object,
        markdownTocIndex: Number,
    },
    methods: {
        scrollToAnchor(newVal) {
            const anchor = "markdownTocID" + newVal;

            // 滚动事件
            if (!this.interruptEventbool) {
                this.$nextTick(() => {
                    const element = this.$refs.scrollContainer.querySelector(`#${anchor}`);
                    if (!element) return;

                    const containerHeight = this.$refs.scrollContainer.offsetHeight;
                    const elementHeight = element.offsetHeight;
                    const containerTop = this.$refs.scrollContainer.offsetTop;
                    this.$refs.scrollContainer.scrollTop = element.offsetTop - containerTop - containerHeight / 2 + elementHeight / 2;
                });
            }

            // 绑定 class
            this.$nextTick(() => {
                const element = this.$refs.scrollContainer.querySelector(`#${anchor}`);
                if (!element) return;

                const oldElement = this.$refs.scrollContainer.querySelector(`.markdownTocSelected`);
                oldElement?.classList.remove('markdownTocSelected');

                element.classList.add('markdownTocSelected');
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
        markdownTocData(newVal) {
            if (newVal.display) {
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
    scrollbar-width: none;
    /* Firefox */
    scrollbar-color: transparent transparent;
    /* Firefox */
}

.markDownToc::-webkit-scrollbar {
    width: 0;
    /* Chrome, Safari, Edge */
}

.markDownToc::-webkit-scrollbar-thumb {
    background-color: transparent;
    /* Chrome, Safari, Edge */
}

.markDownToc:hover {
    scrollbar-width: 0.35rem;
    /* Firefox */

}

.markDownToc:hover::-webkit-scrollbar {
    width: 0.35rem;
    /* Chrome, Safari, Edge */
}

@media screen and (max-width: 1280px) {
    .markDownToc {
        width: 13rem;
    }
}

body .markdownTocSelected a {
    font-weight: 600;
    color: var(--color-theme-blue-1);
}

.announcementBoard a:hover {
    font-weight: 600;
    color: var(--color-theme-grayscale6);
}

body .markdownTocClass1,
body .markdownTocClass2 {
    color: var(--color-theme-grayscale65);
}

body .markdownTocClass3,
body .markdownTocClass4 {
    padding-left: 0.5rem;
}

body .markdownTocClass5,
body .markdownTocClass6 {
    padding-left: 1rem;
}

body .markdownTocClass1,
body .markdownTocClass2,
body .markdownTocClass3,
body .markdownTocClass4,
body .markdownTocClass5,
body .markdownTocClass6 {
    margin-top: 0.8rem;
}

body .markdownTocClass1 a,
body .markdownTocClass2 a,
body .markdownTocClass3 a,
body .markdownTocClass4 a,
body .markdownTocClass5 a,
body .markdownTocClass6 a {
    word-wrap: break-word;
}
</style>