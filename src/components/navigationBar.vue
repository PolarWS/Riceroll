<!-- 导航栏 -->
<template>
    <div class="navigationBar">
        <sideItem v-for="(item, index) in titleData" :key="index" @click.prevent="handleClick(item.title, index)">
            <template #icon>
                <!-- 这个是默认（之后要搞成获取item.link然后改变标签），icon摆烂先，以后要整炫酷点的，传入参数改变颜色改变粗壮之类的现在懒得弄 -->
                <iconHomepage />
            </template>
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
    name: 'navigationBar',
    data() {
        return {
            titleData: [
                { id: "1101", title: "主页主页", link: "homepage" },
                { id: "1102", title: "文章", link: "article" },
                { id: "1103", title: "搜索", link: "search" },
                { id: "1104", title: "留言言", link: "leaveAMessage" },
                { id: "1105", title: "音乐", link: "music" },
                { id: "1106", title: "归档", link: "file" },
                { id: "1107", title: "友链", link: "friendChain" },
                { id: "1108", title: "关于", link: "about" },
            ],
            // 选中条长度
            selectedItemsWidth: 8,
            // 选中条与顶部距离
            clickItem: 8,
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
            }
            this.selectedItemsWidth = 4.5 + length * 0.8;
        }
    },
    created() {
        // 预渲染阶段，默认选中第二个的文字标题，获取第二个标题的长度
        const text = this.titleData[1].title;
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
        }

        this.selectedItemsWidth = 4.5 + length * 0.8;
    },
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