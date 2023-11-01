<!-- 导航栏 -->
<template>
    <div class="navigationBar">
        <sideItem v-for="(item, index) in navigationBarData.titleData" :key="index"
            @click.prevent="handleClick(item.title, index)" :iconSvg="item.icon">
            <template #title>
                {{ item.title }}
            </template>
        </sideItem>
        <!-- 选中条 -->
        <div id="selectedItems"
            :style="{ margin: clickItem + 'rem 0rem 1.5rem 2.15rem', width: selectedItemsWidth + 'rem' }">
        </div>
    </div>
</template>
<script>
import sideItem from './sideItem.vue';
import iconHomepage from './icon/iconHomepage.vue';
export default {
    data() {
        return {
            // 选中条长度
            selectedItemsWidth: 8,
            // 选中条与顶部距离
            clickItem: (this.navigationBarData.defaultSelected - 1) * 5 + 3,
        }
    },
    components: {
        iconHomepage,
        sideItem,
    },
    methods: {
        // 判断选中条长度selectedItemsWidth和到顶部的距离clickItem
        handleClick(title, data) {
            this.clickItem = data * 5 + 3;
            const text = title;
            let length = 0;
            for (let i = 0; i < text.length; i++) {
                const char = text.charAt(i);
                if (char <= '\x7F') {
                    // ASCII字符，通常是英文字符
                    length += 1;
                } else {
                    // 非ASCII字符，通常是中文字符
                    length += 2;
                }
            };
            if (length > 12) {
                length = 12;
            };

            this.selectedItemsWidth = 4.5 + length * 0.8;
        }
    },
    created() {
        // 预渲染阶段，默认选中第二个的文字标题，获取第二个标题的长度
        const textlen = this.navigationBarData.titleData[this.navigationBarData.defaultSelected - 1].title;
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
        this.selectedItemsWidth = 4.5 + length * 0.8;
    },
    props: ['navigationBarData']
}
</script>
<style scoped>
.navigationBar {
    width: 100%;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
}

#selectedItems {
    position: absolute;
    height: 0.75rem;
    background-color: #74E4FB;
    z-index: -1;
}

#selectedItems {
    transition: margin 0.35s cubic-bezier(0, 0, .58, 1), width 0.35s;
}
</style>