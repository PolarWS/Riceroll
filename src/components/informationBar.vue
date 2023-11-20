<!-- 信息栏 -->
<template>
    <div class="informationBar" ref="informationBar" @scroll="handleScroll" v-if="!markDownDisplay">
        <!-- 侧边栏组件 -->
        <announcementBoard v-if="informationBarData.default.announcementBoard.display"
            :announcementBoard="informationBarData.default.announcementBoard" />
        <labelBar v-if="informationBarData.default.labelBar.display" :labelBar="informationBarData.default.labelBar" />
        <replyBar v-if="informationBarData.default.replyBar.display" />
        <!-- 自定义组件 -->
        <sideTemplate v-if="informationBarData.custom.display" v-for="item in informationBarData.custom.content">
            <template #title>
                {{ item.title }}
            </template>
            <template #content>
                <markDown :markDownData="item.markdown" />
            </template>
        </sideTemplate>
        <!-- 脚标 -->
        <div v-for="item in informationBarData.footmark" class="footmark">
            <a :href="item.url">{{ item.title }}</a>
        </div>
    </div>
    <!-- markDown[toc]组件 -->
    <div class="informationBar" ref="informationBar" v-if="markDownDisplay">
        <markDownToc />
    </div>
</template>
<script>
import markDownToc from './sideModule/markDownToc.vue';
import announcementBoard from './sideModule/announcementBoard.vue';
import labelBar from './sideModule/labelBar.vue';
import replyBar from './sideModule/replyBar.vue';
import sideTemplate from './sideTemplate.vue';
import markDown from './markDown.vue';
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
            markDownDisplay: false,
        }
    },
    watch: {
        markDownDisplay(newVal, oldVal) {
            // this.updateComponent();
        },
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
                if (window.scrollY < this.fixedDivDigits && this.stickyBool) {
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
            }
        },
        handleResize() {
            this.pageHeight = window.innerHeight;
            this.handleScroll();
        },
    },
    mounted() {
        this.$nextTick(() => {
            window.addEventListener('resize', this.handleResize);
            window.addEventListener('scroll', this.handleScroll);
            const computedStyle = window.getComputedStyle(this.$refs.informationBar);
            this.divHeight = parseFloat(computedStyle.height) + parseFloat(computedStyle.paddingTop) + parseFloat(computedStyle.paddingBottom);
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
    props: ["informationBarData"],
}
</script>
<style scoped>
.informationBar {
    position: sticky;
    padding-top: 1rem;
    padding-bottom: 1rem;
}

.footmark a {
    text-decoration: none;
    cursor: pointer;
    margin: 1rem 1.5rem;
    padding: 0 1.5rem;
    color: var(--color-theme-grayscale4);
}

.footmark a:hover {
    color: var(--color-theme-grayscale5);
}

.footmark a:active {
    color: var(--color-theme-blue-2);
}

.markdown-body {
    padding: 0;
    background-color: var(--color-theme-grayscale1);
    color: var(--color-theme-grayscale5);
}
</style>