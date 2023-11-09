<!-- 信息栏 -->
<template>
    <div class="informationBar" ref="informationBar" @scroll="handleScroll">
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
                <div v-html="item.html"></div>
            </template>
        </sideTemplate>
        <!-- 脚标 -->
        <div v-for="item in informationBarData.footmark" class="footmark">
            <a :href="item.url">{{ item.title }}</a>
        </div>
    </div>
</template>
<script>
import announcementBoard from './sideModule/announcementBoard.vue';
import labelBar from './sideModule/labelBar.vue';
import replyBar from './sideModule/replyBar.vue';
import sideTemplate from './sideTemplate.vue';
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
    },
    computed: {

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
        },
    },
    mounted() {
        window.addEventListener('resize', this.handleResize);
        window.addEventListener('scroll', this.handleScroll);
        const computedStyle = window.getComputedStyle(this.$refs.informationBar);
        this.divHeight = parseFloat(computedStyle.height) + parseFloat(computedStyle.paddingTop) + parseFloat(computedStyle.paddingBottom);
    },
    updated() {
        const computedStyle = window.getComputedStyle(this.$refs.informationBar);
        this.divHeight = parseFloat(computedStyle.height) + parseFloat(computedStyle.paddingTop) + parseFloat(computedStyle.paddingBottom);
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.handleResize);
        window.removeEventListener('scroll', this.handleScroll);
    },
    props: ["informationBarData"]
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
    color: #D1D2D2;
}

.footmark a:hover {
    color: #8A8E90;
}

.footmark a:active {
    color: #74E4FB;
}
</style>