<template>
    <bodyItem :itemData="this.itemData" />
    <div class="fileBody" v-show="renderBoolean">
        <div v-for="(item, index) in this.filePageData" class="fileBox">
            <div class="fileDate">
                {{ item.date }}
            </div>
            <div v-for="(item, index) in item.title" class="fileItem">
                {{ item }}
            </div>
        </div>
    </div>
    <loadingDynamicEffect v-show="!renderBoolean" />
</template>
<script>
import bodyItem from './bodyItem.vue';
import loadingDynamicEffect from '../loadingDynamicEffect.vue';
import { useCounterStore } from '../../store/axiosStore.js';
export default {
    data() {
        return {
            renderBoolean: false,
            filePageData: Object,
        }
    },
    mounted() {
        useCounterStore().apiRequest(this.api.url + this.api.filePage)
            .then(data => {
                if (data.status == 200) {
                    this.filePageData = data.data;
                    this.renderBoolean = true;
                } else {
                    this.$root.messagePopups({
                        message: '服务器错误',
                        Color: 'messageY',
                    });
                }
            })
            .catch(error => {
                this.$root.myMethod({
                    message: '服务器连接失败',
                    Color: 'messageR',
                });
            });
    },
    components: {
        bodyItem,
        loadingDynamicEffect,
    }, props: {
        itemData: Object,
    },
    inject: ['api'],
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

.fileDate {
    font-size: 1.5rem;
    font-weight: 550;
    margin-bottom: 0.5rem;
    padding-bottom: 0.25rem;
    border-bottom: 2px solid var(--color-theme-frame1);
}

.fileItem {
    margin-bottom: 0.5rem;
    color: var(--color-theme-grayscale6);
}
</style>