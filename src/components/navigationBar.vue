<!-- 导航栏 -->
<template>
    <div class="navigationBar">
        <div class="sideItems">
            <sideItem v-for="(item, index) in navigationBarData.titleData" :key="index"
                @click.prevent="handleClick(item.title, index, item.id, item.url)" :iconSvg="item.icon">
                <template #title>
                    {{ item.title }}
                </template>
            </sideItem>
        </div>
        <!-- 选中条 -->
        <div id="selectedItems" :style="{ marginTop: clickItem + 'rem', width: selectedItemsWidth + 'rem' }">
        </div>
    </div>
</template>
<script>
import sideItem from './sideItem.vue';
export default {
    data() {
        return {
            // 选中条长度
            selectedItemsWidth: Number,
            selectedItemsWidthAdaptation: Number,
            // 选中条与顶部距离
            clickItem: Number,
            selectedItemsIco: true,
        }
    },
    components: {
        sideItem,
    },
    methods: {
        // 判断选中条长度selectedItemsWidth和到顶部的距离clickItem
        handleClick(title, index, id, url) {
            this.checkScreenSize();
            this.selectedCalculation();
            if (url === undefined) {
                this.$emit('handleClick', { id: id, data: index });
            } else {
                location.replace(url);
            }
        },
        checkScreenSize() {
            if (window.innerWidth < 1280) {
                this.selectedItemsIco = false;
                this.selectedItemsWidth = 3;
            } else {
                this.selectedItemsWidth = this.selectedItemsWidthAdaptation;
                this.selectedItemsIco = true;
            }
        },
        selectedCalculation() {
            const titles = this.navigationBarData.titleData.map(title => title.id);
            const path = this.$route.path;
            const parts = path.split('/');
            if (parts.length >= 2 && titles.includes(parts[1])) {
                //查找parts[1]在titles中的位置
                const index = titles.indexOf(parts[1]);
                const titleData = this.navigationBarData.titleData[index];
                this.clickItem = index * 5 + 3;
                const textlen = titleData.title;
                let length = 0;
                for (let i = 0; i < textlen.length; i++) {
                    const char = textlen.charAt(i);
                    if (char <= '\x7F') {
                        // ASCII字符，通常是英文字符
                        length += 1;
                    } else {
                        // 非ASCII字符，通常是中文字符
                        length += 2;
                    }
                }
                if (this.selectedItemsIco) {
                    this.selectedItemsWidthAdaptation = 5.5 + length * 0.75;
                    this.selectedItemsWidth = this.selectedItemsWidthAdaptation
                } else {
                    this.selectedItemsWidthAdaptation = 5.5 + length * 0.75;
                }
            } else {
                this.clickItem = (this.navigationBarData.defaultSelected - 1) * 5 + 3;
                const titleData = this.navigationBarData.titleData[this.navigationBarData.defaultSelected - 1];
                const textlen = titleData.title;
                let length = 0;
                for (let i = 0; i < textlen.length; i++) {
                    const char = textlen.charAt(i);
                    if (char <= '\x7F') {
                        length += 1;
                    } else {
                        length += 2;
                    }
                }
                if (this.selectedItemsIco) {
                    this.selectedItemsWidthAdaptation = 5.5 + length * 0.75;
                    this.selectedItemsWidth = this.selectedItemsWidthAdaptation
                } else {
                    this.selectedItemsWidthAdaptation = 5.5 + length * 0.75;
                }
            }
        }
    },
    watch: {
        '$route'(to, from) {
            if (to.path != from.path) {
                this.selectedCalculation();
            }
        }
    },
    mounted() {
        this.checkScreenSize();
        this.selectedCalculation();
        window.addEventListener('resize', this.checkScreenSize);
    },
    unmounted() {
        window.removeEventListener('resize', this.checkScreenSize);
    },
    props: ['navigationBarData']
}
</script>
<style scoped>
.navigationBar {
    height: 100vh;
    width: 100%;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;

    position: sticky;
    top: 0;
    max-height: 100vh;
}

#selectedItems {
    margin-bottom: 1.5rem;
    margin-left: 2.15rem;
    position: absolute;
    height: 0.8rem;
    background-color: var(--color-theme-blue-1);
    z-index: -1;
    transition: margin 0.35s cubic-bezier(0, 0, .58, 1), width 0.35s;
}

@media screen and (max-width: 1280px) {
    #selectedItems {
        margin-left: 1rem;
    }
}
</style>