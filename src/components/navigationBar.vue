<!-- 导航栏 -->
<template>
    <div class="navigationBar">
        <sideItem v-for="(item, index) in navigationBarData.titleData" :key="index"
            @click.prevent="handleClick(item.title, index, item.id, item.url)" :iconSvg="item.icon">
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
export default {
    data() {
        return {
            // 选中条长度
            selectedItemsWidth: Number,
            // 选中条与顶部距离
            clickItem: (this.navigationBarData.defaultSelected - 1) * 5 + 3,
        }
    },
    components: {
        sideItem,
    },
    methods: {
        // 判断选中条长度selectedItemsWidth和到顶部的距离clickItem
        handleClick(title, index, id, url) {
            if (url === undefined) {
                this.$emit('handleClick', { id: id, data: index });
                this.clickItem = index * 5 + 3;
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
            } else {
                location.replace(url)
            }
        }
    },
    created() {
        //获取this.$route.path的第一个/到/的字符串
        const titles = this.navigationBarData.titleData.map(title => title.id);
        const path = this.$route.path;
        const parts = path.split('/');
        if (parts.length >= 2 && titles.includes(parts[1])) {
            //查找parts[1]在titles中的位置
            const index = titles.indexOf(parts[1]);
            const titleData = this.navigationBarData.titleData[index];
            console.log(titleData);
            if (titleData.url === undefined) {
                this.$emit('handleClick', { id: titleData.id, data: index });
                // 预渲染阶段，默认选中第二个的文字标题，获取第二个标题的长度
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
                this.selectedItemsWidth = 4.5 + length * 0.8;
            } else {
                // 我真不信有人这样干，开局就跳转url
                location.replace(titleData.url)
            }
        } else {
            const titleData = this.navigationBarData.titleData[this.navigationBarData.defaultSelected - 1];
            if (titleData.url === undefined) {
                this.$emit('handleClick', { id: titleData.id, data: this.navigationBarData.defaultSelected - 1 });
                // 预渲染阶段，默认选中第二个的文字标题，获取第二个标题的长度
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
                this.selectedItemsWidth = 4.5 + length * 0.8;
            } else {
                // 我真不信有人这样干，开局就跳转url
                location.replace(titleData.url)
            }
        }
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

    position: sticky;
    top: 0;
    max-height: 100vh;
}

#selectedItems {
    position: absolute;
    height: 0.8rem;
    background-color: var(--color-theme-blue-1);
    z-index: -1;
}

#selectedItems {
    transition: margin 0.35s cubic-bezier(0, 0, .58, 1), width 0.35s;
}
</style>