<!-- 信息栏 -->
<template>
    <div class="informationBar" ref="informationBar" @scroll="handleScroll">
        <announcementBoard v-if="informationBarData.default.announcementBoard.display"
            :announcementBoard="informationBarData.default.announcementBoard" class="labelBarAnimation"
            :style="{ '--i': 0 }" />
        <div v-show="!(this.markdownTocData.display && Object.keys(this.markdownTocData.data).length > 0)">
            <!-- 侧边栏组件 -->
            <labelBar v-if="informationBarData.default.labelBar.display" class="labelBarAnimation"
                :labelBar="informationBarData.default.labelBar" :style="{ '--i': 1 }" />
            <replyBar v-if="informationBarData.default.replyBar.display" class="labelBarAnimation"
                :style="{ '--i': 2 }" />
            <!-- 自定义组件 -->
            <sideTemplate v-if="informationBarData.custom.display" v-for="item in informationBarData.custom.content"
                class="labelBarAnimation" :style="{ '--i': 3 + index }">
                <template #title>
                    {{ item.title }}
                </template>
                <template #content>
                    <markDown :markDownData="item.markdown" />
                </template>
            </sideTemplate>
        </div>
        <!-- markDown[toc]组件 -->
        <div v-show="this.markdownTocData.display && Object.keys(this.markdownTocData.data).length > 0"
            class="labelBarAnimation" :style="{ '--i': 3 + informationBarData.custom.content.length }">
            <markDownToc :markDownToc="markdownTocData" :markdownTocIndex="markdownTocIndex" />
        </div>
        <!-- 脚标 -->

        <div v-for="item in informationBarData.footmark" class="footer">
            <a :href="item.url">{{ item.title }}</a>
        </div>
    </div>
</template>
<script>
import markDownToc from '@/components/sideModule/markDownToc.vue';
import announcementBoard from '@/components/sideModule/announcementBoard.vue';
import labelBar from '@/components/sideModule/labelBar.vue';
import replyBar from '@/components/sideModule/replyBar.vue';
import sideTemplate from '@/components/sideModule/sideTemplate.vue';
import markDown from '@/components/markDown.vue';
export default {
    data() {
        return {
            screenYAxis: 0,
            stickyBool: true,
            changeDirection: false,
            topBoolean: true,
            fixedDivDigits: 0,
            XscreenYAxis: 0,
            divHeight: 0,
            pageHeight: window.innerHeight,
        }
    },
    components: {
        announcementBoard,
        labelBar,
        replyBar,
        sideTemplate,
        markDownToc,
        markDown,
    },
    methods: {
        handleScroll() {
            if (window.scrollY + this.pageHeight <= document.body.scrollHeight) {
                if (this.divHeight > this.pageHeight) {
                    if (this.XscreenYAxis < this.screenYAxis && window.scrollY < this.screenYAxis) {
                        this.changeDirection = true;
                    } else if (this.XscreenYAxis > this.screenYAxis && window.scrollY > this.screenYAxis) {
                        this.changeDirection = true;
                    }
                    else {
                        this.changeDirection = false;
                    }
                    this.XscreenYAxis = this.screenYAxis
                    this.screenYAxis = window.scrollY;
                    if (window.scrollY <= 0) {
                        this.$refs.informationBar.style.top = "0px";
                        this.$refs.informationBar.style.position = 'relative';
                    } else if (window.scrollY < this.fixedDivDigits && this.stickyBool) {
                        this.$refs.informationBar.style.top = "0px";
                        this.$refs.informationBar.style.position = 'sticky';
                        this.stickyBool = false;
                        this.topBoolean = true;
                    } else if (this.screenYAxis > this.fixedDivDigits + this.divHeight - this.pageHeight && this.stickyBool) {

                        this.$refs.informationBar.style.top = (this.pageHeight - this.divHeight) + "px";
                        this.$refs.informationBar.style.position = 'sticky';
                        this.stickyBool = false;
                        this.topBoolean = false;
                    }
                    if (!this.stickyBool && this.changeDirection && !this.topBoolean) {
                        this.fixedDivDigits = this.screenYAxis + this.pageHeight - this.divHeight;
                        this.$refs.informationBar.style.top = (this.screenYAxis + this.pageHeight - this.divHeight) + "px";
                        this.$refs.informationBar.style.position = 'relative';
                        this.stickyBool = true;
                    } else if (!this.stickyBool && this.changeDirection && this.topBoolean) {
                        this.fixedDivDigits = this.screenYAxis;
                        this.$refs.informationBar.style.top = (this.screenYAxis) + "px";
                        this.$refs.informationBar.style.position = 'relative';
                        this.stickyBool = true;
                    }
                } else {
                    this.$refs.informationBar.style.top = "0";
                    this.$refs.informationBar.style.position = 'sticky';
                }
            }
        },
        handleResize() {
            this.pageHeight = window.innerHeight;
            this.handleScroll();
        },
    },
    mounted() {
        this.$nextTick(() => {
            const element = this.$refs.informationBar;
            const resizeObserver = new ResizeObserver(entries => {
                for (let entry of entries) {
                    const computedStyle = window.getComputedStyle(entry.target);
                    this.divHeight = parseFloat(computedStyle.height) + parseFloat(computedStyle.paddingTop) + parseFloat(computedStyle.paddingBottom);
                }
            });

            resizeObserver.observe(element);
            window.addEventListener('resize', this.handleResize);
            window.addEventListener('scroll', this.handleScroll);
        });
    },
    updated() {
        const computedStyle = window.getComputedStyle(this.$refs.informationBar);
        this.divHeight = parseFloat(computedStyle.height) + parseFloat(computedStyle.paddingTop) + parseFloat(computedStyle.paddingBottom);
    },
    unmounted() {
        window.removeEventListener('resize', this.handleResize);
        window.removeEventListener('scroll', this.handleScroll);
    },
    props: {
        markdownTocData: {
            type: Object,
            default: { display: false, data: {} },
        },
        markdownTocIndex: {
            type: Number,
            default: 0,
        },
        informationBarData: Object,
    },
}
</script>
<style scoped>
.informationBar {
    position: sticky;
    padding-top: 1rem;
    padding-bottom: 1rem;
    /* opacity: 0;
    transform: translateY(4rem);
    animation: infoFadeIn 0.8s forwards; */
}

.labelBarAnimation {
    opacity: 0;
    transform: translateY(4rem);
    animation: infoFadeIn 0.8s forwards;
    animation-delay: calc(0.1s * var(--i));
}

@keyframes infoFadeIn {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.footer a {
    text-decoration: none;
    cursor: pointer;
    margin: 1rem 1.5rem;
    padding: 0 1.5rem;
    color: var(--color-theme-grayscale4);
    opacity: 0;
    animation: infoFadeIn 4s forwards;
}

.footer a:hover {
    color: var(--color-theme-grayscale5);
}

.footer a:active {
    color: var(--color-theme-blue-2);
}
</style>