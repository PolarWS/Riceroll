<template>
    <bodyItem :itemData="this.itemData" />
    <div class="fileBody">
        <div v-for="(item, index) in this.data" class="fileBox">
            <div class="fileDate">
                {{ item.date }}
            </div>
            <div v-for="(item, index) in item.title" class="fileItem">
                {{ item }}
            </div>
        </div>
    </div>
</template>
<script>
import bodyItem from './bodyItem.vue';
export default {
    data() {
        return {
            data: [
                {
                    date: "2020/10",
                    title: ["标题标题标题标题标题标题", "标题标题标题标题", "标题标标题标题标题标题题"]
                },
                {
                    date: "2020/09",
                    title: ["标题标题标题标题", "标标题标题题标题", "标题标标题标题标题标题题"]
                },
                {
                    date: "2020/08",
                    title: ["标题标题", "标题标题标题标题", "标标题标题题标题"]
                },
                {
                    date: "2020/07",
                    title: ["标题标题", "标题标标题标题题", "标题标题"]
                }
            ]
        }
    },
    components: {
        bodyItem,
    }, props: {
        itemData: Object,
    }
}
</script>
<style>
.fileBody {
    margin: 0rem 1.5rem 1rem 1.5rem;
}

.fileBox {
    margin-bottom: 1rem;
    padding: 1rem;
    border: 2px solid var(--color-theme-frame1);
}

.fileDate{
    font-size: 1.5rem;
    font-weight: 550;
    margin-bottom: 0.5rem;
    padding-bottom: 0.25rem;
    border-bottom: 2px solid var(--color-theme-frame1);
}

.fileItem{
    margin-bottom: 0.5rem;
    color: var(--color-theme-grayscale6);
}
</style>