<!-- 导航栏 -->
<template>
    <div class="navigationBar">
        <div class="sideItems">
            <sideItem v-for="(item, index) in navigationBarData.titleData" :key="index"
                @click.prevent="handleClick(item.id, item.url)" :iconSvg="item.icon" class="nav-item"
                :style="{ '--i': index }">
                <template #title>
                    {{ item.title }}
                </template>
            </sideItem>
        </div>
        <!-- 选中条 -->
        <div id="selectedItems" :style="{
            '--click-position': clickItem + 'rem',
            width: selectedItemsWidth + 'rem'
        }">
        </div>
    </div>
</template>
<script>
import sideItem from '@/components/sideItem.vue';
import { dataRelayStore } from '@/store/dataRelayStore.js';
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
        handleClick(id, url) {
            if (url === undefined) {
                this.$router.push('/' + id).then(() => {
                    this.checkScreenSize();
                    this.selectedCalculation();
                });
            } else {
                location.replace(url);
            }
        },
        checkScreenSize() {
            if (window.innerWidth <= 1280) {
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
                    this.selectedItemsWidthAdaptation = Math.min(14.5, 5.5 + length * 0.75);
                    this.selectedItemsWidth = this.selectedItemsWidthAdaptation
                } else {
                    this.selectedItemsWidthAdaptation = Math.min(14.5, 5.5 + length * 0.75);
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
                    this.selectedItemsWidthAdaptation = Math.min(14.5, 5.5 + length * 0.75);
                    this.selectedItemsWidth = this.selectedItemsWidthAdaptation
                } else {
                    this.selectedItemsWidthAdaptation = Math.min(14.5, 5.5 + length * 0.75);
                }
            }

            requestAnimationFrame(() => {
                this.$nextTick(() => {
                    // 确保DOM更新后再执行动画
                });
            });
        }
    },
    watch: {
        '$route'(to, from) {
            if (to.path != from.path) {
                this.selectedCalculation();
            }
        }, widthLevel() {
            this.checkScreenSize();
        }
    },
    mounted() {
        this.checkScreenSize();
        this.selectedCalculation();
    },
    computed: {
        widthLevel() {
            return dataRelayStore().widthLevel;
        }
    },
    props: ['navigationBarData']
}
</script>
<style scoped>
.sideItems {
    user-select: none;
}

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
    will-change: transform;
    transition: transform 0.35s cubic-bezier(0.25, 0.1, 0.25, 1),
        width 0.35s cubic-bezier(0.25, 0.1, 0.25, 1);
    transform: translateY(var(--click-position)) translateX(0);
    opacity: 0;
    animation: fadeIn 0.5s forwards;
}

@keyframes fadeIn {
    to {
        opacity: 1;
    }
}

@media screen and (max-width: 1280px) {
    #selectedItems {
        margin-left: 1rem;
    }
}

.nav-fade-enter-from {
    opacity: 0;
    transform: translateX(-20px);
}

.nav-fade-enter-to {
    opacity: 1;
    transform: translateX(0);
}

.nav-fade-enter-active {
    transition: all 0.5s ease;
}

.nav-item {
    transition: all 0.3s ease;
    opacity: 0;
    transform: translateX(-20px);
    animation: navFadeIn 0.5s forwards;
    animation-delay: calc(0.1s * var(--i));
}

@keyframes navFadeIn {
    to {
        opacity: 1;
        transform: translateX(0);
    }
}
</style>